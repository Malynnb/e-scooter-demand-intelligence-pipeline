## 📊 Data Sources

| Source          | Method       | Information Collected                                                 |
| --------------- | ------------ | --------------------------------------------------------------------- |
| Wikipedia       | Web Scraping | City name, state, population, land area and population density        |
| OpenWeather API | REST API     | Temperature, humidity, weather condition and forecast timestamp       |
| AeroDataBox API | REST API     | Airport name, IATA code, ICAO code, municipality and airport location |

---

## ⚠️ Project Scope

The AeroDataBox free subscription tier restricted access to detailed flight-arrival schedules.

As a result, this project focuses on collecting airport infrastructure data instead of flight schedules.

Airport data was successfully collected for the following German cities:

* Berlin
* Munich
* Frankfurt
* Hamburg
* Cologne

A total of **7 airport connections** were identified and stored in MySQL.

---

## 🔄 ETL Pipeline

### Extract

Data was collected from:

* Wikipedia
* OpenWeather API
* AeroDataBox API

### Transform

The collected data was processed using Pandas:

* Cleaned raw datasets
* Standardized column names
* Parsed JSON responses
* Combined API results into DataFrames
* Prepared data for database storage

### Load

The transformed datasets were loaded into MySQL using SQLAlchemy.

Generated tables:

* cities
* weather
* airports

---

## 🌍 Web Scraping: German Cities

German city information was collected from Wikipedia using Pandas.

### Data Collected

* City
* State
* Population
* Land Area
* Population Density

### Example

```python
tables = pd.read_html(url)

cities_df = tables[0]
```

---

## 🌦 Weather Forecast API

Weather forecasts were collected using the OpenWeather API.

### Data Collected

* City
* Temperature
* Humidity
* Weather Condition
* Forecast Timestamp

### Example

```python
response = requests.get(url)

weather_json = response.json()
```

---

## ✈️ Airport Infrastructure API

Airport information was collected using AeroDataBox through RapidAPI.

### Data Collected

* Airport Name
* IATA Code
* ICAO Code
* Municipality
* Latitude
* Longitude

### Airports Identified

| City      | Airport Code |
| --------- | ------------ |
| Berlin    | BER          |
| Berlin    | TXL          |
| Munich    | MUC          |
| Frankfurt | FRA          |
| Hamburg   | HAM          |
| Cologne   | CGN          |
| Cologne   | DUS          |

### Example

```python
response = requests.get(
    url,
    headers=headers,
    params=querystring
)

airports = pd.json_normalize(
    response.json()["items"]
)
```

---

## 🗄 Database Design

### Tables

```text
world_data
│
├── cities
├── weather
└── airports
```

### Data Flow

```text
Wikipedia
      │
      ▼
   cities
      │
      ├─────────────┐
      ▼             ▼
 OpenWeather   AeroDataBox
      │             │
      ▼             ▼
  weather      airports
```

The database stores weather forecasts and airport infrastructure data for selected German cities and can be expanded with additional demand indicators in future versions.

---

## 📈 Business Insights

The collected datasets help identify cities with favorable conditions for future scooter demand analysis.

### Key Findings

* Berlin contains two airport connections (BER and TXL).
* Frankfurt contains Germany's largest international airport (FRA).
* Airport connectivity can serve as an indicator of tourism and mobility activity.
* Weather conditions can be combined with airport infrastructure data to support future scooter-demand forecasting.

### Example Analysis

By combining airport and weather datasets, cities can be compared based on:

* Transportation infrastructure
* Weather conditions
* Potential mobility demand

This creates a foundation for future demand forecasting models and operational planning.
