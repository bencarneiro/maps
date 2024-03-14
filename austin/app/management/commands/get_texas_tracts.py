from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand
from app.models import Tract, County


class Command(BaseCommand):

    def handle(self, *args, **options):
        Tract.objects.all().delete()
        ds = DataSource("/home/tonydeals/app/maps/shapefiles/tl_2022_48_tract.shp")
        lyr = ds[0]
        state_id = 48
        for feat in lyr:
            state_id = int(feat.get("STATEFP"))
            county_id = int(feat.get("COUNTYFP")) + 48000
            tract_id = int(feat.get('TRACTCE'))
            name = feat.get("NAME")
            name_lsad = feat.get("NAMELSAD")
            mtfcc = feat.get("MTFCC")
            funcstat = feat.get("FUNCSTAT")
            aland = feat.get("ALAND")
            awater = feat.get("AWATER")
            intptlat = feat.get("INTPTLAT")
            intptlon = feat.get("INTPTLON")
            new_census_tract = Tract(
                id=tract_id,
                state_id=48,
                county_id=county_id,
                name=name,
                name_lsad=name_lsad,
                mtfcc=mtfcc,
                funcstat=funcstat,
                aland=aland,
                awater=awater,
                intptlat=intptlat,
                intptlon=intptlon,
                shape = feat.geom.wkt
            )
            new_census_tract.save()
            # break
            
        



# class Tract(gismodels.Model):
#     # Regular Django fields corresponding to the attributes in the
#     # world borders shapefile.
#     state = models.ForeignKey(State, on_delete=models.DO_NOTHING)
#     county = models.ForeignKey(County, on_delete=models.DO_NOTHING)
#     tract_id = models.IntegerField(null=False)
#     name = models.CharField(max_length=128)
#     name_lsad = models.CharField(max_length=512)
#     mtfcc = models.CharField(max_length=128)
#     funcstat = models.CharField(max_length=64)
#     aland = models.BigIntegerField(null=True, blank=True)
#     awater = models.BigIntegerField(null=True, blank=True)
#     intptlat = models.FloatField(null=True, blank=True)
#     intptlon = models.FloatField(null=True, blank=True)
#     # shape = models.MultiPolygonField()

#     # GeoDjango-specific: a geometry field (MultiPolygonField)
#     shape = gismodels.PolygonField()