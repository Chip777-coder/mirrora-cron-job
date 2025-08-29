
from fastapi import APIRouter
from utils.fetch_data import fetch

router = APIRouter()

@router.get("/get-price")
async def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    return await fetch(url)
