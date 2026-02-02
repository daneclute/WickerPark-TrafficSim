import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not found. Check your .env file")

def get_data():
    url = "https://data.cityofchicago.org/api/v3/views/n4j6-wkkf/query.json"

    try:
        response = requests.get(url, auth=(API_KEY, API_SECRET))
        if response.status_code == 200:
            data = response.json()
            
            valid_data = [
                segment for segment in data 
                if int(segment.get('_traffic', -1)) > 0
            ]

            return valid_data

    except requests.exceptions.RequestException as e:
        print(f'Failed to fetch data: {e}')
        return None
