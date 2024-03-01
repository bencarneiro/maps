from django.db import models

# Create your models here.

from django.contrib.gis.db import models as gismodels


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512, null = False)

    class Meta:
        db_table="state"
        managed=True

class County(models.Model):
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)
    fips = models.IntegerField(null=False)
    name = models.CharField(max_length=512)

    class Meta:
        db_table="county"
        managed=True




class Tract(gismodels.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    county = models.ForeignKey(County, on_delete=models.DO_NOTHING)
    tract_id = models.IntegerField(null=False)
    name = models.CharField(max_length=128)
    name_lsad = models.CharField(max_length=512)
    mtfcc = models.CharField(max_length=128)
    funcstat = models.CharField(max_length=64)
    aland = models.BigIntegerField(null=True, blank=True)
    awater = models.BigIntegerField(null=True, blank=True)
    intptlat = models.FloatField(null=True, blank=True)
    intptlon = models.FloatField(null=True, blank=True)
    # shape = models.MultiPolygonField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    shape = gismodels.PolygonField(geography=True)

    class Meta:
        db_table="tract"
        managed=True
