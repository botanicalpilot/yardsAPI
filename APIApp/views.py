from django.shortcuts import render
from .models import APIPlantRecord
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import APIAppSerializer

class APIAppViewSet(viewsets.ModelViewSet):
    queryset = APIPlantRecord.objects.all()
    serializer_class = APIAppSerializer

    # @action(detail=False, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     plant = self.get_object()
    #     return Response(plant.highlighted)


 