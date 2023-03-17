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
