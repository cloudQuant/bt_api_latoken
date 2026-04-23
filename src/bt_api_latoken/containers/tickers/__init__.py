from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.tickers.ticker import TickerData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_string


class LatokenTickerData(TickerData):
    def __init__(
        self,
        ticker_info: str | dict[str, Any],
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(ticker_info, has_been_json_encoded)
        self.exchange_name = "LATOKEN"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.ticker_data: dict[str, Any] | None = (
            ticker_info if has_been_json_encoded and isinstance(ticker_info, dict) else None
        )
        self.ticker_symbol_name: str | None = None
        self.last_price: float | None = None
        self.bid_price: float | None = None
        self.ask_price: float | None = None
        self.high: float | None = None
        self.low: float | None = None
        self.volume: float | None = None
        self.server_time: float | None = None
        self.has_been_init_data = False

    def init_data(self) -> LatokenTickerData:
        if not self.has_been_json_encoded:
            self.ticker_data = json.loads(self.ticker_info) if isinstance(self.ticker_info, str) else {}
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        payload = self.ticker_data or {}
        if isinstance(payload, dict):
            self.ticker_symbol_name = from_dict_get_string(payload, "symbol", self.symbol_name)
            self.last_price = from_dict_get_float(payload, "lastPrice")
            self.bid_price = from_dict_get_float(payload, "bidPrice")
            self.ask_price = from_dict_get_float(payload, "askPrice")
            self.high = from_dict_get_float(payload, "high")
            self.low = from_dict_get_float(payload, "low")
            self.volume = from_dict_get_float(payload, "volume")
            timestamp = payload.get("timestamp")
            self.server_time = float(timestamp) / 1000 if timestamp is not None else self.local_update_time

        self.has_been_init_data = True
        return self

    def get_daily_change(self) -> float | None:
        self.init_data()
        if self.high is None or self.low is None:
            return None
        return self.high - self.low

    def get_all_data(self) -> dict[str, Any]:
        self.init_data()
        return {
            "exchange_name": self.exchange_name,
            "symbol_name": self.symbol_name,
            "asset_type": self.asset_type,
            "ticker_symbol_name": self.ticker_symbol_name,
            "server_time": self.server_time,
            "bid_price": self.bid_price,
            "ask_price": self.ask_price,
            "bid_volume": None,
            "ask_volume": None,
            "last_price": self.last_price,
            "last_volume": self.volume,
            "local_update_time": self.local_update_time,
        }

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_local_update_time(self) -> float:
        return float(self.local_update_time)

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_ticker_symbol_name(self) -> str | None:
        self.init_data()
        return self.ticker_symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | None:
        self.init_data()
        return self.server_time

    def get_bid_price(self) -> float | None:
        self.init_data()
        return self.bid_price

    def get_ask_price(self) -> float | None:
        self.init_data()
        return self.ask_price

    def get_bid_volume(self) -> float | None:
        return None

    def get_ask_volume(self) -> float | None:
        return None

    def get_last_price(self) -> float | None:
        self.init_data()
        return self.last_price

    def get_last_volume(self) -> float | None:
        self.init_data()
        return self.volume

    def get_high(self) -> float | None:
        self.init_data()
        return self.high

    def get_low(self) -> float | None:
        self.init_data()
        return self.low

    def get_volume(self) -> float | None:
        self.init_data()
        return self.volume


class LatokenRequestTickerData(LatokenTickerData):
    pass


class LatokenWssTickerData(LatokenTickerData):
    pass


__all__ = ["LatokenTickerData", "LatokenRequestTickerData", "LatokenWssTickerData"]
