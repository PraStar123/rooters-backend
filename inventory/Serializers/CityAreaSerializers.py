from inventory.models import CityAreaModel
from rest_framework import serializers


class CityAreaEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityAreaModel
        exclude = ['city_area_id']


class CityAreaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityAreaModel
        fields = '__all__'

