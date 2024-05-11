from rest_framework import serializers
from index.models import Temperature


class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        exclude = ['date',]
        