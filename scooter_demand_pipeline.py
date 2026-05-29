# -----------------------------------
# IMPORT LIBRARIES
# -----------------------------------

import pandas as pd
import requests
import time
from sqlalchemy import create_engine


# -----------------------------------
# SCRAPE GERMAN CITIES
# -----------------------------------

url = "https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population"

tables = pd.read_html(url)

cities_df = tables[0][[
    "City",
    "State",
    "2021 estimate",
    "2021 land area",
    "2021 population density",
    "Location"
]]


# -----------------------------------
# CITY COORDINATES
# -----------------------------------

city_coordinates = pd.DataFrame({
    "City": [
        "Berlin",
        "Munich",
        "Frankfurt",
        "Hamburg",
        "Cologne"
    ],
    "latitude": [
        52.52,
        48.13,
        50.11,
        53.55,
        50.94
    ],
    "longitude": [
        13.40,
        11.58,
        8.68,
        10.00,
        6.96
    ]
})


# -----------------------------------
# COLLECT WEATHER DATA
# -----------------------------------

weather_data = []

for _, row in city_coordinates.iterrows():

    city = row["City"]
    lat = row["latitude"]
    lon = row["longitude"]

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={lat}&lon={lon}"
        f"&appid=YOUR_API_KEY"
        f"&units=metric"
    )

    response = requests.get(url)
    weather_json = response.json()

    weather_data.append({
        "city": city,
        "temperature": weather_json["list"][0]["main"]["temp"],
        "humidity": weather_json["list"][0]["main"]["humidity"],
        "weather": weather_json["list"][0]["weather"][0]["main"],
        "forecast_time": weather_json["list"][0]["dt_txt"]
    })

weather_df = pd.DataFrame(weather_data)


# -----------------------------------
# AERODATABOX API HEADERS
# -----------------------------------

headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "aerodatabox.p.rapidapi.com",
    "Content-Type": "application/json"
}


# -----------------------------------
# COLLECT AIRPORT DATA
# -----------------------------------

all_airports = []

for _, row in city_coordinates.iterrows():

    city = row["City"]
    lat = row["latitude"]
    lon = row["longitude"]

    url = (
        "https://aerodatabox.p.rapidapi.com"
        "/airports/search/location"
    )

    querystring = {
        "lat": lat,
        "lon": lon,
        "radiusKm": "50",
        "limit": "10",
        "withFlightInfoOnly": "true"
    }

    response = requests.get(
        url,
        headers=headers,
        params=querystring
    )

    if response.status_code == 200:

        airports = pd.json_normalize(
            response.json()["items"]
        )

        airports["city"] = city

        all_airports.append(airports)

    time.sleep(5)

airports_df = pd.concat(
    all_airports,
    ignore_index=True
)


# -----------------------------------
# CONNECT TO MYSQL
# -----------------------------------

engine = create_engine(
    "mysql+pymysql://username:password@localhost/world_data"
)


# -----------------------------------
# LOAD DATA TO MYSQL
# -----------------------------------

weather_df.to_sql(
    "weather",
    con=engine,
    if_exists="replace",
    index=False
)

airports_df.to_sql(
    "airports",
    con=engine,
    if_exists="replace",
    index=False
)


# -----------------------------------
# PROJECT COMPLETE
# -----------------------------------

print("Weather and airport data loaded successfully.")
