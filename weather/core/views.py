from datetime import timedelta, datetime as dt
from rest_framework.views import APIView, Response, status
from .models import Location, CurrentWeather, DailyForecast, ApiKey, APILimit
from .serializers import LocationSerializer, DailyForecastSerializer, CurrentWeatherSerializer
from .functions import weather


class LocationView(APIView):
    def get(self, request):
        location = request.GET.get('location', None)
        if location:
            serializer = LocationSerializer(Location.objects.get(locationId=location))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': 'Location is required parameter'}, status=status.HTTP_400_BAD_REQUEST)


class LocationsView(APIView):
    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Weather(APIView):
    def get(self, request):
        location = request.GET.get('location', None)
        api_limit = APILimit.objects.get(pk=1)

        if api_limit.currentLimit == api_limit.limit:
            return Response({'message': 'Limit is reached, try fetch data tomorrow'}, status=status.HTTP_403_FORBIDDEN)

        if location:
            loc = Location.objects.get(locationId=location)
            current = CurrentWeather.objects.filter(location=loc, fetched=dt.today())
            loc_serializer = LocationSerializer(loc)
            if current.exists() and dt.today().date() != api_limit.resetDate:
                # get data from cache
                current_weather = CurrentWeatherSerializer(current[0]).data
                day_forecast = DailyForecast.objects.filter(location=loc, fetched=dt.today())
                daily_forecast = DailyForecastSerializer(day_forecast, many=True).data
            else:
                # fetch new data
                delete_weather(loc)
                data = get_data(loc)
                current_weather = data['current']
                daily_forecast = data['daily']
                api_limit.resetDate = dt.today() + timedelta(days=1)
                api_limit.currentLimit += 1
                api_limit.save()

            resp = {
                'location': loc_serializer.data,
                'current': current_weather,
                'forecast': daily_forecast
            }

            return Response({'data': resp}, status=status.HTTP_200_OK)

        return Response({'message': 'Location is required parameter'}, status=status.HTTP_400_BAD_REQUEST)


class OneForecast(APIView):
    def get(self, request):
        location = request.GET.get('location', None)
        api_key = request.GET.get('key', None)
        api_limit = APILimit.objects.get(pk=1)

        if api_limit.currentLimit == api_limit.limit:
            return Response({'message': 'Limit is reached, try fetch data tomorrow'}, status=status.HTTP_403_FORBIDDEN)

        if location and api_key:
            loc = Location.objects.get(locationId=location)
            key = ApiKey.objects.filter(key=api_key)
            if not key.exists():
                return Response({'message': 'invalid key'}, status=status.HTTP_401_UNAUTHORIZED)

            tomorrow = dt.today().date() + timedelta(days=1)
            day_forecast = DailyForecast.objects.filter(location=loc, date=tomorrow)
            if day_forecast.exists() and dt.today().date() != api_limit.resetDate:
                serializer = DailyForecastSerializer(day_forecast[0])
            else:
                # fetch new data
                delete_weather(loc)
                get_data(loc)
                day_forecast = DailyForecast.objects.get(location=loc, date=tomorrow)
                serializer = DailyForecastSerializer(day_forecast)
                api_limit.resetDate = dt.today() + timedelta(days=1)
                api_limit.currentLimit += 1
                api_limit.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({'message': 'Location and apiKey is required parameter'}, status=status.HTTP_400_BAD_REQUEST)


def delete_weather(location):
    current = CurrentWeather.objects.filter(location=location)
    daily = DailyForecast.objects.filter(location=location)
    if current.exists():
        current.delete()
    if daily.exists():
        daily.delete()


def get_data(location):
    weather_data = weather(location.lat, location.lon)
    current_weather = weather_data['current']
    daily_forecast = weather_data['daily']
    current_weather.update({'location': location.pk})
    cur_serializer = CurrentWeatherSerializer(data=current_weather)
    if cur_serializer.is_valid():
        cur_serializer.save()

    for day in daily_forecast:
        day.update({'location': location.pk})
        day_serializer = DailyForecastSerializer(data=day)
        if day_serializer.is_valid():
            day_serializer.save()

    return {'current': current_weather, 'daily': daily_forecast}
