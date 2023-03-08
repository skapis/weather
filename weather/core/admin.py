from django.contrib import admin
from .models import ApiKey, Location, DailyForecast, CurrentWeather, APILimit

admin.site.register(ApiKey)
admin.site.register(Location)
admin.site.register(DailyForecast)
admin.site.register(CurrentWeather)
admin.site.register(APILimit)
