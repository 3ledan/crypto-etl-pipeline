from connect_db import insert_data

# Load block
def load(processed_data):
    for record in processed_data:
        currency, price, market_cap, change_24h = record
        insert_data(currency,price,market_cap,change_24h)
        print(f"{currency} inserted successfully")