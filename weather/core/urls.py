from django.urls import path
from .views import LocationView, Weather, OneForecast

urlpatterns = [
    path('weather', Weather.as_view(), name='weather'),
    path('location', LocationView.as_view(), name='location'),
    path('weather/one', OneForecast.as_view(), name='one_forecast')
]