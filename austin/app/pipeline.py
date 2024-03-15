from app.models import ACSVariable, ACS5ValueByTract
from app.serializers import geojsonify

def get_census_data(acs_code, list_of_cbsas):
    print(f"finding {acs_code} for these cbsas: {list_of_cbsas}")
    try:
        variable = ACSVariable.objects.get(id=acs_code)
    except:
        return {"error":"VAR NOT FOUND"}
    data_already_found = ACS5ValueByTract.objects.filter(acs_variable=variable, tract_id__county_id__cbsa_id__in=list_of_cbsas)
    return geojsonify(data_already_found)