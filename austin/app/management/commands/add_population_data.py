from django.core.management.base import BaseCommand
from app.models import Tract, ACSVariable, ACS5ValueByTract, County
import requests


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        counties = County.objects.filter(fips__in=[48453, 48055, 48209, 48491, 48021])
        ids = []
        for county in counties:
            ids += [county.id]
        census_api_key="db87451d2114e8ee87f1fc8d516119219cae4699"
        url = f"https://api.census.gov/data/2022/acs/acs5?get=NAME,B01001_001E&for=tract:*&in=state:48&in=county:453,209,021,055,491&key={census_api_key}"
        r = requests.get(url)
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
            tract = Tract.objects.get(county_id__in=ids, tract_id=int(row[4]))
            new_value = ACS5ValueByTract(
                acs_variable_id="B01001_001E",
                year=year,
                value = int(row[1]),
                tract=tract
            )
            new_value.save()
            print(row)