# Import the Flask class to create our web application.
import os
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

import db
from db import get_db
from flask import Flask, abort, redirect, render_template, request, url_for

# Create the Flask application using this file's name.
app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.instance_path, "cafe.sqlite")
os.makedirs(app.instance_path, exist_ok=True)
db.init_app(app)

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
    items = get_db().execute(
        "SELECT * FROM menu_items WHERE available = 1 ORDER BY name"
    ).fetchall()
    return render_template("menu.html", items=items)


# Menu item detail page
@app.get("/menu/<int:item_id>")
def item_detail(item_id: int):
    item = get_db().execute(
        "SELECT * FROM menu_items WHERE id = ?",
        (item_id,)
    ).fetchone()

    if item is None:
        abort(404)

    return render_template("item.html", item=item)


# Staff menu item form
@app.route("/admin/menu/new", methods=["GET", "POST"])
def new_menu_item():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        price = request.form.get("price", "").strip()
        available = request.form.get("available") == "on"
        error = None

        if not name:
            error = "Name is required."
        else:
            try:
                price_cents = int(
                    (Decimal(price) * 100).quantize(
                        Decimal("1"), rounding=ROUND_HALF_UP
                    )
                )
                if price_cents < 0:
                    error = "Price must be zero or greater."
            except (InvalidOperation, ValueError):
                error = "Enter a valid price."

        if error is not None:
            return render_template(
                "menu_item_new.html",
                error=error,
                name=name,
                category=category,
                price=price,
                available=available,
            ), 400

        connection = get_db()
        connection.execute(
            """
            INSERT INTO menu_items (name, category, price_cents, available)
            VALUES (?, ?, ?, ?)
            """,
            (name, category, price_cents, int(available)),
        )
        connection.commit()
        return redirect(url_for("menu"))

    return render_template(
        "menu_item_new.html",
        name="",
        category="",
        price="",
        available=True,
    )


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