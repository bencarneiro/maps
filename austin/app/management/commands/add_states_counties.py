from django.core.management.base import BaseCommand
from app.models import State, County


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        State.objects.all().delete()
        County.objects.all().delete()
        new_state = State(
            id = 1,
            name = 'ALABAMA'
        )
        new_state.save()
    

        new_state = State(
            id = 2,
            name = 'ALASKA'
        )
        new_state.save()
    

        new_state = State(
            id = 4,
            name = 'ARIZONA'
        )
        new_state.save()
    

        new_state = State(
            id = 5,
            name = 'ARKANSAS'
        )
        new_state.save()
    

        new_state = State(
            id = 6,
            name = 'CALIFORNIA'
        )
        new_state.save()
    

        new_state = State(
            id = 8,
            name = 'COLORADO'
        )
        new_state.save()
    

        new_state = State(
            id = 9,
            name = 'CONNECTICUT'
        )
        new_state.save()
    

        new_state = State(
            id = 10,
            name = 'DELAWARE'
        )
        new_state.save()
    

        new_state = State(
            id = 11,
            name = 'DISTRICTOFCOLUMBIA'
        )
        new_state.save()
    

        new_state = State(
            id = 12,
            name = 'FLORIDA'
        )
        new_state.save()
    

        new_state = State(
            id = 13,
            name = 'GEORGIA'
        )
        new_state.save()
    

        new_state = State(
            id = 15,
            name = 'HAWAII'
        )
        new_state.save()
    

        new_state = State(
            id = 16,
            name = 'IDAHO'
        )
        new_state.save()
    

        new_state = State(
            id = 17,
            name = 'ILLINOIS'
        )
        new_state.save()
    

        new_state = State(
            id = 18,
            name = 'INDIANA'
        )
        new_state.save()
    

        new_state = State(
            id = 19,
            name = 'IOWA'
        )
        new_state.save()
    

        new_state = State(
            id = 20,
            name = 'KANSAS'
        )
        new_state.save()
    

        new_state = State(
            id = 21,
            name = 'KENTUCKY'
        )
        new_state.save()
    

        new_state = State(
            id = 22,
            name = 'LOUISIANA'
        )
        new_state.save()
    

        new_state = State(
            id = 23,
            name = 'MAINE'
        )
        new_state.save()
    

        new_state = State(
            id = 24,
            name = 'MARYLAND'
        )
        new_state.save()
    

        new_state = State(
            id = 25,
            name = 'MASSACHUSETTS'
        )
        new_state.save()
    

        new_state = State(
            id = 26,
            name = 'MICHIGAN'
        )
        new_state.save()
    

        new_state = State(
            id = 27,
            name = 'MINNESOTA'
        )
        new_state.save()
    

        new_state = State(
            id = 28,
            name = 'MISSISSIPPI'
        )
        new_state.save()
    

        new_state = State(
            id = 29,
            name = 'MISSOURI'
        )
        new_state.save()
    

        new_state = State(
            id = 30,
            name = 'MONTANA'
        )
        new_state.save()
    

        new_state = State(
            id = 31,
            name = 'NEBRASKA'
        )
        new_state.save()
    

        new_state = State(
            id = 32,
            name = 'NEVADA'
        )
        new_state.save()
    

        new_state = State(
            id = 33,
            name = 'NEWHAMPSHIRE'
        )
        new_state.save()
    

        new_state = State(
            id = 34,
            name = 'NEWJERSEY'
        )
        new_state.save()
    

        new_state = State(
            id = 35,
            name = 'NEWMEXICO'
        )
        new_state.save()
    

        new_state = State(
            id = 36,
            name = 'NEWYORK'
        )
        new_state.save()
    

        new_state = State(
            id = 37,
            name = 'NORTHCAROLINA'
        )
        new_state.save()
    

        new_state = State(
            id = 38,
            name = 'NORTHDAKOTA'
        )
        new_state.save()
    

        new_state = State(
            id = 39,
            name = 'OHIO'
        )
        new_state.save()
    

        new_state = State(
            id = 40,
            name = 'OKLAHOMA'
        )
        new_state.save()
    

        new_state = State(
            id = 41,
            name = 'OREGON'
        )
        new_state.save()
    

        new_state = State(
            id = 42,
            name = 'PENNSYLVANIA'
        )
        new_state.save()
    

        new_state = State(
            id = 44,
            name = 'RHODEISLAND'
        )
        new_state.save()
    

        new_state = State(
            id = 45,
            name = 'SOUTHCAROLINA'
        )
        new_state.save()
    

        new_state = State(
            id = 46,
            name = 'SOUTHDAKOTA'
        )
        new_state.save()
    

        new_state = State(
            id = 47,
            name = 'TENNESSEE'
        )
        new_state.save()
    

        new_state = State(
            id = 48,
            name = 'TEXAS'
        )
        new_state.save()
    

        new_state = State(
            id = 49,
            name = 'UTAH'
        )
        new_state.save()
    

        new_state = State(
            id = 50,
            name = 'VERMONT'
        )
        new_state.save()
    

        new_state = State(
            id = 51,
            name = 'VIRGINIA'
        )
        new_state.save()
    

        new_state = State(
            id = 53,
            name = 'WASHINGTON'
        )
        new_state.save()
    

        new_state = State(
            id = 54,
            name = 'WESTVIRGINIA'
        )
        new_state.save()
    

        new_state = State(
            id = 55,
            name = 'WISCONSIN'
        )
        new_state.save()
    

        new_state = State(
            id = 56,
            name = 'WYOMING'
        )
        new_state.save()
        
        new_county = County(
            state_id=1,
            fips = 1000,
            name = 'Alabama'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1001,
            name = 'AutaugaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1003,
            name = 'BaldwinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1005,
            name = 'BarbourCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1007,
            name = 'BibbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1009,
            name = 'BlountCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1011,
            name = 'BullockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1013,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1015,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1017,
            name = 'ChambersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1019,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1021,
            name = 'ChiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1023,
            name = 'ChoctawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1025,
            name = 'ClarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1027,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1029,
            name = 'CleburneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1031,
            name = 'CoffeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1033,
            name = 'ColbertCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1035,
            name = 'ConecuhCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1037,
            name = 'CoosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1039,
            name = 'CovingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1041,
            name = 'CrenshawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1043,
            name = 'CullmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1045,
            name = 'DaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1047,
            name = 'DallasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1049,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1051,
            name = 'ElmoreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1053,
            name = 'EscambiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1055,
            name = 'EtowahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1057,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1059,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1061,
            name = 'GenevaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1063,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1065,
            name = 'HaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1067,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1069,
            name = 'HoustonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1071,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1073,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1075,
            name = 'LamarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1077,
            name = 'LauderdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1079,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1081,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1083,
            name = 'LimestoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1085,
            name = 'LowndesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1087,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1089,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1091,
            name = 'MarengoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1093,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1095,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1097,
            name = 'MobileCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1099,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1101,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1103,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1105,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1107,
            name = 'PickensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1109,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1111,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1113,
            name = 'RussellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1115,
            name = 'St.ClairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1117,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1119,
            name = 'SumterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1121,
            name = 'TalladegaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1123,
            name = 'TallapoosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1125,
            name = 'TuscaloosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1127,
            name = 'WalkerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1129,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1131,
            name = 'WilcoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=1,
            fips = 1133,
            name = 'WinstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2000,
            name = 'Alaska'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2013,
            name = 'AleutiansEastBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2016,
            name = 'AleutiansWestCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2020,
            name = 'AnchorageBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2050,
            name = 'BethelCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2060,
            name = 'BristolBayBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 20681990,
            name = 'DenaliBorough(createdafter)'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2070,
            name = 'DillinghamCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2090,
            name = 'FairbanksNorthStarBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2100,
            name = 'HainesBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2110,
            name = 'JuneauBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2122,
            name = 'KenaiPeninsulaBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2130,
            name = 'KetchikanGatewayBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2150,
            name = 'KodiakIslandBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2164,
            name = 'LakeandPeninsulaBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2170,
            name = 'Matanuska-SusitnaBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2180,
            name = 'NomeCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2185,
            name = 'NorthSlopeBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2188,
            name = 'NorthwestArcticBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2201,
            name = 'PrinceofWales-OuterKetchikanCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2220,
            name = 'SitkaBorough'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 22311990,
            name = 'Skagway-Yakutat-AngoonCensusArea(CensusArea)'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 22321990,
            name = 'Skagway-Hoonah-AngoonCensusArea(createdafter)'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2240,
            name = 'SoutheastFairbanksCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2261,
            name = 'Valdez-CordovaCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2270,
            name = 'WadeHamptonCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2280,
            name = 'Wrangell-PetersburgCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 22821990,
            name = 'YakutatBorough(createdafter)'
        )
        new_county.save()
    

        new_county = County(
            state_id=2,
            fips = 2290,
            name = 'Yukon-KoyukukCensusArea'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4000,
            name = 'Arizona'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4001,
            name = 'ApacheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4003,
            name = 'CochiseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4005,
            name = 'CoconinoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4007,
            name = 'GilaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4009,
            name = 'GrahamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4011,
            name = 'GreenleeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4012,
            name = 'LaPazCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4013,
            name = 'MaricopaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4015,
            name = 'MohaveCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4017,
            name = 'NavajoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4019,
            name = 'PimaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4021,
            name = 'PinalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4023,
            name = 'SantaCruzCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4025,
            name = 'YavapaiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=4,
            fips = 4027,
            name = 'YumaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5000,
            name = 'Arkansas'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5001,
            name = 'ArkansasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5003,
            name = 'AshleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5005,
            name = 'BaxterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5007,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5009,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5011,
            name = 'BradleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5013,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5015,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5017,
            name = 'ChicotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5019,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5021,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5023,
            name = 'CleburneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5025,
            name = 'ClevelandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5027,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5029,
            name = 'ConwayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5031,
            name = 'CraigheadCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5033,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5035,
            name = 'CrittendenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5037,
            name = 'CrossCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5039,
            name = 'DallasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5041,
            name = 'DeshaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5043,
            name = 'DrewCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5045,
            name = 'FaulknerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5047,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5049,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5051,
            name = 'GarlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5053,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5055,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5057,
            name = 'HempsteadCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5059,
            name = 'HotSpringCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5061,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5063,
            name = 'IndependenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5065,
            name = 'IzardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5067,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5069,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5071,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5073,
            name = 'LafayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5075,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5077,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5079,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5081,
            name = 'LittleRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5083,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5085,
            name = 'LonokeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5087,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5089,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5091,
            name = 'MillerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5093,
            name = 'MississippiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5095,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5097,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5099,
            name = 'NevadaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5101,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5103,
            name = 'OuachitaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5105,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5107,
            name = 'PhillipsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5109,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5111,
            name = 'PoinsettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5113,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5115,
            name = 'PopeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5117,
            name = 'PrairieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5119,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5121,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5123,
            name = 'St.FrancisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5125,
            name = 'SalineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5127,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5129,
            name = 'SearcyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5131,
            name = 'SebastianCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5133,
            name = 'SevierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5135,
            name = 'SharpCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5137,
            name = 'StoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5139,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5141,
            name = 'VanBurenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5143,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5145,
            name = 'WhiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5147,
            name = 'WoodruffCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=5,
            fips = 5149,
            name = 'YellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6000,
            name = 'California'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6001,
            name = 'AlamedaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6003,
            name = 'AlpineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6005,
            name = 'AmadorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6007,
            name = 'ButteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6009,
            name = 'CalaverasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6011,
            name = 'ColusaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6013,
            name = 'ContraCostaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6015,
            name = 'DelNorteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6017,
            name = 'ElDoradoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6019,
            name = 'FresnoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6021,
            name = 'GlennCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6023,
            name = 'HumboldtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6025,
            name = 'ImperialCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6027,
            name = 'InyoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6029,
            name = 'KernCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6031,
            name = 'KingsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6033,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6035,
            name = 'LassenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6037,
            name = 'LosAngelesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6039,
            name = 'MaderaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6041,
            name = 'MarinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6043,
            name = 'MariposaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6045,
            name = 'MendocinoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6047,
            name = 'MercedCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6049,
            name = 'ModocCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6051,
            name = 'MonoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6053,
            name = 'MontereyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6055,
            name = 'NapaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6057,
            name = 'NevadaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6059,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6061,
            name = 'PlacerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6063,
            name = 'PlumasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6065,
            name = 'RiversideCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6067,
            name = 'SacramentoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6069,
            name = 'SanBenitoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6071,
            name = 'SanBernardinoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6073,
            name = 'SanDiegoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6075,
            name = 'SanFranciscoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6077,
            name = 'SanJoaquinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6079,
            name = 'SanLuisObispoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6081,
            name = 'SanMateoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6083,
            name = 'SantaBarbaraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6085,
            name = 'SantaClaraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6087,
            name = 'SantaCruzCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6089,
            name = 'ShastaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6091,
            name = 'SierraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6093,
            name = 'SiskiyouCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6095,
            name = 'SolanoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6097,
            name = 'SonomaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6099,
            name = 'StanislausCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6101,
            name = 'SutterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6103,
            name = 'TehamaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6105,
            name = 'TrinityCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6107,
            name = 'TulareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6109,
            name = 'TuolumneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6111,
            name = 'VenturaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6113,
            name = 'YoloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=6,
            fips = 6115,
            name = 'YubaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8000,
            name = 'Colorado'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8003,
            name = 'AlamosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8005,
            name = 'ArapahoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8007,
            name = 'ArchuletaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8009,
            name = 'BacaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8011,
            name = 'BentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8013,
            name = 'BoulderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8015,
            name = 'ChaffeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8017,
            name = 'CheyenneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8019,
            name = 'ClearCreekCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8021,
            name = 'ConejosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8023,
            name = 'CostillaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8025,
            name = 'CrowleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8027,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8029,
            name = 'DeltaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8031,
            name = 'DenverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8033,
            name = 'DoloresCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8035,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8037,
            name = 'EagleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8039,
            name = 'ElbertCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8041,
            name = 'ElPasoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8043,
            name = 'FremontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8045,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8047,
            name = 'GilpinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8049,
            name = 'GrandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8051,
            name = 'GunnisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8053,
            name = 'HinsdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8055,
            name = 'HuerfanoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8057,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8059,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8061,
            name = 'KiowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8063,
            name = 'KitCarsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8065,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8067,
            name = 'LaPlataCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8069,
            name = 'LarimerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8071,
            name = 'LasAnimasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8073,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8075,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8077,
            name = 'MesaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8079,
            name = 'MineralCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8081,
            name = 'MoffatCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8083,
            name = 'MontezumaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8085,
            name = 'MontroseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8087,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8089,
            name = 'OteroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8091,
            name = 'OurayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8093,
            name = 'ParkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8095,
            name = 'PhillipsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8097,
            name = 'PitkinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8099,
            name = 'ProwersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8101,
            name = 'PuebloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8103,
            name = 'RioBlancoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8105,
            name = 'RioGrandeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8107,
            name = 'RouttCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8109,
            name = 'SaguacheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8111,
            name = 'SanJuanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8113,
            name = 'SanMiguelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8115,
            name = 'SedgwickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8117,
            name = 'SummitCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8119,
            name = 'TellerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8121,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8123,
            name = 'WeldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=8,
            fips = 8125,
            name = 'YumaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9000,
            name = 'Connecticut'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9001,
            name = 'FairfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9003,
            name = 'HartfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9005,
            name = 'LitchfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9007,
            name = 'MiddlesexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9009,
            name = 'NewHavenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9011,
            name = 'NewLondonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9013,
            name = 'TollandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=9,
            fips = 9015,
            name = 'WindhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=10,
            fips = 10000,
            name = 'Delaware'
        )
        new_county.save()
    

        new_county = County(
            state_id=10,
            fips = 10001,
            name = 'KentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=10,
            fips = 10003,
            name = 'NewCastleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=10,
            fips = 10005,
            name = 'SussexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=11,
            fips = 11000,
            name = 'DistrictofColumbia'
        )
        new_county.save()
    

        new_county = County(
            state_id=11,
            fips = 11001,
            name = 'DistrictofColumbia'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12000,
            name = 'Florida'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12001,
            name = 'AlachuaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12003,
            name = 'BakerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12005,
            name = 'BayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12007,
            name = 'BradfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12009,
            name = 'BrevardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12011,
            name = 'BrowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12013,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12015,
            name = 'CharlotteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12017,
            name = 'CitrusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12019,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12021,
            name = 'CollierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12023,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12025,
            name = 'DadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12027,
            name = 'DeSotoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12029,
            name = 'DixieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12031,
            name = 'DuvalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12033,
            name = 'EscambiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12035,
            name = 'FlaglerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12037,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12039,
            name = 'GadsdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12041,
            name = 'GilchristCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12043,
            name = 'GladesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12045,
            name = 'GulfCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12047,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12049,
            name = 'HardeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12051,
            name = 'HendryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12053,
            name = 'HernandoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12055,
            name = 'HighlandsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12057,
            name = 'HillsboroughCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12059,
            name = 'HolmesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12061,
            name = 'IndianRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12063,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12065,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12067,
            name = 'LafayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12069,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12071,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12073,
            name = 'LeonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12075,
            name = 'LevyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12077,
            name = 'LibertyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12079,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12081,
            name = 'ManateeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12083,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12085,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12087,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12089,
            name = 'NassauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12091,
            name = 'OkaloosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12093,
            name = 'OkeechobeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12095,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12097,
            name = 'OsceolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12099,
            name = 'PalmBeachCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12101,
            name = 'PascoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12103,
            name = 'PinellasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12105,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12107,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12109,
            name = 'St.JohnsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12111,
            name = 'St.LucieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12113,
            name = 'SantaRosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12115,
            name = 'SarasotaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12117,
            name = 'SeminoleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12119,
            name = 'SumterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12121,
            name = 'SuwanneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12123,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12125,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12127,
            name = 'VolusiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12129,
            name = 'WakullaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12131,
            name = 'WaltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=12,
            fips = 12133,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13000,
            name = 'Georgia'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13001,
            name = 'ApplingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13003,
            name = 'AtkinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13005,
            name = 'BaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13007,
            name = 'BakerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13009,
            name = 'BaldwinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13011,
            name = 'BanksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13013,
            name = 'BarrowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13015,
            name = 'BartowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13017,
            name = 'BenHillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13019,
            name = 'BerrienCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13021,
            name = 'BibbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13023,
            name = 'BleckleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13025,
            name = 'BrantleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13027,
            name = 'BrooksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13029,
            name = 'BryanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13031,
            name = 'BullochCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13033,
            name = 'BurkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13035,
            name = 'ButtsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13037,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13039,
            name = 'CamdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13043,
            name = 'CandlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13045,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13047,
            name = 'CatoosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13049,
            name = 'CharltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13051,
            name = 'ChathamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13053,
            name = 'ChattahoocheeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13055,
            name = 'ChattoogaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13057,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13059,
            name = 'ClarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13061,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13063,
            name = 'ClaytonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13065,
            name = 'ClinchCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13067,
            name = 'CobbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13069,
            name = 'CoffeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13071,
            name = 'ColquittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13073,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13075,
            name = 'CookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13077,
            name = 'CowetaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13079,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13081,
            name = 'CrispCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13083,
            name = 'DadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13085,
            name = 'DawsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13087,
            name = 'DecaturCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13089,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13091,
            name = 'DodgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13093,
            name = 'DoolyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13095,
            name = 'DoughertyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13097,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13099,
            name = 'EarlyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13101,
            name = 'EcholsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13103,
            name = 'EffinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13105,
            name = 'ElbertCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13107,
            name = 'EmanuelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13109,
            name = 'EvansCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13111,
            name = 'FanninCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13113,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13115,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13117,
            name = 'ForsythCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13119,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13121,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13123,
            name = 'GilmerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13125,
            name = 'GlascockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13127,
            name = 'GlynnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13129,
            name = 'GordonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13131,
            name = 'GradyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13133,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13135,
            name = 'GwinnettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13137,
            name = 'HabershamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13139,
            name = 'HallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13141,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13143,
            name = 'HaralsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13145,
            name = 'HarrisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13147,
            name = 'HartCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13149,
            name = 'HeardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13151,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13153,
            name = 'HoustonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13155,
            name = 'IrwinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13157,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13159,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13161,
            name = 'JeffDavisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13163,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13165,
            name = 'JenkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13167,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13169,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13171,
            name = 'LamarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13173,
            name = 'LanierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13175,
            name = 'LaurensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13177,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13179,
            name = 'LibertyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13181,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13183,
            name = 'LongCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13185,
            name = 'LowndesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13187,
            name = 'LumpkinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13189,
            name = 'McDuffieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13191,
            name = 'McIntoshCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13193,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13195,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13197,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13199,
            name = 'MeriwetherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13201,
            name = 'MillerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13205,
            name = 'MitchellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13207,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13209,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13211,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13213,
            name = 'MurrayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13215,
            name = 'MuscogeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13217,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13219,
            name = 'OconeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13221,
            name = 'OglethorpeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13223,
            name = 'PauldingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13225,
            name = 'PeachCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13227,
            name = 'PickensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13229,
            name = 'PierceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13231,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13233,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13235,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13237,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13239,
            name = 'QuitmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13241,
            name = 'RabunCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13243,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13245,
            name = 'RichmondCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13247,
            name = 'RockdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13249,
            name = 'SchleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13251,
            name = 'ScrevenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13253,
            name = 'SeminoleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13255,
            name = 'SpaldingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13257,
            name = 'StephensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13259,
            name = 'StewartCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13261,
            name = 'SumterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13263,
            name = 'TalbotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13265,
            name = 'TaliaferroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13267,
            name = 'TattnallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13269,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13271,
            name = 'TelfairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13273,
            name = 'TerrellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13275,
            name = 'ThomasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13277,
            name = 'TiftCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13279,
            name = 'ToombsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13281,
            name = 'TownsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13283,
            name = 'TreutlenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13285,
            name = 'TroupCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13287,
            name = 'TurnerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13289,
            name = 'TwiggsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13291,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13293,
            name = 'UpsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13295,
            name = 'WalkerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13297,
            name = 'WaltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13299,
            name = 'WareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13301,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13303,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13305,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13307,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13309,
            name = 'WheelerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13311,
            name = 'WhiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13313,
            name = 'WhitfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13315,
            name = 'WilcoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13317,
            name = 'WilkesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13319,
            name = 'WilkinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=13,
            fips = 13321,
            name = 'WorthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15000,
            name = 'Hawaii'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15001,
            name = 'HawaiiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15003,
            name = 'HonoluluCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15005,
            name = 'KalawaoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15007,
            name = 'KauaiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=15,
            fips = 15009,
            name = 'MauiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16000,
            name = 'Idaho'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16001,
            name = 'AdaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16003,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16005,
            name = 'BannockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16007,
            name = 'BearLakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16009,
            name = 'BenewahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16011,
            name = 'BinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16013,
            name = 'BlaineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16015,
            name = 'BoiseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16017,
            name = 'BonnerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16019,
            name = 'BonnevilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16021,
            name = 'BoundaryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16023,
            name = 'ButteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16025,
            name = 'CamasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16027,
            name = 'CanyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16029,
            name = 'CaribouCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16031,
            name = 'CassiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16033,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16035,
            name = 'ClearwaterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16037,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16039,
            name = 'ElmoreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16041,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16043,
            name = 'FremontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16045,
            name = 'GemCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16047,
            name = 'GoodingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16049,
            name = 'IdahoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16051,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16053,
            name = 'JeromeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16055,
            name = 'KootenaiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16057,
            name = 'LatahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16059,
            name = 'LemhiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16061,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16063,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16065,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16067,
            name = 'MinidokaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16069,
            name = 'NezPerceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16071,
            name = 'OneidaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16073,
            name = 'OwyheeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16075,
            name = 'PayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16077,
            name = 'PowerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16079,
            name = 'ShoshoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16081,
            name = 'TetonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16083,
            name = 'TwinFallsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16085,
            name = 'ValleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=16,
            fips = 16087,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17000,
            name = 'Illinois'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17003,
            name = 'AlexanderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17005,
            name = 'BondCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17007,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17009,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17011,
            name = 'BureauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17013,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17015,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17017,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17019,
            name = 'ChampaignCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17021,
            name = 'ChristianCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17023,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17025,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17027,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17029,
            name = 'ColesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17031,
            name = 'CookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17033,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17035,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17037,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17039,
            name = 'DeWittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17041,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17043,
            name = 'DuPageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17045,
            name = 'EdgarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17047,
            name = 'EdwardsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17049,
            name = 'EffinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17051,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17053,
            name = 'FordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17055,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17057,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17059,
            name = 'GallatinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17061,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17063,
            name = 'GrundyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17065,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17067,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17069,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17071,
            name = 'HendersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17073,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17075,
            name = 'IroquoisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17077,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17079,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17081,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17083,
            name = 'JerseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17085,
            name = 'JoDaviessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17087,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17089,
            name = 'KaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17091,
            name = 'KankakeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17093,
            name = 'KendallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17095,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17097,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17099,
            name = 'LaSalleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17101,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17103,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17105,
            name = 'LivingstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17107,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17109,
            name = 'McDonoughCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17111,
            name = 'McHenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17113,
            name = 'McLeanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17115,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17117,
            name = 'MacoupinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17119,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17121,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17123,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17125,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17127,
            name = 'MassacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17129,
            name = 'MenardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17131,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17133,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17135,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17137,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17139,
            name = 'MoultrieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17141,
            name = 'OgleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17143,
            name = 'PeoriaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17145,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17147,
            name = 'PiattCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17149,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17151,
            name = 'PopeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17153,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17155,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17157,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17159,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17161,
            name = 'RockIslandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17163,
            name = 'St.ClairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17165,
            name = 'SalineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17167,
            name = 'SangamonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17169,
            name = 'SchuylerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17171,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17173,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17175,
            name = 'StarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17177,
            name = 'StephensonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17179,
            name = 'TazewellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17181,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17183,
            name = 'VermilionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17185,
            name = 'WabashCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17187,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17189,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17191,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17193,
            name = 'WhiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17195,
            name = 'WhitesideCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17197,
            name = 'WillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17199,
            name = 'WilliamsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17201,
            name = 'WinnebagoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=17,
            fips = 17203,
            name = 'WoodfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18000,
            name = 'Indiana'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18003,
            name = 'AllenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18005,
            name = 'BartholomewCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18007,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18009,
            name = 'BlackfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18011,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18013,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18015,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18017,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18019,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18021,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18023,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18025,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18027,
            name = 'DaviessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18029,
            name = 'DearbornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18031,
            name = 'DecaturCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18033,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18035,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18037,
            name = 'DuboisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18039,
            name = 'ElkhartCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18041,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18043,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18045,
            name = 'FountainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18047,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18049,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18051,
            name = 'GibsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18053,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18055,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18057,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18059,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18061,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18063,
            name = 'HendricksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18065,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18067,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18069,
            name = 'HuntingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18071,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18073,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18075,
            name = 'JayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18077,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18079,
            name = 'JenningsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18081,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18083,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18085,
            name = 'KosciuskoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18087,
            name = 'LagrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18089,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18091,
            name = 'LaPorteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18093,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18095,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18097,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18099,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18101,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18103,
            name = 'MiamiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18105,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18107,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18109,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18111,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18113,
            name = 'NobleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18115,
            name = 'OhioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18117,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18119,
            name = 'OwenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18121,
            name = 'ParkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18123,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18125,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18127,
            name = 'PorterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18129,
            name = 'PoseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18131,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18133,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18135,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18137,
            name = 'RipleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18139,
            name = 'RushCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18141,
            name = 'St.JosephCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18143,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18145,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18147,
            name = 'SpencerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18149,
            name = 'StarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18151,
            name = 'SteubenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18153,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18155,
            name = 'SwitzerlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18157,
            name = 'TippecanoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18159,
            name = 'TiptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18161,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18163,
            name = 'VanderburghCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18165,
            name = 'VermillionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18167,
            name = 'VigoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18169,
            name = 'WabashCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18171,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18173,
            name = 'WarrickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18175,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18177,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18179,
            name = 'WellsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18181,
            name = 'WhiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=18,
            fips = 18183,
            name = 'WhitleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19000,
            name = 'Iowa'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19001,
            name = 'AdairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19003,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19005,
            name = 'AllamakeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19007,
            name = 'AppanooseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19009,
            name = 'AudubonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19011,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19013,
            name = 'BlackHawkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19015,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19017,
            name = 'BremerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19019,
            name = 'BuchananCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19021,
            name = 'BuenaVistaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19023,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19025,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19027,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19029,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19031,
            name = 'CedarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19033,
            name = 'CerroGordoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19035,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19037,
            name = 'ChickasawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19039,
            name = 'ClarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19041,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19043,
            name = 'ClaytonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19045,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19047,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19049,
            name = 'DallasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19051,
            name = 'DavisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19053,
            name = 'DecaturCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19055,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19057,
            name = 'DesMoinesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19059,
            name = 'DickinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19061,
            name = 'DubuqueCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19063,
            name = 'EmmetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19065,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19067,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19069,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19071,
            name = 'FremontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19073,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19075,
            name = 'GrundyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19077,
            name = 'GuthrieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19079,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19081,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19083,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19085,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19087,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19089,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19091,
            name = 'HumboldtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19093,
            name = 'IdaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19095,
            name = 'IowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19097,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19099,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19101,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19103,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19105,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19107,
            name = 'KeokukCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19109,
            name = 'KossuthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19111,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19113,
            name = 'LinnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19115,
            name = 'LouisaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19117,
            name = 'LucasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19119,
            name = 'LyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19121,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19123,
            name = 'MahaskaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19125,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19127,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19129,
            name = 'MillsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19131,
            name = 'MitchellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19133,
            name = 'MononaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19135,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19137,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19139,
            name = 'MuscatineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19141,
            name = 'O'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19143,
            name = 'OsceolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19145,
            name = 'PageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19147,
            name = 'PaloAltoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19149,
            name = 'PlymouthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19151,
            name = 'PocahontasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19153,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19155,
            name = 'PottawattamieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19157,
            name = 'PoweshiekCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19159,
            name = 'RinggoldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19161,
            name = 'SacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19163,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19165,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19167,
            name = 'SiouxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19169,
            name = 'StoryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19171,
            name = 'TamaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19173,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19175,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19177,
            name = 'VanBurenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19179,
            name = 'WapelloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19181,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19183,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19185,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19187,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19189,
            name = 'WinnebagoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19191,
            name = 'WinneshiekCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19193,
            name = 'WoodburyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19195,
            name = 'WorthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=19,
            fips = 19197,
            name = 'WrightCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20000,
            name = 'Kansas'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20001,
            name = 'AllenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20003,
            name = 'AndersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20005,
            name = 'AtchisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20007,
            name = 'BarberCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20009,
            name = 'BartonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20011,
            name = 'BourbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20013,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20015,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20017,
            name = 'ChaseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20019,
            name = 'ChautauquaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20021,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20023,
            name = 'CheyenneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20025,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20027,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20029,
            name = 'CloudCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20031,
            name = 'CoffeyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20033,
            name = 'ComancheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20035,
            name = 'CowleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20037,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20039,
            name = 'DecaturCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20041,
            name = 'DickinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20043,
            name = 'DoniphanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20045,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20047,
            name = 'EdwardsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20049,
            name = 'ElkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20051,
            name = 'EllisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20053,
            name = 'EllsworthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20055,
            name = 'FinneyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20057,
            name = 'FordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20059,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20061,
            name = 'GearyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20063,
            name = 'GoveCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20065,
            name = 'GrahamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20067,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20069,
            name = 'GrayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20071,
            name = 'GreeleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20073,
            name = 'GreenwoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20075,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20077,
            name = 'HarperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20079,
            name = 'HarveyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20081,
            name = 'HaskellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20083,
            name = 'HodgemanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20085,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20087,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20089,
            name = 'JewellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20091,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20093,
            name = 'KearnyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20095,
            name = 'KingmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20097,
            name = 'KiowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20099,
            name = 'LabetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20101,
            name = 'LaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20103,
            name = 'LeavenworthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20105,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20107,
            name = 'LinnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20109,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20111,
            name = 'LyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20113,
            name = 'McPhersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20115,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20117,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20119,
            name = 'MeadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20121,
            name = 'MiamiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20123,
            name = 'MitchellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20125,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20127,
            name = 'MorrisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20129,
            name = 'MortonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20131,
            name = 'NemahaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20133,
            name = 'NeoshoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20135,
            name = 'NessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20137,
            name = 'NortonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20139,
            name = 'OsageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20141,
            name = 'OsborneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20143,
            name = 'OttawaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20145,
            name = 'PawneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20147,
            name = 'PhillipsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20149,
            name = 'PottawatomieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20151,
            name = 'PrattCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20153,
            name = 'RawlinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20155,
            name = 'RenoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20157,
            name = 'RepublicCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20159,
            name = 'RiceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20161,
            name = 'RileyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20163,
            name = 'RooksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20165,
            name = 'RushCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20167,
            name = 'RussellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20169,
            name = 'SalineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20171,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20173,
            name = 'SedgwickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20175,
            name = 'SewardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20177,
            name = 'ShawneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20179,
            name = 'SheridanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20181,
            name = 'ShermanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20183,
            name = 'SmithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20185,
            name = 'StaffordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20187,
            name = 'StantonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20189,
            name = 'StevensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20191,
            name = 'SumnerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20193,
            name = 'ThomasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20195,
            name = 'TregoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20197,
            name = 'WabaunseeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20199,
            name = 'WallaceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20201,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20203,
            name = 'WichitaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20205,
            name = 'WilsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20207,
            name = 'WoodsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=20,
            fips = 20209,
            name = 'WyandotteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21000,
            name = 'Kentucky'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21001,
            name = 'AdairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21003,
            name = 'AllenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21005,
            name = 'AndersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21007,
            name = 'BallardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21009,
            name = 'BarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21011,
            name = 'BathCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21013,
            name = 'BellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21015,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21017,
            name = 'BourbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21019,
            name = 'BoydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21021,
            name = 'BoyleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21023,
            name = 'BrackenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21025,
            name = 'BreathittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21027,
            name = 'BreckinridgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21029,
            name = 'BullittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21031,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21033,
            name = 'CaldwellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21035,
            name = 'CallowayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21037,
            name = 'CampbellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21039,
            name = 'CarlisleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21041,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21043,
            name = 'CarterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21045,
            name = 'CaseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21047,
            name = 'ChristianCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21049,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21051,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21053,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21055,
            name = 'CrittendenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21057,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21059,
            name = 'DaviessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21061,
            name = 'EdmonsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21063,
            name = 'ElliottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21065,
            name = 'EstillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21067,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21069,
            name = 'FlemingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21071,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21073,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21075,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21077,
            name = 'GallatinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21079,
            name = 'GarrardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21081,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21083,
            name = 'GravesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21085,
            name = 'GraysonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21087,
            name = 'GreenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21089,
            name = 'GreenupCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21091,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21093,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21095,
            name = 'HarlanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21097,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21099,
            name = 'HartCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21101,
            name = 'HendersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21103,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21105,
            name = 'HickmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21107,
            name = 'HopkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21109,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21111,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21113,
            name = 'JessamineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21115,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21117,
            name = 'KentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21119,
            name = 'KnottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21121,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21123,
            name = 'LarueCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21125,
            name = 'LaurelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21127,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21129,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21131,
            name = 'LeslieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21133,
            name = 'LetcherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21135,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21137,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21139,
            name = 'LivingstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21141,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21143,
            name = 'LyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21145,
            name = 'McCrackenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21147,
            name = 'McCrearyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21149,
            name = 'McLeanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21151,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21153,
            name = 'MagoffinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21155,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21157,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21159,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21161,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21163,
            name = 'MeadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21165,
            name = 'MenifeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21167,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21169,
            name = 'MetcalfeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21171,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21173,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21175,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21177,
            name = 'MuhlenbergCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21179,
            name = 'NelsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21181,
            name = 'NicholasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21183,
            name = 'OhioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21185,
            name = 'OldhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21187,
            name = 'OwenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21189,
            name = 'OwsleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21191,
            name = 'PendletonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21193,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21195,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21197,
            name = 'PowellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21199,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21201,
            name = 'RobertsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21203,
            name = 'RockcastleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21205,
            name = 'RowanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21207,
            name = 'RussellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21209,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21211,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21213,
            name = 'SimpsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21215,
            name = 'SpencerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21217,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21219,
            name = 'ToddCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21221,
            name = 'TriggCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21223,
            name = 'TrimbleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21225,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21227,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21229,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21231,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21233,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21235,
            name = 'WhitleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21237,
            name = 'WolfeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=21,
            fips = 21239,
            name = 'WoodfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22000,
            name = 'Louisiana'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22001,
            name = 'AcadiaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22003,
            name = 'AllenParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22005,
            name = 'AscensionParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22007,
            name = 'AssumptionParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22009,
            name = 'AvoyellesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22011,
            name = 'BeauregardParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22013,
            name = 'BienvilleParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22015,
            name = 'BossierParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22017,
            name = 'CaddoParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22019,
            name = 'CalcasieuParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22021,
            name = 'CaldwellParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22023,
            name = 'CameronParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22025,
            name = 'CatahoulaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22027,
            name = 'ClaiborneParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22029,
            name = 'ConcordiaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22031,
            name = 'DeSotoParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22033,
            name = 'EastBatonRougeParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22035,
            name = 'EastCarrollParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22037,
            name = 'EastFelicianaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22039,
            name = 'EvangelineParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22041,
            name = 'FranklinParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22043,
            name = 'GrantParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22045,
            name = 'IberiaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22047,
            name = 'IbervilleParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22049,
            name = 'JacksonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22051,
            name = 'JeffersonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22053,
            name = 'JeffersonDavisParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22055,
            name = 'LafayetteParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22057,
            name = 'LafourcheParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22059,
            name = 'LaSalleParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22061,
            name = 'LincolnParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22063,
            name = 'LivingstonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22065,
            name = 'MadisonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22067,
            name = 'MorehouseParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22069,
            name = 'NatchitochesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22071,
            name = 'OrleansParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22073,
            name = 'OuachitaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22075,
            name = 'PlaqueminesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22077,
            name = 'PointeCoupeeParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22079,
            name = 'RapidesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22081,
            name = 'RedRiverParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22083,
            name = 'RichlandParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22085,
            name = 'SabineParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22087,
            name = 'St.BernardParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22089,
            name = 'St.CharlesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22091,
            name = 'St.HelenaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22093,
            name = 'St.JamesParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22095,
            name = 'St.JohntheBaptistParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22097,
            name = 'St.LandryParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22099,
            name = 'St.MartinParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22101,
            name = 'St.MaryParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22103,
            name = 'St.TammanyParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22105,
            name = 'TangipahoaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22107,
            name = 'TensasParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22109,
            name = 'TerrebonneParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22111,
            name = 'UnionParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22113,
            name = 'VermilionParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22115,
            name = 'VernonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22117,
            name = 'WashingtonParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22119,
            name = 'WebsterParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22121,
            name = 'WestBatonRougeParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22123,
            name = 'WestCarrollParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22125,
            name = 'WestFelicianaParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=22,
            fips = 22127,
            name = 'WinnParish'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23000,
            name = 'Maine'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23001,
            name = 'AndroscogginCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23003,
            name = 'AroostookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23005,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23007,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23009,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23011,
            name = 'KennebecCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23013,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23015,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23017,
            name = 'OxfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23019,
            name = 'PenobscotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23021,
            name = 'PiscataquisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23023,
            name = 'SagadahocCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23025,
            name = 'SomersetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23027,
            name = 'WaldoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23029,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=23,
            fips = 23031,
            name = 'YorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24000,
            name = 'Maryland'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24001,
            name = 'AlleganyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24003,
            name = 'AnneArundelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24005,
            name = 'BaltimoreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24009,
            name = 'CalvertCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24011,
            name = 'CarolineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24013,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24015,
            name = 'CecilCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24017,
            name = 'CharlesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24019,
            name = 'DorchesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24021,
            name = 'FrederickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24023,
            name = 'GarrettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24025,
            name = 'HarfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24027,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24029,
            name = 'KentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24031,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24033,
            name = 'PrinceGeorge'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24035,
            name = 'QueenAnne'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24037,
            name = 'St.Mary'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24039,
            name = 'SomersetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24041,
            name = 'TalbotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24043,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24045,
            name = 'WicomicoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24047,
            name = 'WorcesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=24,
            fips = 24510,
            name = 'Baltimorecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25000,
            name = 'Massachusetts'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25001,
            name = 'BarnstableCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25003,
            name = 'BerkshireCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25005,
            name = 'BristolCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25007,
            name = 'DukesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25009,
            name = 'EssexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25011,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25013,
            name = 'HampdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25015,
            name = 'HampshireCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25017,
            name = 'MiddlesexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25019,
            name = 'NantucketCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25021,
            name = 'NorfolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25023,
            name = 'PlymouthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25025,
            name = 'SuffolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=25,
            fips = 25027,
            name = 'WorcesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26000,
            name = 'Michigan'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26001,
            name = 'AlconaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26003,
            name = 'AlgerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26005,
            name = 'AlleganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26007,
            name = 'AlpenaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26009,
            name = 'AntrimCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26011,
            name = 'ArenacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26013,
            name = 'BaragaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26015,
            name = 'BarryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26017,
            name = 'BayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26019,
            name = 'BenzieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26021,
            name = 'BerrienCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26023,
            name = 'BranchCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26025,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26027,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26029,
            name = 'CharlevoixCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26031,
            name = 'CheboyganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26033,
            name = 'ChippewaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26035,
            name = 'ClareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26037,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26039,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26041,
            name = 'DeltaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26043,
            name = 'DickinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26045,
            name = 'EatonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26047,
            name = 'EmmetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26049,
            name = 'GeneseeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26051,
            name = 'GladwinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26053,
            name = 'GogebicCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26055,
            name = 'GrandTraverseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26057,
            name = 'GratiotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26059,
            name = 'HillsdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26061,
            name = 'HoughtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26063,
            name = 'HuronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26065,
            name = 'InghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26067,
            name = 'IoniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26069,
            name = 'IoscoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26071,
            name = 'IronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26073,
            name = 'IsabellaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26075,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26077,
            name = 'KalamazooCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26079,
            name = 'KalkaskaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26081,
            name = 'KentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26083,
            name = 'KeweenawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26085,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26087,
            name = 'LapeerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26089,
            name = 'LeelanauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26091,
            name = 'LenaweeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26093,
            name = 'LivingstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26095,
            name = 'LuceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26097,
            name = 'MackinacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26099,
            name = 'MacombCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26101,
            name = 'ManisteeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26103,
            name = 'MarquetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26105,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26107,
            name = 'MecostaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26109,
            name = 'MenomineeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26111,
            name = 'MidlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26113,
            name = 'MissaukeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26115,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26117,
            name = 'MontcalmCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26119,
            name = 'MontmorencyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26121,
            name = 'MuskegonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26123,
            name = 'NewaygoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26125,
            name = 'OaklandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26127,
            name = 'OceanaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26129,
            name = 'OgemawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26131,
            name = 'OntonagonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26133,
            name = 'OsceolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26135,
            name = 'OscodaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26137,
            name = 'OtsegoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26139,
            name = 'OttawaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26141,
            name = 'PresqueIsleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26143,
            name = 'RoscommonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26145,
            name = 'SaginawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26147,
            name = 'St.ClairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26149,
            name = 'St.JosephCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26151,
            name = 'SanilacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26153,
            name = 'SchoolcraftCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26155,
            name = 'ShiawasseeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26157,
            name = 'TuscolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26159,
            name = 'VanBurenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26161,
            name = 'WashtenawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26163,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=26,
            fips = 26165,
            name = 'WexfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27000,
            name = 'Minnesota'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27001,
            name = 'AitkinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27003,
            name = 'AnokaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27005,
            name = 'BeckerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27007,
            name = 'BeltramiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27009,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27011,
            name = 'BigStoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27013,
            name = 'BlueEarthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27015,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27017,
            name = 'CarltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27019,
            name = 'CarverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27021,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27023,
            name = 'ChippewaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27025,
            name = 'ChisagoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27027,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27029,
            name = 'ClearwaterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27031,
            name = 'CookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27033,
            name = 'CottonwoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27035,
            name = 'CrowWingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27037,
            name = 'DakotaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27039,
            name = 'DodgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27041,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27043,
            name = 'FaribaultCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27045,
            name = 'FillmoreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27047,
            name = 'FreebornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27049,
            name = 'GoodhueCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27051,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27053,
            name = 'HennepinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27055,
            name = 'HoustonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27057,
            name = 'HubbardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27059,
            name = 'IsantiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27061,
            name = 'ItascaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27063,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27065,
            name = 'KanabecCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27067,
            name = 'KandiyohiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27069,
            name = 'KittsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27071,
            name = 'KoochichingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27073,
            name = 'LacquiParleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27075,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27077,
            name = 'LakeoftheWoodsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27079,
            name = 'LeSueurCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27081,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27083,
            name = 'LyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27085,
            name = 'McLeodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27087,
            name = 'MahnomenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27089,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27091,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27093,
            name = 'MeekerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27095,
            name = 'MilleLacsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27097,
            name = 'MorrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27099,
            name = 'MowerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27101,
            name = 'MurrayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27103,
            name = 'NicolletCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27105,
            name = 'NoblesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27107,
            name = 'NormanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27109,
            name = 'OlmstedCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27111,
            name = 'OtterTailCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27113,
            name = 'PenningtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27115,
            name = 'PineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27117,
            name = 'PipestoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27119,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27121,
            name = 'PopeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27123,
            name = 'RamseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27125,
            name = 'RedLakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27127,
            name = 'RedwoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27129,
            name = 'RenvilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27131,
            name = 'RiceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27133,
            name = 'RockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27135,
            name = 'RoseauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27137,
            name = 'St.LouisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27139,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27141,
            name = 'SherburneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27143,
            name = 'SibleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27145,
            name = 'StearnsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27147,
            name = 'SteeleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27149,
            name = 'StevensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27151,
            name = 'SwiftCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27153,
            name = 'ToddCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27155,
            name = 'TraverseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27157,
            name = 'WabashaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27159,
            name = 'WadenaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27161,
            name = 'WasecaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27163,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27165,
            name = 'WatonwanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27167,
            name = 'WilkinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27169,
            name = 'WinonaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27171,
            name = 'WrightCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=27,
            fips = 27173,
            name = 'YellowMedicineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28000,
            name = 'Mississippi'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28003,
            name = 'AlcornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28005,
            name = 'AmiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28007,
            name = 'AttalaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28009,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28011,
            name = 'BolivarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28013,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28015,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28017,
            name = 'ChickasawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28019,
            name = 'ChoctawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28021,
            name = 'ClaiborneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28023,
            name = 'ClarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28025,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28027,
            name = 'CoahomaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28029,
            name = 'CopiahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28031,
            name = 'CovingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28033,
            name = 'DeSotoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28035,
            name = 'ForrestCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28037,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28039,
            name = 'GeorgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28041,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28043,
            name = 'GrenadaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28045,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28047,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28049,
            name = 'HindsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28051,
            name = 'HolmesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28053,
            name = 'HumphreysCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28055,
            name = 'IssaquenaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28057,
            name = 'ItawambaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28059,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28061,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28063,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28065,
            name = 'JeffersonDavisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28067,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28069,
            name = 'KemperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28071,
            name = 'LafayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28073,
            name = 'LamarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28075,
            name = 'LauderdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28077,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28079,
            name = 'LeakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28081,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28083,
            name = 'LefloreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28085,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28087,
            name = 'LowndesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28089,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28091,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28093,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28095,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28097,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28099,
            name = 'NeshobaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28101,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28103,
            name = 'NoxubeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28105,
            name = 'OktibbehaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28107,
            name = 'PanolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28109,
            name = 'PearlRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28111,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28113,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28115,
            name = 'PontotocCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28117,
            name = 'PrentissCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28119,
            name = 'QuitmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28121,
            name = 'RankinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28123,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28125,
            name = 'SharkeyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28127,
            name = 'SimpsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28129,
            name = 'SmithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28131,
            name = 'StoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28133,
            name = 'SunflowerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28135,
            name = 'TallahatchieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28137,
            name = 'TateCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28139,
            name = 'TippahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28141,
            name = 'TishomingoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28143,
            name = 'TunicaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28145,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28147,
            name = 'WalthallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28149,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28151,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28153,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28155,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28157,
            name = 'WilkinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28159,
            name = 'WinstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28161,
            name = 'YalobushaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=28,
            fips = 28163,
            name = 'YazooCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29000,
            name = 'Missouri'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29001,
            name = 'AdairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29003,
            name = 'AndrewCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29005,
            name = 'AtchisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29007,
            name = 'AudrainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29009,
            name = 'BarryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29011,
            name = 'BartonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29013,
            name = 'BatesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29015,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29017,
            name = 'BollingerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29019,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29021,
            name = 'BuchananCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29023,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29025,
            name = 'CaldwellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29027,
            name = 'CallawayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29029,
            name = 'CamdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29031,
            name = 'CapeGirardeauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29033,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29035,
            name = 'CarterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29037,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29039,
            name = 'CedarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29041,
            name = 'CharitonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29043,
            name = 'ChristianCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29045,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29047,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29049,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29051,
            name = 'ColeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29053,
            name = 'CooperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29055,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29057,
            name = 'DadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29059,
            name = 'DallasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29061,
            name = 'DaviessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29063,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29065,
            name = 'DentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29067,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29069,
            name = 'DunklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29071,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29073,
            name = 'GasconadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29075,
            name = 'GentryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29077,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29079,
            name = 'GrundyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29081,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29083,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29085,
            name = 'HickoryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29087,
            name = 'HoltCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29089,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29091,
            name = 'HowellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29093,
            name = 'IronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29095,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29097,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29099,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29101,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29103,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29105,
            name = 'LacledeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29107,
            name = 'LafayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29109,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29111,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29113,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29115,
            name = 'LinnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29117,
            name = 'LivingstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29119,
            name = 'McDonaldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29121,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29123,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29125,
            name = 'MariesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29127,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29129,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29131,
            name = 'MillerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29133,
            name = 'MississippiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29135,
            name = 'MoniteauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29137,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29139,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29141,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29143,
            name = 'NewMadridCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29145,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29147,
            name = 'NodawayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29149,
            name = 'OregonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29151,
            name = 'OsageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29153,
            name = 'OzarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29155,
            name = 'PemiscotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29157,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29159,
            name = 'PettisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29161,
            name = 'PhelpsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29163,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29165,
            name = 'PlatteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29167,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29169,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29171,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29173,
            name = 'RallsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29175,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29177,
            name = 'RayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29179,
            name = 'ReynoldsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29181,
            name = 'RipleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29183,
            name = 'St.CharlesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29185,
            name = 'St.ClairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29186,
            name = 'Ste.GenevieveCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29187,
            name = 'St.FrancoisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29189,
            name = 'St.LouisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29195,
            name = 'SalineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29197,
            name = 'SchuylerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29199,
            name = 'ScotlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29201,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29203,
            name = 'ShannonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29205,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29207,
            name = 'StoddardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29209,
            name = 'StoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29211,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29213,
            name = 'TaneyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29215,
            name = 'TexasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29217,
            name = 'VernonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29219,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29221,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29223,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29225,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29227,
            name = 'WorthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29229,
            name = 'WrightCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=29,
            fips = 29510,
            name = 'St.Louiscity'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30000,
            name = 'Montana'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30001,
            name = 'BeaverheadCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30003,
            name = 'BigHornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30005,
            name = 'BlaineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30007,
            name = 'BroadwaterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30009,
            name = 'CarbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30011,
            name = 'CarterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30013,
            name = 'CascadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30015,
            name = 'ChouteauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30017,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30019,
            name = 'DanielsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30021,
            name = 'DawsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30023,
            name = 'DeerLodgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30025,
            name = 'FallonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30027,
            name = 'FergusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30029,
            name = 'FlatheadCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30031,
            name = 'GallatinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30033,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30035,
            name = 'GlacierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30037,
            name = 'GoldenValleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30039,
            name = 'GraniteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30041,
            name = 'HillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30043,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30045,
            name = 'JudithBasinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30047,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30049,
            name = 'LewisandClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30051,
            name = 'LibertyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30053,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30055,
            name = 'McConeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30057,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30059,
            name = 'MeagherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30061,
            name = 'MineralCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30063,
            name = 'MissoulaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30065,
            name = 'MusselshellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30067,
            name = 'ParkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30069,
            name = 'PetroleumCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30071,
            name = 'PhillipsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30073,
            name = 'PonderaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30075,
            name = 'PowderRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30077,
            name = 'PowellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30079,
            name = 'PrairieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30081,
            name = 'RavalliCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30083,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30085,
            name = 'RooseveltCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30087,
            name = 'RosebudCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30089,
            name = 'SandersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30091,
            name = 'SheridanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30093,
            name = 'SilverBowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30095,
            name = 'StillwaterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30097,
            name = 'SweetGrassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30099,
            name = 'TetonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30101,
            name = 'TooleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30103,
            name = 'TreasureCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30105,
            name = 'ValleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30107,
            name = 'WheatlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30109,
            name = 'WibauxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30111,
            name = 'YellowstoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=30,
            fips = 30113,
            name = 'YellowstoneNationalPark'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31000,
            name = 'Nebraska'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31003,
            name = 'AntelopeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31005,
            name = 'ArthurCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31007,
            name = 'BannerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31009,
            name = 'BlaineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31011,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31013,
            name = 'BoxButteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31015,
            name = 'BoydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31017,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31019,
            name = 'BuffaloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31021,
            name = 'BurtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31023,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31025,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31027,
            name = 'CedarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31029,
            name = 'ChaseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31031,
            name = 'CherryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31033,
            name = 'CheyenneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31035,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31037,
            name = 'ColfaxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31039,
            name = 'CumingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31041,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31043,
            name = 'DakotaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31045,
            name = 'DawesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31047,
            name = 'DawsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31049,
            name = 'DeuelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31051,
            name = 'DixonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31053,
            name = 'DodgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31055,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31057,
            name = 'DundyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31059,
            name = 'FillmoreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31061,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31063,
            name = 'FrontierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31065,
            name = 'FurnasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31067,
            name = 'GageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31069,
            name = 'GardenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31071,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31073,
            name = 'GosperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31075,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31077,
            name = 'GreeleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31079,
            name = 'HallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31081,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31083,
            name = 'HarlanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31085,
            name = 'HayesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31087,
            name = 'HitchcockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31089,
            name = 'HoltCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31091,
            name = 'HookerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31093,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31095,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31097,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31099,
            name = 'KearneyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31101,
            name = 'KeithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31103,
            name = 'KeyaPahaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31105,
            name = 'KimballCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31107,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31109,
            name = 'LancasterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31111,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31113,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31115,
            name = 'LoupCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31117,
            name = 'McPhersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31119,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31121,
            name = 'MerrickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31123,
            name = 'MorrillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31125,
            name = 'NanceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31127,
            name = 'NemahaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31129,
            name = 'NuckollsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31131,
            name = 'OtoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31133,
            name = 'PawneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31135,
            name = 'PerkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31137,
            name = 'PhelpsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31139,
            name = 'PierceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31141,
            name = 'PlatteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31143,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31145,
            name = 'RedWillowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31147,
            name = 'RichardsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31149,
            name = 'RockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31151,
            name = 'SalineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31153,
            name = 'SarpyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31155,
            name = 'SaundersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31157,
            name = 'ScottsBluffCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31159,
            name = 'SewardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31161,
            name = 'SheridanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31163,
            name = 'ShermanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31165,
            name = 'SiouxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31167,
            name = 'StantonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31169,
            name = 'ThayerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31171,
            name = 'ThomasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31173,
            name = 'ThurstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31175,
            name = 'ValleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31177,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31179,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31181,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31183,
            name = 'WheelerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=31,
            fips = 31185,
            name = 'YorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32000,
            name = 'Nevada'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32001,
            name = 'ChurchillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32003,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32005,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32007,
            name = 'ElkoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32009,
            name = 'EsmeraldaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32011,
            name = 'EurekaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32013,
            name = 'HumboldtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32015,
            name = 'LanderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32017,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32019,
            name = 'LyonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32021,
            name = 'MineralCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32023,
            name = 'NyeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32027,
            name = 'PershingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32029,
            name = 'StoreyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32031,
            name = 'WashoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32033,
            name = 'WhitePineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=32,
            fips = 32510,
            name = 'CarsonCity'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33000,
            name = 'NewHampshire'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33001,
            name = 'BelknapCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33003,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33005,
            name = 'CheshireCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33007,
            name = 'CoosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33009,
            name = 'GraftonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33011,
            name = 'HillsboroughCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33013,
            name = 'MerrimackCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33015,
            name = 'RockinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33017,
            name = 'StraffordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=33,
            fips = 33019,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34000,
            name = 'NewJersey'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34001,
            name = 'AtlanticCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34003,
            name = 'BergenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34005,
            name = 'BurlingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34007,
            name = 'CamdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34009,
            name = 'CapeMayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34011,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34013,
            name = 'EssexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34015,
            name = 'GloucesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34017,
            name = 'HudsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34019,
            name = 'HunterdonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34021,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34023,
            name = 'MiddlesexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34025,
            name = 'MonmouthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34027,
            name = 'MorrisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34029,
            name = 'OceanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34031,
            name = 'PassaicCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34033,
            name = 'SalemCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34035,
            name = 'SomersetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34037,
            name = 'SussexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34039,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=34,
            fips = 34041,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35000,
            name = 'NewMexico'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35001,
            name = 'BernalilloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35003,
            name = 'CatronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35005,
            name = 'ChavesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35006,
            name = 'CibolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35007,
            name = 'ColfaxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35009,
            name = 'CurryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35011,
            name = 'DeBacaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35013,
            name = 'DonaAnaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35015,
            name = 'EddyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35017,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35019,
            name = 'GuadalupeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35021,
            name = 'HardingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35023,
            name = 'HidalgoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35025,
            name = 'LeaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35027,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35028,
            name = 'LosAlamosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35029,
            name = 'LunaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35031,
            name = 'McKinleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35033,
            name = 'MoraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35035,
            name = 'OteroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35037,
            name = 'QuayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35039,
            name = 'RioArribaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35041,
            name = 'RooseveltCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35043,
            name = 'SandovalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35045,
            name = 'SanJuanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35047,
            name = 'SanMiguelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35049,
            name = 'SantaFeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35051,
            name = 'SierraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35053,
            name = 'SocorroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35055,
            name = 'TaosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35057,
            name = 'TorranceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35059,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=35,
            fips = 35061,
            name = 'ValenciaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36000,
            name = 'NewYork'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36001,
            name = 'AlbanyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36003,
            name = 'AlleganyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36005,
            name = 'BronxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36007,
            name = 'BroomeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36009,
            name = 'CattaraugusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36011,
            name = 'CayugaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36013,
            name = 'ChautauquaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36015,
            name = 'ChemungCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36017,
            name = 'ChenangoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36019,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36021,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36023,
            name = 'CortlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36025,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36027,
            name = 'DutchessCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36029,
            name = 'ErieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36031,
            name = 'EssexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36033,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36035,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36037,
            name = 'GeneseeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36039,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36041,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36043,
            name = 'HerkimerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36045,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36047,
            name = 'KingsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36049,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36051,
            name = 'LivingstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36053,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36055,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36057,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36059,
            name = 'NassauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36061,
            name = 'NewYorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36063,
            name = 'NiagaraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36065,
            name = 'OneidaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36067,
            name = 'OnondagaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36069,
            name = 'OntarioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36071,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36073,
            name = 'OrleansCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36075,
            name = 'OswegoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36077,
            name = 'OtsegoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36079,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36081,
            name = 'QueensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36083,
            name = 'RensselaerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36085,
            name = 'RichmondCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36087,
            name = 'RocklandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36089,
            name = 'St.LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36091,
            name = 'SaratogaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36093,
            name = 'SchenectadyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36095,
            name = 'SchoharieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36097,
            name = 'SchuylerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36099,
            name = 'SenecaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36101,
            name = 'SteubenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36103,
            name = 'SuffolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36105,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36107,
            name = 'TiogaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36109,
            name = 'TompkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36111,
            name = 'UlsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36113,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36115,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36117,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36119,
            name = 'WestchesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36121,
            name = 'WyomingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=36,
            fips = 36123,
            name = 'YatesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37000,
            name = 'NorthCarolina'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37001,
            name = 'AlamanceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37003,
            name = 'AlexanderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37005,
            name = 'AlleghanyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37007,
            name = 'AnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37009,
            name = 'AsheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37011,
            name = 'AveryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37013,
            name = 'BeaufortCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37015,
            name = 'BertieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37017,
            name = 'BladenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37019,
            name = 'BrunswickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37021,
            name = 'BuncombeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37023,
            name = 'BurkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37025,
            name = 'CabarrusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37027,
            name = 'CaldwellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37029,
            name = 'CamdenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37031,
            name = 'CarteretCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37033,
            name = 'CaswellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37035,
            name = 'CatawbaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37037,
            name = 'ChathamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37039,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37041,
            name = 'ChowanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37043,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37045,
            name = 'ClevelandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37047,
            name = 'ColumbusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37049,
            name = 'CravenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37051,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37053,
            name = 'CurrituckCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37055,
            name = 'DareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37057,
            name = 'DavidsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37059,
            name = 'DavieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37061,
            name = 'DuplinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37063,
            name = 'DurhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37065,
            name = 'EdgecombeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37067,
            name = 'ForsythCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37069,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37071,
            name = 'GastonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37073,
            name = 'GatesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37075,
            name = 'GrahamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37077,
            name = 'GranvilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37079,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37081,
            name = 'GuilfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37083,
            name = 'HalifaxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37085,
            name = 'HarnettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37087,
            name = 'HaywoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37089,
            name = 'HendersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37091,
            name = 'HertfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37093,
            name = 'HokeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37095,
            name = 'HydeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37097,
            name = 'IredellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37099,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37101,
            name = 'JohnstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37103,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37105,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37107,
            name = 'LenoirCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37109,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37111,
            name = 'McDowellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37113,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37115,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37117,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37119,
            name = 'MecklenburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37121,
            name = 'MitchellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37123,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37125,
            name = 'MooreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37127,
            name = 'NashCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37129,
            name = 'NewHanoverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37131,
            name = 'NorthamptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37133,
            name = 'OnslowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37135,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37137,
            name = 'PamlicoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37139,
            name = 'PasquotankCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37141,
            name = 'PenderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37143,
            name = 'PerquimansCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37145,
            name = 'PersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37147,
            name = 'PittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37149,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37151,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37153,
            name = 'RichmondCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37155,
            name = 'RobesonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37157,
            name = 'RockinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37159,
            name = 'RowanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37161,
            name = 'RutherfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37163,
            name = 'SampsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37165,
            name = 'ScotlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37167,
            name = 'StanlyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37169,
            name = 'StokesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37171,
            name = 'SurryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37173,
            name = 'SwainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37175,
            name = 'TransylvaniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37177,
            name = 'TyrrellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37179,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37181,
            name = 'VanceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37183,
            name = 'WakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37185,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37187,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37189,
            name = 'WataugaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37191,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37193,
            name = 'WilkesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37195,
            name = 'WilsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37197,
            name = 'YadkinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=37,
            fips = 37199,
            name = 'YanceyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38000,
            name = 'NorthDakota'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38003,
            name = 'BarnesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38005,
            name = 'BensonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38007,
            name = 'BillingsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38009,
            name = 'BottineauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38011,
            name = 'BowmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38013,
            name = 'BurkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38015,
            name = 'BurleighCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38017,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38019,
            name = 'CavalierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38021,
            name = 'DickeyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38023,
            name = 'DivideCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38025,
            name = 'DunnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38027,
            name = 'EddyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38029,
            name = 'EmmonsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38031,
            name = 'FosterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38033,
            name = 'GoldenValleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38035,
            name = 'GrandForksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38037,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38039,
            name = 'GriggsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38041,
            name = 'HettingerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38043,
            name = 'KidderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38045,
            name = 'LaMoureCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38047,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38049,
            name = 'McHenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38051,
            name = 'McIntoshCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38053,
            name = 'McKenzieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38055,
            name = 'McLeanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38057,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38059,
            name = 'MortonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38061,
            name = 'MountrailCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38063,
            name = 'NelsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38065,
            name = 'OliverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38067,
            name = 'PembinaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38069,
            name = 'PierceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38071,
            name = 'RamseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38073,
            name = 'RansomCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38075,
            name = 'RenvilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38077,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38079,
            name = 'RoletteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38081,
            name = 'SargentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38083,
            name = 'SheridanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38085,
            name = 'SiouxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38087,
            name = 'SlopeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38089,
            name = 'StarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38091,
            name = 'SteeleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38093,
            name = 'StutsmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38095,
            name = 'TownerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38097,
            name = 'TraillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38099,
            name = 'WalshCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38101,
            name = 'WardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38103,
            name = 'WellsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=38,
            fips = 38105,
            name = 'WilliamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39000,
            name = 'Ohio'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39003,
            name = 'AllenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39005,
            name = 'AshlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39007,
            name = 'AshtabulaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39009,
            name = 'AthensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39011,
            name = 'AuglaizeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39013,
            name = 'BelmontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39015,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39017,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39019,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39021,
            name = 'ChampaignCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39023,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39025,
            name = 'ClermontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39027,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39029,
            name = 'ColumbianaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39031,
            name = 'CoshoctonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39033,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39035,
            name = 'CuyahogaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39037,
            name = 'DarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39039,
            name = 'DefianceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39041,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39043,
            name = 'ErieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39045,
            name = 'FairfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39047,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39049,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39051,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39053,
            name = 'GalliaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39055,
            name = 'GeaugaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39057,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39059,
            name = 'GuernseyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39061,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39063,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39065,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39067,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39069,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39071,
            name = 'HighlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39073,
            name = 'HockingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39075,
            name = 'HolmesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39077,
            name = 'HuronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39079,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39081,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39083,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39085,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39087,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39089,
            name = 'LickingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39091,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39093,
            name = 'LorainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39095,
            name = 'LucasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39097,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39099,
            name = 'MahoningCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39101,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39103,
            name = 'MedinaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39105,
            name = 'MeigsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39107,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39109,
            name = 'MiamiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39111,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39113,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39115,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39117,
            name = 'MorrowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39119,
            name = 'MuskingumCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39121,
            name = 'NobleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39123,
            name = 'OttawaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39125,
            name = 'PauldingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39127,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39129,
            name = 'PickawayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39131,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39133,
            name = 'PortageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39135,
            name = 'PrebleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39137,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39139,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39141,
            name = 'RossCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39143,
            name = 'SanduskyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39145,
            name = 'SciotoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39147,
            name = 'SenecaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39149,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39151,
            name = 'StarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39153,
            name = 'SummitCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39155,
            name = 'TrumbullCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39157,
            name = 'TuscarawasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39159,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39161,
            name = 'VanWertCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39163,
            name = 'VintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39165,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39167,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39169,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39171,
            name = 'WilliamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39173,
            name = 'WoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=39,
            fips = 39175,
            name = 'WyandotCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40000,
            name = 'Oklahoma'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40001,
            name = 'AdairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40003,
            name = 'AlfalfaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40005,
            name = 'AtokaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40007,
            name = 'BeaverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40009,
            name = 'BeckhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40011,
            name = 'BlaineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40013,
            name = 'BryanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40015,
            name = 'CaddoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40017,
            name = 'CanadianCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40019,
            name = 'CarterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40021,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40023,
            name = 'ChoctawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40025,
            name = 'CimarronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40027,
            name = 'ClevelandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40029,
            name = 'CoalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40031,
            name = 'ComancheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40033,
            name = 'CottonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40035,
            name = 'CraigCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40037,
            name = 'CreekCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40039,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40041,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40043,
            name = 'DeweyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40045,
            name = 'EllisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40047,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40049,
            name = 'GarvinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40051,
            name = 'GradyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40053,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40055,
            name = 'GreerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40057,
            name = 'HarmonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40059,
            name = 'HarperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40061,
            name = 'HaskellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40063,
            name = 'HughesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40065,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40067,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40069,
            name = 'JohnstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40071,
            name = 'KayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40073,
            name = 'KingfisherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40075,
            name = 'KiowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40077,
            name = 'LatimerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40079,
            name = 'LeFloreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40081,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40083,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40085,
            name = 'LoveCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40087,
            name = 'McClainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40089,
            name = 'McCurtainCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40091,
            name = 'McIntoshCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40093,
            name = 'MajorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40095,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40097,
            name = 'MayesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40099,
            name = 'MurrayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40101,
            name = 'MuskogeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40103,
            name = 'NobleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40105,
            name = 'NowataCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40107,
            name = 'OkfuskeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40109,
            name = 'OklahomaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40111,
            name = 'OkmulgeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40113,
            name = 'OsageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40115,
            name = 'OttawaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40117,
            name = 'PawneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40119,
            name = 'PayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40121,
            name = 'PittsburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40123,
            name = 'PontotocCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40125,
            name = 'PottawatomieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40127,
            name = 'PushmatahaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40129,
            name = 'RogerMillsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40131,
            name = 'RogersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40133,
            name = 'SeminoleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40135,
            name = 'SequoyahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40137,
            name = 'StephensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40139,
            name = 'TexasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40141,
            name = 'TillmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40143,
            name = 'TulsaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40145,
            name = 'WagonerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40147,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40149,
            name = 'WashitaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40151,
            name = 'WoodsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=40,
            fips = 40153,
            name = 'WoodwardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41000,
            name = 'Oregon'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41001,
            name = 'BakerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41003,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41005,
            name = 'ClackamasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41007,
            name = 'ClatsopCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41009,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41011,
            name = 'CoosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41013,
            name = 'CrookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41015,
            name = 'CurryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41017,
            name = 'DeschutesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41019,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41021,
            name = 'GilliamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41023,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41025,
            name = 'HarneyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41027,
            name = 'HoodRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41029,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41031,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41033,
            name = 'JosephineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41035,
            name = 'KlamathCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41037,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41039,
            name = 'LaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41041,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41043,
            name = 'LinnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41045,
            name = 'MalheurCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41047,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41049,
            name = 'MorrowCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41051,
            name = 'MultnomahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41053,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41055,
            name = 'ShermanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41057,
            name = 'TillamookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41059,
            name = 'UmatillaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41061,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41063,
            name = 'WallowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41065,
            name = 'WascoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41067,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41069,
            name = 'WheelerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=41,
            fips = 41071,
            name = 'YamhillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42000,
            name = 'Pennsylvania'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42003,
            name = 'AlleghenyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42005,
            name = 'ArmstrongCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42007,
            name = 'BeaverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42009,
            name = 'BedfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42011,
            name = 'BerksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42013,
            name = 'BlairCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42015,
            name = 'BradfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42017,
            name = 'BucksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42019,
            name = 'ButlerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42021,
            name = 'CambriaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42023,
            name = 'CameronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42025,
            name = 'CarbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42027,
            name = 'CentreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42029,
            name = 'ChesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42031,
            name = 'ClarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42033,
            name = 'ClearfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42035,
            name = 'ClintonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42037,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42039,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42041,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42043,
            name = 'DauphinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42045,
            name = 'DelawareCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42047,
            name = 'ElkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42049,
            name = 'ErieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42051,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42053,
            name = 'ForestCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42055,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42057,
            name = 'FultonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42059,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42061,
            name = 'HuntingdonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42063,
            name = 'IndianaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42065,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42067,
            name = 'JuniataCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42069,
            name = 'LackawannaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42071,
            name = 'LancasterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42073,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42075,
            name = 'LebanonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42077,
            name = 'LehighCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42079,
            name = 'LuzerneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42081,
            name = 'LycomingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42083,
            name = 'McKeanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42085,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42087,
            name = 'MifflinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42089,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42091,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42093,
            name = 'MontourCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42095,
            name = 'NorthamptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42097,
            name = 'NorthumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42099,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42101,
            name = 'PhiladelphiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42103,
            name = 'PikeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42105,
            name = 'PotterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42107,
            name = 'SchuylkillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42109,
            name = 'SnyderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42111,
            name = 'SomersetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42113,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42115,
            name = 'SusquehannaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42117,
            name = 'TiogaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42119,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42121,
            name = 'VenangoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42123,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42125,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42127,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42129,
            name = 'WestmorelandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42131,
            name = 'WyomingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=42,
            fips = 42133,
            name = 'YorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44000,
            name = 'RhodeIsland'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44001,
            name = 'BristolCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44003,
            name = 'KentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44005,
            name = 'NewportCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44007,
            name = 'ProvidenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=44,
            fips = 44009,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45000,
            name = 'SouthCarolina'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45001,
            name = 'AbbevilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45003,
            name = 'AikenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45005,
            name = 'AllendaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45007,
            name = 'AndersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45009,
            name = 'BambergCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45011,
            name = 'BarnwellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45013,
            name = 'BeaufortCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45015,
            name = 'BerkeleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45017,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45019,
            name = 'CharlestonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45021,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45023,
            name = 'ChesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45025,
            name = 'ChesterfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45027,
            name = 'ClarendonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45029,
            name = 'ColletonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45031,
            name = 'DarlingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45033,
            name = 'DillonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45035,
            name = 'DorchesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45037,
            name = 'EdgefieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45039,
            name = 'FairfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45041,
            name = 'FlorenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45043,
            name = 'GeorgetownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45045,
            name = 'GreenvilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45047,
            name = 'GreenwoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45049,
            name = 'HamptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45051,
            name = 'HorryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45053,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45055,
            name = 'KershawCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45057,
            name = 'LancasterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45059,
            name = 'LaurensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45061,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45063,
            name = 'LexingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45065,
            name = 'McCormickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45067,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45069,
            name = 'MarlboroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45071,
            name = 'NewberryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45073,
            name = 'OconeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45075,
            name = 'OrangeburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45077,
            name = 'PickensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45079,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45081,
            name = 'SaludaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45083,
            name = 'SpartanburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45085,
            name = 'SumterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45087,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45089,
            name = 'WilliamsburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=45,
            fips = 45091,
            name = 'YorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46000,
            name = 'SouthDakota'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46003,
            name = 'AuroraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46005,
            name = 'BeadleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46007,
            name = 'BennettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46009,
            name = 'BonHommeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46011,
            name = 'BrookingsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46013,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46015,
            name = 'BruleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46017,
            name = 'BuffaloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46019,
            name = 'ButteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46021,
            name = 'CampbellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46023,
            name = 'CharlesMixCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46025,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46027,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46029,
            name = 'CodingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46031,
            name = 'CorsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46033,
            name = 'CusterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46035,
            name = 'DavisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46037,
            name = 'DayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46039,
            name = 'DeuelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46041,
            name = 'DeweyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46043,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46045,
            name = 'EdmundsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46047,
            name = 'FallRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46049,
            name = 'FaulkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46051,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46053,
            name = 'GregoryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46055,
            name = 'HaakonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46057,
            name = 'HamlinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46059,
            name = 'HandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46061,
            name = 'HansonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46063,
            name = 'HardingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46065,
            name = 'HughesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46067,
            name = 'HutchinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46069,
            name = 'HydeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46071,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46073,
            name = 'JerauldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46075,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46077,
            name = 'KingsburyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46079,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46081,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46083,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46085,
            name = 'LymanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46087,
            name = 'McCookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46089,
            name = 'McPhersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46091,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46093,
            name = 'MeadeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46095,
            name = 'MelletteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46097,
            name = 'MinerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46099,
            name = 'MinnehahaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46101,
            name = 'MoodyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46103,
            name = 'PenningtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46105,
            name = 'PerkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46107,
            name = 'PotterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46109,
            name = 'RobertsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46111,
            name = 'SanbornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46113,
            name = 'ShannonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46115,
            name = 'SpinkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46117,
            name = 'StanleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46119,
            name = 'SullyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46121,
            name = 'ToddCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46123,
            name = 'TrippCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46125,
            name = 'TurnerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46127,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46129,
            name = 'WalworthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46135,
            name = 'YanktonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=46,
            fips = 46137,
            name = 'ZiebachCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47000,
            name = 'Tennessee'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47001,
            name = 'AndersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47003,
            name = 'BedfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47005,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47007,
            name = 'BledsoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47009,
            name = 'BlountCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47011,
            name = 'BradleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47013,
            name = 'CampbellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47015,
            name = 'CannonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47017,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47019,
            name = 'CarterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47021,
            name = 'CheathamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47023,
            name = 'ChesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47025,
            name = 'ClaiborneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47027,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47029,
            name = 'CockeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47031,
            name = 'CoffeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47033,
            name = 'CrockettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47035,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47037,
            name = 'DavidsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47039,
            name = 'DecaturCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47041,
            name = 'DeKalbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47043,
            name = 'DicksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47045,
            name = 'DyerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47047,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47049,
            name = 'FentressCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47051,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47053,
            name = 'GibsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47055,
            name = 'GilesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47057,
            name = 'GraingerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47059,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47061,
            name = 'GrundyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47063,
            name = 'HamblenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47065,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47067,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47069,
            name = 'HardemanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47071,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47073,
            name = 'HawkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47075,
            name = 'HaywoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47077,
            name = 'HendersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47079,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47081,
            name = 'HickmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47083,
            name = 'HoustonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47085,
            name = 'HumphreysCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47087,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47089,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47091,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47093,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47095,
            name = 'LakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47097,
            name = 'LauderdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47099,
            name = 'LawrenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47101,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47103,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47105,
            name = 'LoudonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47107,
            name = 'McMinnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47109,
            name = 'McNairyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47111,
            name = 'MaconCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47113,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47115,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47117,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47119,
            name = 'MauryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47121,
            name = 'MeigsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47123,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47125,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47127,
            name = 'MooreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47129,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47131,
            name = 'ObionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47133,
            name = 'OvertonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47135,
            name = 'PerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47137,
            name = 'PickettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47139,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47141,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47143,
            name = 'RheaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47145,
            name = 'RoaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47147,
            name = 'RobertsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47149,
            name = 'RutherfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47151,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47153,
            name = 'SequatchieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47155,
            name = 'SevierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47157,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47159,
            name = 'SmithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47161,
            name = 'StewartCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47163,
            name = 'SullivanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47165,
            name = 'SumnerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47167,
            name = 'TiptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47169,
            name = 'TrousdaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47171,
            name = 'UnicoiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47173,
            name = 'UnionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47175,
            name = 'VanBurenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47177,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47179,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47181,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47183,
            name = 'WeakleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47185,
            name = 'WhiteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47187,
            name = 'WilliamsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=47,
            fips = 47189,
            name = 'WilsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48000,
            name = 'Texas'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48001,
            name = 'AndersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48003,
            name = 'AndrewsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48005,
            name = 'AngelinaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48007,
            name = 'AransasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48009,
            name = 'ArcherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48011,
            name = 'ArmstrongCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48013,
            name = 'AtascosaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48015,
            name = 'AustinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48017,
            name = 'BaileyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48019,
            name = 'BanderaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48021,
            name = 'BastropCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48023,
            name = 'BaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48025,
            name = 'BeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48027,
            name = 'BellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48029,
            name = 'BexarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48031,
            name = 'BlancoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48033,
            name = 'BordenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48035,
            name = 'BosqueCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48037,
            name = 'BowieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48039,
            name = 'BrazoriaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48041,
            name = 'BrazosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48043,
            name = 'BrewsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48045,
            name = 'BriscoeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48047,
            name = 'BrooksCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48049,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48051,
            name = 'BurlesonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48053,
            name = 'BurnetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48055,
            name = 'CaldwellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48057,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48059,
            name = 'CallahanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48061,
            name = 'CameronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48063,
            name = 'CampCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48065,
            name = 'CarsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48067,
            name = 'CassCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48069,
            name = 'CastroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48071,
            name = 'ChambersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48073,
            name = 'CherokeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48075,
            name = 'ChildressCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48077,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48079,
            name = 'CochranCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48081,
            name = 'CokeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48083,
            name = 'ColemanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48085,
            name = 'CollinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48087,
            name = 'CollingsworthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48089,
            name = 'ColoradoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48091,
            name = 'ComalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48093,
            name = 'ComancheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48095,
            name = 'ConchoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48097,
            name = 'CookeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48099,
            name = 'CoryellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48101,
            name = 'CottleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48103,
            name = 'CraneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48105,
            name = 'CrockettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48107,
            name = 'CrosbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48109,
            name = 'CulbersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48111,
            name = 'DallamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48113,
            name = 'DallasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48115,
            name = 'DawsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48117,
            name = 'DeafSmithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48119,
            name = 'DeltaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48121,
            name = 'DentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48123,
            name = 'DeWittCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48125,
            name = 'DickensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48127,
            name = 'DimmitCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48129,
            name = 'DonleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48131,
            name = 'DuvalCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48133,
            name = 'EastlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48135,
            name = 'EctorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48137,
            name = 'EdwardsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48139,
            name = 'EllisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48141,
            name = 'ElPasoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48143,
            name = 'ErathCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48145,
            name = 'FallsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48147,
            name = 'FanninCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48149,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48151,
            name = 'FisherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48153,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48155,
            name = 'FoardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48157,
            name = 'FortBendCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48159,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48161,
            name = 'FreestoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48163,
            name = 'FrioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48165,
            name = 'GainesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48167,
            name = 'GalvestonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48169,
            name = 'GarzaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48171,
            name = 'GillespieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48173,
            name = 'GlasscockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48175,
            name = 'GoliadCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48177,
            name = 'GonzalesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48179,
            name = 'GrayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48181,
            name = 'GraysonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48183,
            name = 'GreggCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48185,
            name = 'GrimesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48187,
            name = 'GuadalupeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48189,
            name = 'HaleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48191,
            name = 'HallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48193,
            name = 'HamiltonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48195,
            name = 'HansfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48197,
            name = 'HardemanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48199,
            name = 'HardinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48201,
            name = 'HarrisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48203,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48205,
            name = 'HartleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48207,
            name = 'HaskellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48209,
            name = 'HaysCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48211,
            name = 'HemphillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48213,
            name = 'HendersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48215,
            name = 'HidalgoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48217,
            name = 'HillCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48219,
            name = 'HockleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48221,
            name = 'HoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48223,
            name = 'HopkinsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48225,
            name = 'HoustonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48227,
            name = 'HowardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48229,
            name = 'HudspethCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48231,
            name = 'HuntCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48233,
            name = 'HutchinsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48235,
            name = 'IrionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48237,
            name = 'JackCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48239,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48241,
            name = 'JasperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48243,
            name = 'JeffDavisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48245,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48247,
            name = 'JimHoggCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48249,
            name = 'JimWellsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48251,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48253,
            name = 'JonesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48255,
            name = 'KarnesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48257,
            name = 'KaufmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48259,
            name = 'KendallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48261,
            name = 'KenedyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48263,
            name = 'KentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48265,
            name = 'KerrCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48267,
            name = 'KimbleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48269,
            name = 'KingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48271,
            name = 'KinneyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48273,
            name = 'KlebergCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48275,
            name = 'KnoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48277,
            name = 'LamarCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48279,
            name = 'LambCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48281,
            name = 'LampasasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48283,
            name = 'LaSalleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48285,
            name = 'LavacaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48287,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48289,
            name = 'LeonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48291,
            name = 'LibertyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48293,
            name = 'LimestoneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48295,
            name = 'LipscombCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48297,
            name = 'LiveOakCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48299,
            name = 'LlanoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48301,
            name = 'LovingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48303,
            name = 'LubbockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48305,
            name = 'LynnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48307,
            name = 'McCullochCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48309,
            name = 'McLennanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48311,
            name = 'McMullenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48313,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48315,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48317,
            name = 'MartinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48319,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48321,
            name = 'MatagordaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48323,
            name = 'MaverickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48325,
            name = 'MedinaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48327,
            name = 'MenardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48329,
            name = 'MidlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48331,
            name = 'MilamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48333,
            name = 'MillsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48335,
            name = 'MitchellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48337,
            name = 'MontagueCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48339,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48341,
            name = 'MooreCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48343,
            name = 'MorrisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48345,
            name = 'MotleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48347,
            name = 'NacogdochesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48349,
            name = 'NavarroCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48351,
            name = 'NewtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48353,
            name = 'NolanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48355,
            name = 'NuecesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48357,
            name = 'OchiltreeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48359,
            name = 'OldhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48361,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48363,
            name = 'PaloPintoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48365,
            name = 'PanolaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48367,
            name = 'ParkerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48369,
            name = 'ParmerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48371,
            name = 'PecosCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48373,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48375,
            name = 'PotterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48377,
            name = 'PresidioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48379,
            name = 'RainsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48381,
            name = 'RandallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48383,
            name = 'ReaganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48385,
            name = 'RealCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48387,
            name = 'RedRiverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48389,
            name = 'ReevesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48391,
            name = 'RefugioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48393,
            name = 'RobertsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48395,
            name = 'RobertsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48397,
            name = 'RockwallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48399,
            name = 'RunnelsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48401,
            name = 'RuskCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48403,
            name = 'SabineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48405,
            name = 'SanAugustineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48407,
            name = 'SanJacintoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48409,
            name = 'SanPatricioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48411,
            name = 'SanSabaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48413,
            name = 'SchleicherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48415,
            name = 'ScurryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48417,
            name = 'ShackelfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48419,
            name = 'ShelbyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48421,
            name = 'ShermanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48423,
            name = 'SmithCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48425,
            name = 'SomervellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48427,
            name = 'StarrCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48429,
            name = 'StephensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48431,
            name = 'SterlingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48433,
            name = 'StonewallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48435,
            name = 'SuttonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48437,
            name = 'SwisherCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48439,
            name = 'TarrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48441,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48443,
            name = 'TerrellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48445,
            name = 'TerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48447,
            name = 'ThrockmortonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48449,
            name = 'TitusCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48451,
            name = 'TomGreenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48453,
            name = 'TravisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48455,
            name = 'TrinityCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48457,
            name = 'TylerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48459,
            name = 'UpshurCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48461,
            name = 'UptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48463,
            name = 'UvaldeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48465,
            name = 'ValVerdeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48467,
            name = 'VanZandtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48469,
            name = 'VictoriaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48471,
            name = 'WalkerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48473,
            name = 'WallerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48475,
            name = 'WardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48477,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48479,
            name = 'WebbCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48481,
            name = 'WhartonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48483,
            name = 'WheelerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48485,
            name = 'WichitaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48487,
            name = 'WilbargerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48489,
            name = 'WillacyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48491,
            name = 'WilliamsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48493,
            name = 'WilsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48495,
            name = 'WinklerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48497,
            name = 'WiseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48499,
            name = 'WoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48501,
            name = 'YoakumCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48503,
            name = 'YoungCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48505,
            name = 'ZapataCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=48,
            fips = 48507,
            name = 'ZavalaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49000,
            name = 'Utah'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49001,
            name = 'BeaverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49003,
            name = 'BoxElderCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49005,
            name = 'CacheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49007,
            name = 'CarbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49009,
            name = 'DaggettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49011,
            name = 'DavisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49013,
            name = 'DuchesneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49015,
            name = 'EmeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49017,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49019,
            name = 'GrandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49021,
            name = 'IronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49023,
            name = 'JuabCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49025,
            name = 'KaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49027,
            name = 'MillardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49029,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49031,
            name = 'PiuteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49033,
            name = 'RichCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49035,
            name = 'SaltLakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49037,
            name = 'SanJuanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49039,
            name = 'SanpeteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49041,
            name = 'SevierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49043,
            name = 'SummitCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49045,
            name = 'TooeleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49047,
            name = 'UintahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49049,
            name = 'UtahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49051,
            name = 'WasatchCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49053,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49055,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=49,
            fips = 49057,
            name = 'WeberCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50000,
            name = 'Vermont'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50001,
            name = 'AddisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50003,
            name = 'BenningtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50005,
            name = 'CaledoniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50007,
            name = 'ChittendenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50009,
            name = 'EssexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50011,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50013,
            name = 'GrandIsleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50015,
            name = 'LamoilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50017,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50019,
            name = 'OrleansCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50021,
            name = 'RutlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50023,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50025,
            name = 'WindhamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=50,
            fips = 50027,
            name = 'WindsorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51000,
            name = 'Virginia'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51001,
            name = 'AccomackCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51003,
            name = 'AlbemarleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51005,
            name = 'AlleghanyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51007,
            name = 'AmeliaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51009,
            name = 'AmherstCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51011,
            name = 'AppomattoxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51013,
            name = 'ArlingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51015,
            name = 'AugustaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51017,
            name = 'BathCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51019,
            name = 'BedfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51021,
            name = 'BlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51023,
            name = 'BotetourtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51025,
            name = 'BrunswickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51027,
            name = 'BuchananCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51029,
            name = 'BuckinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51031,
            name = 'CampbellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51033,
            name = 'CarolineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51035,
            name = 'CarrollCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51036,
            name = 'CharlesCityCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51037,
            name = 'CharlotteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51041,
            name = 'ChesterfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51043,
            name = 'ClarkeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51045,
            name = 'CraigCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51047,
            name = 'CulpeperCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51049,
            name = 'CumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51051,
            name = 'DickensonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51053,
            name = 'DinwiddieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51057,
            name = 'EssexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51059,
            name = 'FairfaxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51061,
            name = 'FauquierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51063,
            name = 'FloydCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51065,
            name = 'FluvannaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51067,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51069,
            name = 'FrederickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51071,
            name = 'GilesCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51073,
            name = 'GloucesterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51075,
            name = 'GoochlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51077,
            name = 'GraysonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51079,
            name = 'GreeneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51081,
            name = 'GreensvilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51083,
            name = 'HalifaxCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51085,
            name = 'HanoverCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51087,
            name = 'HenricoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51089,
            name = 'HenryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51091,
            name = 'HighlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51093,
            name = 'IsleofWightCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51095,
            name = 'JamesCityCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51097,
            name = 'KingandQueenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51099,
            name = 'KingGeorgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51101,
            name = 'KingWilliamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51103,
            name = 'LancasterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51105,
            name = 'LeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51107,
            name = 'LoudounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51109,
            name = 'LouisaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51111,
            name = 'LunenburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51113,
            name = 'MadisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51115,
            name = 'MathewsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51117,
            name = 'MecklenburgCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51119,
            name = 'MiddlesexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51121,
            name = 'MontgomeryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51125,
            name = 'NelsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51127,
            name = 'NewKentCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51131,
            name = 'NorthamptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51133,
            name = 'NorthumberlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51135,
            name = 'NottowayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51137,
            name = 'OrangeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51139,
            name = 'PageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51141,
            name = 'PatrickCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51143,
            name = 'PittsylvaniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51145,
            name = 'PowhatanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51147,
            name = 'PrinceEdwardCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51149,
            name = 'PrinceGeorgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51153,
            name = 'PrinceWilliamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51155,
            name = 'PulaskiCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51157,
            name = 'RappahannockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51159,
            name = 'RichmondCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51161,
            name = 'RoanokeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51163,
            name = 'RockbridgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51165,
            name = 'RockinghamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51167,
            name = 'RussellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51169,
            name = 'ScottCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51171,
            name = 'ShenandoahCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51173,
            name = 'SmythCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51175,
            name = 'SouthamptonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51177,
            name = 'SpotsylvaniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51179,
            name = 'StaffordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51181,
            name = 'SurryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51183,
            name = 'SussexCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51185,
            name = 'TazewellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51187,
            name = 'WarrenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51191,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51193,
            name = 'WestmorelandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51195,
            name = 'WiseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51197,
            name = 'WytheCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51199,
            name = 'YorkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51510,
            name = 'Alexandriacity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51515,
            name = 'Bedfordcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51520,
            name = 'Bristolcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51530,
            name = 'BuenaVistacity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51540,
            name = 'Charlottesvillecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51550,
            name = 'Chesapeakecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51560,
            name = 'CliftonForgecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51570,
            name = 'ColonialHeightscity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51580,
            name = 'Covingtoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51590,
            name = 'Danvillecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51595,
            name = 'Emporiacity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51600,
            name = 'Fairfaxcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51610,
            name = 'FallsChurchcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51620,
            name = 'Franklincity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51630,
            name = 'Fredericksburgcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51640,
            name = 'Galaxcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51650,
            name = 'Hamptoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51660,
            name = 'Harrisonburgcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51670,
            name = 'Hopewellcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51678,
            name = 'Lexingtoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51680,
            name = 'Lynchburgcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51683,
            name = 'Manassascity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51685,
            name = 'ManassasParkcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51690,
            name = 'Martinsvillecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51700,
            name = 'NewportNewscity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51710,
            name = 'Norfolkcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51720,
            name = 'Nortoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51730,
            name = 'Petersburgcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51735,
            name = 'Poquosoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51740,
            name = 'Portsmouthcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51750,
            name = 'Radfordcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51760,
            name = 'Richmondcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51770,
            name = 'Roanokecity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51775,
            name = 'Salemcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 517801990,
            name = 'SouthBostoncity(After,partofHalifaxCounty)'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51790,
            name = 'Stauntoncity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51800,
            name = 'Suffolkcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51810,
            name = 'VirginiaBeachcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51820,
            name = 'Waynesborocity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51830,
            name = 'Williamsburgcity'
        )
        new_county.save()
    

        new_county = County(
            state_id=51,
            fips = 51840,
            name = 'Winchestercity'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53000,
            name = 'Washington'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53003,
            name = 'AsotinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53005,
            name = 'BentonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53007,
            name = 'ChelanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53009,
            name = 'ClallamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53011,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53013,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53015,
            name = 'CowlitzCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53017,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53019,
            name = 'FerryCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53021,
            name = 'FranklinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53023,
            name = 'GarfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53025,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53027,
            name = 'GraysHarborCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53029,
            name = 'IslandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53031,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53033,
            name = 'KingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53035,
            name = 'KitsapCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53037,
            name = 'KittitasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53039,
            name = 'KlickitatCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53041,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53043,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53045,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53047,
            name = 'OkanoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53049,
            name = 'PacificCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53051,
            name = 'PendOreilleCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53053,
            name = 'PierceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53055,
            name = 'SanJuanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53057,
            name = 'SkagitCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53059,
            name = 'SkamaniaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53061,
            name = 'SnohomishCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53063,
            name = 'SpokaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53065,
            name = 'StevensCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53067,
            name = 'ThurstonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53069,
            name = 'WahkiakumCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53071,
            name = 'WallaWallaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53073,
            name = 'WhatcomCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53075,
            name = 'WhitmanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=53,
            fips = 53077,
            name = 'YakimaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54000,
            name = 'WestVirginia'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54001,
            name = 'BarbourCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54003,
            name = 'BerkeleyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54005,
            name = 'BooneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54007,
            name = 'BraxtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54009,
            name = 'BrookeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54011,
            name = 'CabellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54013,
            name = 'CalhounCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54015,
            name = 'ClayCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54017,
            name = 'DoddridgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54019,
            name = 'FayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54021,
            name = 'GilmerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54023,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54025,
            name = 'GreenbrierCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54027,
            name = 'HampshireCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54029,
            name = 'HancockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54031,
            name = 'HardyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54033,
            name = 'HarrisonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54035,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54037,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54039,
            name = 'KanawhaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54041,
            name = 'LewisCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54043,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54045,
            name = 'LoganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54047,
            name = 'McDowellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54049,
            name = 'MarionCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54051,
            name = 'MarshallCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54053,
            name = 'MasonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54055,
            name = 'MercerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54057,
            name = 'MineralCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54059,
            name = 'MingoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54061,
            name = 'MonongaliaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54063,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54065,
            name = 'MorganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54067,
            name = 'NicholasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54069,
            name = 'OhioCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54071,
            name = 'PendletonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54073,
            name = 'PleasantsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54075,
            name = 'PocahontasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54077,
            name = 'PrestonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54079,
            name = 'PutnamCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54081,
            name = 'RaleighCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54083,
            name = 'RandolphCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54085,
            name = 'RitchieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54087,
            name = 'RoaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54089,
            name = 'SummersCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54091,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54093,
            name = 'TuckerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54095,
            name = 'TylerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54097,
            name = 'UpshurCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54099,
            name = 'WayneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54101,
            name = 'WebsterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54103,
            name = 'WetzelCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54105,
            name = 'WirtCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54107,
            name = 'WoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=54,
            fips = 54109,
            name = 'WyomingCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55000,
            name = 'Wisconsin'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55001,
            name = 'AdamsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55003,
            name = 'AshlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55005,
            name = 'BarronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55007,
            name = 'BayfieldCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55009,
            name = 'BrownCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55011,
            name = 'BuffaloCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55013,
            name = 'BurnettCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55015,
            name = 'CalumetCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55017,
            name = 'ChippewaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55019,
            name = 'ClarkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55021,
            name = 'ColumbiaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55023,
            name = 'CrawfordCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55025,
            name = 'DaneCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55027,
            name = 'DodgeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55029,
            name = 'DoorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55031,
            name = 'DouglasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55033,
            name = 'DunnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55035,
            name = 'EauClaireCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55037,
            name = 'FlorenceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55039,
            name = 'FondduLacCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55041,
            name = 'ForestCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55043,
            name = 'GrantCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55045,
            name = 'GreenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55047,
            name = 'GreenLakeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55049,
            name = 'IowaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55051,
            name = 'IronCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55053,
            name = 'JacksonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55055,
            name = 'JeffersonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55057,
            name = 'JuneauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55059,
            name = 'KenoshaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55061,
            name = 'KewauneeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55063,
            name = 'LaCrosseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55065,
            name = 'LafayetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55067,
            name = 'LangladeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55069,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55071,
            name = 'ManitowocCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55073,
            name = 'MarathonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55075,
            name = 'MarinetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55077,
            name = 'MarquetteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55078,
            name = 'MenomineeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55079,
            name = 'MilwaukeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55081,
            name = 'MonroeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55083,
            name = 'OcontoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55085,
            name = 'OneidaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55087,
            name = 'OutagamieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55089,
            name = 'OzaukeeCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55091,
            name = 'PepinCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55093,
            name = 'PierceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55095,
            name = 'PolkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55097,
            name = 'PortageCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55099,
            name = 'PriceCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55101,
            name = 'RacineCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55103,
            name = 'RichlandCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55105,
            name = 'RockCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55107,
            name = 'RuskCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55109,
            name = 'St.CroixCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55111,
            name = 'SaukCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55113,
            name = 'SawyerCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55115,
            name = 'ShawanoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55117,
            name = 'SheboyganCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55119,
            name = 'TaylorCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55121,
            name = 'TrempealeauCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55123,
            name = 'VernonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55125,
            name = 'VilasCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55127,
            name = 'WalworthCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55129,
            name = 'WashburnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55131,
            name = 'WashingtonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55133,
            name = 'WaukeshaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55135,
            name = 'WaupacaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55137,
            name = 'WausharaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55139,
            name = 'WinnebagoCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=55,
            fips = 55141,
            name = 'WoodCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56000,
            name = 'Wyoming'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56001,
            name = 'AlbanyCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56003,
            name = 'BigHornCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56005,
            name = 'CampbellCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56007,
            name = 'CarbonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56009,
            name = 'ConverseCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56011,
            name = 'CrookCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56013,
            name = 'FremontCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56015,
            name = 'GoshenCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56017,
            name = 'HotSpringsCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56019,
            name = 'JohnsonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56021,
            name = 'LaramieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56023,
            name = 'LincolnCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56025,
            name = 'NatronaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56027,
            name = 'NiobraraCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56029,
            name = 'ParkCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56031,
            name = 'PlatteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56033,
            name = 'SheridanCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56035,
            name = 'SubletteCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56037,
            name = 'SweetwaterCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56039,
            name = 'TetonCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56041,
            name = 'UintaCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56043,
            name = 'WashakieCounty'
        )
        new_county.save()
    

        new_county = County(
            state_id=56,
            fips = 56045,
            name = 'WestonCounty'
        )
        new_county.save()
    