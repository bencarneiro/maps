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

    url = f"https://api.census.gov/data/2024/acs/acs5?get=NAME,{variable}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_county_id}&key={census_api_key}"
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
    year = 2024
    
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

def download_data_for_cbsa(counties, variable):
    print(counties)
    print(variable)
    census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
    stringified_list_of_county_ids=""
    requests_by_state_dict={}
    for c in counties:
        if c.state.id in requests_by_state_dict:
            requests_by_state_dict[c.state.id] += str(c.id)[-3:]
            requests_by_state_dict[c.state.id] += ","
        else:
            requests_by_state_dict[c.state.id] = str(c.id)[-3:]
            requests_by_state_dict[c.state.id] += ","
    for state in requests_by_state_dict:
        stringified_list_of_county_ids = requests_by_state_dict[state][:-1]
        stringified_state_id = str(state)
        if len(stringified_state_id) == 1:
            stringified_state_id = "0" + stringified_state_id
        url = f"https://api.census.gov/data/2024/acs/acs5?get=NAME,{variable}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_list_of_county_ids}&key={census_api_key}"
        print(url)
        r = requests.get(url)
        pop = r.json()
        columns = [
            "tract_name",
            "tract_id",
            "population"
        ]
        year = 2024
        
        for row in pop[1:]:
            if not row[1]:
                value = 0
            else:
                value = int(row[1])
            # tract = Tract.objects.get(county_id__in=ids, tract_id=int(row[4]))
            new_value = ACS5ValueByTract(
                acs_variable_id=variable,
                year=year,
                value = value,
                tract_id=int(row[2] + row[3] + row[4])
            )
            new_value.save()
            print(row)


    print(requests_by_state_dict)


def batch_download_variables(variables, requests_by_state_dict, census_api_key):

    stringified_list_of_variables = ""
    for idx in range(len(variables)):
        stringified_list_of_variables += variables[idx].id
        stringified_list_of_variables += ","
    if stringified_list_of_variables:
        stringified_list_of_variables = stringified_list_of_variables[:-1]


    for state in requests_by_state_dict:
        stringified_list_of_county_ids = requests_by_state_dict[state][:-1]
        stringified_state_id = str(state)
        if len(stringified_state_id) == 1:
            stringified_state_id = "0" + stringified_state_id

        url = f"https://api.census.gov/data/2024/acs/acs5?get=NAME,{stringified_list_of_variables}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_list_of_county_ids}&key={census_api_key}"
        print(url)
        r = requests.get(url)
        pop = r.json()
        columns = [
            "tract_name",
            "tract_id",
            "population"
        ]
        year = 2024
        
        for row in pop[1:]:
            print(row)
            tract_id = int(row[-3] + row[-2] + row[-1])
            for idx in range(len(variables)):
                if not row[idx + 1]:
                    value = 0
                else:
                    value = int(row[idx + 1])
                # tract = Tract.objects.get(county_id__in=ids, tract_id=int(row[4]))
                new_value = ACS5ValueByTract(
                    acs_variable_id=variables[idx].id,
                    year=year,
                    value = value,
                    tract_id=tract_id
                )
                new_value.save()
                print(row)


    print(requests_by_state_dict)

def download_group_data_for_cbsa(counties, variables):
    print(counties)
    print(variables)
    census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
    stringified_list_of_county_ids=""
    requests_by_state_dict={}

    for c in counties:
        if c.state.id in requests_by_state_dict:
            requests_by_state_dict[c.state.id] += str(c.id)[-3:]
            requests_by_state_dict[c.state.id] += ","
        else:
            requests_by_state_dict[c.state.id] = str(c.id)[-3:]
            requests_by_state_dict[c.state.id] += ","

    variables2, variables3 = None, None

    if len(variables) > 49:
        variables2 = variables[50:]
        variables = variables[:49]
    

    if variables2 and len(variables2) > 49:
        variables3 = variables3[50:]
        variables2 = variables2[:49]

    batch_download_variables(variables, requests_by_state_dict, census_api_key)

    if variables2:
        batch_download_variables(variables2, requests_by_state_dict, census_api_key)

    if variables3:
        batch_download_variables(variables3, requests_by_state_dict, census_api_key)


    # url = f"https://api.census.gov/data/2022/acs/acs5?get=NAME,{variable}&for=tract:*&in=state:{stringified_state_id}&in=county:{stringified_county_id}&key={census_api_key}"
    # r = requests.get(url)
    # # print(url)
    # # print(r.text)
    # pop = r.json()
    # columns = [
    #     "tract_name",
    #     "tract_id",
    #     "population"
    # ]
    # # df = pd.DataFrame(columns=columns, data=[])
    # # acs_code = ACSVariable.objects.get(acs_code="")
    # year = 2022
    
    # for row in pop[1:]:
    #     # tract = Tract.objects.get(county_id__in=ids, tract_id=int(row[4]))
    #     new_value = ACS5ValueByTract(
    #         acs_variable_id=variable,
    #         year=year,
    #         value = int(row[1]),
    #         tract_id=int(row[2] + row[3] + row[4])
    #     )
    #     new_value.save()
    #     print(row)
