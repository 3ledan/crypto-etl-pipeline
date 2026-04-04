import requests
from config import API_URL

# Extract block
def crypto_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching data")