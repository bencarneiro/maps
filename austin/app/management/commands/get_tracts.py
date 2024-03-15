from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand
from app.models import Tract, State


class Command(BaseCommand):

    def handle(self, *args, **options):
        Tract.objects.all().delete()
        states = State.objects.all()
        for s in states:
            stringified_state_fips_code = str(s.id)
            if len(stringified_state_fips_code) == 1:
                stringified_state_fips_code = "0" + stringified_state_fips_code
            
            print(s.name)
            print(stringified_state_fips_code)
            try:
                ds = DataSource(f"/home/tonydeals/app/maps/shapefiles/{stringified_state_fips_code}/tl_2022_{stringified_state_fips_code}_tract/tl_2022_{stringified_state_fips_code}_tract.shp")
                lyr = ds[0]
                for feat in lyr:
                    state_id_str = feat.get("STATEFP")
                    state_id = int(state_id_str)
                    print(f"state: {state_id_str}")
                    print(feat.get("COUNTYFP"))
                    print(feat.get("NAMELSAD"))
                    county_id = int(feat.get("COUNTYFP")) + (s.id * 1000)
                    county_id_str = str(county_id)
                    if len(county_id_str) == 4:
                        county_id_str = "0" + county_id_str
                    print(f"county: {county_id_str}")
                    tract_id = int(feat.get('TRACTCE'))
                    tract_id_str = str(tract_id)

                    if len(tract_id_str) == 3:
                        tract_id_str = "000" + tract_id_str
                    if len(tract_id_str) == 4:
                        tract_id_str = "00" + tract_id_str
                    if len(tract_id_str) == 5:
                        tract_id_str = "0" + tract_id_str
                    full_tract_fips = county_id_str + tract_id_str
                    print(full_tract_fips)
                    if len(full_tract_fips) != 11:
                        print("ERROR ERROR ERROR ERROR ERROR WRONG FIPS LENGTH")
                        print(len(full_tract_fips))
                    # print(f"tract {tract_id}")
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
                        state_id=state_id,
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
            except Exception as e:
                print(f"FAILURE FAILURE FAILURE on {s.name}")
                print(e)
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