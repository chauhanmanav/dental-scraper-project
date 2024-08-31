import json
from typing import List

class DataStorage:
    def __init__(self, filename: str = "data/scraped_data.json"):
        self.filename = filename

    def save_data(self, data: List[dict]):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {self.filename}")
