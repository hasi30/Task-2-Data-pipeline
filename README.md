# Weather Data Pipeline using Open-Meteo API and Google BigQuery

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data pipeline using the Open-Meteo Weather API, Python, Pandas, and Google BigQuery. The pipeline extracts weather forecast data from an external API, transforms and cleans the data using Python, stores it as a CSV file, uploads it into Google BigQuery, and performs SQL-based analysis.

The objective of this project is to showcase practical data engineering concepts including API integration, data transformation, cloud data warehousing, SQL analytics, and structured project organization.

---

## Technologies Used

- Python
- Pandas
- Requests
- Google BigQuery
- SQL
- VS Code
- GitHub

---

## Project Architecture

Open-Meteo API  
↓  
Python Extraction Script  
↓  
Data Transformation using Pandas  
↓  
CSV File Storage  
↓  
Google BigQuery Upload  
↓  
SQL Analysis  

---

## Folder Structure

task2_pipeline/

├── data/  
│   └── weather_data.csv  

├── logs/  

├── scripts/  
│   ├── fetch_data.py  
│   └── load_bigquery.py  

├── sql/  
│   └── analysis.sql  

├── README.md  
├── requirements.txt  
└── .gitignore  

---

## Features Implemented

- API data extraction using Open-Meteo API
- Error handling and logging
- JSON to DataFrame transformation
- Data cleaning using Pandas
- Derived analytical column creation
- CSV storage
- Google BigQuery integration
- SQL-based analysis
- Organized project structure

---

## Data Pipeline Workflow

1. Fetch weather forecast data from Open-Meteo API
2. Convert JSON response into structured tabular format
3. Clean and transform data using Pandas
4. Store transformed data as CSV
5. Upload CSV data into Google BigQuery
6. Perform SQL analysis on cloud-hosted data

---

## How to Run the Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Data Extraction Script

```bash
python fetch_data.py
```

### 3. Upload Data to BigQuery

```bash
python load_bigquery.py
```

---

## Sample SQL Analysis

```sql
SELECT
    temperature_category,
    COUNT(*) AS total_days,
    AVG(max_temperature) AS average_temperature
FROM `pipeline-497605.weather_pipeline.weather_data`
GROUP BY temperature_category
ORDER BY average_temperature DESC;
```

---

## Sample Output

The SQL analysis provides:

- Total number of weather records
- Temperature category distribution
- Average maximum temperature analysis

---

## Key Learnings

- Working with REST APIs
- Building ETL pipelines
- Data transformation using Pandas
- Cloud data warehousing with BigQuery
- SQL analytics
- Project structuring and documentation

---

## Future Improvements

- Automate pipeline scheduling using Airflow or Cron Jobs
- Add real-time weather streaming
- Implement dashboard visualization
- Add monitoring and alerting system
- Integrate historical weather datasets

---

## Author

Mohamed Hasik
M.Sc. Applied Data Science
