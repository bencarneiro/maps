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