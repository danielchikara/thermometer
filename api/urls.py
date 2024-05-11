from django.urls import path
from .views import CreateValueThermometer

app_name = 'api'

urlpatterns = [
    # ...
    
    path('value/create/', CreateValueThermometer.as_view(), name="create_value"),
    
    
]