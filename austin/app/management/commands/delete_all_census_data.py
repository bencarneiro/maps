from django.core.management.base import BaseCommand
from app.models import ACS5ValueByTract, ACS1ValueByTract


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        ACS1ValueByTract.objects.all().delete()
        ACS5ValueByTract.objects.all().delete()
        # print(len(a))
        # for b in a:
        #     print(b.acs_variable.concept)
        #     print(b.tract.county.name)