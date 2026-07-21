from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

print("========== Binance Trading Bot ==========")

symbol = input("Enter Symbol (e.g., BTCUSDT): ").upper()

if not validate_symbol(symbol):
    print("❌ Invalid Symbol")
    exit()

side = input("Enter Side (BUY/SELL): ").upper()

if not validate_side(side):
    print("❌ Invalid Side")
    exit()

order_type = input("Order Type (MARKET/LIMIT): ").upper()

if not validate_order_type(order_type):
    print("❌ Invalid Order Type")
    exit()

quantity = float(input("Enter Quantity: "))

if not validate_quantity(quantity):
    print("❌ Quantity must be greater than 0")
    exit()

if order_type == "MARKET":
    place_market_order(symbol, side, quantity)

elif order_type == "LIMIT":
    price = float(input("Enter Limit Price: "))

    if not validate_price(price):
        print("❌ Price must be greater than 0")
        exit()

    place_limit_order(symbol, side, quantity, price)
    