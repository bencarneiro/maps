from django.contrib import admin

# Register your models here.
from .models import State, County, Tract, ACSVariable

admin.site.register(State)
admin.site.register(County)
admin.site.register(Tract)
admin.site.register(ACSVariable)