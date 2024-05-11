from django.shortcuts import render
from rest_framework import generics
from .serializers import SensorValueSerializer
from index.models import Temperature
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class CreateValueThermometer(generics.CreateAPIView):
    serializer_class = SensorValueSerializer
    
    
class GetLastValueTHermometer(generics.RetrieveAPIView):
    serializer_class = SensorValueSerializer
    
    def get_object(self):
        sensor_id = self.kwargs['sensor_id']
        get_object =  Temperature.objects.all().order_by('-datetime').first()
        print(get_object)
        return get_object