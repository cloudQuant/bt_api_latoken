from __future__ import annotations

from bt_api_base.registry import ExchangeRegistry

from bt_api_latoken.exchange_data import LatokenExchangeDataSpot
from bt_api_latoken.feeds.live_latoken.spot import LatokenRequestDataSpot


def register_latoken(registry: ExchangeRegistry | type[ExchangeRegistry]) -> None:
    registry.register_feed("LATOKEN___SPOT", LatokenRequestDataSpot)
    registry.register_exchange_data("LATOKEN___SPOT", LatokenExchangeDataSpot)


def register(registry: ExchangeRegistry | None = None) -> None:
    if registry is None:
        register_latoken(ExchangeRegistry)
        return
    register_latoken(registry)
