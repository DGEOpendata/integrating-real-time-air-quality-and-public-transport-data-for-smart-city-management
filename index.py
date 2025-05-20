python
import requests
import pandas as pd

# API endpoints
aqi_api_url = 'https://api.example.com/airquality'
transport_api_url = 'https://api.example.com/publictransport'

# Fetch Air Quality Index data
def get_aqi_data():
    response = requests.get(aqi_api_url)
    aqi_data = response.json()
    return pd.DataFrame(aqi_data)

# Fetch Public Transport data
def get_transport_data():
    response = requests.get(transport_api_url)
    transport_data = response.json()
    return pd.DataFrame(transport_data)

# Integrate the datasets
def integrate_data(aqi_df, transport_df):
    # Example: Merge datasets based on location
    integrated_df = pd.merge(aqi_df, transport_df, on='location')
    return integrated_df

# Main function
if __name__ == "__main__":
    aqi_df = get_aqi_data()
    transport_df = get_transport_data()
    integrated_data = integrate_data(aqi_df, transport_df)
    print(integrated_data.head())
