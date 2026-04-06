from extract import extract_data
from transform import transform_data
from load import load_fetched_data
import logging

logging.basicConfig(
    filename= 'pipeline.log',
    level= logging.INFO,
    format= '%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    try:
        data = extract_data()
        logging.info("API fetch successful")
    except Exception as e:
        logging.error(f"API Fetch failed: {e}")
        return
    processed_data = transform_data(data)
    try:
        load_fetched_data(processed_data)
        logging.info("Data inserted successfully")
    except Exception as e:
        logging.error(f"An error occured: {e}")

if __name__ == "__main__":
    run_pipeline()
