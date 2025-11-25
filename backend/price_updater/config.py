
import os

# asset_id → ticker
TICKERS = {
    2: "GAZP",
    1: "SBER",
    9: "LKOH",
    10: "ROSN",
    11: "MGNT"
}

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
UPDATE_INTERVAL = 10  # секунды