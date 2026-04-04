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
