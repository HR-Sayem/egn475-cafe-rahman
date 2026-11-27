# Import the Flask class to create our web application.
from flask import Flask, render_template, abort

# Create the Flask application using this file's name.
app = Flask(__name__)
# Sample menu items
SAMPLE_ITEMS = [
    {
        "id": 1,
        "name": "Cafe con leche",
        "category": "Drinks",
        "price_cents": 350
    },
    {
        "id": 2,
        "name": "Cuban sandwich",
        "category": "Food",
        "price_cents": 1100
    },
    {
        "id": 3,
        "name": "Guava pastelito",
        "category": "Bakery",
        "price_cents": 225
    },
    {
        "id": 4,
        "name": "Croqueta",
        "category": "Food",
        "price_cents": 150
    },
    {
        "id": 5,
        "name": "Cortadito",
        "category": "Drinks",
        "price_cents": 275
    },
    {
        "id": 6,
        "name": "Iced Coffee",
        "category": "Drinks",
        "price_cents": 450
    }
]


# Sample kitchen orders
SAMPLE_KITCHEN_ORDERS = [
    {
        "id": 101,
        "customer": "John",
        "items": "Cuban sandwich",
        "status": "Preparing"
    },
    {
        "id": 102,
        "customer": "Sarah",
        "items": "Cafe con leche",
        "status": "Ready"
    },
    {
        "id": 103,
        "customer": "Michael",
        "items": "Croqueta",
        "status": "New"
    }
]


# Sample order history
SAMPLE_ORDERS = [
    {
        "id": 201,
        "customer": "John",
        "total_cents": 1100,
        "status": "Completed"
    },
    {
        "id": 202,
        "customer": "Sarah",
        "total_cents": 350,
        "status": "Completed"
    },
    {
        "id": 203,
        "customer": "Michael",
        "total_cents": 150,
        "status": "Completed"
    }
]

# Set the home page URL to the root address.
@app.get("/")
def index():
    return render_template("index.html")

# Menu page
@app.get("/menu")
def menu():
    return render_template("menu.html", items=SAMPLE_ITEMS)
# Menu item detail page
@app.get("/menu/<int:item_id>")
def item_detail(item_id: int):
    item = next(
        (item for item in SAMPLE_ITEMS if item["id"] == item_id),
        None
    )

    if item is None:
        abort(404)

    return render_template("item.html", item=item)
# Place an order page
@app.get("/order/new")
def place_order():
    return render_template("order_new.html", items=SAMPLE_ITEMS)
# Kitchen board page
@app.get("/kitchen")
def kitchen():
    return render_template(
        "kitchen.html",
        orders=SAMPLE_KITCHEN_ORDERS
    )
# Order history page
@app.get("/orders")
def orders():
    return render_template(
        "orders.html",
        orders=SAMPLE_ORDERS
    )