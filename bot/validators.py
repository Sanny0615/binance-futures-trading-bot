VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    return symbol.endswith("USDT")


def validate_side(side):
    return side in VALID_SIDES


def validate_order_type(order_type):
    return order_type in VALID_ORDER_TYPES


def validate_quantity(quantity):
    return quantity > 0


def validate_price(price):
    return price > 0