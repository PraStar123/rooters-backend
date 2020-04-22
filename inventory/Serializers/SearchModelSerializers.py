from django.db import models
from inventory.models import SearchModel
from rest_framework import serializers
import inventory.Serializers.BusConfigSerializers as BusConfigSerializers
import uuid


class SearchEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchModel
        fields = '__all__'


class SearchListSerializer(serializers.ModelSerializer):
    bus_config = BusConfigSerializers.BusConfigListSerializer(read_only=True)
    class Meta:
        model = SearchModel
        fields= '__all__'


