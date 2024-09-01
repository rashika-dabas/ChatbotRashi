import requests

from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():

    data = request.get_json()

    print(data)

    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    print(source_currency)
    print(amount)
    print(target_currency)

    cf = fetch_conversion(source_currency, target_currency)

    print(cf)

    val = round(amount * cf)

    print(val)

    return "<h1>Hello</h1>"


def fetch_conversion(source, target):
    url = 'https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=768e7a6914ea773708a7'.format(source,
                                                                                                              target)
    response = requests.get(url)
    r = response.json()
    s = r['{}_{}'.format(source, target)]
    return s


if __name__ == "__main__":
    app.run(debug=True)
