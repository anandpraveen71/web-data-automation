import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "data", "cleaned_products.csv")
db_path = os.path.join(BASE_DIR, "data", "products.db")


def store_data():
    print("Loading cleaned data...")
    df = pd.read_csv(input_path)

    print("Connecting to database...")
    conn = sqlite3.connect(db_path)

    print("Storing data into SQL table...")
    df.to_sql("products", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Data stored in SQLite DB (products.db)")


if __name__ == "__main__":
    store_data()