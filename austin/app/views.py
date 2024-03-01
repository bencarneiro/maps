from django.shortcuts import render

import folium
from app.models import Tract, County

# Create your views here.

def home(request):
    m = folium.Map(location=(30.269122995392824, -97.74242563746505))
    counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
    ids = []
    for county in counties:
        ids += [county.id]

    tracts = Tract.objects.filter(county_id__in=ids)
    for t in tracts:
        html = f"<h1>{t.name_lsad}</h1>\n"
        folium.GeoJson(t.shape.geojson, tooltip=html).add_to(m)
    m = m._repr_html_()
    context = {"map": m}
    return render(request, "home.html", context)
