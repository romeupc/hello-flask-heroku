from flask import Flask, Response, render_template, url_for
from datetime import datetime
import time
import requests

app = Flask(__name__)


@app.route('/')
def time_feed():
    def generate():
        while True:
            rsp = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=BTCUSDT').json()

            yield str(rsp)
            time.sleep(1)
    return Response(generate())

if __name__ == '__main__':
    app.run()
