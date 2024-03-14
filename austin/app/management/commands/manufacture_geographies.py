import pandas as pd
metros = pd.read_excel("https://www2.census.gov/programs-surveys/metro-micro/geographies/reference-files/2023/delineation-files/list1_2023.xlsx")
new_header = metros.iloc[1] #grab the first row for the header
metros = metros[2:1917] #take the data less the header row
metros.columns = new_header 
csa_dict = {}
cbsa_dict = {}
cbsa_to_csa_link = {}
county_to_cbsa_link = {}
for x in metros.index:
    cbsa_code = metros['CBSA Code'][x]
    cbsa_title = metros['CBSA Title'][x]
    csa_code = metros['CSA Code'][x]
    csa_title = metros['CSA Title'][x]
    state_fips = metros['FIPS State Code'][x]
#     print(state_fips)
    county_fips = metros['FIPS County Code'][x]
    full_county_fips = state_fips + county_fips
    if cbsa_code not in cbsa_dict:
        cbsa_dict[cbsa_code] = cbsa_title
    if type(csa_code) is str and csa_code not in csa_dict:
        csa_dict[csa_code] = csa_title
    county_to_cbsa_link[full_county_fips] = cbsa_code
    if type(csa_code) is str and cbsa_code not in cbsa_to_csa_link:
        cbsa_to_csa_link[cbsa_code] = csa_code
        
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_United_States_FIPS_codes_by_county")[1]

state_dict = {} 
county_dict = {}
for x in df.index:
    county_fips = df['FIPS'][x]
    clean_name = df['County or equivalent'][x].split("[")[0]
    stringified_county_code = str(county_fips)
    if len(stringified_county_code) == 4:
        state_fips = int(stringified_county_code[0:1])
        stringified_county_code = "0" + stringified_county_code
    else:
        state_fips = int(stringified_county_code[0:2])
    if state_fips not in state_dict:
        state_dict[state_fips] = df['State or equivalent'][x]
    county_key = str(int(county_fips))
    try:
        cbsa = county_to_cbsa_link[stringified_county_code]
    except:
        cbsa = None
    county_dict[stringified_county_code] = {"state": state_fips, "name": clean_name, "cbsa": cbsa}
    
for key in state_dict:
    print(f"""
        new_state = State(
            id = {key},
            name = "{state_dict[key]}"
        )
        new_state.save()
    """)

    
for key in csa_dict:
    print(f"""
        new_csa = CombinedStatisticalArea(
            id = {key},
            name = "{csa_dict[key]}"
        )
        new_csa.save()
    """)

for key in cbsa_dict:
    if key in cbsa_to_csa_link:
        print(f"""
            new_cbsa = CoreBaseStatisticalArea(
                id = {key},
                name = "{cbsa_dict[key]}",
                csa_id = {cbsa_to_csa_link[key]}
            )
            new_cbsa.save()
        """)
    else:
        print(f"""
            new_cbsa = CoreBaseStatisticalArea(
                id = {key},
                name = "{cbsa_dict[key]}"
            )
            new_cbsa.save()
        """)

for key in county_dict:
    if key in county_to_cbsa_link:
        print(f"""
            new_county = County(
                id = {int(key)},
                state_id = {county_dict[key]['state']},
                name = "{county_dict[key]['name']}",
                cbsa_id = {county_to_cbsa_link[key]}
            )
            new_county.save()
        """)
    else:
        print(f"""
            new_county = County(
                id = {int(key)},
                state_id = {county_dict[key]['state']},
                name = "{county_dict[key]['name']}"
            )
            new_county.save()
        """)