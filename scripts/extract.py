from config import API_URL
import requests

def extract_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("An error has occured...")
    
