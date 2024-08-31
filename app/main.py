from fastapi import FastAPI
from app.routers import scraping

app = FastAPI()

# Include the scraping router
app.include_router(scraping.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
