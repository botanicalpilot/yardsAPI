from django.shortcuts import render
from .models import APIPlantRecord
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import APIAppSerializer, UserSerializer
from django_filters import rest_framework as filters

class APIAppSearch(filters.FilterSet):
    # search_fields = ['scientificNameAuthor', 'nationalCommonName', 'family', ]
    class Meta:
        model = APIPlantRecord
        fields = {
            'symbol':['iexact'],
            'scientificNameAuthor':['icontains'],
            'nationalCommonName':['icontains'],
            'family':['icontains'],
            'nativeState':['iexact'],
            'isInvasive':['iexact'],


        }



class APIAppViewSet(viewsets.ModelViewSet):
    queryset = APIPlantRecord.objects.all()
    serializer_class = APIAppSerializer
    filterset_class = APIAppSearch

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    

 