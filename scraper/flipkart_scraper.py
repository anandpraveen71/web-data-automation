from playwright.sync_api import sync_playwright
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logger import logger


def scrape_books():
    data = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        logger.info("Opening website...")
        page.goto("https://books.toscrape.com/")

        page.wait_for_timeout(3000)

        books = page.query_selector_all("article.product_pod")

        logger.info(f"Found {len(books)} books")

        for book in books:
            try:
                name = book.query_selector("h3 a").get_attribute("title")
                price = book.query_selector(".price_color").inner_text()

                data.append({
                    "name": name,
                    "price": price
                })
            except Exception as e:
                logger.error(f"Error extracting book: {e}")

        browser.close()

    return data


if __name__ == "__main__":
    result = scrape_books()

    if result:
        df = pd.DataFrame(result)
        df.to_csv("data/products.csv", index=False)
        logger.info("Data saved successfully")
    else:
        print("❌ No data found")