import os

ALPACA_BASE = os.getenv("ALPACA_BASE", "")
ALPACA_KEY = os.getenv("ALPACA_API_KEY", "https://paper-api.alpaca.markets/v2")
ALPACA_SECRET = os.getenv("ALPACA_SECRET_KEY", "")

ALLOWED_SYMBOLS = set(filter(None, os.getenv("ALLOWED_SYMBOLS", "").upper().split(",")))
MAX_ORDER_VALUE = float(os.getenv("MAX_ORDER_VALUE", "1000"))

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))