"""
pricing.py: the code you are writing tests FOR. (Don't edit this file.)
"""


def apply_discount(price, percent):
    """Return price reduced by `percent` (0-100), rounded to 2 decimals.

    Raises ValueError if percent is below 0 or above 100.
    """
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 - percent / 100), 2)


def shipping(order_total):
    """Shipping is free for orders of $50 or more, otherwise $4.99."""
    if order_total >= 50:
        return 0
    return 4.99


def parse_price(text):
    """Turn text like "$1,234.50" or " 12 " into a float.

    Raises ValueError if the text isn't a price.
    """
    cleaned = text.strip().replace("$", "").replace(",", "")
    return float(cleaned)
