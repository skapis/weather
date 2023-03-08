import requests as r
from datetime import datetime as dt


def weather(lat, lon):
    api_key = 'xxxxx'
    url = f'https://api.openweathermap.org/data/3.0/onecall'
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely',
        'appid': api_key,
        'lang': 'cz',
        'units': 'metric'
    }
    response = r.get(url, params)
    data = response.json()
    current = parse_data(data['current'])
    daily_weather = list(map(lambda x: parse_data(x), data['daily']))
    return {'current': current, 'daily': daily_weather}


def parse_data(data):
    resp = {
        'date': dt.fromtimestamp(data['dt']).date(),
        'timestamp': dt.fromtimestamp(data['dt']),
        'sunrise': dt.fromtimestamp(data['sunrise']),
        'sunset': dt.fromtimestamp(data['sunset']),
        'pressure': data['pressure'],
        'humidity': data['humidity'],
        'wind_speed': data['wind_speed'],
        'weather': data['weather'][0]['main'],
        'weather_desc': data['weather'][0]['description']
    }

    if isinstance(data['temp'], dict):
        day_temp = data['temp']['day']
        night_temp = data['temp']['day']
        resp.update({'day_temp': day_temp})
        resp.update({'night_temp': night_temp})
    else:
        temp = data['temp']
        temp_feels_like = data['feels_like']
        resp.update({'temp': temp})
        resp.update({'temp_feels_like': temp_feels_like})

    return resp

