from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "data", "products.db")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.get("/products")
def get_products():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products LIMIT 10")
    rows = cursor.fetchall()

    conn.close()

    return {"data": rows}