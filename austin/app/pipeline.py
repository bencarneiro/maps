from app.models import ACSVariable, ACS5ValueByTract
from app.serializers import geojsonify
import requests

def get_census_data(acs_code, list_of_cbsas):
    print(f"finding {acs_code} for these cbsas: {list_of_cbsas}")
    try:
        variable = ACSVariable.objects.get(id=acs_code)
    except:
        return {"error":"VAR NOT FOUND"}
    data_already_found = ACS5ValueByTract.objects.filter(acs_variable=variable, tract_id__county_id__cbsa_id__in=list_of_cbsas)
    return geojsonify(data_already_found)


def download_data_for_a_single_county(county, variable):
    census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
    stringified_state_id = str(county.state.id)
    if len(stringified_state_id) == 1:
        stringified_state_id = "0" + stringified_state_id
    stringified_county_id = str(county.id)[-3:]

    url = f"https://api.census.gov/data/2022/acs/acs5?get=NAME,{variable}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_county_id}&key={census_api_key}"
    r = requests.get(url)
    # print(url)
    # print(r.text)
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
