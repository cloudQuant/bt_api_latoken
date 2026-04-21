from __future__ import annotations
from unittest.mock import AsyncMock, MagicMock
import pytest
from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_latoken.feeds.live_latoken.request_base import LatokenRequestData


def test_latoken_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = LatokenRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="LATOKEN___SPOT",
    )

    monkeypatch.setattr(
        request_data,
        "http_request",
        lambda method, url, headers, body, timeout: {"status": "SUCCESS"},
    )

    result = request_data.request("GET /v2/trading/pairs")

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"status": "SUCCESS"}
