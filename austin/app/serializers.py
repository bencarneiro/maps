from app.models import ACS5ValueByTract, Tract
def geojsonify(values):
    geojson_list = ['{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": [']
    for tv in values:
        try:
            pop_dens = str(round(float(tv.value) / ((float(tv.tract.aland) + float(tv.tract.awater)) * (0.000000386102))))
        except:
            pop_dens = "0"
        geojson_list += ['{"type": "Feature", "properties": {"tract_id": ', str(tv.tract.id), ', "acs_code": "', tv.acs_variable.id, '", "label": "', tv.acs_variable.label, '", "concept": "', tv.acs_variable.concept, '", "population": ', str(tv.value), ', "population_density": ', pop_dens, ', "year": ', str(tv.year), ', "county": "', tv.tract.county.name, '", "name_lsad": "', tv.tract.name_lsad, '", "land_area": ', str(tv.tract.aland), ', "water_area": ', str(tv.tract.awater), '}, "geometry": ', tv.tract.shape.geojson, '}, ']
    # print(geojson_list)
    geojson_list[-1] = geojson_list[-1][:-2]
    geojson_list += ["]}"]
    return ''.join(geojson_list)
    

    

def get_group_geojson(group_id, cbsa_id):
    #   tract_values = ACS5ValueByTract.objects.filter(acs_variable_id=variable, tract_id__county_id__cbsa_id=int(cbsa))
    # tract_values = ACS5ValueByTract.objects.filter(acs_variable_id__group=group_id, tract_id__county_id__cbsa_id=int(cbsa_id))
    tracts = Tract.objects.filter(county_id__cbsa_id=cbsa_id)
    geojson_list = ['{"type": "FeatureCollection", "crs": {"type": "name", "properties": {"name": "EPSG:4326"}}, "features": [']
    for tract in tracts:
        values = ACS5ValueByTract.objects.filter(acs_variable_id__group=group_id, tract_id=tract.id).order_by("acs_variable_id")
        total_pop_for_tract = values[0].value


        geojson_list += ['{"type": "Feature", "properties": {"tract_id": ', str(tract.id), ', "county": "', tract.county.name, '", "name_lsad": "', tract.name_lsad, '", "land_area": ', str(tract.aland), ', "water_area": ', str(tract.awater), ', "data": {']

        # feature_str = '{"type": "Feature", "properties": {'

        # feature_str += f'"tract_id": {tract.id}, '
        # feature_str += f'"county": "{tract.county.name}", '
        # feature_str += f'"name_lsad": "{tract.name_lsad}", '
        # feature_str += f'"land_area": {tract.aland}, '
        # feature_str += f'"data": {{'
        
        # concept
        for value in values:
            try:
                pop_dens = str(round(float(value.value) / ((float(value.tract.aland) + float(value.tract.awater)) * (0.000000386102))))
                percentage = str(round(float(value.value) / float(total_pop_for_tract) * 100, 1)) + "%"
            except:
                pop_dens = "0"
                percentage = "0.0%"

            geojson_list += [
                '"', 
                value.acs_variable.id, 
                '": {"id": "', 
                value.acs_variable.id, 
                '","label": "', 
                value.acs_variable.label, 
                '", "population": ', 
                str(value.value), 
                ', "density": ',
                pop_dens, ', "percentage": "', 
                percentage, 
                '"}, ']
            # feature_str += f'"{value.acs_variable.id}": {{"id": "{value.acs_variable.id}","label": "{value.acs_variable.label}", "population": {value.value}, "density": {pop_dens}, "percentage": "{percentage}"}}, '
        geojson_list[-1] = geojson_list[-1][:-2]
        # feature_str = feature_str[:-2]
        geojson_list += [ '}', '}, "geometry": ',  tract.shape.geojson, '}, ']
        # feature_str += '}'
        # feature_str += '}, "geometry": '
        # feature_str += tract.shape.geojson

        # feature_str += '}, '
        # json_str += feature_str
    geojson_list[-1] = geojson_list[-1][:-2]
    geojson_list += [']}']
    # json_str = json_str[:-2]
    # json_str += ']}'
    # print(json_str)
    return "".join(geojson_list)
