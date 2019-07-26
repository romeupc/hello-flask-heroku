from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    rsp = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT').json()
    return rsp['price']

if __name__ == '__main__':
    app.run()
