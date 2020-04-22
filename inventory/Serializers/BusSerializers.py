from inventory.models import BusModel
from rest_framework import serializers


class BusEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusModel
        exclude = ['bus_id']


class BusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusModel
        fields = '__all__'

