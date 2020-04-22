from inventory.models import CityModel
from rest_framework import serializers


class CityEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        exclude = ['city_id']


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'
