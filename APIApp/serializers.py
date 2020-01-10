from rest_framework import serializers
from APIApp.models import APIPlantRecord

class APIAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIPlantRecord
        fields = ['symbol', 'synonymSymbol', 'scientificNameAuthor', 'nationalCommonName', 'family', 'nativeState']