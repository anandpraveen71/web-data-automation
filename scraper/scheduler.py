import schedule
import time
from flipkart_scraper import scrape_books

def job():
    print("⏳ Running scheduled scraping...")
    scrape_books()
    print("✅ Job completed\n")

# Run every 1 minute (you can change later)
schedule.every().day.at("10:00").do(job)

print("🚀 Scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)