from rest_framework import serializers

from shoeapp.models import Shoe, Manufacturer, Shoetype, ShoeColor


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id',
            'size',
            'brand_name',
            'color',
            'manufacturer',
            'material',
            'shoe_type',
            'fasten_type'
        ]


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = [
            'id',
            'name',
            'website'
        ]


class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = [
            'color_name'
        ]


class ShoetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoetype
        fields = [
            'style'
        ]
