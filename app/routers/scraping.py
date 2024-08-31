from fastapi import APIRouter, Depends
from app.dependencies import verify_token
from app.core.scraper import Scraper
from app.core.storage import DataStorage
from app.core.cache import Cache
from app.core.notifier import Notifier
from app.core.tool import ScrapingTool

router = APIRouter()

# @router.get("/start_scraping/", dependencies=[Depends(verify_token)])
@router.get("/start_scraping/")
def start_scraping(pages: int = 5, proxy: str = None):
    scraper = Scraper(base_url="https://dentalstall.com/shop/", pages=pages, proxy=proxy)
    storage = DataStorage()
    cache = Cache()
    notifier = Notifier()
    tool = ScrapingTool(scraper, storage, cache, notifier)
    tool.run()
    return {"message": f"Scraping completed for {pages} pages"}
