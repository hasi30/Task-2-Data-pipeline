import requests
import pandas as pd
import logging
import os

# -------------------------------
# LOGGING SETUP
# -------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# -------------------------------
# CREATE DATA FOLDER IF NOT EXISTS
# -------------------------------

os.makedirs("data", exist_ok=True)

# -------------------------------
# API URL
# -------------------------------

url = "https://api.open-meteo.com/v1/forecast"

# -------------------------------
# PARAMETERS
# -------------------------------

params = {
    "latitude": 13.08,
    "longitude": 80.27,
    "daily": "temperature_2m_max,temperature_2m_min",
    "forecast_days": 14,
    "timezone": "auto"
}

try:

    # -------------------------------
    # FETCH DATA
    # -------------------------------

    logging.info("Fetching weather data from API...")

    response = requests.get(url, params=params)

    # Raise error if API fails
    response.raise_for_status()

    data = response.json()

    logging.info("Data fetched successfully!")

    # -------------------------------
    # TRANSFORM DATA
    # -------------------------------

    logging.info("Transforming data...")

    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "max_temperature": data["daily"]["temperature_2m_max"],
        "min_temperature": data["daily"]["temperature_2m_min"]
    })

    # -------------------------------
    # HANDLE NULL VALUES
    # -------------------------------

    df.fillna(0, inplace=True)

    # -------------------------------
    # DERIVED FIELD
    # -------------------------------

    def temperature_category(temp):

        if temp >= 35:
            return "Hot"

        elif temp >= 25:
            return "Moderate"

        else:
            return "Cold"

    df["temperature_category"] = df["max_temperature"].apply(
        temperature_category
    )

    # -------------------------------
    # SAVE CSV
    # -------------------------------

    output_path = "data/weather_data.csv"

    df.to_csv(output_path, index=False)

    logging.info(f"CSV saved successfully at: {output_path}")

    # -------------------------------
    # DISPLAY DATA
    # -------------------------------

    print("\nFinal Transformed Data:\n")

    print(df)

except requests.exceptions.RequestException as e:

    logging.error(f"API Request Error: {e}")

except Exception as e:

    logging.error(f"Unexpected Error: {e}")
    
    