from rest_framework import serializers
from .models import Location, DailyForecast, CurrentWeather


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['locationId', 'name', 'lat', 'lon']


class DailyForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyForecast
        fields = '__all__'


class CurrentWeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentWeather
        fields = '__all__'
