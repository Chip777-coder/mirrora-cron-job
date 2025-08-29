
from fastapi import APIRouter
from utils.fetch_data import fetch

router = APIRouter()

@router.get("/get-block-number")
async def get_block():
    url = "https://eth.llamarpc.com"
    payload = {
        "jsonrpc":"2.0",
        "id":1,
        "method":"eth_blockNumber",
        "params":[]
    }
    return await fetch(url)
