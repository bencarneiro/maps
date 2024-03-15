from django.shortcuts import render

import folium
from app.models import Tract, County, ACS5ValueByTract, ACSVariable
import pandas as pd
import geopandas as gpd
import requests
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from keplergl import KeplerGl



def geojsonify(values):
    json_str = '{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": ['
    for tv in values:
        feature_str = '{"type": "Feature", "properties": {'
        try:
            pop_dens = str(round(float(tv.value) / (float(tv.tract.aland) * (0.000000386102))))
        except:
            pop_dens = "0"
        feature_str += f'"tract_id": {tv.tract.tract_id}, '
        feature_str += f'"acs_code": "{tv.acs_variable.acs_code}", '
        feature_str += f'"label": "{tv.acs_variable.label}", '
        feature_str += f'"concept": "{tv.acs_variable.concept}", '
        feature_str += f'"population": {tv.value}, '
        feature_str += f'"population_density": {pop_dens}, '
        feature_str += f'"year": {tv.year}, '
        feature_str += f'"county": "{tv.tract.county.name}", '
        feature_str += f'"name_lsad": "{tv.tract.name_lsad}", '
        feature_str += f'"land_area": {tv.tract.aland}'
        feature_str += '}, "geometry": '
        feature_str += tv.tract.shape.geojson

        feature_str += '}, '
        json_str += feature_str
    json_str = json_str[:-2]
    json_str += ']}'
    # print(json_str)
    return json_str



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
    # census_data_to_df = []
    # for tv in tract_values:
    #     try:
    #         pop_dens = float(tv.value) / (float(tv.tract.aland) * (0.000000386102))
    #     except:
    #         pop_dens = 0
    #     census_data_to_df += [{
    #         "acs_code": tv.acs_variable.acs_code,
    #         "label": tv.acs_variable.label,
    #         "concept": tv.acs_variable.concept,
    #         "population": tv.value,
    #         "pop_dens": pop_dens,
    #         "year": tv.year,
    #         "tract_id": tv.tract.tract_id,
    #         "county": tv.tract.county.name,
    #         "land_area": tv.tract.aland
    #     }]
    # df = pd.DataFrame(census_data_to_df)
    # print(len(df))
    # print(df.columns)
    # print(df.to_string())
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
    # tooltip.add_to

    # folium.GeoJsonTooltip(['name', 'unemployment']).add_to(cp.geojson)
    # for t in tracts:
    #     html = f"<h1>{t.name_lsad}</h1>\n"
        # tip = folium.GeoJson(t.shape.geojson, tooltip=html).add_to(m)

        # folium.GeoJsonTooltip(['name']).add_to(cp.geojson)
    m = m._repr_html_()
    context = {"map": m}
    return render(request, "home.html", context)

def map_page(request):
    context = {}
    return render(request, "state.html", context)



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

def get_tracts_by_state(request):
    if "state" in request.GET and request.GET['state']:
        state = request.GET['state']
        geojson = serialize("geojson", Tract.objects.filter(state_id=state))
    return JsonResponse(json.loads(geojson), safe=False)