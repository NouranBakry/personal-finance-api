from fastapi import FastAPI
from app.database import engine, Base
from app.models import User, Account, Transaction
from app.routers import accounts, auth, transactions

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Service is healthy"}

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
