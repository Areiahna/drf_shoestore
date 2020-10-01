from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import ShoeSerializer, ManufacturerSerializer, ShoeColorSerializer, ShoetypeSerializer
from shoeapp.models import Shoe, Manufacturer, Shoetype, ShoeColor
# Create your views here.


class ShoeViewSet (viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ManufacturerViewSet (viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoetypeViewSet(viewsets.ModelViewSet):
    queryset = Shoetype.objects.all()
    serializer_class = ShoetypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer
