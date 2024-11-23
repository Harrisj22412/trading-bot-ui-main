from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/buyorsell', methods=['POST'])
def buy_or_sell():
    try:
        data = request.get_json()
        ticker = data.get('ticker')
    except Exception as e:
        return jsonify({'error': 'Invalid request format'}), 400
    
    if not ticker:
        return jsonify({'error': 'Missing required field: ticker'}), 400
    
    ## TODO: We need to Fetch the market data for the ticker

    ##TODO: Parse the market Data  displaying potentially the closing prices

    ##TODO: Perform a technical analysis using indicators like rsi, macd

    ##TODO: Then define that trading strategy if the rsi is greater than a certain number "BUY" , or if its less than a certain number "SELL"
    
    decision = random.choice(['BUY', 'SELL'])
    message = f"{decision} for ticker: {ticker}"
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
