from django.urls import path
from .views import LocationView, Weather, OneForecast, LocationsView

urlpatterns = [
    path('weather', Weather.as_view(), name='weather'),
    path('location', LocationView.as_view(), name='location'),
    path('locations', LocationsView.as_view(), name='all_locations'),
    path('weather/one', OneForecast.as_view(), name='one_forecast')
]