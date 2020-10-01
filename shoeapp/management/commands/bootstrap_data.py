from django.core.management.base import BaseCommand, CommandError
from shoeapp.models import Shoetype, ShoeColor


class Command(BaseCommand):

    def handle(self, *args, **options):
        Shoetype.objects.create(style='Sneaker')
        Shoetype.objects.create(style='Boot')
        Shoetype.objects.create(style='Sandal')
        Shoetype.objects.create(style='Dress')
        Shoetype.objects.create(style='Other')

        ShoeColor.objects.create(color_name='RED')
        ShoeColor.objects.create(color_name='ORANGE')
        ShoeColor.objects.create(color_name='YELLOW')
        ShoeColor.objects.create(color_name='GREEN')
        ShoeColor.objects.create(color_name='BLUE')
        ShoeColor.objects.create(color_name='INDIGO')
        ShoeColor.objects.create(color_name='WHITE')
        ShoeColor.objects.create(color_name='BLACK')
