from inventory.models import RouteModel
from rest_framework import serializers


class RouteEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        exclude = ['route_id']


class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'

