# E-scooter-Demand-Intelligence-Pipeline
An end-to-end data engineering project using Python, Web Scraping, APIs and MySQL to collect and store external demand signals including weather forecasts, flight arrivals and local events.


# 🛴 Gans – Predicting Where E-Scooters Are Needed

## 📖 Project Overview

This project was built during my Data Analytics training to develop an end-to-end data pipeline that collects external data, transforms it, and stores it in a relational database.

The goal is to help an e-scooter company predict where scooters should be placed by analyzing external factors that influence demand.

The project combines:

- Web Scraping
- REST APIs
- Python
- SQL
- Database Design
- ETL Concepts

---

## 🎯 Business Problem

Gans is a fictional e-scooter sharing company operating across European cities.

Scooters only generate revenue when they are available where customers need them. To improve scooter placement, Gans wants to identify external factors that can help predict future demand.

Questions explored:

- Which cities have the highest potential demand?
- How does weather affect scooter usage?
- Do flight arrivals increase demand?
- Can local events predict demand spikes?

---

## 🛠 Technologies Used

### Programming & Analysis

- Python
- Pandas
- Requests
- BeautifulSoup
- SQLAlchemy

### Database

- MySQL
- MySQL Workbench

### APIs

- OpenWeather API
- AeroDataBox API
- Ticketmaster API

### Development Tools

- VS Code
- Jupyter Notebook
- Git
- GitHub

---

## 📊 Data Sources

| Source | Method | Data Collected |
|----------|----------|----------|
| Wikipedia | Web Scraping | Population, area, coordinates, elevation |
| OpenWeather | REST API | Temperature, rain probability, wind speed |
| AeroDataBox | REST API | Flight arrivals |
| Ticketmaster | REST API | Events and concerts |

---

## 🔄 ETL Pipeline

The project follows a simple ETL process:

### Extract

Collect data from:

- Wikipedia
- OpenWeather API
- AeroDataBox API
- Ticketmaster API

### Transform

- Clean raw data
- Handle missing values
- Format timestamps
- Normalize columns
- Convert JSON responses into structured tables

### Load

Store data into a MySQL database using SQLAlchemy.

---

## 🌍 Web Scraping: Wikipedia

BeautifulSoup was used to collect city information from Wikipedia.

Data collected:

- Population
- Area
- Elevation
- Latitude
- Longitude

Example:

```python
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
```

---

## 🌦 Weather Forecast API

Weather forecasts were collected using the OpenWeather API.

Data collected:

- Forecast timestamp
- Temperature
- Rain probability
- Wind speed

Example:

```python
weather_response = requests.get(weather_url)
weather_data = weather_response.json()
```

---

## ✈️ Flight Arrivals API

Flight arrival information was collected using AeroDataBox through RapidAPI.

Data collected:

- Airport code
- Flight number
- Scheduled arrival time
- Arrival airport

Example:

```python
headers = {
    "X-RapidAPI-Key": api_key
}
```

---

## 🎵 Events API

Upcoming events were collected using the Ticketmaster API.

Data collected:

- Event name
- Venue
- Event date
- Classification

Example:

```python
events_response = requests.get(ticketmaster_url)
events_data = events_response.json()
```

---

## 🗄 Database Design

The database was designed using a relational structure.

### Tables

```text
cities
│
├── populations
├── weather
├── flights
└── events
```

### Relationship Structure

```text
cities.city_id
        │
        ├── weather.city_id
        ├── flights.city_id
        ├── events.city_id
        └── populations.city_id
```

The `city_id` acts as the primary key in the cities table and as a foreign key in all related tables.

This design allows historical data to be stored without overwriting previous records.

---

## 💾 SQL Skills Demonstrated

### Creating Databases

```sql
CREATE DATABASE gans;
```

### Creating Tables

```sql
CREATE TABLE cities (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(50)
);
```

### Primary Keys

```sql
PRIMARY KEY(city_id)
```

### Foreign Keys

```sql
FOREIGN KEY(city_id)
REFERENCES cities(city_id)
```

### Inserting Data

```sql
INSERT INTO cities
VALUES (...);
```

---

## 📈 Skills Demonstrated

### Python

- Functions
- Loops
- Dictionaries
- Data Cleaning
- API Requests

### SQL

- Database Design
- Table Relationships
- Primary Keys
- Foreign Keys
- Data Insertion

### Data Engineering

- ETL Pipelines
- Data Collection
- Data Storage
- Data Transformation

### Web Scraping

- HTML Parsing
- BeautifulSoup
- Extracting Structured Data

### APIs

- GET Requests
- JSON Handling
- API Authentication
- Working with Nested JSON

---

## 🚀 Future Improvements

Possible next steps:

- Automate the pipeline using cloud services
- Schedule daily data collection
- Create dashboards using Tableau
- Build a machine learning model to predict scooter demand
- Deploy the project using AWS

---

## ▶️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/gans-predicting-scooter-demand.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create Database

Run:

```sql
gans_schema.sql
```

inside MySQL Workbench.

### 4. Configure Environment Variables

Create a `.env` file:

```text
OPENWEATHER_KEY=
RAPIDAPI_KEY=
TICKETMASTER_KEY=
MYSQL_PASSWORD=
```

### 5. Run Pipeline

```bash
python main.py
```

---

## 📂 Project Structure

```text
gans-predicting-scooter-demand/
│
├── notebooks/
│   └── gans_pipeline.ipynb
│
├── sql/
│   └── gans_schema.sql
│
├── src/
│   ├── wikipedia_scraper.py
│   ├── weather_api.py
│   ├── flight_api.py
│   ├── ticketmaster_api.py
│   └── database.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 👤 Author

**Malynn Buranawichian**

Aspiring Data Analyst 

### Skills

- Python
- SQL
- MySQL
- APIs
- Web Scraping
- Pandas
- ETL Pipelines
- Git & GitHub
- Data Visualization
