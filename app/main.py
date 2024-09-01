from fastapi import FastAPI
from app.routers import scraping
from app.utils.utils import get_host, get_port

app = FastAPI()

# Include the scraping router
app.include_router(scraping.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=get_host(), port=get_port())
