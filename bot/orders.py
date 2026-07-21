from binance.enums import *
from bot.client import client
from bot.logging_config import logger


def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity,
        )

        print("\n✅ Market Order Placed Successfully")
        print(order)
        logger.info(f"Limit Order: {order}")
        

        return order

    except Exception as e:
      logger.error(f"Error placing order: {str(e)}")
      print(f"\n❌ Error placing order: {e}")
      return None