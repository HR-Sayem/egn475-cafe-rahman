DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu_items;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'customer'
);

CREATE TABLE menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price_cents INTEGER NOT NULL,
    available INTEGER NOT NULL DEFAULT 1,
    CHECK (available IN (0, 1))
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    customer_name TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'New',
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE RESTRICT
);

CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    menu_item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL DEFAULT 1,
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (menu_item_id) REFERENCES menu_items(id) ON DELETE RESTRICT,
    CHECK (quantity > 0)
);

INSERT INTO users (id, username, password_hash, role) VALUES
    (1, 'john', 'sample-password-hash-john', 'customer'),
    (2, 'sarah', 'sample-password-hash-sarah', 'customer'),
    (3, 'michael', 'sample-password-hash-michael', 'customer');

INSERT INTO menu_items (id, name, category, price_cents, available) VALUES
    (1, 'Cafe con leche', 'Drinks', 350, 1),
    (2, 'Cuban sandwich', 'Food', 1100, 1),
    (3, 'Guava pastelito', 'Bakery', 225, 1),
    (4, 'Croqueta', 'Food', 150, 1),
    (5, 'Cortadito', 'Drinks', 275, 1),
    (6, 'Iced Coffee', 'Drinks', 450, 1);

INSERT INTO orders (id, user_id, customer_name, status, notes, created_at) VALUES
    (101, 1, 'John', 'Preparing', 'Please make the sandwich warm.', '2026-11-27 10:00:00'),
    (102, 2, 'Sarah', 'Ready', 'No sugar in the cafe con leche.', '2026-11-27 10:10:00'),
    (103, 3, 'Michael', 'New', '', '2026-11-27 10:20:00');

INSERT INTO order_items (order_id, menu_item_id, quantity) VALUES
    (101, 2, 1),
    (102, 1, 1),
    (103, 4, 2);
