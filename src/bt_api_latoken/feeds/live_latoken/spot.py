from __future__ import annotations

from typing import Any

from bt_api_latoken.feeds.live_latoken.request_base import LatokenRequestData


class LatokenRequestDataSpot(LatokenRequestData):
    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        super().__init__(data_queue, **kwargs)

    def get_server_time(self, extra_data=None, **kwargs):
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_server_time(self, extra_data=None, **kwargs):
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_tick(self, symbol, extra_data=None, **kwargs):
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        del count
        path, params, extra = self._get_depth(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_depth(self, symbol, count=20, extra_data=None, **kwargs):
        del count
        path, params, extra = self._get_depth(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_exchange_info(self, extra_data=None, **kwargs):
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_deals(self, symbol, count=20, start_time=None, end_time=None, extra_data=None, **kwargs):
        del count, start_time, end_time
        path, params, extra = self._get_deals(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_deals(self, symbol, count=20, start_time=None, end_time=None, extra_data=None, **kwargs):
        del count, start_time, end_time
        path, params, extra = self._get_deals(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_recent_trades(self, symbol, extra_data=None, **kwargs):
        return self.get_deals(symbol, extra_data=extra_data, **kwargs)

    async def async_get_recent_trades(self, symbol, extra_data=None, **kwargs):
        return await self.async_get_deals(symbol, extra_data=extra_data, **kwargs)

    def get_kline(self, symbol, period="1h", count=100, extra_data=None, **kwargs):
        path, params, extra = self._get_kline(symbol, period, count, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_kline(self, symbol, period="1h", count=100, extra_data=None, **kwargs):
        path, params, extra = self._get_kline(symbol, period, count, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def make_order(
        self,
        symbol,
        volume,
        price,
        order_type,
        offset="open",
        post_only=False,
        client_order_id=None,
        extra_data=None,
        **kwargs,
    ):
        del post_only, client_order_id
        side = "buy" if str(offset).upper() in {"BUY", "OPEN"} else "sell"
        path, body, extra = self._make_order(symbol, side, order_type, volume, price, extra_data, **kwargs)
        return self.request(path, body=body, extra_data=extra)

    async def async_make_order(
        self,
        symbol,
        volume,
        price,
        order_type,
        offset="open",
        post_only=False,
        client_order_id=None,
        extra_data=None,
        **kwargs,
    ):
        del post_only, client_order_id
        side = "buy" if str(offset).upper() in {"BUY", "OPEN"} else "sell"
        path, body, extra = self._make_order(symbol, side, order_type, volume, price, extra_data, **kwargs)
        return await self.async_request(path, body=body, extra_data=extra)

    def cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return self.request(path, body=body, extra_data=extra)

    async def async_cancel_order(self, symbol, order_id, extra_data=None, **kwargs):
        del symbol
        path, body, extra = self._cancel_order(order_id, extra_data, **kwargs)
        return await self.async_request(path, body=body, extra_data=extra)

    def get_open_orders(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra = self._get_open_orders(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_open_orders(self, symbol=None, extra_data=None, **kwargs):
        path, params, extra = self._get_open_orders(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_balance(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_balance(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_account(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, params, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_account(self, symbol=None, extra_data=None, **kwargs):
        del symbol
        path, params, extra = self._get_account(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)
