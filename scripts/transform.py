def transform_data(data):
    columns = []
    for info in data:
        currency = info.get('id')
        price_usd = info.get('current_price')
        market_cap = info.get('market_cap')
        total_volume = info.get('total_volume')
        price_change_24h = info.get('price_change_percentage_24h')
        columns.append((currency, price_usd, market_cap, total_volume, price_change_24h))
    
    return columns
