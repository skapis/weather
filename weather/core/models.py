import uuid
from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    locationId = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9999, decimal_places=4)
    lon = models.DecimalField(max_digits=9999, decimal_places=4)

    def __str__(self):
        return f'{self.name}'


class CurrentWeather(models.Model):
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    date = models.DateField()
    timestamp = models.DateTimeField(null=True)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    temp = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    temp_feels_like = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    pressure = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    wind_speed = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    weather = models.CharField(max_length=255)
    weather_desc = models.CharField(max_length=255)
    fetched = models.DateField(default=now)

    def __str__(self):
        return f'{self.location.name} - {self.date}'


class DailyForecast(models.Model):
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)
    date = models.DateField()
    timestamp = models.DateTimeField(null=True)
    day_temp = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    night_temp = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    pressure = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    humidity = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    wind_speed = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    weather = models.CharField(max_length=255)
    weather_desc = models.CharField(max_length=255)
    fetched = models.DateField(default=now)

    def __str__(self):
        return f'{self.location.name} - {self.date}'


class ApiKey(models.Model):
    name = models.CharField(max_length=255)
    key = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name_plural = 'Api Keys'

    def __str__(self):
        return self.name


class APILimit(models.Model):
    name = models.CharField(max_length=255)
    limit = models.IntegerField()
    currentLimit = models.IntegerField()
    resetDate = models.DateField()

    class Meta:
        verbose_name_plural = 'API Limit'

    def __str__(self):
        return self.name
