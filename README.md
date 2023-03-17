# Weather
In this repository is simple weather app, which contains simple weather widget and weather API. 
App uses Django Framework and Django REST Framework for the backend and for the frontend is used ReactJS.

## API
Source of weather data is API from external service. App uses cache to save api calls to external service, because there is daily limit.

### Endpoints

#### Locations
Serve all locations, which is registered in app database. Because of app uses external service to get weather data there is no POST method. 
New location can be registered only by admin in Django Administration.

```http
GET /locations
```

**Response**
```
[
    {
        "locationId": "4eb72ff9-c1a2-4c1d-82a3-35c894c2ce02",
        "name": "Hradec Králové",
        "lat": "50.2092",
        "lon": "15.8320"
    },
    {
        "locationId": "11537030-41ab-40aa-b898-fde7601e6816",
        "name": "Praha",
        "lat": "50.0800",
        "lon": "14.4200"
    }
]
```

#### Single location
To get data about specific location can be used this api endpoint which provides data for single location

```http
GET /location?location={locationId}
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `location` | `uuid` | **Required**. ID of requested location|

**Response**
```
{
    "locationId": "4eb72ff9-c1a2-4c1d-82a3-35c894c2ce02",
    "name": "Hradec Králové",
    "lat": "50.2092",
    "lon": "15.8320"
}
```

#### Location Weather
This endpoint provides current weather and 8 day weather forecast for requested location. Location is represented as a paramater (location) in URL.

```http
GET /weather?location={locationId}
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `location` | `uuid` | **Required**. ID of requested location|

**Response**
```
{
    "data": {
        "location": {
            "locationId": "11537030-41ab-40aa-b898-fde7601e6816",
            "name": "Praha",
            "lat": "50.0800",
            "lon": "14.4200"
        },
        "current": {
            "date": "2023-03-17",
            "timestamp": "2023-03-17T10:15:34",
            "sunrise": "2023-03-17T06:12:45",
            "sunset": "2023-03-17T18:08:55",
            "pressure": 1015,
            "humidity": 56,
            "wind_speed": 2.57,
            "weather": "Clear",
            "weather_desc": "jasno",
            "temp": 6.48,
            "temp_feels_like": 4.6,
            "location": 2
        },
        "forecast": [
            {
                "date": "2023-03-17",
                "timestamp": "2023-03-17T12:00:00",
                "sunrise": "2023-03-17T06:12:45",
                "sunset": "2023-03-17T18:08:55",
                "pressure": 1016,
                "humidity": 48,
                "wind_speed": 5.19,
                "weather": "Clouds",
                "weather_desc": "polojasno",
                "day_temp": 7.94,
                "night_temp": 5.44,
                "location": 2
            },
            {
                "date": "2023-03-18",
                "timestamp": "2023-03-18T12:00:00",
                "sunrise": "2023-03-18T06:10:34",
                "sunset": "2023-03-18T18:10:31",
                "pressure": 1017,
                "humidity": 48,
                "wind_speed": 3.7,
                "weather": "Clouds",
                "weather_desc": "zataženo",
                "day_temp": 9.29,
                "night_temp": 6.34,
                "location": 2
            },
            {
                "date": "2023-03-19",
                "timestamp": "2023-03-19T12:00:00",
                "sunrise": "2023-03-19T06:08:22",
                "sunset": "2023-03-19T18:12:06",
                "pressure": 1019,
                "humidity": 52,
                "wind_speed": 1.56,
                "weather": "Clouds",
                "weather_desc": "zataženo",
                "day_temp": 11.57,
                "night_temp": 8.71,
                "location": 2
            },
            {
                "date": "2023-03-20",
                "timestamp": "2023-03-20T12:00:00",
                "sunrise": "2023-03-20T06:06:10",
                "sunset": "2023-03-20T18:13:41",
                "pressure": 1020,
                "humidity": 64,
                "wind_speed": 2.16,
                "weather": "Clouds",
                "weather_desc": "zataženo",
                "day_temp": 13.63,
                "night_temp": 11.57,
                "location": 2
            },
            {
                "date": "2023-03-21",
                "timestamp": "2023-03-21T12:00:00",
                "sunrise": "2023-03-21T06:03:58",
                "sunset": "2023-03-21T18:15:15",
                "pressure": 1016,
                "humidity": 53,
                "wind_speed": 3.02,
                "weather": "Clouds",
                "weather_desc": "zataženo",
                "day_temp": 15.45,
                "night_temp": 12.56,
                "location": 2
            },
            {
                "date": "2023-03-22",
                "timestamp": "2023-03-22T12:00:00",
                "sunrise": "2023-03-22T06:01:46",
                "sunset": "2023-03-22T18:16:50",
                "pressure": 1011,
                "humidity": 46,
                "wind_speed": 6.93,
                "weather": "Clouds",
                "weather_desc": "oblačno",
                "day_temp": 15.73,
                "night_temp": 12.23,
                "location": 2
            },
            {
                "date": "2023-03-23",
                "timestamp": "2023-03-23T12:00:00",
                "sunrise": "2023-03-23T05:59:34",
                "sunset": "2023-03-23T18:18:24",
                "pressure": 1011,
                "humidity": 59,
                "wind_speed": 6.93,
                "weather": "Clouds",
                "weather_desc": "zataženo",
                "day_temp": 16.07,
                "night_temp": 13.4,
                "location": 2
            },
            {
                "date": "2023-03-24",
                "timestamp": "2023-03-24T12:00:00",
                "sunrise": "2023-03-24T05:57:22",
                "sunset": "2023-03-24T18:19:59",
                "pressure": 1012,
                "humidity": 45,
                "wind_speed": 2.83,
                "weather": "Clear",
                "weather_desc": "jasno",
                "day_temp": 19.96,
                "night_temp": 14.27,
                "location": 2
            }
        ]
    }
}
```

#### One Forecast
This endpoint provides forecast for tomorrow for requested location. This endpoint is protected by apiKey. In Django administration admin can create apikey for specific users.

```http
GET /weather/one?location={locationId}&key={apiKey}
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `location` | `uuid` | **Required**. ID of requested location|
| `key` | `uuid` | **Required**. Unique api key for specific user|

**Response**
```
{
    "id": 90,
    "date": "2023-03-18",
    "timestamp": "2023-03-18T12:00:00+01:00",
    "day_temp": "9.21",
    "night_temp": "4.58",
    "pressure": "1018.00",
    "humidity": "43.00",
    "wind_speed": "5.09",
    "weather": "Clouds",
    "weather_desc": "zataženo",
    "fetched": "2023-03-17",
    "location": 1
}
```

## Weather Widget
For the common users is created simple weather widget, which shows current weather in selected location and 7 day weather forecast. User can switch between locations by select in the top of widget.

![Desktop Version](https://github.com/skapis/appscreenshots/blob/main/Weather/Widget_Desktop.png)

### Mobile Version of Widget
On mobile widget looks little different

![Mobile Version](https://github.com/skapis/appscreenshots/blob/main/Weather/Widget_Mobile.png)



