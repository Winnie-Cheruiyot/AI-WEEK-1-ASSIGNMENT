from flask import Flask, render_template, request
import requests

app = Flask(__name__)

COINS = {
    "bitcoin": "Bitcoin",
    "ethereum": "Ethereum",
    "solana": "Solana",
    "dogecoin": "Dogecoin",
    "cardano": "Cardano"
}

def fetch_crypto_data():
    ids = ','.join(COINS.keys())
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={ids}&order=market_cap_desc"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    crypto_data = fetch_crypto_data()
    advice = ""
    if request.method == "POST":
        query = request.form.get("user_input", "").lower()
        if "sustainable" in query:
            advice = "Try Cardano – eco-friendly with a high sustainability score! 🌱"
        elif "growth" in query or "invest" in query:
            advice = "Solana and Ethereum show strong trends for long-term growth 🚀"
        elif "dogecoin" in query:
            advice = "Dogecoin is meme-powered 🐶 — high risk, high laughs!"
        else:
            advice = "Look into Bitcoin or Ethereum for strong historical performance."
    return render_template("index.html", data=crypto_data, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)


