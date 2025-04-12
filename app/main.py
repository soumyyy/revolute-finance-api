from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify([
        {"id": 1, "amount": 200, "currency": "USD", "type": "deposit"},
        {"id": 2, "amount": -50, "currency": "USD", "type": "withdrawal"}
    ])

if __name__ == '__main__':
    app.run(debug=True)