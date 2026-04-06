# Crypto ETL Pipeline

A modular data engineering project that extracts real-time cryptocurrency market data from the CoinGecko API, transforms it, and loads it into a PostgreSQL database.

---

## 🚀 Overview

This project demonstrates a complete **ETL (Extract, Transform, Load) pipeline** built with Python. It automates the ingestion of cryptocurrency data and stores it in a structured format for analysis.

---

## ⚙️ Features

- Extracts real-time data from CoinGecko API
- Supports multiple cryptocurrencies (Bitcoin, Ethereum, Solana)
- Captures key metrics:
  - Price (USD)
  - Market Capitalization
  - Total Volume
  - 24h Price Change
- Stores data in PostgreSQL with automatic timestamps
- Modular pipeline architecture (Extract → Transform → Load)
- Logging implemented for monitoring and debugging
- Cron-ready for automated scheduling

---

## 🛠️ Tech Stack

- **Python**
- **PostgreSQL**
- **psycopg2**
- **requests**
- **Cron (for scheduling)**

---

## ▶️ How to Run

1. Clone the repository:
   git clone <your-repo-url>
   cd <repo-name>
   
2. Install dependencies:
   pip install -r requirements.txt
   
3. Configure database:
- Update `config.py` with your PostgreSQL credentials
- Ensure your database and tables are created

4. Run the pipeline:
   
3. Configure database:
- Update `config.py` with your PostgreSQL credentials
- Ensure your database and tables are created

4. Run the pipeline:
   python scripts/main.py


---

## 🗄️ Database Schema

Example fields stored:

- `currency`
- `price_usd`
- `market_cap`
- `total_volume`
- `price_change_24h`
- `fetched_at` (auto-generated timestamp)

---

## ⏱️ Scheduling

The pipeline is designed to run automatically using **cron jobs**, enabling continuous data collection and historical tracking.

---

## 📈 Use Cases

- Time-series analysis of cryptocurrency prices
- Market trend analysis
- Data engineering practice (ETL pipelines)
- Backend data source for dashboards

---

## 🔧 Future Improvements

- Add support for more cryptocurrencies
- Implement retry logic for API failures
- Introduce data validation and deduplication
- Build a visualization/dashboard layer
- Containerize with Docker

---

## 👤 Author

John Eledan  
