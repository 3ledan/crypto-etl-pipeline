from config import DB_CONFIG
import psycopg2

def insert_data(currency, price_usd, market_cap, total_volume, price_change_24h):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # Replace "table_name" with your table name
    insert_query = "INSERT INTO table_name (currency, price_usd, market_cap, total_volume, price_change_24h) VALUES (%s,%s,%s,%s,%s)"
    cur.execute(insert_query, (currency, price_usd, market_cap, total_volume, price_change_24h))
    
    conn.commit()
    cur.close()
    conn.close()
