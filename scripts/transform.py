# import extract data:
# from extract import crypto_data

# Transform block
def transform_data(data):
    processed = []
    for coin in data:
        currency = coin.get("id")
        price = coin.get("current_price")
        market_cap = coin.get("market_cap")
        change_24h = coin.get("price_change_24h")
        if price is not None:
            processed.append((currency, price, market_cap, change_24h))
        
    return processed

# Test extracted data:
# print(transform_data(crypto_data()))