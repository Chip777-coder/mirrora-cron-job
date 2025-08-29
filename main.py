
from fastapi import FastAPI
from routes import price, solana, block

app = FastAPI()

app.include_router(price.router)
app.include_router(solana.router)
app.include_router(block.router)
