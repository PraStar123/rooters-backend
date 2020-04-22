from inventory.models import TripModel
from rest_framework import serializers


class TripEditSerializer(serializers.Serializer):
    class Meta:
        model = TripModel
        exclude = ['trip_id']


class TripListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripModel
        fields = '__all__'

