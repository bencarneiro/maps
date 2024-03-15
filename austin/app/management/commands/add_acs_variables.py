from django.core.management.base import BaseCommand
import requests
import pandas as pd
from app.models import ACSVariable


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        ACSVariable.objects.all().delete()
        df = pd.read_html("https://api.census.gov/data/2022/acs/acs5/variables.html")
        data = df[0]
        for x in data.index:
            if type(data['Concept'][x]) is str:
                if data['Required'][x] == "not required":
                    required = False
                else:
                    required = True
                new_acs_variable = ACSVariable(
                    id=data['Name'][x],
                    concept=data['Concept'][x],
                    label=data['Label'][x],
                    group=data['Group'][x],
                    required=required,
                    predicate_type=data['Predicate Type'][x]
                )
                new_acs_variable.save()
                print(f"var {new_acs_variable.id} is saved successfully")


# class ACSVariable(models.Model):

#     acs_code = models.CharField(max_length=64)
#     label = models.CharField(max_length = 1024)
#     concept = models.CharField(max_length = 1024)
#     group = models.CharField(max_length = 64)
#     required = models.BooleanField(default=False)
#     predicate_type = models.CharField(max_length=64)

#     class Meta:
#         db_table = "acs_variable"
#         managed=True