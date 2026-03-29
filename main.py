from flask import Flask, request, jsonify

app = Flask(__name__)

# "База данных" (в памяти)
orders = []

# Класс Product
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Класс Order
class Order:
    def __init__(self, products, discount_percent=0):
        self.products = products
        self.discount_percent = discount_percent
        self.total = self.calculate_total()

    def calculate_total(self):
        total = sum(p.price * p.quantity for p in self.products)
        total = total * (1 - self.discount_percent / 100)
        return total

    def to_dict(self):
        return {
            "products": [
                {
                    "name": p.name,
                    "price": p.price,
                    "quantity": p.quantity
                } for p in self.products
            ],
            "discount_percent": self.discount_percent,
            "total": self.total
        }

# Главная страница (чтобы не было 404)
@app.route("/", methods=["GET", "POST"])
def home():
    return "API работает"

# POST /orders
@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    products = [
        Product(p["name"], p["price"], p["quantity"])
        for p in data["products"]
    ]

    discount = data.get("discount_percent", 0)

    order = Order(products, discount)
    orders.append(order)

    return jsonify(order.to_dict())

# GET /orders
@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify([o.to_dict() for o in orders])

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
