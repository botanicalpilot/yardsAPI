from rest_framework import serializers
from APIApp.models import APIPlantRecord
from django.contrib.auth.models import User


class APIAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIPlantRecord
        fields = ['symbol', 'synonymSymbol', 'scientificNameAuthor', 'nationalCommonName', 'family', 'nativeState', 'isInvasive']

class UserSerializer(serializers.ModelSerializer):
    apiPlant = serializers.PrimaryKeyRelatedField(many=True, queryset=APIPlantRecord.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'APIApp']