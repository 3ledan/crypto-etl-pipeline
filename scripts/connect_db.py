import psycopg2
from config import DB_CONFIG

# Establish Python-PostgresSQL Connection
def insert_data(currency, price_usd, market_cap, change_24h):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    insert_query = "INSERT INTO crypto_prices (currency, price_usd, market_cap, change_24h) VALUES (%s,%s,%s,%s)"
    cur.execute(insert_query, (currency, price_usd, market_cap, change_24h))

    conn.commit()
    cur.close()
    conn.close()