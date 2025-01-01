
import requests
import os

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-03.parquet"
local_parquet = "/data/datasets/data/yellow_tripdata_2024-03.parquet"
local_csv = "/data/datasets/data/yellow_tripdata_2024-03.csv"

if not os.path.exists(local_parquet):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

    with open(local_parquet, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {local_parquet}")
else:
    print(f"File {local_parquet} already exists, skipping download.")
