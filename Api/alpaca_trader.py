import alpaca_trade_api as tradeapi


#API Key and Secret Key
api_key = ''
api_secret = ''
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(api_key, api_secret, BASE_URL, api_version='v2')

def buy_stock(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"Bought {qty} shares of {symbol}")

def sell_stock(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f"Sold {qty} shares of {symbol}")

if __name__ == '__main__':
    stock_symbol = ''
    quantity_to_trade = ''

    buy_stock(stock_symbol, quantity_to_trade)

    sell_stock(stock_symbol, quantity_to_trade)


