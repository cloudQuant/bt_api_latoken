from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class LatokenExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "LATOKEN___SPOT"
        self.asset_type = "SPOT"
        self.rest_url = "https://api.latoken.com"
        self.wss_url = ""
        self.rest_paths = {}

        self.kline_periods = {
            "1m": "1",
            "5m": "5",
            "15m": "15",
            "30m": "30",
            "1h": "60",
            "4h": "240",
            "1d": "1D",
            "1w": "1W",
        }
        self.reverse_kline_periods = {v: k for k, v in self.kline_periods.items()}
        self.legal_currency = ["USDT", "BTC", "ETH", "LA"]

    @staticmethod
    def get_symbol(symbol):
        return symbol.lower().replace("/", "_").replace("-", "_")

    @staticmethod
    def get_reverse_symbol(symbol):
        return symbol.upper().replace("_", "-")

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        path = self.rest_paths[key]
        if kwargs:
            for k, v in kwargs.items():
                path = path.replace(f"{{{k}}}", str(v).lower())
        return path

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)

    def get_reverse_period(self, period: str) -> str:
        return self.reverse_kline_periods.get(period, period)


class LatokenExchangeDataSpot(LatokenExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.api_key: str | None = None
        self.api_secret: str | None = None
        self.rest_paths = {
            "get_server_time": "GET /v2/time",
            "get_tick": "GET /v2/ticker/{base}/{quote}",
            "get_all_tickers": "GET /v2/ticker",
            "get_depth": "GET /v2/book/{currency}/{quote}",
            "get_deals": "GET /v2/trade/history/{currency}/{quote}",
            "get_exchange_info": "GET /v2/pair",
            "get_currencies": "GET /v2/currency",
            "get_kline": "GET /v2/chart/week/{currency}/{quote}",
            "make_order": "POST /v2/auth/order/place",
            "cancel_order": "POST /v2/auth/order/cancel",
            "get_open_orders": "GET /v2/auth/order/pair/{currency}/{quote}/active",
            "get_balance": "GET /v2/auth/account",
            "get_account": "GET /v2/auth/account",
        }
