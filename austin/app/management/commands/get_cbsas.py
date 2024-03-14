from django.core.management.base import BaseCommand
from app.models import CoreBaseStatisticalArea


class Command(BaseCommand):

    def handle(self, *args, **options):
        new_cbsa = CoreBaseStatisticalArea(
            id = 10100,
            name = "Aberdeen, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10140,
            name = "Aberdeen, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10180,
            name = "Abilene, TX",
            csa_id = 101
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10220,
            name = "Ada, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10300,
            name = "Adrian, MI",
            csa_id = 220
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10380,
            name = "Aguadilla, PR",
            csa_id = 364
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10420,
            name = "Akron, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10460,
            name = "Alamogordo, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10480,
            name = "Alamosa, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10500,
            name = "Albany, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10540,
            name = "Albany, OR",
            csa_id = 440
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10580,
            name = "Albany-Schenectady-Troy, NY",
            csa_id = 104
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10620,
            name = "Albemarle, NC",
            csa_id = 172
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10660,
            name = "Albert Lea, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10700,
            name = "Albertville, AL",
            csa_id = 290
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10740,
            name = "Albuquerque, NM",
            csa_id = 105
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10760,
            name = "Alexander City, AL",
            csa_id = 194
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10780,
            name = "Alexandria, LA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10820,
            name = "Alexandria, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10860,
            name = "Alice, TX",
            csa_id = 204
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10900,
            name = "Allentown-Bethlehem-Easton, PA-NJ",
            csa_id = 106
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10940,
            name = "Alma, MI",
            csa_id = 394
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 10980,
            name = "Alpena, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11020,
            name = "Altoona, PA",
            csa_id = 107
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11060,
            name = "Altus, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11100,
            name = "Amarillo, TX",
            csa_id = 108
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11140,
            name = "Americus, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11180,
            name = "Ames, IA",
            csa_id = 218
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11200,
            name = "Amherst Town-Northampton, MA",
            csa_id = 521
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11220,
            name = "Amsterdam, NY",
            csa_id = 104
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11260,
            name = "Anchorage, AK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11360,
            name = "Anderson Creek, NC",
            csa_id = 450
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11380,
            name = "Andrews, TX",
            csa_id = 372
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11420,
            name = "Angola, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11460,
            name = "Ann Arbor, MI",
            csa_id = 220
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11500,
            name = "Anniston-Oxford, AL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11540,
            name = "Appleton, WI",
            csa_id = 118
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11580,
            name = "Arcadia, FL",
            csa_id = 412
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11620,
            name = "Ardmore, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11640,
            name = "Arecibo, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11660,
            name = "Arkadelphia, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11680,
            name = "Arkansas City-Winfield, KS",
            csa_id = 556
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11700,
            name = "Asheville, NC",
            csa_id = 120
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11740,
            name = "Ashland, OH",
            csa_id = 360
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11820,
            name = "Astoria, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11860,
            name = "Atchison, KS",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11900,
            name = "Athens, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11940,
            name = "Athens, TN",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 11980,
            name = "Athens, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12020,
            name = "Athens-Clarke County, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12060,
            name = "Atlanta-Sandy Springs-Roswell, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12100,
            name = "Atlantic City-Hammonton, NJ",
            csa_id = 428
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12140,
            name = "Auburn, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12180,
            name = "Auburn, NY",
            csa_id = 532
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12220,
            name = "Auburn-Opelika, AL",
            csa_id = 194
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12260,
            name = "Augusta-Richmond County, GA-SC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12300,
            name = "Augusta-Waterville, ME"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12380,
            name = "Austin, MN",
            csa_id = 462
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12420,
            name = "Austin-Round Rock-San Marcos, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12460,
            name = "Bainbridge, GA",
            csa_id = 533
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12520,
            name = "Baker City, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12540,
            name = "Bakersfield-Delano, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12580,
            name = "Baltimore-Columbia-Towson, MD",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12620,
            name = "Bangor, ME"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12660,
            name = "Baraboo, WI",
            csa_id = 357
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12700,
            name = "Barnstable Town, MA",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12740,
            name = "Barre, VT",
            csa_id = 162
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12780,
            name = "Bartlesville, OK",
            csa_id = 538
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12860,
            name = "Batavia, NY",
            csa_id = 464
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12900,
            name = "Batesville, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12940,
            name = "Baton Rouge, LA",
            csa_id = 132
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 12980,
            name = "Battle Creek, MI",
            csa_id = 310
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13020,
            name = "Bay City, MI",
            csa_id = 474
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13060,
            name = "Bay City, TX",
            csa_id = 288
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13100,
            name = "Beatrice, NE",
            csa_id = 339
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13140,
            name = "Beaumont-Port Arthur, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13180,
            name = "Beaver Dam, WI",
            csa_id = 376
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13220,
            name = "Beckley, WV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13260,
            name = "Bedford, IN",
            csa_id = 144
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13300,
            name = "Beeville, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13340,
            name = "Bellefontaine, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13380,
            name = "Bellingham, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13420,
            name = "Bemidji, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13460,
            name = "Bend, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13540,
            name = "Bennington, VT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13660,
            name = "Big Rapids, MI",
            csa_id = 266
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13700,
            name = "Big Spring, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13740,
            name = "Billings, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13780,
            name = "Binghamton, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13820,
            name = "Birmingham, AL",
            csa_id = 142
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13860,
            name = "Bishop, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13900,
            name = "Bismarck, ND"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13940,
            name = "Blackfoot, ID",
            csa_id = 292
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 13980,
            name = "Blacksburg-Christiansburg-Radford, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14010,
            name = "Bloomington, IL",
            csa_id = 145
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14020,
            name = "Bloomington, IN",
            csa_id = 144
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14100,
            name = "Bloomsburg-Berwick, PA",
            csa_id = 146
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14140,
            name = "Bluefield, WV-VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14180,
            name = "Blytheville, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14220,
            name = "Bogalusa, LA",
            csa_id = 406
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14260,
            name = "Boise City, ID",
            csa_id = 147
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14300,
            name = "Bonham, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14380,
            name = "Boone, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14420,
            name = "Borger, TX",
            csa_id = 108
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14460,
            name = "Boston-Cambridge-Newton, MA-NH",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14500,
            name = "Boulder, CO",
            csa_id = 216
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14540,
            name = "Bowling Green, KY",
            csa_id = 150
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14580,
            name = "Bozeman, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14620,
            name = "Bradford, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14660,
            name = "Brainerd, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14700,
            name = "Branson, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14710,
            name = "Brattleboro, VT",
            csa_id = 313
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14720,
            name = "Breckenridge, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14740,
            name = "Bremerton-Silverdale-Port Orchard, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14780,
            name = "Brenham, TX",
            csa_id = 288
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14820,
            name = "Brevard, NC",
            csa_id = 120
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14860,
            name = "Bridgeport-Stamford-Danbury, CT",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 14940,
            name = "Brigham City, UT-ID",
            csa_id = 482
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15020,
            name = "Brookhaven, MS",
            csa_id = 298
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15060,
            name = "Brookings, OR",
            csa_id = 152
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15100,
            name = "Brookings, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15180,
            name = "Brownsville-Harlingen, TX",
            csa_id = 154
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15220,
            name = "Brownwood, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15260,
            name = "Brunswick-St. Simons, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15340,
            name = "Bucyrus, OH",
            csa_id = 360
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15380,
            name = "Buffalo-Cheektowaga, NY",
            csa_id = 160
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15420,
            name = "Burley, ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15460,
            name = "Burlington, IA-IL",
            csa_id = 161
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15500,
            name = "Burlington, NC",
            csa_id = 268
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15540,
            name = "Burlington-South Burlington, VT",
            csa_id = 162
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15580,
            name = "Butte-Silver Bow, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15620,
            name = "Cadillac, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15660,
            name = "Calhoun, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15700,
            name = "Cambridge, MD",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15740,
            name = "Cambridge, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15780,
            name = "Camden, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15820,
            name = "Campbellsville, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15860,
            name = "Cañon City, CO",
            csa_id = 444
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15900,
            name = "Canton, IL",
            csa_id = 427
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15940,
            name = "Canton-Massillon, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 15980,
            name = "Cape Coral-Fort Myers, FL",
            csa_id = 163
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16020,
            name = "Cape Girardeau, MO-IL",
            csa_id = 164
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16060,
            name = "Carbondale, IL",
            csa_id = 166
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16100,
            name = "Carlsbad-Artesia, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16140,
            name = "Carroll, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16180,
            name = "Carson City, NV",
            csa_id = 456
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16220,
            name = "Casper, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16260,
            name = "Cedar City, UT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16300,
            name = "Cedar Rapids, IA",
            csa_id = 168
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16340,
            name = "Cedartown, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16380,
            name = "Celina, OH",
            csa_id = 338
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16460,
            name = "Centralia, IL",
            csa_id = 476
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16500,
            name = "Centralia, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16540,
            name = "Chambersburg, PA",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16580,
            name = "Champaign-Urbana, IL",
            csa_id = 169
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16620,
            name = "Charleston, WV",
            csa_id = 170
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16660,
            name = "Charleston-Mattoon, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16700,
            name = "Charleston-North Charleston, SC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16740,
            name = "Charlotte-Concord-Gastonia, NC-SC",
            csa_id = 172
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16820,
            name = "Charlottesville, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16860,
            name = "Chattanooga, TN-GA",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16940,
            name = "Cheyenne, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 16980,
            name = "Chicago-Naperville-Elgin, IL-IN",
            csa_id = 176
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17020,
            name = "Chico, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17060,
            name = "Chillicothe, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17140,
            name = "Cincinnati, OH-KY-IN",
            csa_id = 178
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17220,
            name = "Clarksburg, WV",
            csa_id = 242
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17260,
            name = "Clarksdale, MS",
            csa_id = 368
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17300,
            name = "Clarksville, TN-KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17340,
            name = "Clearlake, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17380,
            name = "Cleveland, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17410,
            name = "Cleveland, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17420,
            name = "Cleveland, TN",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17500,
            name = "Clewiston, FL",
            csa_id = 163
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17540,
            name = "Clinton, IA",
            csa_id = 209
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17580,
            name = "Clovis, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17620,
            name = "Coamo, PR",
            csa_id = 434
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17640,
            name = "Coco, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17650,
            name = "Cody, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17660,
            name = "Coeur d'Alene, ID",
            csa_id = 518
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17740,
            name = "Coldwater, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17780,
            name = "College Station-Bryan, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17820,
            name = "Colorado Springs, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17860,
            name = "Columbia, MO",
            csa_id = 190
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17900,
            name = "Columbia, SC",
            csa_id = 192
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 17980,
            name = "Columbus, GA-AL",
            csa_id = 194
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18020,
            name = "Columbus, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18060,
            name = "Columbus, MS",
            csa_id = 523
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18100,
            name = "Columbus, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18140,
            name = "Columbus, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18180,
            name = "Concord, NH",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18220,
            name = "Connersville, IN",
            csa_id = 458
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18260,
            name = "Cookeville, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18300,
            name = "Coos Bay-North Bend, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18340,
            name = "Corbin, KY",
            csa_id = 371
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18380,
            name = "Cordele, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18420,
            name = "Corinth, MS",
            csa_id = 539
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18460,
            name = "Cornelia, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18500,
            name = "Corning, NY",
            csa_id = 236
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18580,
            name = "Corpus Christi, TX",
            csa_id = 204
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18620,
            name = "Corsicana, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18660,
            name = "Cortland, NY",
            csa_id = 296
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18700,
            name = "Corvallis, OR",
            csa_id = 440
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18740,
            name = "Coshocton, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18820,
            name = "Crawfordsville, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18860,
            name = "Crescent City, CA",
            csa_id = 152
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18880,
            name = "Crestview-Fort Walton Beach-Destin, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18900,
            name = "Crossville, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 18980,
            name = "Cullman, AL",
            csa_id = 142
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19060,
            name = "Cumberland, MD-WV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19100,
            name = "Dallas-Fort Worth-Arlington, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19140,
            name = "Dalton, GA",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19180,
            name = "Danville, IL",
            csa_id = 169
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19220,
            name = "Danville, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19260,
            name = "Danville, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19300,
            name = "Daphne-Fairhope-Foley, AL",
            csa_id = 380
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19340,
            name = "Davenport-Moline-Rock Island, IA-IL",
            csa_id = 209
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19430,
            name = "Dayton-Kettering-Beavercreek, OH",
            csa_id = 212
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19460,
            name = "Decatur, AL",
            csa_id = 290
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19500,
            name = "Decatur, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19540,
            name = "Decatur, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19580,
            name = "Defiance, OH"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19620,
            name = "Del Rio, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19660,
            name = "Deltona-Daytona Beach-Ormond Beach, FL",
            csa_id = 422
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19700,
            name = "Deming, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19740,
            name = "Denver-Aurora-Centennial, CO",
            csa_id = 216
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19760,
            name = "DeRidder, LA",
            csa_id = 324
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19780,
            name = "Des Moines-West Des Moines, IA",
            csa_id = 218
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19810,
            name = "Detroit Lakes, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19820,
            name = "Detroit-Warren-Dearborn, MI",
            csa_id = 220
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19860,
            name = "Dickinson, ND"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19940,
            name = "Dixon, IL",
            csa_id = 221
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 19980,
            name = "Dodge City, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20020,
            name = "Dothan, AL",
            csa_id = 222
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20060,
            name = "Douglas, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20100,
            name = "Dover, DE",
            csa_id = 428
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20140,
            name = "Dublin, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20180,
            name = "DuBois, PA",
            csa_id = 524
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20220,
            name = "Dubuque, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20260,
            name = "Duluth, MN-WI",
            csa_id = 228
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20300,
            name = "Dumas, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20340,
            name = "Duncan, OK",
            csa_id = 334
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20420,
            name = "Durango, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20460,
            name = "Durant, OK",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20500,
            name = "Durham-Chapel Hill, NC",
            csa_id = 450
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20540,
            name = "Dyersburg, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20580,
            name = "Eagle Pass, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20660,
            name = "Easton, MD",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20700,
            name = "East Stroudsburg, PA",
            csa_id = 106
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20740,
            name = "Eau Claire, WI",
            csa_id = 232
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20780,
            name = "Edwards, CO",
            csa_id = 233
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20820,
            name = "Effingham, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20900,
            name = "El Campo, TX",
            csa_id = 288
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20940,
            name = "El Centro, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 20980,
            name = "El Dorado, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21020,
            name = "Elizabeth City, NC",
            csa_id = 545
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21060,
            name = "Elizabethtown, KY",
            csa_id = 350
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21120,
            name = "Elk City, OK",
            csa_id = 555
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21140,
            name = "Elkhart-Goshen, IN",
            csa_id = 515
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21180,
            name = "Elkins, WV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21220,
            name = "Elko, NV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21260,
            name = "Ellensburg, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21300,
            name = "Elmira, NY",
            csa_id = 236
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21340,
            name = "El Paso, TX",
            csa_id = 238
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21380,
            name = "Emporia, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21420,
            name = "Enid, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21460,
            name = "Enterprise, AL",
            csa_id = 222
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21500,
            name = "Erie, PA",
            csa_id = 240
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21540,
            name = "Escanaba, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21580,
            name = "Española, NM",
            csa_id = 105
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21640,
            name = "Eufaula, AL-GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21660,
            name = "Eugene-Springfield, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21700,
            name = "Eureka-Arcata, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21740,
            name = "Evanston, WY-UT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21780,
            name = "Evansville, IN",
            csa_id = 241
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21820,
            name = "Fairbanks-College, AK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21860,
            name = "Fairmont, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21900,
            name = "Fairmont, WV",
            csa_id = 242
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 21980,
            name = "Fallon, NV",
            csa_id = 456
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22020,
            name = "Fargo, ND-MN",
            csa_id = 244
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22060,
            name = "Faribault-Northfield, MN",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22100,
            name = "Farmington, MO",
            csa_id = 476
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22140,
            name = "Farmington, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22180,
            name = "Fayetteville, NC",
            csa_id = 246
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22190,
            name = "Fayetteville, TN",
            csa_id = 290
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22220,
            name = "Fayetteville-Springdale-Rogers, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22260,
            name = "Fergus Falls, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22300,
            name = "Findlay, OH",
            csa_id = 248
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22340,
            name = "Fitzgerald, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22380,
            name = "Flagstaff, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22420,
            name = "Flint, MI",
            csa_id = 220
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22500,
            name = "Florence, SC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22520,
            name = "Florence-Muscle Shoals, AL",
            csa_id = 250
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22540,
            name = "Fond du Lac, WI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22580,
            name = "Forest City, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22620,
            name = "Forrest City, AR",
            csa_id = 368
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22660,
            name = "Fort Collins-Loveland, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22700,
            name = "Fort Dodge, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22780,
            name = "Fort Leonard Wood, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22800,
            name = "Fort Madison, IA",
            csa_id = 161
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22820,
            name = "Fort Morgan, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22840,
            name = "Fort Payne, AL",
            csa_id = 290
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 22900,
            name = "Fort Smith, AR-OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23060,
            name = "Fort Wayne, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23140,
            name = "Frankfort, IN",
            csa_id = 320
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23180,
            name = "Frankfort, KY",
            csa_id = 336
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23190,
            name = "Franklin, KY",
            csa_id = 150
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23240,
            name = "Fredericksburg, TX",
            csa_id = 484
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23300,
            name = "Freeport, IL",
            csa_id = 466
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23340,
            name = "Fremont, NE",
            csa_id = 420
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23380,
            name = "Fremont, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23420,
            name = "Fresno, CA",
            csa_id = 260
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23460,
            name = "Gadsden, AL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23500,
            name = "Gaffney, SC",
            csa_id = 273
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23540,
            name = "Gainesville, FL",
            csa_id = 264
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23580,
            name = "Gainesville, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23620,
            name = "Gainesville, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23660,
            name = "Galesburg, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23680,
            name = "Gallipolis, OH"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23700,
            name = "Gallup, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23780,
            name = "Garden City, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23820,
            name = "Gardnerville Ranchos, NV-CA",
            csa_id = 456
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23900,
            name = "Gettysburg, PA",
            csa_id = 276
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23940,
            name = "Gillette, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 23980,
            name = "Glasgow, KY",
            csa_id = 150
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24020,
            name = "Glens Falls, NY",
            csa_id = 104
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24100,
            name = "Gloversville, NY",
            csa_id = 104
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24140,
            name = "Goldsboro, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24180,
            name = "Granbury, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24220,
            name = "Grand Forks, ND-MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24260,
            name = "Grand Island, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24300,
            name = "Grand Junction, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24330,
            name = "Grand Rapids, MN",
            csa_id = 228
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24340,
            name = "Grand Rapids-Wyoming-Kentwood, MI",
            csa_id = 266
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24420,
            name = "Grants Pass, OR",
            csa_id = 366
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24460,
            name = "Great Bend, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24500,
            name = "Great Falls, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24540,
            name = "Greeley, CO",
            csa_id = 216
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24580,
            name = "Green Bay, WI",
            csa_id = 267
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24600,
            name = "Greencastle, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24620,
            name = "Greeneville, TN",
            csa_id = 304
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24640,
            name = "Greenfield, MA",
            csa_id = 521
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24660,
            name = "Greensboro-High Point, NC",
            csa_id = 268
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24700,
            name = "Greensburg, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24740,
            name = "Greenville, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24780,
            name = "Greenville, NC",
            csa_id = 274
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24820,
            name = "Greenville, OH",
            csa_id = 212
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24860,
            name = "Greenville-Anderson-Greer, SC",
            csa_id = 273
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24900,
            name = "Greenwood, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24940,
            name = "Greenwood, SC",
            csa_id = 273
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 24980,
            name = "Grenada, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25020,
            name = "Guayama, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25060,
            name = "Gulfport-Biloxi, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25100,
            name = "Guymon, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25180,
            name = "Hagerstown-Martinsburg, MD-WV",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25200,
            name = "Hailey, ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25220,
            name = "Hammond, LA",
            csa_id = 132
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25260,
            name = "Hanford-Corcoran, CA",
            csa_id = 260
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25300,
            name = "Hannibal, MO",
            csa_id = 448
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25420,
            name = "Harrisburg-Carlisle, PA",
            csa_id = 276
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25460,
            name = "Harrison, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25500,
            name = "Harrisonburg, VA",
            csa_id = 277
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25540,
            name = "Hartford-West Hartford-East Hartford, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25580,
            name = "Hastings, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25620,
            name = "Hattiesburg, MS",
            csa_id = 279
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25700,
            name = "Hays, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25720,
            name = "Heber, UT",
            csa_id = 482
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25740,
            name = "Helena, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25770,
            name = "Hemlock Farms, PA",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25775,
            name = "Henderson, KY",
            csa_id = 241
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25780,
            name = "Henderson, NC",
            csa_id = 450
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25820,
            name = "Hereford, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25840,
            name = "Hermiston-Pendleton, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25850,
            name = "Hermitage, PA",
            csa_id = 430
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25860,
            name = "Hickory-Lenoir-Morganton, NC",
            csa_id = 172
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25880,
            name = "Hillsdale, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25900,
            name = "Hilo-Kailua, HI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25940,
            name = "Hilton Head Island-Bluffton-Port Royal, SC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 25980,
            name = "Hinesville, GA",
            csa_id = 496
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26020,
            name = "Hobbs, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26090,
            name = "Holland, MI",
            csa_id = 266
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26140,
            name = "Homosassa Springs, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26220,
            name = "Hood River, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26300,
            name = "Hot Springs, AR",
            csa_id = 284
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26340,
            name = "Houghton, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26380,
            name = "Houma-Bayou Cane-Thibodaux, LA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26420,
            name = "Houston-Pasadena-The Woodlands, TX",
            csa_id = 288
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26460,
            name = "Hudson, NY",
            csa_id = 104
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26500,
            name = "Huntingdon, PA",
            csa_id = 107
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26540,
            name = "Huntington, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26580,
            name = "Huntington-Ashland, WV-KY-OH",
            csa_id = 170
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26620,
            name = "Huntsville, AL",
            csa_id = 290
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26660,
            name = "Huntsville, TX",
            csa_id = 288
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26700,
            name = "Huron, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26740,
            name = "Hutchinson, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26780,
            name = "Hutchinson, MN",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26820,
            name = "Idaho Falls, ID",
            csa_id = 292
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26860,
            name = "Indiana, PA",
            csa_id = 430
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26900,
            name = "Indianapolis-Carmel-Greenwood, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 26980,
            name = "Iowa City, IA",
            csa_id = 168
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27020,
            name = "Iron Mountain, MI-WI",
            csa_id = 361
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27060,
            name = "Ithaca, NY",
            csa_id = 296
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27100,
            name = "Jackson, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27140,
            name = "Jackson, MS",
            csa_id = 298
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27180,
            name = "Jackson, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27220,
            name = "Jackson, WY-ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27260,
            name = "Jacksonville, FL",
            csa_id = 300
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27300,
            name = "Jacksonville, IL",
            csa_id = 522
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27340,
            name = "Jacksonville, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27380,
            name = "Jacksonville, TX",
            csa_id = 540
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27420,
            name = "Jamestown, ND"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27460,
            name = "Jamestown-Dunkirk, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27500,
            name = "Janesville-Beloit, WI",
            csa_id = 357
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27540,
            name = "Jasper, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27600,
            name = "Jefferson, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27620,
            name = "Jefferson City, MO",
            csa_id = 190
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27700,
            name = "Jesup, GA",
            csa_id = 496
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27740,
            name = "Johnson City, TN",
            csa_id = 304
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27780,
            name = "Johnstown, PA",
            csa_id = 306
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27860,
            name = "Jonesboro, AR",
            csa_id = 308
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27900,
            name = "Joplin, MO-KS",
            csa_id = 309
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27940,
            name = "Juneau, AK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 27980,
            name = "Kahului-Wailuku, HI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28020,
            name = "Kalamazoo-Portage, MI",
            csa_id = 310
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28060,
            name = "Kalispell, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28100,
            name = "Kankakee, IL",
            csa_id = 176
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28140,
            name = "Kansas City, MO-KS",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28180,
            name = "Kapaa, HI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28260,
            name = "Kearney, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28300,
            name = "Keene, NH",
            csa_id = 313
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28340,
            name = "Kendallville, IN",
            csa_id = 258
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28380,
            name = "Kennett, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28420,
            name = "Kennewick-Richland, WA",
            csa_id = 314
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28450,
            name = "Kenosha, WI",
            csa_id = 176
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28500,
            name = "Kerrville, TX",
            csa_id = 484
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28540,
            name = "Ketchikan, AK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28580,
            name = "Key West-Key Largo, FL",
            csa_id = 370
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28620,
            name = "Kill Devil Hills, NC",
            csa_id = 545
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28660,
            name = "Killeen-Temple, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28680,
            name = "Kingsland, GA",
            csa_id = 300
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28700,
            name = "Kingsport-Bristol, TN-VA",
            csa_id = 304
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28740,
            name = "Kingston, NY",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28780,
            name = "Kingsville, TX",
            csa_id = 204
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28820,
            name = "Kinston, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28860,
            name = "Kirksville, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28880,
            name = "Kiryas Joel-Poughkeepsie-Newburgh, NY",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28900,
            name = "Klamath Falls, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 28940,
            name = "Knoxville, TN",
            csa_id = 315
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29020,
            name = "Kokomo, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29060,
            name = "Laconia, NH",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29100,
            name = "La Crosse-Onalaska, WI-MN",
            csa_id = 317
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29180,
            name = "Lafayette, LA",
            csa_id = 318
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29200,
            name = "Lafayette-West Lafayette, IN",
            csa_id = 320
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29260,
            name = "La Grande, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29300,
            name = "LaGrange, GA-AL",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29340,
            name = "Lake Charles, LA",
            csa_id = 324
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29380,
            name = "Lake City, FL",
            csa_id = 264
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29420,
            name = "Lake Havasu City-Kingman, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29460,
            name = "Lakeland-Winter Haven, FL",
            csa_id = 422
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29470,
            name = "Lake of the Woods, VA",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29540,
            name = "Lancaster, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29620,
            name = "Lansing-East Lansing, MI",
            csa_id = 330
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29660,
            name = "Laramie, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29700,
            name = "Laredo, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29720,
            name = "Lares, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29740,
            name = "Las Cruces, NM",
            csa_id = 238
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29780,
            name = "Las Vegas, NM",
            csa_id = 105
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29820,
            name = "Las Vegas-Henderson-North Las Vegas, NV",
            csa_id = 332
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29860,
            name = "Laurel, MS",
            csa_id = 279
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29900,
            name = "Laurinburg, NC",
            csa_id = 246
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29940,
            name = "Lawrence, KS",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 29980,
            name = "Lawrenceburg, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30020,
            name = "Lawton, OK",
            csa_id = 334
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30060,
            name = "Lebanon, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30140,
            name = "Lebanon, PA",
            csa_id = 276
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30150,
            name = "Lebanon-Claremont, NH-VT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30180,
            name = "Le Mars, IA",
            csa_id = 512
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30260,
            name = "Lewisburg, PA",
            csa_id = 146
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30280,
            name = "Lewisburg, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30300,
            name = "Lewiston, ID-WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30340,
            name = "Lewiston-Auburn, ME",
            csa_id = 438
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30380,
            name = "Lewistown, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30420,
            name = "Lexington, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30460,
            name = "Lexington-Fayette, KY",
            csa_id = 336
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30500,
            name = "Lexington Park, MD",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30580,
            name = "Liberal, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30620,
            name = "Lima, OH",
            csa_id = 338
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30660,
            name = "Lincoln, IL",
            csa_id = 522
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30700,
            name = "Lincoln, NE",
            csa_id = 339
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30780,
            name = "Little Rock-North Little Rock-Conway, AR",
            csa_id = 340
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30820,
            name = "Lock Haven, PA",
            csa_id = 558
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30860,
            name = "Logan, UT-ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30900,
            name = "Logansport, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 30980,
            name = "Longview, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31020,
            name = "Longview-Kelso, WA",
            csa_id = 440
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31060,
            name = "Los Alamos, NM",
            csa_id = 105
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31080,
            name = "Los Angeles-Long Beach-Anaheim, CA",
            csa_id = 348
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31140,
            name = "Louisville/Jefferson County, KY-IN",
            csa_id = 350
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31180,
            name = "Lubbock, TX",
            csa_id = 352
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31220,
            name = "Ludington, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31260,
            name = "Lufkin, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31300,
            name = "Lumberton, NC",
            csa_id = 246
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31340,
            name = "Lynchburg, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31380,
            name = "Macomb, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31420,
            name = "Macon-Bibb County, GA",
            csa_id = 356
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31500,
            name = "Madison, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31540,
            name = "Madison, WI",
            csa_id = 357
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31580,
            name = "Madisonville, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31620,
            name = "Magnolia, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31680,
            name = "Malvern, AR",
            csa_id = 284
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31700,
            name = "Manchester-Nashua, NH",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31740,
            name = "Manhattan, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31820,
            name = "Manitowoc, WI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31860,
            name = "Mankato, MN",
            csa_id = 359
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31900,
            name = "Mansfield, OH",
            csa_id = 360
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31930,
            name = "Marietta, OH",
            csa_id = 425
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31940,
            name = "Marinette, WI-MI",
            csa_id = 361
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 31980,
            name = "Marion, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32000,
            name = "Marion, NC",
            csa_id = 172
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32020,
            name = "Marion, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32060,
            name = "Marion-Herrin, IL",
            csa_id = 166
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32100,
            name = "Marquette, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32140,
            name = "Marshall, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32180,
            name = "Marshall, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32260,
            name = "Marshalltown, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32280,
            name = "Martin, TN",
            csa_id = 542
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32300,
            name = "Martinsville, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32340,
            name = "Maryville, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32380,
            name = "Mason City, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32390,
            name = "Massena-Ogdensburg, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32420,
            name = "Mayagüez, PR",
            csa_id = 364
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32460,
            name = "Mayfield, KY",
            csa_id = 424
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32540,
            name = "McAlester, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32580,
            name = "McAllen-Edinburg-Mission, TX",
            csa_id = 365
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32620,
            name = "McComb, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32660,
            name = "McMinnville, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32700,
            name = "McPherson, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32740,
            name = "Meadville, PA",
            csa_id = 240
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32780,
            name = "Medford, OR",
            csa_id = 366
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32820,
            name = "Memphis, TN-MS-AR",
            csa_id = 368
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32860,
            name = "Menomonie, WI",
            csa_id = 232
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32900,
            name = "Merced, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 32940,
            name = "Meridian, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33020,
            name = "Mexico, MO",
            csa_id = 190
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33060,
            name = "Miami, OK",
            csa_id = 309
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33100,
            name = "Miami-Fort Lauderdale-West Palm Beach, FL",
            csa_id = 370
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33140,
            name = "Michigan City-La Porte, IN",
            csa_id = 176
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33180,
            name = "Middlesborough, KY",
            csa_id = 371
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33220,
            name = "Midland, MI",
            csa_id = 474
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33260,
            name = "Midland, TX",
            csa_id = 372
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33300,
            name = "Milledgeville, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33340,
            name = "Milwaukee-Waukesha, WI",
            csa_id = 376
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33380,
            name = "Minden, LA",
            csa_id = 508
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33420,
            name = "Mineral Wells, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33460,
            name = "Minneapolis-St. Paul-Bloomington, MN-WI",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33500,
            name = "Minot, ND"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33540,
            name = "Missoula, MT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33580,
            name = "Mitchell, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33620,
            name = "Moberly, MO",
            csa_id = 190
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33660,
            name = "Mobile, AL",
            csa_id = 380
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33700,
            name = "Modesto, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33740,
            name = "Monroe, LA",
            csa_id = 384
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33780,
            name = "Monroe, MI",
            csa_id = 220
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33860,
            name = "Montgomery, AL",
            csa_id = 388
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33900,
            name = "Monticello, IN",
            csa_id = 320
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33910,
            name = "Monticello, NY",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33940,
            name = "Montrose, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 33980,
            name = "Morehead City, NC",
            csa_id = 404
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34020,
            name = "Morgan City, LA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34060,
            name = "Morgantown, WV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34100,
            name = "Morristown, TN",
            csa_id = 315
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34140,
            name = "Moscow, ID",
            csa_id = 446
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34180,
            name = "Moses Lake, WA",
            csa_id = 393
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34220,
            name = "Moultrie, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34260,
            name = "Mountain Home, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34300,
            name = "Mountain Home, ID",
            csa_id = 147
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34340,
            name = "Mount Airy, NC",
            csa_id = 268
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34380,
            name = "Mount Pleasant, MI",
            csa_id = 394
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34420,
            name = "Mount Pleasant, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34460,
            name = "Mount Sterling, KY",
            csa_id = 336
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34500,
            name = "Mount Vernon, IL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34540,
            name = "Mount Vernon, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34580,
            name = "Mount Vernon-Anacortes, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34620,
            name = "Muncie, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34660,
            name = "Murray, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34680,
            name = "Murrells Inlet, SC",
            csa_id = 396
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34700,
            name = "Muscatine, IA",
            csa_id = 209
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34740,
            name = "Muskegon-Norton Shores, MI",
            csa_id = 266
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34780,
            name = "Muskogee, OK",
            csa_id = 538
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34820,
            name = "Myrtle Beach-Conway-North Myrtle Beach, SC",
            csa_id = 396
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34860,
            name = "Nacogdoches, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34880,
            name = "Nantucket, MA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34900,
            name = "Napa, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34940,
            name = "Naples-Marco Island, FL",
            csa_id = 163
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 34980,
            name = "Nashville-Davidson--Murfreesboro--Franklin, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35020,
            name = "Natchez, MS-LA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35060,
            name = "Natchitoches, LA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35100,
            name = "New Bern, NC",
            csa_id = 404
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35140,
            name = "Newberry, SC",
            csa_id = 192
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35220,
            name = "New Castle, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35300,
            name = "New Haven, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35340,
            name = "New Iberia, LA",
            csa_id = 318
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35380,
            name = "New Orleans-Metairie, LA",
            csa_id = 406
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35420,
            name = "New Philadelphia-Dover, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35440,
            name = "Newport, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35460,
            name = "Newport, TN",
            csa_id = 315
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35580,
            name = "New Ulm, MN",
            csa_id = 359
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35620,
            name = "New York-Newark-Jersey City, NY-NJ",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35660,
            name = "Niles, MI",
            csa_id = 515
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35700,
            name = "Nogales, AZ",
            csa_id = 536
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35740,
            name = "Norfolk, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35820,
            name = "North Platte, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35840,
            name = "North Port-Bradenton-Sarasota, FL",
            csa_id = 412
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35900,
            name = "North Wilkesboro, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35940,
            name = "Norwalk, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 35980,
            name = "Norwich-New London-Willimantic, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36020,
            name = "Oak Harbor, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36100,
            name = "Ocala, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36180,
            name = "Ocean Pines, MD",
            csa_id = 480
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36220,
            name = "Odessa, TX",
            csa_id = 372
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36260,
            name = "Ogden, UT",
            csa_id = 482
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36340,
            name = "Oil City, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36380,
            name = "Okeechobee, FL",
            csa_id = 370
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36420,
            name = "Oklahoma City, OK",
            csa_id = 416
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36460,
            name = "Olean, NY",
            csa_id = 160
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36500,
            name = "Olympia-Lacey-Tumwater, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36540,
            name = "Omaha, NE-IA",
            csa_id = 420
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36580,
            name = "Oneonta, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36620,
            name = "Ontario, OR-ID",
            csa_id = 147
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36660,
            name = "Opelousas, LA",
            csa_id = 318
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36700,
            name = "Orangeburg, SC",
            csa_id = 192
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36740,
            name = "Orlando-Kissimmee-Sanford, FL",
            csa_id = 422
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36780,
            name = "Oshkosh-Neenah, WI",
            csa_id = 118
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36820,
            name = "Oskaloosa, IA",
            csa_id = 218
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36830,
            name = "Othello, WA",
            csa_id = 393
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36837,
            name = "Ottawa, IL",
            csa_id = 176
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36840,
            name = "Ottawa, KS",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36900,
            name = "Ottumwa, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36940,
            name = "Owatonna, MN",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 36980,
            name = "Owensboro, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37020,
            name = "Owosso, MI",
            csa_id = 330
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37060,
            name = "Oxford, MS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37100,
            name = "Oxnard-Thousand Oaks-Ventura, CA",
            csa_id = 348
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37120,
            name = "Ozark, AL",
            csa_id = 222
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37140,
            name = "Paducah, KY-IL",
            csa_id = 424
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37220,
            name = "Pahrump, NV",
            csa_id = 332
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37260,
            name = "Palatka, FL",
            csa_id = 300
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37300,
            name = "Palestine, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37340,
            name = "Palm Bay-Melbourne-Titusville, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37420,
            name = "Pampa, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37460,
            name = "Panama City-Panama City Beach, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37500,
            name = "Paragould, AR",
            csa_id = 308
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37540,
            name = "Paris, TN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37580,
            name = "Paris, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37620,
            name = "Parkersburg-Vienna, WV",
            csa_id = 425
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37740,
            name = "Payson, AZ",
            csa_id = 429
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37800,
            name = "Pella, IA",
            csa_id = 218
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37860,
            name = "Pensacola-Ferry Pass-Brent, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37900,
            name = "Peoria, IL",
            csa_id = 427
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37940,
            name = "Peru, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37950,
            name = "Petoskey, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 37980,
            name = "Philadelphia-Camden-Wilmington, PA-NJ-DE-MD",
            csa_id = 428
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38060,
            name = "Phoenix-Mesa-Chandler, AZ",
            csa_id = 429
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38100,
            name = "Picayune, MS",
            csa_id = 406
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38180,
            name = "Pierre, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38210,
            name = "Pikeville, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38220,
            name = "Pine Bluff, AR",
            csa_id = 340
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38240,
            name = "Pinehurst-Southern Pines, NC",
            csa_id = 246
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38260,
            name = "Pittsburg, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38300,
            name = "Pittsburgh, PA",
            csa_id = 430
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38340,
            name = "Pittsfield, MA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38380,
            name = "Plainview, TX",
            csa_id = 352
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38420,
            name = "Platteville, WI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38460,
            name = "Plattsburgh, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38500,
            name = "Plymouth, IN",
            csa_id = 515
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38540,
            name = "Pocatello, ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38620,
            name = "Ponca City, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38660,
            name = "Ponce, PR",
            csa_id = 434
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38700,
            name = "Pontiac, IL",
            csa_id = 145
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38740,
            name = "Poplar Bluff, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38820,
            name = "Port Angeles, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38860,
            name = "Portland-South Portland, ME",
            csa_id = 438
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38900,
            name = "Portland-Vancouver-Hillsboro, OR-WA",
            csa_id = 440
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38920,
            name = "Port Lavaca, TX",
            csa_id = 544
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 38940,
            name = "Port St. Lucie, FL",
            csa_id = 370
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39020,
            name = "Portsmouth, OH",
            csa_id = 170
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39040,
            name = "Port Townsend, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39060,
            name = "Pottsville, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39150,
            name = "Prescott Valley-Prescott, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39220,
            name = "Price, UT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39300,
            name = "Providence-Warwick, RI-MA",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39340,
            name = "Provo-Orem-Lehi, UT",
            csa_id = 482
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39380,
            name = "Pueblo, CO",
            csa_id = 444
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39420,
            name = "Pullman, WA",
            csa_id = 446
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39460,
            name = "Punta Gorda, FL",
            csa_id = 412
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39480,
            name = "Putnam, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39500,
            name = "Quincy, IL-MO",
            csa_id = 448
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39540,
            name = "Racine-Mount Pleasant, WI",
            csa_id = 376
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39580,
            name = "Raleigh-Cary, NC",
            csa_id = 450
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39660,
            name = "Rapid City, SD",
            csa_id = 452
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39700,
            name = "Raymondville, TX",
            csa_id = 154
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39740,
            name = "Reading, PA",
            csa_id = 428
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39780,
            name = "Red Bluff, CA",
            csa_id = 454
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39820,
            name = "Redding, CA",
            csa_id = 454
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39860,
            name = "Red Wing, MN",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39900,
            name = "Reno, NV",
            csa_id = 456
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39940,
            name = "Rexburg, ID",
            csa_id = 292
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39960,
            name = "Rice Lake, WI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 39980,
            name = "Richmond, IN",
            csa_id = 458
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40060,
            name = "Richmond, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40080,
            name = "Richmond-Berea, KY",
            csa_id = 336
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40090,
            name = "Rifle, CO",
            csa_id = 233
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40100,
            name = "Rio Grande City-Roma, TX",
            csa_id = 365
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40140,
            name = "Riverside-San Bernardino-Ontario, CA",
            csa_id = 348
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40180,
            name = "Riverton, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40220,
            name = "Roanoke, VA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40260,
            name = "Roanoke Rapids, NC",
            csa_id = 468
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40300,
            name = "Rochelle, IL",
            csa_id = 466
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40340,
            name = "Rochester, MN",
            csa_id = 462
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40380,
            name = "Rochester, NY",
            csa_id = 464
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40420,
            name = "Rockford, IL",
            csa_id = 466
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40460,
            name = "Rockingham, NC",
            csa_id = 246
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40540,
            name = "Rock Springs, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40580,
            name = "Rocky Mount, NC",
            csa_id = 468
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40620,
            name = "Rolla, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40660,
            name = "Rome, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40700,
            name = "Roseburg, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40740,
            name = "Roswell, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40760,
            name = "Ruidoso, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40770,
            name = "Russellville, AL",
            csa_id = 250
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40780,
            name = "Russellville, AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40820,
            name = "Ruston, LA",
            csa_id = 384
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40860,
            name = "Rutland, VT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40900,
            name = "Sacramento-Roseville-Folsom, CA",
            csa_id = 472
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40940,
            name = "Safford, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 40980,
            name = "Saginaw, MI",
            csa_id = 474
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41060,
            name = "St. Cloud, MN",
            csa_id = 378
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41100,
            name = "St. George, UT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41140,
            name = "St. Joseph, MO-KS",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41180,
            name = "St. Louis, MO-IL",
            csa_id = 476
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41260,
            name = "St. Marys, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41400,
            name = "Salem, OH",
            csa_id = 566
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41420,
            name = "Salem, OR",
            csa_id = 440
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41460,
            name = "Salina, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41500,
            name = "Salinas, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41540,
            name = "Salisbury, MD",
            csa_id = 480
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41620,
            name = "Salt Lake City-Murray, UT",
            csa_id = 482
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41660,
            name = "San Angelo, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41700,
            name = "San Antonio-New Braunfels, TX",
            csa_id = 484
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41740,
            name = "San Diego-Chula Vista-Carlsbad, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41760,
            name = "Sandpoint, ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41780,
            name = "Sandusky, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41820,
            name = "Sanford, NC",
            csa_id = 450
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41860,
            name = "San Francisco-Oakland-Fremont, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41940,
            name = "San Jose-Sunnyvale-Santa Clara, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 41980,
            name = "San Juan-Bayamón-Caguas, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42020,
            name = "San Luis Obispo-Paso Robles, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42100,
            name = "Santa Cruz-Watsonville, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42140,
            name = "Santa Fe, NM",
            csa_id = 105
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42200,
            name = "Santa Maria-Santa Barbara, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42220,
            name = "Santa Rosa-Petaluma, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42300,
            name = "Sault Ste. Marie, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42340,
            name = "Savannah, GA",
            csa_id = 496
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42380,
            name = "Sayre, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42420,
            name = "Scottsbluff, NE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42460,
            name = "Scottsboro, AL",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42540,
            name = "Scranton--Wilkes-Barre, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42580,
            name = "Seaford, DE"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42620,
            name = "Searcy, AR",
            csa_id = 340
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42660,
            name = "Seattle-Tacoma-Bellevue, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42680,
            name = "Sebastian-Vero Beach-West Vero Corridor, FL",
            csa_id = 370
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42700,
            name = "Sebring, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42740,
            name = "Sedalia, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42780,
            name = "Selinsgrove, PA",
            csa_id = 146
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42820,
            name = "Selma, AL",
            csa_id = 388
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42860,
            name = "Seneca, SC",
            csa_id = 273
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42900,
            name = "Seneca Falls, NY",
            csa_id = 464
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42940,
            name = "Sevierville, TN",
            csa_id = 315
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 42980,
            name = "Seymour, IN",
            csa_id = 294
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43020,
            name = "Shawano, WI",
            csa_id = 267
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43060,
            name = "Shawnee, OK",
            csa_id = 416
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43100,
            name = "Sheboygan, WI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43140,
            name = "Shelby-Kings Mountain, NC",
            csa_id = 172
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43180,
            name = "Shelbyville, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43220,
            name = "Shelton, WA",
            csa_id = 500
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43260,
            name = "Sheridan, WY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43300,
            name = "Sherman-Denison, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43320,
            name = "Show Low, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43340,
            name = "Shreveport-Bossier City, LA",
            csa_id = 508
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43380,
            name = "Sidney, OH",
            csa_id = 212
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43420,
            name = "Sierra Vista-Douglas, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43460,
            name = "Sikeston, MO",
            csa_id = 164
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43500,
            name = "Silver City, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43580,
            name = "Sioux City, IA-NE-SD",
            csa_id = 512
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43620,
            name = "Sioux Falls, SD-MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43640,
            name = "Slidell-Mandeville-Covington, LA",
            csa_id = 406
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43660,
            name = "Snyder, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43700,
            name = "Somerset, KY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43740,
            name = "Somerset, PA",
            csa_id = 306
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43760,
            name = "Sonora, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43780,
            name = "South Bend-Mishawaka, IN-MI",
            csa_id = 515
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43890,
            name = "Sparta, WI",
            csa_id = 317
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43900,
            name = "Spartanburg, SC",
            csa_id = 273
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43940,
            name = "Spearfish, SD",
            csa_id = 452
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 43980,
            name = "Spencer, IA",
            csa_id = 517
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44020,
            name = "Spirit Lake, IA",
            csa_id = 517
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44060,
            name = "Spokane-Spokane Valley, WA",
            csa_id = 518
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44100,
            name = "Springfield, IL",
            csa_id = 522
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44140,
            name = "Springfield, MA",
            csa_id = 521
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44180,
            name = "Springfield, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44220,
            name = "Springfield, OH",
            csa_id = 212
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44260,
            name = "Starkville, MS",
            csa_id = 523
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44300,
            name = "State College, PA",
            csa_id = 524
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44340,
            name = "Statesboro, GA",
            csa_id = 496
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44420,
            name = "Staunton-Stuarts Draft, VA",
            csa_id = 277
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44460,
            name = "Steamboat Springs, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44500,
            name = "Stephenville, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44540,
            name = "Sterling, CO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44580,
            name = "Sterling, IL",
            csa_id = 221
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44620,
            name = "Stevens Point-Plover, WI",
            csa_id = 554
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44660,
            name = "Stillwater, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44700,
            name = "Stockton-Lodi, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44740,
            name = "Storm Lake, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44780,
            name = "Sturgis, MI",
            csa_id = 310
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44860,
            name = "Sulphur Springs, TX",
            csa_id = 206
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44900,
            name = "Summerville, GA",
            csa_id = 174
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44940,
            name = "Sumter, SC",
            csa_id = 192
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 44980,
            name = "Sunbury, PA",
            csa_id = 146
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45000,
            name = "Susanville, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45020,
            name = "Sweetwater, TX",
            csa_id = 101
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45060,
            name = "Syracuse, NY",
            csa_id = 532
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45140,
            name = "Tahlequah, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45180,
            name = "Talladega-Sylacauga, AL",
            csa_id = 142
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45220,
            name = "Tallahassee, FL",
            csa_id = 533
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45300,
            name = "Tampa-St. Petersburg-Clearwater, FL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45340,
            name = "Taos, NM"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45380,
            name = "Taylorville, IL",
            csa_id = 522
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45460,
            name = "Terre Haute, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45500,
            name = "Texarkana, TX-AR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45520,
            name = "The Dalles, OR"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45580,
            name = "Thomaston, GA",
            csa_id = 122
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45620,
            name = "Thomasville, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45660,
            name = "Tiffin, OH",
            csa_id = 248
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45700,
            name = "Tifton, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45740,
            name = "Toccoa, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45780,
            name = "Toledo, OH"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45820,
            name = "Topeka, KS"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45860,
            name = "Torrington, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45880,
            name = "Town of Pecos, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45900,
            name = "Traverse City, MI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45940,
            name = "Trenton-Princeton, NJ",
            csa_id = 408
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 45980,
            name = "Troy, AL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46020,
            name = "Truckee-Grass Valley, CA",
            csa_id = 472
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46060,
            name = "Tucson, AZ",
            csa_id = 536
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46100,
            name = "Tullahoma-Manchester, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46140,
            name = "Tulsa, OK",
            csa_id = 538
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46180,
            name = "Tupelo, MS",
            csa_id = 539
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46220,
            name = "Tuscaloosa, AL"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46300,
            name = "Twin Falls, ID"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46340,
            name = "Tyler, TX",
            csa_id = 540
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46380,
            name = "Ukiah, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46460,
            name = "Union City, TN",
            csa_id = 542
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46500,
            name = "Urbana, OH",
            csa_id = 212
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46520,
            name = "Urban Honolulu, HI"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46540,
            name = "Utica-Rome, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46580,
            name = "Utuado, PR",
            csa_id = 490
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46620,
            name = "Uvalde, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46660,
            name = "Valdosta, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46700,
            name = "Vallejo, CA",
            csa_id = 488
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46780,
            name = "Van Wert, OH",
            csa_id = 338
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46820,
            name = "Vermillion, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46860,
            name = "Vernal, UT"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46900,
            name = "Vernon, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 46980,
            name = "Vicksburg, MS",
            csa_id = 298
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47020,
            name = "Victoria, TX",
            csa_id = 544
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47080,
            name = "Vidalia, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47180,
            name = "Vincennes, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47220,
            name = "Vineland, NJ",
            csa_id = 428
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47240,
            name = "Vineyard Haven, MA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47260,
            name = "Virginia Beach-Chesapeake-Norfolk, VA-NC",
            csa_id = 545
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47300,
            name = "Visalia, CA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47340,
            name = "Wabash, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47380,
            name = "Waco, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47420,
            name = "Wahpeton, ND-MN",
            csa_id = 244
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47460,
            name = "Walla Walla, WA",
            csa_id = 314
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47540,
            name = "Wapakoneta, OH",
            csa_id = 338
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47580,
            name = "Warner Robins, GA",
            csa_id = 356
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47620,
            name = "Warren, PA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47660,
            name = "Warrensburg, MO",
            csa_id = 312
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47700,
            name = "Warsaw, IN",
            csa_id = 515
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47780,
            name = "Washington, IN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47820,
            name = "Washington, NC",
            csa_id = 274
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47900,
            name = "Washington-Arlington-Alexandria, DC-VA-MD-WV",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47920,
            name = "Washington Court House, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47930,
            name = "Waterbury-Shelton, CT",
            csa_id = 405
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47940,
            name = "Waterloo-Cedar Falls, IA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 47980,
            name = "Watertown, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48020,
            name = "Watertown-Fort Atkinson, WI",
            csa_id = 376
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48060,
            name = "Watertown-Fort Drum, NY"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48140,
            name = "Wausau, WI",
            csa_id = 554
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48180,
            name = "Waycross, GA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48200,
            name = "Waynesville, NC",
            csa_id = 120
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48220,
            name = "Weatherford, OK",
            csa_id = 555
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48260,
            name = "Weirton-Steubenville, WV-OH",
            csa_id = 430
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48300,
            name = "Wenatchee-East Wenatchee, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48460,
            name = "West Plains, MO"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48540,
            name = "Wheeling, WV-OH"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48580,
            name = "Whitewater-Elkhorn, WI",
            csa_id = 376
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48620,
            name = "Wichita, KS",
            csa_id = 556
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48660,
            name = "Wichita Falls, TX"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48680,
            name = "Wildwood-The Villages, FL",
            csa_id = 422
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48700,
            name = "Williamsport, PA",
            csa_id = 558
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48780,
            name = "Williston, ND"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48820,
            name = "Willmar, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48900,
            name = "Wilmington, NC"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48940,
            name = "Wilmington, OH",
            csa_id = 178
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 48980,
            name = "Wilson, NC",
            csa_id = 468
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49010,
            name = "Winchester, TN",
            csa_id = 400
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49020,
            name = "Winchester, VA-WV",
            csa_id = 548
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49080,
            name = "Winnemucca, NV"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49100,
            name = "Winona, MN",
            csa_id = 462
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49180,
            name = "Winston-Salem, NC",
            csa_id = 268
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49220,
            name = "Wisconsin Rapids-Marshfield, WI",
            csa_id = 554
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49260,
            name = "Woodward, OK"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49300,
            name = "Wooster, OH",
            csa_id = 184
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49340,
            name = "Worcester, MA",
            csa_id = 148
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49380,
            name = "Worthington, MN"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49420,
            name = "Yakima, WA"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49460,
            name = "Yankton, SD"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49620,
            name = "York-Hanover, PA",
            csa_id = 276
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49660,
            name = "Youngstown-Warren, OH",
            csa_id = 566
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49700,
            name = "Yuba City, CA",
            csa_id = 472
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49740,
            name = "Yuma, AZ"
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49780,
            name = "Zanesville, OH",
            csa_id = 198
        )
        new_cbsa.save()
    

        new_cbsa = CoreBaseStatisticalArea(
            id = 49820,
            name = "Zapata, TX"
        )
        new_cbsa.save()
    