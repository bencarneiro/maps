from django.core.management.base import BaseCommand
from app.models import ACS5ValueByTract,ACS1ValueByTract, Tract


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        ACS5ValueByTract.objects.all().delete()
        ACS1ValueByTract.objects.all().delete()
        Tract.objects.all().delete()
        # print(len(a))
        # for b in a:
        #     print(b.acs_variable.concept)
        #     print(b.tract.county.name)