from db_connect import insert_data

def load_fetched_data(fetched_data):
    for record in fetched_data:
        currency, price_usd, market_cap, total_volume, price_change_24h = record
        insert_data(currency, price_usd, market_cap, total_volume, price_change_24h)
        print(f"{currency} inserted successfully")
