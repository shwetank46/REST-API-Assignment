# Technical Project Manager Assignment

## Project Overview

This project demonstrates the implementation of a complete Order Management System including API development, database design, and data analysis.

The project is divided into three main parts:

1. REST API Development
2. Database Design and ER Diagram
3. Data Analysis and Insights

---

# Part 1 — REST API

## Features Implemented

- GET /customers → Retrieve all customers
- GET /products → Retrieve all products
- POST /orders → Create new order
- GET /orders → Retrieve all orders

## API Documentation

Swagger documentation is available at:

https://rest-api-assignment-five.vercel.app/apidocs/

## Deployment

The API is deployed using Vercel.

---

# Part 2 — Database Design

## Tables Created

- Customers
- Products
- Orders
- Order_Items
- Payments

## Key Relationships

- One Customer can place multiple Orders
- One Order can contain multiple Products
- Products are linked using Order_Items bridge table
- Each Order has Payment details

## ER Diagram

The ER diagram includes:

- Primary Keys
- Foreign Keys
- Crow's Foot Notation
- Entity Relationships

---

# Part 3 — Data Analysis

## Dataset Used

File:
Indus Action Technical Project Manager Pre Work.xlsx

Total Records:
251

Columns:

- User ID
- Timestamp
- Action
- Product Category
- Revenue

---

## Analysis Performed

- Data Cleaning
- Missing Value Handling
- Category Popularity Analysis
- Conversion Rate Calculation
- User Activity Trend Analysis
- Revenue Analysis by Category

---

## Key Insights

- Electronics category recorded the highest number of interactions.
- Books category generated the highest revenue.
- The conversion rate was calculated at 28.23%.
- User engagement was balanced across multiple product categories.

---

## Recommendations

- Focus promotions on Electronics and Sports categories.
- Increase investment in Books category due to high revenue.
- Optimize lower-performing categories such as Home & Kitchen.
- Continue improving checkout experience to enhance conversion rates.

---

# Tools and Technologies Used

- Python
- Pandas
- Matplotlib
- SQL
- REST API
- Swagger
- VS Code
- Vercel

---

# Conclusion

This project demonstrates end-to-end project delivery capability including API development, database modeling, data analysis, and business insight generation.