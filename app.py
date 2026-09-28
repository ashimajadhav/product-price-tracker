from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Product Price Tracker</h1>
    <p>Welcome to the Product Price Tracker.</p>
    <p>Use /products to view products.</p>
    """


@app.route("/products")
def products():
    products = [
        {"name": "Laptop", "price": 50000},
        {"name": "Headphones", "price": 2000},
        {"name": "Keyboard", "price": 1500}
    ]
    return jsonify(products)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)