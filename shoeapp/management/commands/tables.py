from django.core.management.base import BaseCommand, CommandError
from shoeapp.models import Shoetype, ShoeColor
# ?? Import bootstrap? - just installed it never used it before


class bootstrap_data(BaseCommand):

   # def "?? Function that connects bootstrap to shoeapp"
    def shoe_color(self, parser):
        pass

       # "?? Setup like views in other applications? "
       # the command should populate the model tables with their choices.
