# 🔄 ETL Pipeline for E-Commerce Orders using Python & MySQL

This project demonstrates a simple **ETL (Extract, Transform, Load) pipeline** for an e-commerce system. It simulates raw order data, processes it, and loads the transformed data into a MySQL database.

---

## 🚀 Project Overview

ETL pipelines are a core component of data engineering and business intelligence systems.  
This project covers the complete ETL lifecycle:

- **Extract**: Generate raw order data
- **Transform**: Clean and enrich the data
- **Load**: Store the processed data into a MySQL database

The pipeline is automated and designed for learning and demonstration purposes.

---

## 🧠 ETL Pipeline Stages

### 1. Extract
- Simulates raw e-commerce order data
- Generates fields such as:
  - Order ID
  - User ID
  - Product ID
  - Quantity
  - Price
  - Order timestamp

### 2. Transform
- Calculates total order amount
- Extracts order date from timestamp
- Prepares data for database insertion

### 3. Load
- Loads transformed data into a MySQL database
- Inserts records into the `orders` table

---

## 🗂️ Database Requirements

### MySQL Database
- **Database Name:** `ecommerce`
- **Table Name:** `orders`

### Sample Table Schema
```sql
CREATE TABLE orders (
    order_id INT,
    user_id INT,
    product_id INT,
    quantity INT,
    price FLOAT,
    total_amount FLOAT,
    order_date DATE
);
