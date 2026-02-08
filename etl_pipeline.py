import pandas as pd
import random
from datetime import datetime
import mysql.connector

# ------------------------------
# 1. Simulate Raw Order Data
# ------------------------------
def generate_orders(n=20):
    data = []
    for i in range(n):
        data.append({
            "order_id": i + 1,
            "user_id": random.randint(1000, 2000),
            "product_id": random.randint(1, 100),
            "quantity": random.randint(1, 5),
            "price": round(random.uniform(50, 500), 2),
            "order_time": datetime.now()
        })
    return pd.DataFrame(data)

# ------------------------------
# 2. Extract
# ------------------------------
def extract():
    df = generate_orders()
    return df

# ------------------------------
# 3. Transform
# ------------------------------
def transform(df):
    df["total_amount"] = df["quantity"] * df["price"]
    df["order_date"] = pd.to_datetime(df["order_time"]).dt.date
    return df

# ------------------------------
# 4. Load into MySQL
# ------------------------------
def load_mysql(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="etl_user",          # change if needed
        password="etl_password",  # change if needed
        database="ecommerce",
        auth_plugin="mysql_native_password"
    )

    cursor = conn.cursor()

    insert_query = """
        INSERT INTO orders
        (order_id, user_id, product_id, quantity, price, total_amount, order_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, (
            int(row["order_id"]),
            int(row["user_id"]),
            int(row["product_id"]),
            int(row["quantity"]),
            float(row["price"]),
            float(row["total_amount"]),
            row["order_date"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

# ------------------------------
# 5. Run ETL Pipeline
# ------------------------------
def run_etl():
    df = extract()
    df = transform(df)
    load_mysql(df)
    print("ETL Pipeline Executed Successfully")

run_etl()

