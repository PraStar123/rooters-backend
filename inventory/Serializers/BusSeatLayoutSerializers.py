from inventory.models import BusSeatLayoutModel
from rest_framework import serializers


class BusSeatLayoutEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSeatLayoutModel
        exclude = ['seat_layout_id']


class BusSeatLayoutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSeatLayoutModel
        fields = '__all__'

