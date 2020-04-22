from inventory.models import BusDocumentModel
from rest_framework import serializers


class BusDocumentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusDocumentModel
        exclude = ['bus_document_id']


class BusDocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusDocumentModel
        fields = '__all__'

