import time
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from .alpaca import AlpacaAPI
from .config import ALLOWED_SYMBOLS, MAX_ORDER_VALUE

router = APIRouter()
alpaca = AlpacaAPI()

# Models
class BuyText(BaseModel):
    command: str = Field(..., description="Format: buy TICKER --AMOUNT, or sell TICKER --AMOUNT")

class OrderRequest(BaseModel):
    symbol: str
    qty: int
    side: str  # 'buy' or 'sell'

# Helpers
def _guard_symbol(symbol: str):
    s = symbol.upper()
    if ALLOWED_SYMBOLS and s not in ALLOWED_SYMBOLS:
        raise HTTPException(400, f"Symbol '{s}' not allowed in v1.")
    asset = alpaca.asset(s)
    if not asset.get("tradable", False):
        raise HTTPException(400, f"Asset '{s}' not tradable.")
    return s

def _guard_market_open():
    clock = alpaca.clock()
    if not clock.get("is_open", False):
        raise HTTPException(400, "Market is closed for paper trading.")

def _guard_cash_for_buy(symbol: str, qty: int):
    q = alpaca.latest_quote(symbol)
    ask = q.get("quote", {}).get("ap")
    if not ask:
        raise HTTPException(400, f"No live ask for {symbol}.")
    est_cost = ask * qty * 1.01
    if est_cost > MAX_ORDER_VALUE:
        raise HTTPException(400, f"Order exceeds per-order cap ${MAX_ORDER_VALUE:.2f}.")
    acct = alpaca.account()
    cash = float(acct.get("cash", 0))
    if est_cost > cash:
        raise HTTPException(400, f"Insufficient cash. Need ~${est_cost:.2f}, have ${cash:.2f}.")
    return ask, est_cost

def _parse_buy_text(cmd: str) -> OrderRequest:
    # Strict grammar: "buy NVDA --2" or "sell AAPL --1"
    parts = cmd.strip().split()
    # Minimal robust parse:
    try:
        side = parts[0].lower()
        symbol = parts[1].upper()
        qty_str = parts[2] if parts[2].startswith("--") else parts[-1]
        if qty_str.startswith("--"):
            qty = int(qty_str.replace("--", ""))
        else:
            raise ValueError
    except Exception:
        raise HTTPException(400, "Format must be: buy TICKER --AMOUNT (e.g., 'buy NVDA --2').")
    if side not in ("buy","sell"):
        raise HTTPException(400, "Side must be 'buy' or 'sell'.")
    if qty <= 0:
        raise HTTPException(400, "Quantity must be > 0.")
    return OrderRequest(symbol=symbol, qty=qty, side=side)

# Routes
@router.get("/health")
def health():
    return {"ok": True}

@router.get("/portfolio")
def get_portfolio():
    return {"account": alpaca.account(), "positions": alpaca.positions()}

@router.get("/market-data")
def market_data(symbol: str = Query(..., min_length=1, max_length=10), timeframe: str = "1Day", limit: int = 100):
    s = _guard_symbol(symbol)
    latest = alpaca.latest_quote(s)
    hist = alpaca.bars(s, timeframe=timeframe, limit=limit)
    return {"latest_quote": latest, "bars": hist}

@router.post("/order")
def place_order(orq: OrderRequest):
    s = _guard_symbol(orq.symbol)
    _guard_market_open()

    if orq.side == "buy":
        ask, est = _guard_cash_for_buy(s, orq.qty)

    order = alpaca.place_order(symbol=s, qty=orq.qty, side=orq.side, type_="market", tif="day")

    # Poll briefly for terminal status (filled/canceled/rejected/expired)
    for _ in range(10):
        o = alpaca.get_order(order["id"])
        if o["status"] in ("filled", "canceled", "rejected", "expired"):
            return {"submitted": order, "final": o}
        time.sleep(1)

    return {"submitted": order, "note": "Order pending; check status later."}

@router.post("/buy-text")
def buy_text(req: BuyText):
    orq = _parse_buy_text(req.command)
    return place_order(orq)
