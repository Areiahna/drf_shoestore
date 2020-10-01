from django.contrib import admin

# Register your models here.
from shoeapp.models import Shoe, Manufacturer, Shoetype, ShoeColor
admin.site.register(Shoe)
admin.site.register(Shoetype)
admin.site.register(ShoeColor)
admin.site.register(Manufacturer)
