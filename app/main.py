from fastapi import FastAPI
from app.routers import auth


app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Service is healthy"}

app.include_router(auth.router)
