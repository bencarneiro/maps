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
    id = models.PositiveIntegerField(primary_key=True)
    state = models.ForeignKey(State, null=False, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=512)

    class Meta:
        db_table="county"
        managed=True


class CombinedStatisticalArea(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    class Meta:
        db_table="csa"
        managed=True


class CoreBasedStatisticalArea(models.Model):

    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=512)

    class Meta:
        db_table="cbsa"
        managed=True

class CBSAToCSA(models.Model):
    cbsa = models.ForeignKey(CoreBasedStatisticalArea, on_delete=models.DO_NOTHING)
    csa = models.ForeignKey(CombinedStatisticalArea, on_delete=models.DO_NOTHING)

    class Meta:
        db_table="cbsa_to_csa"
        managed=True

class CountyToCBSA(models.Model):

    cbsa = models.ForeignKey(CoreBasedStatisticalArea, on_delete=models.DO_NOTHING)
    county = models.ForeignKey(County, on_delete=models.DO_NOTHING)

    class Meta:
        db_table="county_to_cbsa"
        managed=True


class Tract(gismodels.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    id = models.PositiveBigIntegerField(primary_key=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
    county = models.ForeignKey(County, on_delete=models.DO_NOTHING)
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

class ACSVariable(models.Model):

    id = models.CharField(max_length=64, primary_key=True)
    label = models.CharField(max_length = 1024)
    concept = models.CharField(max_length = 1024)
    group = models.CharField(max_length = 64)
    required = models.BooleanField(default=False)
    predicate_type = models.CharField(max_length=64)

    class Meta:
        db_table = "acs_variable"
        managed=True

class ACS1ValueByTract(models.Model):
    acs_variable = models.ForeignKey(ACSVariable, on_delete = models.DO_NOTHING)
    year = models.IntegerField(null=False, blank=False)
    tract = models.ForeignKey(Tract, on_delete = models.DO_NOTHING)
    value = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = "acs1_value_by_tract"
        managed=True

class ACS5ValueByTract(models.Model):

    acs_variable = models.ForeignKey(ACSVariable, on_delete = models.DO_NOTHING)
    year = models.IntegerField(null=False, blank=False)
    tract = models.ForeignKey(Tract, on_delete = models.DO_NOTHING)
    value = models.IntegerField(default=0, null=True, blank=True)

    @property
    def name(self):
        return self.tract.name
    
    @property
    def name_lsad(self):
        return self.tract.name_lsad
    
    @property
    def shape(self):
        return self.tract.shape

    class Meta:
        db_table = "acs5_value_by_tract"
        managed=True

