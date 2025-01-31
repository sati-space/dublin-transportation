import requests
import pandas as pd
import io
from datetime import datetime, timedelta

# Define the base URL and system_id
BASE_URL = "https://data.smartdublin.ie/dublinbikes-api/bikes"
SYSTEM_ID = "dublin_bikes"

# Define the time range (last 3 months)
end_date = datetime.today()
start_date = end_date - timedelta(days=90)

# Iterate through each month to fetch data
data_frames = []
for i in range(3):
    month_start = (start_date + timedelta(days=i*30)).strftime('%Y-%m-%dT00:00:00')
    month_end = (start_date + timedelta(days=(i+1)*30)).strftime('%Y-%m-%dT23:59:59')

    # Build the endpoint URL with query parameters
    url = f"{BASE_URL}/{SYSTEM_ID}/historical/stations.csv"
    params = {"dt_start": month_start, "dt_end": month_end}

    # Fetch the data
    response = requests.get(url, params=params)

    if response.status_code == 200:
        # Read the CSV content into a DataFrame
        df = pd.read_csv(io.StringIO(response.text))
        data_frames.append(df)
        print(f"Fetched data for {month_start} to {month_end}")
    else:
        print(f"Failed to fetch data for {month_start} to {month_end}: {response.status_code}")

# Combine all the DataFrames
combined_df = pd.concat(data_frames, ignore_index=True)

# Save the combined data to a local CSV file
combined_df.to_csv("dublin_bikes_last_3_months.csv", index=False)
print("Data saved to 'dublin_bikes_last_3_months.csv'")