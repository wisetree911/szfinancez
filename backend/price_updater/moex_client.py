# import random

# async def get_price_from_moex(ticker: str) -> float:
#     base = {
#         "GAZP": 152,
#         "SBER": 290,
#         "LKOH": 6700,
#         "ROSN": 520,
#         "MGNT": 5500
#     }.get(ticker, 100)

#     return round(base + random.uniform(-3, 3), 2)

import aiohttp

BASE_URL = "https://iss.moex.com/iss"


class MoexClient:
    @staticmethod
    async def get_last_price(ticker: str) -> float:
        url = f"{BASE_URL}/engines/stock/markets/shares/securities/{ticker}.json"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
        
        return float(data["marketdata"]["data"][1][12])