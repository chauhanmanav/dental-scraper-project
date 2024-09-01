from fastapi import APIRouter, Depends
from app.dependencies import verify_token
from app.core.scraper import Scraper
from app.core.storage import DataStorage
from app.core.cache import Cache
from app.core.notifier import Notifier
from app.core.tool import ScrapingTool
from app.utils.utils import get_base_url

router = APIRouter()

@router.get("/start_scraping/", dependencies=[Depends(verify_token)])
def start_scraping(pages: int = 5, proxy: str = None):
    scraper = Scraper(base_url=get_base_url(), pages=pages, proxy=proxy)
    storage = DataStorage()
    cache = Cache()
    notifier = Notifier()
    tool = ScrapingTool(scraper, storage, cache, notifier)
    tool.run()
    return {"message": f"Scraping completed for {pages} pages"}
