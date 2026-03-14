from flask import Flask, request, jsonify

app = Flask(__name__)

# linia 4
items = []

# linia 8
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    data = request.json
    items.append(data)
    return jsonify(data)

# linia 12
tomasz = {
    "name": "Tomasz",
    "age": 25,
    "city": "Warsaw"
}

items.append(tomasz)

users = []
orders = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    if "name" not in data or "email" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    users.append(data)
    return jsonify(data)

    users.append(data)
    return jsonify(data)

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.json
    orders.append(data)
    return jsonify(data)

@app.route('/users/count', methods=['GET'])
def count_users():
    return jsonify({"total_users": len(users)})

if __name__ == '__main__':
    app.run(debug=True)
