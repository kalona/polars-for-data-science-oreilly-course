import os

import requests

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-03.parquet"
local_parquet = "/data/datasets/data/yellow_tripdata_2024-03.parquet"
local_csv = "/data/datasets/data/yellow_tripdata_2024-03.csv"
taxi_zone_lookup_url = (
    "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
)
taxi_zone_lookup_local = "/data/datasets/data/taxi_zone_lookup.csv"

taxi_zone_lookup_parquet = "/data/datasets/data/taxi_zone_lookup.parquet"

# Download the taxi zone lookup file and the parquet file if they don't exist using for loops

# Define the file paths and URLs
files = [(local_parquet, url), (taxi_zone_lookup_local, taxi_zone_lookup_url)]

# Loop through the files and download if they do not exist
for local_path, download_url in files:
    if not os.path.exists(local_path):
        print(f"Downloading {download_url} to {local_path}")
        response = requests.get(download_url)
        with open(local_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"{local_path} already exists")

# Print the local variables and paths
print(f"\nlocal_parquet = {local_parquet}")
print(f"local_csv = {local_csv}")
print(f"taxi_zone_lookup_local = {taxi_zone_lookup_local}")
print(f"taxi_zone_lookup_parquet = {taxi_zone_lookup_parquet}")
