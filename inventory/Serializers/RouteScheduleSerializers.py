from django.db import models
from inventory.models import RouteScheduleModel
from rest_framework import serializers
import inventory.Serializers.BusConfigSerializers as BusConfigSerializers
import inventory.Serializers.RouteSerializers as RouteSerializers
import uuid


class RouteScheduleEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteScheduleModel
        exclude = ['route_schedule_id']


class RouteScheduleListSerializer(serializers.ModelSerializer):
    bus_config = BusConfigSerializers.BusConfigListSerializer(read_only=True)
    #route = RouteSerializers.RouteListSerializer(read_only=True)
    class Meta:
        model = RouteScheduleModel
        fields= '__all__'


class RouteScheduleDisplaySerializer(serializers.Serializer):
    route_group = serializers.CharField(max_length=50)
    from_source = serializers.CharField(max_length=50)
    to_dest = serializers.CharField(max_length=50)
    bus_config = BusConfigSerializers.BusConfigListSerializer()
    dep_date = serializers.DateField()
    arr_date = serializers.DateField()
    dep_time = serializers.TimeField()
    arr_time = serializers.TimeField()
    from_order = serializers.IntegerField()
    to_order = serializers.IntegerField()