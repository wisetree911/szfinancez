from datetime import datetime
from app.repositories.asset_prices import AssetPriceRepository
from price_updater.moex_client import MoexClient
from price_updater.config import TICKERS
from loguru import logger

async def update_prices(session, redis):
    logger.info("⏳ Обновление цен...")

    for asset_id, ticker in TICKERS.items():

        price = await MoexClient.get_last_price(ticker)

        await AssetPriceRepository.add_price(
            session=session,
            asset_id=asset_id,
            price=price,
            currency="RUB",
            source="moex"
        )

        await redis.set(f"price:{ticker}", price)

        logger.info(f"Обновили цену {ticker} → {price}")

    await session.commit()
    logger.info("Обновление завершено")