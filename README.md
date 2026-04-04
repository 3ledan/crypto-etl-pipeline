# Crypto ETL Pipeline

This project is a modular ETL pipeline that extracts real-time cryptocurrency data from the CoinGecko API, transforms it, and loads it into a PostgreSQL database.

## Features
- Extracts data for Bitcoin, Ethereum, and Solana
- Stores price, market cap, and 24h change
- Uses PostgreSQL with automatic timestamping
- Modular structure (Extract, Transform, Load)
- Cron-ready for scheduling

## Tech Stack
- Python
- requests
- PostgreSQL
- psycopg2

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Set up your database and update config.py

3. Run the pipeline:
   python scripts/main.py

## Project Structure

scripts/

├── main.py        # pipeline orchestrator
├── extract.py     # API data extraction
├── transform.py   # data transformation
├── load.py        # database loading
├── connect_db.py  # database connection
├── config.py      # configuration

## Example Output

bitcoin 65000 1200000000 2.5
ethereum 3200 400000000 1.2

## Scheduling

The pipeline is scheduled using cron for periodic data ingestion.
