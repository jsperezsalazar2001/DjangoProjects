from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Temperature
from .models import Mediciones
from .serializers import TemperatureSerializer
from .serializers import MedicionesSerializer

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all().order_by('-created')
    serializer_class = TemperatureSerializer

class MedicionesViewSet(viewsets.ModelViewSet):
    queryset = Mediciones.objects.all().order_by('-created')
    serializer_class = MedicionesSerializer
