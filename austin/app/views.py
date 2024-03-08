from django.shortcuts import render

import folium
from app.models import Tract, County, ACS5ValueByTract, ACSVariable
import pandas as pd
import geopandas as gpd
import requests
from django.core.serializers import serialize
import json

# from django.contrib.gis.serializers.geojson import Serializer 

# class CustomSerializer(Serializer):

#     def end_object(self, obj):
#         for field in self.selected_fields:
#             if field == 'pk':
#                 continue
#             elif field in self._current.keys():
#                 continue
#             else:
#                 try:
#                     if '__' in field:
#                         fields = field.split('__')
#                         value = obj
#                         for f in fields:
#                             value = getattr(value, f)
#                         if value != obj:
#                             self._current[field] = value

#                 except AttributeError:
#                     pass
#         super(CustomSerializer, self).end_object(obj)

# Create your views here.

def home(request):
    counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
    ids = []
    for county in counties:
        ids += [county.id]

    tract_shapes = Tract.objects.filter(county_id__in=ids)
    print(len(tract_shapes))

    tract_shapes = serialize("geojson", tract_shapes)
    print(tract_shapes[:1000])
    # print(tract_shapes)
    # gdf = gpd.read_file(tract_shapes)
    # tracts = Tract.objects.filter(county_id__in=ids)
    census_variable = ACSVariable.objects.get(acs_code="B01001_001E")


    tract_values = ACS5ValueByTract.objects.filter(acs_variable=census_variable, tract_id__county_id__in=ids)
    shapes_json = json.loads(tract_shapes)
    for shape in shapes_json['features']:
        shape['properties']['test'] = "DUMMY DATA"
        try:
            tv = tract_values.get(tract_id__tract_id=int(shape['properties']['tract_id']))
            pop_dens = tv.value / (int(shape['properties']['aland']) * (0.000000386102))
            shape['properties']['group'] = tv.acs_variable.group
            shape['properties']['concept'] = tv.acs_variable.concept
            shape['properties']['label'] = tv.acs_variable.label
            shape['properties']['population'] = tv.value
            shape['properties']['pop_dens'] = pop_dens
        except Exception as e:
            print(e)
            shape['properties']['group'] = ""
            shape['properties']['concept'] = ""
            shape['properties']['label'] = ""
            shape['properties']['population'] = ""
            shape['properties']['pop_dens'] = ""
            continue

    tract_shapes = json.dumps(shapes_json)
    print(tract_shapes[:1000])
    census_data_to_df = []
    for tv in tract_values:
        try:
            pop_dens = float(tv.value) / (float(tv.tract.aland) * (0.000000386102))
        except:
            pop_dens = 0
        census_data_to_df += [{
            "acs_code": tv.acs_variable.acs_code,
            "label": tv.acs_variable.label,
            "concept": tv.acs_variable.concept,
            "population": tv.value,
            "pop_dens": pop_dens,
            "year": tv.year,
            "tract_id": tv.tract.tract_id,
            "county": tv.tract.county.name,
            "land_area": tv.tract.aland
        }]
    df = pd.DataFrame(census_data_to_df)
    # print(gdf.columns)
    # print(gdf.to_string())
    print(len(df))
    print(df.columns)
    print(df.to_string())
    # us_data_gdf = pd.merge(left = gdf,
    #                     right = df,
    #                     how = "right", 
    #                     left_on = ["tract_id"],
    #                 tract_id    right_on = ["tract_id"]
    #                     )
    # print(us_data_gdf.columns)
    # print(len(us_data_gdf))
    # print(us_data_gdf.to_string())
    
    # print(df.to_csv())

    # print(tracts[0])


    # census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
    # url = f"https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=tract:*&in=state:48&in=county:453,209,21,55,491&key={census_api_key}"
    # r = requests.get(url)
    # pop = r.json()
    # columns = [
    #     "tract_name",
    #     "tract_id",
    #     "population"
    # ]
    # df = pd.DataFrame(columns=columns, data=[])
    # for row in pop[1:]:
    #     df.loc[len(df.index)] = [row[0], row[4], row[1]]
    #     print(row)

    # serializers = CustomSerializer()
    # geodata = serialize("geojson", tracts, geometry_field='tract__shape')
    # print(geodata)

    m = folium.Map(location=(30.269122995392824, -97.74242563746505))

    tooltip = folium.GeoJsonTooltip(
        geo_data=tract_shapes,
        fields=["name_lsad", "pop_dens"],
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
        data=df,
        name="choropleth",
        columns= ["tract_id", "pop_dens"],
        key_on="feature.properties.tract_id",
        fill_color="RdYlGn",
        bins=15,
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
