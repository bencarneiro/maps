from django.contrib import admin

# Register your models here.
from .models import State, County, Tract

admin.site.register(State)
admin.site.register(County)
admin.site.register(Tract)