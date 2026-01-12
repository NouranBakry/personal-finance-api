from fastapi import FastAPI
from app.routers import accounts, auth, transactions


app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Service is healthy"}

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)

