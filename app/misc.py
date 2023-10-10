from aiohttp import ClientSession
import json
from typing import List, Dict


base_url = 'https://jservice.io/api/random?count={num}'


async def get_quiz(count: int = 5) -> List[Dict] or None:
    async with ClientSession() as session:
        async with session.get(base_url.format(num=count)) as resp:
            if resp.status != 200:
                return

            return json.loads(await resp.text())


async def validate_count(count: str) -> bool:
    try:
        count = int(count)
    except:
        return False
    if count < 0:
        return False

    return count
