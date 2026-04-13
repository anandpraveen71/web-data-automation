import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

input_path = os.path.join(BASE_DIR, "data", "products.csv")
output_path = os.path.join(BASE_DIR, "data", "cleaned_products.csv")


def clean_data():
    print("Loading data...")
    df = pd.read_csv(input_path)

    print("Original Data:")
    print(df.head())

    # 🔹 Remove duplicates
    df = df.drop_duplicates()

    # 🔹 Remove null values
    df = df.dropna()

    # 🔹 Clean price (remove £ symbol)
    df["price"] = df["price"].str.replace("£", "")
    df["price"] = df["price"].astype(float)

    print("\nCleaned Data:")
    print(df.head())

    df.to_csv(output_path, index=False)

    print("\n✅ Cleaned data saved to cleaned_products.csv")


if __name__ == "__main__":
    clean_data()