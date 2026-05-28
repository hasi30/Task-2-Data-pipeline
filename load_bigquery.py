from google.cloud import bigquery
import pandas as pd
import os

# -----------------------------
# AUTHENTICATION
# -----------------------------

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../service_account.json"

# -----------------------------
# READ CSV FILE
# -----------------------------

csv_path = "../data/weather_data.csv"

df = pd.read_csv(csv_path)

# -----------------------------
# CREATE BIGQUERY CLIENT
# -----------------------------

client = bigquery.Client()

# -----------------------------
# BIGQUERY TABLE ID
# -----------------------------

table_id = "pipeline-497605.weather_pipeline.weather_data"

# -----------------------------
# UPLOAD DATA
# -----------------------------

job = client.load_table_from_dataframe(df, table_id)

job.result()

print("Data uploaded successfully to BigQuery!")

# Upload dataframe to BigQuery
job = client.load_table_from_dataframe(df, table_id)

# Wait until upload completes
job.result()

print("Data uploaded successfully to BigQuery!")