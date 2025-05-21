from flask import Flask, request, jsonify
from mt5_handler import send_order

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Servidor Flask funcionando com MT5!', 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Dados inválidos'}), 400

    symbol = data.get('symbol')
    action = data.get('action')  # "buy" ou "sell"
    lot = float(data.get('lot', 0.01))

    result = send_order(symbol, action, lot)
    return jsonify({'resultado': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
