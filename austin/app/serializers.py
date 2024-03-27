from app.models import ACS5ValueByTract, Tract
def geojsonify(values):
    json_str = '{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": ['
    for tv in values:
        feature_str = '{"type": "Feature", "properties": {'
        try:
            pop_dens = str(round(float(tv.value) / (float(tv.tract.aland) * (0.000000386102))))
        except:
            pop_dens = "0"
        feature_str += f'"tract_id": {tv.tract.id}, '
        feature_str += f'"acs_code": "{tv.acs_variable.id}", '
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
    

    

def get_group_geojson(group_id, cbsa_id):
    #   tract_values = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa))
    # tract_values = ACS5ValueByTract.objects.filter(acs_variable_id__group=group_id, tract_id__county_id__cbsa_id=int(cbsa_id))
    tracts = Tract.objects.filter(county_id__cbsa_id=cbsa_id)
    json_str = '{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": ['
    for tract in tracts:
        values = ACS5ValueByTract.objects.filter(acs_variable_id__group=group_id, tract_id=tract.id).order_by("acs_variable_id")
        total_pop_for_tract = values[0].value
        feature_str = '{"type": "Feature", "properties": {'

        feature_str += f'"tract_id": {tract.id}, '
        feature_str += f'"county": "{tract.county.name}", '
        feature_str += f'"name_lsad": "{tract.name_lsad}", '
        feature_str += f'"land_area": {tract.aland}, '
        # concept
        for value in values:
            
            # print(percentage)
            try:
                pop_dens = str(round(float(value.value) / (float(value.tract.aland) * (0.000000386102))))
                percentage = str(round(float(value.value) / float(total_pop_for_tract) * 100, 1)) + "%"
                
            except:
                pop_dens = "0"
                percentage = "0.0%"

            feature_str += f'"{value.acs_variable.id}": {{"id": "{value.acs_variable.id}","label": "{value.acs_variable.label}", "population": {value.value}, "density": {pop_dens}, "percentage": "{percentage}"}}, '

        feature_str = feature_str[:-2]
        feature_str += '}, "geometry": '
        feature_str += tract.shape.geojson

        feature_str += '}, '
        json_str += feature_str
    json_str = json_str[:-2]
    json_str += ']}'
    # print(json_str)
    return json_str
