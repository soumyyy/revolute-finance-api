from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/transactions", methods=["GET"])
def get_transactions():
    return jsonify([
        {"id": 1, "amount": 200, "currency": "USD", "type": "deposit"},
        {"id": 2, "amount": -50, "currency": "USD", "type": "withdrawal"},
        {"id": 3, "amount": 1200, "currency": "INR", "type": "deposit"},
        {"id": 4, "amount": 10000, "currency": "INR", "type": "deposit"}
    ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=True, host="0.0.0.0", port=port)