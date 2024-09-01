import requests
from bs4 import BeautifulSoup
import os
import time
from typing import List

class Scraper:
    def __init__(self, base_url: str, pages: int = 5, proxy: str = None):
        self.base_url = base_url
        self.pages = pages
        self.proxy = {"http": proxy, "https": proxy} if proxy else None
        self.retry_delay = 5  # seconds

    def getUrl(self, page: int):
        if(page==1):
            return self.base_url
        return f"{self.base_url}/page/{page}/"

    def scrape(self) -> List[dict]:
        scraped_data = []
        for page in range(1, self.pages + 1):
            url = self.getUrl(page)
            try:
                response = self.get_page(url)
                soup = BeautifulSoup(response.content, "html.parser")
                products = soup.find_all('div', class_ ='product-inner')
                for product in products:
                    imgtag = product.find('div', attrs={'class':'mf-product-thumbnail'}).find('img')
                    path_to_image = imgtag.get("data-lazy-src")
                    captionDetails = product.find('div', attrs={'class':'mf-product-content'})
                    title = captionDetails.find('h2', attrs={'class':'woo-loop-product__title'}).find('a').get_text(strip=True)
                    priceDetails = product.find('div', attrs={'class':'mf-product-price-box'})
                    priceWithSymbol = priceDetails.find('span', attrs={'class':'woocommerce-Price-amount amount'}).find('bdi').get_text(strip=True)
                    price = float(priceWithSymbol[1:])
                    image_path = self.download_image(path_to_image, title)
                    scraped_data.append({
                        "product_title": title,
                        "product_price": price,
                        "path_to_image": image_path,
                    })
            except Exception as e:
                print(f"Error scraping {url}: {e}")
                continue
        return scraped_data

    def get_page(self, url: str) -> requests.Response:
        for _ in range(3):  # retry 3 times
            try:
                response = requests.get(url, proxies=self.proxy)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Request error: {e}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
        raise Exception(f"Failed to retrieve page: {url}")

    def download_image(self, url: str, product_title: str) -> str:
        image_name = f"{product_title.replace(' ', '_')}.jpg"
        image_path = os.path.join('images', image_name)
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
        return image_path
