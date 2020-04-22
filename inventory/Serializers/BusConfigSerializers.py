from rest_framework import serializers
from inventory.models import BusConfigModel
from .BusSeatLayoutSerializers import BusSeatLayoutListSerializer
from django.db import models


class BusConfigEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusConfigModel
        exclude = ['bus_config_id']


class BusConfigListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusConfigModel
        fields = '__all__'
