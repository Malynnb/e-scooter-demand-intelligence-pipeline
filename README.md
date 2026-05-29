# 🛴 Gans E-Scooter Demand Intelligence Pipeline

## 📖 Project Overview

This project builds an end-to-end ETL (Extract, Transform, Load) pipeline for Gans, a fictional e-scooter sharing company.

The goal is to collect external demand indicators that could support future scooter demand forecasting and operational decision-making. Rather than predicting demand directly, this project focuses on gathering and storing relevant city-level information from multiple data sources.

The collected datasets are processed using Python and stored in a MySQL database for future analysis.

---

## 🎯 Business Problem

Gans wants to improve scooter availability by understanding factors that may influence mobility demand across cities.

Questions explored include:

* Which cities have the largest populations?
* How do weather conditions vary between cities?
* Which cities have strong airport connectivity?
* Can airport infrastructure serve as a proxy indicator for mobility activity?

---

## 🛠 Technologies Used

### Programming & Analysis

* Python
* Pandas
* Requests
* SQLAlchemy

### Database

* MySQL
* MySQL Workbench

### APIs

* OpenWeather API
* AeroDataBox API

### Development Tools

* VS Code
* Jupyter Notebook

---

## 📊 Data Sources

| Source          | Method       | Information Collected                                                   |
| --------------- | ------------ | ----------------------------------------------------------------------- |
| Wikipedia       | Web Scraping | City name, state, population estimate, land area and population density |
| OpenWeather API | REST API     | Temperature, humidity, weather condition and forecast timestamp         |
| AeroDataBox API | REST API     | Airport name, IATA code, ICAO code, municipality and airport location   |

---

## 🔄 ETL Pipeline

### Extract

Data was collected from:

* Wikipedia
* OpenWeather API
* AeroDataBox API

### Transform

The collected data was transformed using Pandas:

* Parsing JSON responses
* Cleaning datasets
* Standardizing columns
* Creating DataFrames
* Preparing data for database storage

### Load

The processed datasets were loaded into MySQL using SQLAlchemy.

Tables created:

* cities
* weather
* airports

---

## 🌍 German Cities Dataset

German city information was collected from Wikipedia using Pandas `read_html()`.

### Data Collected

* City
* State
* Population Estimate
* Land Area
* Population Density
* Geographic Location

### Example

```python
tables = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population"
)

cities_df = tables[0]
```

---

## 🌦 Weather Forecast Dataset

Weather forecast information was collected using the OpenWeather API.

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

## ✈️ Airport Infrastructure Dataset

Airport information was collected using AeroDataBox through RapidAPI.

### Data Collected

* Airport Name
* IATA Code
* ICAO Code
* Municipality
* Latitude
* Longitude

### Cities Processed

* Berlin
* Munich
* Frankfurt
* Hamburg
* Cologne

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

A total of **7 airport connections** were collected and stored.

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

## ⚠️ Project Scope

The AeroDataBox free subscription tier restricted access to detailed flight-arrival schedules.

As a result, this project focuses on airport infrastructure data rather than flight-arrival information.

The current architecture can easily be extended in future versions to include:

* Flight arrivals
* Local events
* Tourism indicators
* Demand forecasting models

---

## 🗄 Database Design

### Database

```text
world_data
```

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

---

## 💾 SQL Integration

DataFrames generated in Python were loaded directly into MySQL using SQLAlchemy.

Example:

```python
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
```

---

## 📈 Example Insights

The collected datasets can be used to support future scooter demand analysis.

Key observations:

* Berlin has two airport connections (BER and TXL).
* Frankfurt contains Germany's largest international airport (FRA).
* Airport infrastructure may serve as an indicator of mobility and tourism activity.
* Weather conditions can be combined with airport data to support future forecasting models.

---

## 🚀 Skills Demonstrated

### Python

* Functions
* Loops
* API Requests
* JSON Processing
* Data Cleaning
* Pandas DataFrames

### SQL

* Database Design
* Data Loading
* SQL Queries
* Table Management

### Data Engineering

* ETL Pipelines
* API Integration
* Data Transformation
* Database Storage

### Web Scraping

* Data Extraction
* HTML Table Processing
* Pandas `read_html()`

---

## 📂 Project Structure

```text
gans-predicting-scooter-demand/
│
├── notebooks/
│   ├── 01_city_scraping.ipynb
│   ├── 02_weather_api.ipynb
│   └── 03_airports_api.ipynb
│
├── src/
│   └── gans_etl_pipeline.py
│
├── sql/
│   └── analysis_queries.sql
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔮 Future Improvements

* Automate daily data collection
* Integrate detailed flight-arrival schedules
* Add local event information
* Build demand forecasting models
* Deploy the pipeline to the cloud
* Create interactive dashboards
