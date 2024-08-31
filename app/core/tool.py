from app.core.scraper import Scraper
from app.core.storage import DataStorage
from app.core.cache import Cache
from app.core.notifier import Notifier

class ScrapingTool:
    def __init__(self, scraper: Scraper, storage: DataStorage, cache: Cache, notifier: Notifier):
        self.scraper = scraper
        self.storage = storage
        self.cache = cache
        self.notifier = notifier

    def run(self):
        data = self.scraper.scrape()
        updated_data = []
        print("scraped data: ", data)
        for item in data:
            if not self.cache.is_cached(item["product_title"], item["product_price"]):
                updated_data.append(item)
                self.cache.update_cache(item["product_title"], item["product_price"])
        self.storage.save_data(updated_data)
        self.notifier.notify(f"Scraping completed. {len(updated_data)} products updated.")
