
import httpx

async def fetch(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()
