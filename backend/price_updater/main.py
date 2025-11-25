import asyncio
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from redis.asyncio import Redis

from app.core.database import async_session_maker
from price_updater.service import update_prices
from price_updater.config import UPDATE_INTERVAL, REDIS_URL


async def job():
    async with async_session_maker() as session:
        redis = Redis.from_url(REDIS_URL, decode_responses=True)

        await update_prices(session, redis)

        await redis.close()


async def main():
    logger.info("🚀 Price Updater Service запущен")

    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, "interval", seconds=UPDATE_INTERVAL)
    scheduler.start()

    # выполнить один раз при старте (можно выключить)
    await job()

    # держим процесс живым
    while True:
        await asyncio.sleep(3600)


if __name__ == "__main__":
    asyncio.run(main())