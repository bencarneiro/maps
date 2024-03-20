from django.shortcuts import render

import folium
from app.models import Tract, County, ACS5ValueByTract, ACSVariable, CoreBaseStatisticalArea, CombinedStatisticalArea
import pandas as pd
import geopandas as gpd
import requests
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from keplergl import KeplerGl
from app.serializers import geojsonify
from app.pipeline import get_census_data

from django.db.models import Q

def map_page(request):
    context = {}
    return render(request, "map.html", context)


def get_tracts_by_state(request):
    if "state" in request.GET and request.GET['state']:
        state = request.GET['state']
        geojson = serialize("geojson", Tract.objects.filter(state_id=state))
    return JsonResponse(json.loads(geojson), safe=False)


def get_demographic_data_by_metro(request):
    csa, cbsa = None, None
    if "csa" in request.GET and request.GET['csa']:
        csa = int(request.GET['csa'])
    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = int(request.GET['cbsa'])
    if not csa and not cbsa:
        return JsonResponse({"error": "you didn't send a metro"}, safe=False)
    cbsas = []
    if csa:
        cbsa_qs = CoreBaseStatisticalArea.objects.filter(csa_id=csa)
        for c in cbsa_qs:
            cbsas += [c.id]
    else:
        cbsas += [cbsa]
    # tract_names = list(Tract.objects.filter(county_id__cbsa_id__in=cbsas).values("name_lsad", "county_id__name"))
    # print(tract_names)
    data = get_census_data("B01001_001E", cbsas)
    print(data)
    return JsonResponse(json.loads(data), safe=False)


def efficient_home(request):
    counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
    ids = []
    for county in counties:
        ids += [county.id]

    tract_shapes = Tract.objects.filter(county_id__in=ids)
    print(len(tract_shapes))

    tract_shapes = serialize("geojson", tract_shapes)
    print(tract_shapes[:1000])
    census_variable = ACSVariable.objects.get(acs_code="B01001_001E")


    tract_values = ACS5ValueByTract.objects.filter(acs_variable=census_variable, tract_id__county_id__in=ids)
    tract_shapes = geojsonify(tract_values)
    gdf = gpd.read_file(tract_shapes)
    # Load a map with data and config and height
    m = KeplerGl(height=1000)
    m.add_data(data=gdf, name="tracts")
    m = m._repr_html_()
    context = {"map": m}
    return render(request, "home.html", context)



def home(request):
    counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
    ids = []
    for county in counties:
        ids += [county.id]

    tract_shapes = Tract.objects.filter(county_id__in=ids)
    print(len(tract_shapes))

    tract_shapes = serialize("geojson", tract_shapes)
    print(tract_shapes[:1000])
    census_variable = ACSVariable.objects.get(acs_code="B01001_001E")


    tract_values = ACS5ValueByTract.objects.filter(acs_variable=census_variable, tract_id__county_id__in=ids)
    tract_shapes = geojsonify(tract_values)
    gdf = gpd.read_file(tract_shapes)
    print(tract_shapes[:1000])
    m = folium.Map(location=(30.269122995392824, -97.74242563746505))

    tooltip = folium.GeoJsonTooltip(
        geo_data=tract_shapes,
        fields=["name_lsad", "population_density"],
        aliases=["Census Tract", "Population Density"],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=800,
    )
    #Create style_function
    style_function = lambda x: {'fillColor': '#ffffff', 
                                'color':'#000000', 
                                'fillOpacity': 0.1, 
                                'weight': 0.1}

    #Create highlight_function
    highlight_function = lambda x: {'fillColor': '#000000', 
                                    'color':'#000000', 
                                    'fillOpacity': 0.50, 
                                    'weight': 0.1}

    #Create popup tooltip object
    NIL = folium.features.GeoJson(
        tract_shapes,
        style_function=style_function, 
        control=False,
        highlight_function=highlight_function, 
        tooltip=tooltip)

    cp = folium.Choropleth(
        geo_data=tract_shapes,
        data=gdf,
        name="choropleth",
        columns= ["tract_id", "population_density"],
        key_on="feature.properties.tract_id",
        fill_color="RdYlGn",
        bins=40,
        fill_opacity=.8,
        line_opacity=0.2,
        legend_name="Total Population By State, 2021").add_to(m)

    m.add_child(NIL)
    m.keep_in_front(NIL)
    folium.LayerControl().add_to(m)
    m = m._repr_html_()
    context = {"map": m}
    return render(request, "home.html", context)



def population_density_geojson(request):
    # Austin Metro Counties
    counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
    ids = []
    for county in counties:
        ids += [county.id]
    census_variable = ACSVariable.objects.get(acs_code="B01001_001E")


    tract_values = ACS5ValueByTract.objects.filter(acs_variable_id=census_variable, tract_id__county_id__in=ids)
    geojson = geojsonify(tract_values)

    return JsonResponse(json.loads(geojson), safe=False)


def list_msas(request):
    if "search" in request.GET and request.GET['search']:
        q = request.GET['search']
        csas = CoreBaseStatisticalArea.objects.filter(name__icontains=q)
    else:
        csas = CoreBaseStatisticalArea.objects.all()
    
    context = {"csas": csas}
    
    return render(request, "msa_table.html", context)

# Item.objects.filter(Q(creator=owner) | Q(moderated=False))
def list_acs_variables(request):
    if "search" in request.GET and request.GET['search']:
        q = request.GET['search']
        variables = ACSVariable.objects.filter(Q(label__icontains=q) | Q(concept__icontains=q)).values("concept", "group").distinct()[:200]
    else:
        variables = ACSVariable.objects.values("concept", "group").distinct().order_by()
    
    context = {"variables": variables}
    
    return render(request, "concepts_table.html", context)

def acs_concept_by_id(request):
    if "search" in request.GET and request.GET['search']:
        q = request.GET['search']
        variables = ACSVariable.objects.filter(group=q)
    else:
        variables = ACSVariable.objects.all()[:3]
    
    context = {"variables": variables}
    
    return render(request, "variables_table.html", context)



def msa_search(request):
    return render(request, "msa_search.html")

def download_data_for_a_single_county(county, variable):
    census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
    stringified_state_id = str(county.state.id)
    if len(stringified_state_id) == 1:
        stringified_state_id = "0" + stringified_state_id
    stringified_county_id = str(county.id)[-3:]

    url = f"https://api.census.gov/data/2022/acs/acs5?get=NAME,{variable}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_county_id}&key={census_api_key}"
    r = requests.get(url)
    print(url)
    print(r.text)
    pop = r.json()
    columns = [
        "tract_name",
        "tract_id",
        "population"
    ]
    # df = pd.DataFrame(columns=columns, data=[])
    # acs_code = ACSVariable.objects.get(acs_code="")
    year = 2022
    
    for row in pop[1:]:
        # tract = Tract.objects.get(county_id__in=ids, tract_id=int(row[4]))
        new_value = ACS5ValueByTract(
            acs_variable_id=variable,
            year=year,
            value = int(row[1]),
            tract_id=int(row[2] + row[3] + row[4])
        )
        new_value.save()
        print(row)

def get_map(request):

    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = request.GET['cbsa']
    else:
        return JsonResponse({}, safe=False)
    if "variable" in request.GET and request.GET['variable']:
        variable = request.GET['variable']
    else:
        return JsonResponse({}, safe=False)
    counties = County.objects.filter(cbsa=int(cbsa))
    for county in counties:
        print(county.name)
        county_results = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract__county_id=county.id, year=2022)
        print(variable)
        print(county.id)
        print(county_results)
        if len(county_results) == 0:
            print("NEED TO MAKE REQUEST")
            download_data_for_a_single_county(county, variable)
        else:
            print("DON'T NEED TO MAKE REQUEST")
    
    tract_values = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa))
    print(len(tract_values))
    print(tract_values)
    geojson = geojsonify(tract_values)
    print(geojson)

    return JsonResponse(json.loads(geojson), safe=False)
    
