from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from django.views.generic.base import RedirectView

import folium
from app.models import Tract, County, ACS5ValueByTract, ACSVariable, CoreBaseStatisticalArea, CombinedStatisticalArea
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from app.serializers import geojsonify, get_group_geojson
from app.pipeline import get_census_data, download_data_for_a_single_county, download_data_for_cbsa, download_group_data_for_cbsa

from django.db.models import Q

def homepage(request):
    return redirect("landing_page")

def index(request):
    return render(request, "index.html", {})

def map_page(request):
    context = {}
    return render(request, "map.html", context)

def examples(request):
    context = {}
    return render(request, "examples.html", context)


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

@cache_page(60 * 60 * 24 * 30)
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
        variables = ACSVariable.objects.filter((Q(concept__icontains=q) | Q(id__icontains=q)) & Q(predicate_type="int")).values("concept", "group").order_by("group").distinct()[:200]
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

# need to make this a post request
@cache_page(60 * 60 * 24 * 30)
def get_geojson_by_cbsa(request):

    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = request.GET['cbsa']
    else:
        return JsonResponse({}, safe=False)
    if "variable" in request.GET and request.GET['variable']:
        variable = request.GET['variable']
    else:
        return JsonResponse({}, safe=False)
    counties = County.objects.filter(cbsa=int(cbsa))

    found_results = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa)).count()
    if not found_results:
        download_data_for_cbsa(counties, variable)
    else:
        print("NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT")
    
    tract_values = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa))
    geojson = geojsonify(tract_values)

    return JsonResponse(json.loads(geojson), safe=False)

@cache_page(60 * 60 * 24 * 30)
def get_group_geojson_by_cbsa(request):

    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = request.GET['cbsa']
    else:
        return JsonResponse({}, safe=False)
    if "group" in request.GET and request.GET['group']:
        group = request.GET['group']
    else:
        return JsonResponse({}, safe=False)
    counties = County.objects.filter(cbsa=int(cbsa))
    variables = ACSVariable.objects.filter(group=group).order_by("id")
    variables_to_be_downloaded = []
    for v in variables:
        print(v)
        print(v.id)
        print(v.label)
        found_results = ACS5ValueByTract.objects.filter(acs_variable_id=v.id, tract_id__county_id__cbsa_id=int(cbsa)).count()
        if not found_results:
            variables_to_be_downloaded += [v]
            
    if variables_to_be_downloaded:
        download_group_data_for_cbsa(counties, variables_to_be_downloaded)

    geojson = get_group_geojson(group, cbsa)
    # print(geojson)
    return JsonResponse(json.loads(geojson), safe=False)

    return JsonResponse({}, safe=False)
    # found_results = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa)).count()
    # if not found_results:
    #     download_data_for_cbsa(counties, variable)
    # else:
    #     print("NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT NOT DOWNLOADING SHIT")
    

def get_map(request):
    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = request.GET['cbsa']
        cbsa_obj = CoreBaseStatisticalArea.objects.get(id=int(cbsa))
    else:
        return JsonResponse({}, safe=False)
    if "variable" in request.GET and request.GET['variable']:
        variable = request.GET['variable']
    else:
        return JsonResponse({}, safe=False)
    # first_tract = Tract.objects.filter(county_id__cbsa_id=int(cbsa))[0]
    # if "lat" in request.GET and request.GET['lat']:
    #     lat = request.GET['lat']
    # else:
    #     lat = 30.277914
    # if "lon" in request.GET and request.GET['lon']:
    #     lon = request.GET['lon']
    # else:
    #     lon = -97.739747
    url = f"/jsonify.json?cbsa={cbsa}&variable={variable}"
    print("URL URL URL URL")
    print(url)
    context = {
        "cbsa": cbsa_obj.name,
        "start_longitude": cbsa_obj.longitude,
        "start_latitude": cbsa_obj.latitude,
        "url": url,
        
    }
    return render(request, "cbsa_map.html", context)


def get_group_map(request):
    if "cbsa" in request.GET and request.GET['cbsa']:
        cbsa = request.GET['cbsa']
        cbsa_obj = CoreBaseStatisticalArea.objects.get(id=int(cbsa))
    else:
        return JsonResponse({}, safe=False)
    if "group" in request.GET and request.GET['group']:
        group = request.GET['group']
    else:
        return JsonResponse({}, safe=False)
    # first_tract = Tract.objects.filter(county_id__cbsa_id=int(cbsa))[0]
    # if "lat" in request.GET and request.GET['lat']:
    #     lat = request.GET['lat']
    # else:
    #     lat = 30.277914
    # if "lon" in request.GET and request.GET['lon']:
    #     lon = request.GET['lon']
    # else:
    #     lon = -97.739747
    url = f"/group.json?cbsa={cbsa}&group={group}"
    variables = ACSVariable.objects.filter(group=group)
    print("URL URL URL URL")
    print(url)
    context = {
        "cbsa": cbsa_obj.name,
        "start_longitude": cbsa_obj.longitude,
        "start_latitude": cbsa_obj.latitude,
        "url": url,
        "variables": variables,
        "first_variable": variables[0].id
        
    }
    return render(request, "group_map.html", context)

def benny_boy_resume(request):
    return render(request, "resume.html")

def landing_page(request):
    return render(request, "landing_page.html")


favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)