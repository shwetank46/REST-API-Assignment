-- =========================
-- ORDER MANAGEMENT SYSTEM
-- DATABASE SCHEMA
-- =========================

-- Customers Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2) NOT NULL
);

-- Orders Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50),

    FOREIGN KEY (customer_id)
    REFERENCES Customers(customer_id)
);

-- Order Items Table (Important Bridge Table)
CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,

    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id),

    FOREIGN KEY (product_id)
    REFERENCES Products(product_id)
);

-- Payments Table
CREATE TABLE Payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10,2),
    payment_method VARCHAR(50),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id)
    REFERENCES Orders(order_id)
);

-- =========================
-- SAMPLE DATA INSERTION
-- =========================

-- Insert Customers (5 Customers)
INSERT INTO Customers VALUES
(1, 'Rahul Sharma', 'rahul@example.com', '9876543210', CURRENT_TIMESTAMP),
(2, 'Priya Singh', 'priya@example.com', '9876543211', CURRENT_TIMESTAMP),
(3, 'Amit Verma', 'amit@example.com', '9876543212', CURRENT_TIMESTAMP),
(4, 'Neha Gupta', 'neha@example.com', '9876543213', CURRENT_TIMESTAMP),
(5, 'Vikas Mehta', 'vikas@example.com', '9876543214', CURRENT_TIMESTAMP);

-- Insert Products
INSERT INTO Products VALUES
(1, 'Laptop', 'Electronics', 75000.00),
(2, 'Mobile Phone', 'Electronics', 25000.00),
(3, 'Office Chair', 'Furniture', 8000.00),
(4, 'Desk', 'Furniture', 15000.00),
(5, 'Headphones', 'Accessories', 2000.00);

-- Insert Orders (10 Orders)
INSERT INTO Orders VALUES
(1, 1, CURRENT_TIMESTAMP, 'Completed'),
(2, 2, CURRENT_TIMESTAMP, 'Completed'),
(3, 3, CURRENT_TIMESTAMP, 'Pending'),
(4, 1, CURRENT_TIMESTAMP, 'Completed'),
(5, 4, CURRENT_TIMESTAMP, 'Shipped'),
(6, 5, CURRENT_TIMESTAMP, 'Completed'),
(7, 2, CURRENT_TIMESTAMP, 'Pending'),
(8, 3, CURRENT_TIMESTAMP, 'Completed'),
(9, 4, CURRENT_TIMESTAMP, 'Completed'),
(10, 5, CURRENT_TIMESTAMP, 'Shipped');

-- Insert Order Items
INSERT INTO Order_Items VALUES
(1, 1, 1, 1),
(2, 2, 2, 2),
(3, 3, 3, 1),
(4, 4, 4, 1),
(5, 5, 5, 3),
(6, 6, 1, 1),
(7, 7, 2, 1),
(8, 8, 3, 2),
(9, 9, 4, 1),
(10, 10, 5, 2);

-- Insert Payments
INSERT INTO Payments VALUES
(1, 1, 75000.00, 'Credit Card', CURRENT_TIMESTAMP),
(2, 2, 50000.00, 'UPI', CURRENT_TIMESTAMP),
(3, 3, 8000.00, 'Debit Card', CURRENT_TIMESTAMP),
(4, 4, 15000.00, 'UPI', CURRENT_TIMESTAMP),
(5, 5, 6000.00, 'Cash', CURRENT_TIMESTAMP),
(6, 6, 75000.00, 'Credit Card', CURRENT_TIMESTAMP),
(7, 7, 25000.00, 'UPI', CURRENT_TIMESTAMP),
(8, 8, 16000.00, 'Debit Card', CURRENT_TIMESTAMP),
(9, 9, 15000.00, 'UPI', CURRENT_TIMESTAMP),
(10, 10, 4000.00, 'Cash', CURRENT_TIMESTAMP);

-- =========================
-- REQUIRED SQL QUERIES
-- =========================

-- 1. Top 3 Customers with Highest Number of Orders

SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o 
    ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.name
ORDER BY 
    total_orders DESC
LIMIT 3;


-- 2. Retrieve Orders Placed in Last 30 Days

SELECT *
FROM Orders
WHERE order_date >= NOW() - INTERVAL 30 DAY;


-- 3. Calculate Total Revenue for Each Product

SELECT 
    p.product_name,
    SUM(oi.quantity * p.price) AS total_revenue
FROM Products p
JOIN Order_Items oi 
    ON p.product_id = oi.product_id
GROUP BY 
    p.product_name
ORDER BY 
    total_revenue DESC;