
from fastapi import APIRouter
from utils.fetch_data import fetch

router = APIRouter()

@router.get("/get-solana-slot")
async def get_slot():
    url = "https://api.mainnet-beta.solana.com"
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSlot"
    }
    return await fetch(url)
