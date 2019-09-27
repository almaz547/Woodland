print("Oess worlt")
import requests
import flask
import json
from flask import Flask


test = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
currencies = json.loads(test)
for currency in currencies["Valute"] :
    print(currencies)



app = Flask(__name__)

@app.route("/")
def hello():
    test = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(test)
    rezult = ''
    for currency in currencies["Valute"]:
        rezult += str(currency) + '<br>'
    return rezult

if __name__ == "__main__":
    app.run()