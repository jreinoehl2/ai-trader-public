from typing import Any, Dict, List, Optional
import requests
from config import ALPACA_BASE, ALPACA_KEY, ALPACA_SECRET, REQUEST_TIMEOUT

class AlpacaAPI:
    def __init__(self, base_url: str = ALPACA_BASE, api_key: str = ALPACA_KEY, api_secret: str = ALPACA_SECRET):
        self.base_url = base_url
        self.headers = {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": api_secret,
        }
    
    def _req(self, method: str, endpoint: str, json: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, json=json, params=params, timeout=REQUEST_TIMEOUT)
        if response.status_code >= 400:
            raise RuntimeError(f"Alpaca error {response.status_code}: {response.text}")
        return response.json()
    
    # Account and Portfolio
    def account(self) -> Dict[str, Any]:
        return self._req("GET", "account")

    def positions(self) -> Dict[str, Any]:
        return self._req("GET", "positions")
    
    # Market Clock and Assets
    def clock(self) -> Dict[str, Any]:
        return self._req("GET", "clock")

    def asset(self, symbol: str) -> Dict[str, Any]:
        return self._req("GET", f"assets/{symbol.upper()}")
    
    # Quotes and Bars
    def latest_quote(self, symbol: str) -> Dict[str, Any]:
        return self._req("GET", f"stocks/{symbol.upper()}/quotes/latest")
    
    def bars(self, symbol: str, timeframe: str = "1Day", limit: int = 100, start: Optional[str] = None, end: Optional[str] = None) -> Dict[str, Any]:
        params = {"timeframe": timeframe, "limit": limit}
        if start: params["start"] = start
        if end: params["end"] = end
        return self._req("GET", f"stocks/{symbol.upper()}/bars", params=params)

        # Orders
    def place_order(self, symbol: str, qty: int, side: str, type_: str = "market", tif: str = "day") -> Dict[str, Any]:
        payload = {
            "symbol": symbol.upper(),
            "qty": qty,
            "side": side,              # 'buy' or 'sell'
            "type": type_,             # 'market' for v1
            "time_in_force": tif       # 'day' for v1
        }
        return self._req("POST", "orders", json=payload)
    
    def get_order(self, order_id: str) -> Dict[str, Any]:
        return self._req("GET", f"orders/{order_id}")