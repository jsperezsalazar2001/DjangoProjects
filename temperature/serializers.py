from rest_framework import serializers
from .models import Temperature
from .models import Mediciones

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ('id', 'type', 'value')

class MedicionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mediciones
        fields = ('id', 'fecha', 'origen', 'valor', 'codigos', 'observacion')