from django.core.management import BaseCommand

from musiclib.models import CustomUser, MusicFiles


class Command(BaseCommand):

    def handle(self, *args, **options):
        import sys
        print(sys.path)
     