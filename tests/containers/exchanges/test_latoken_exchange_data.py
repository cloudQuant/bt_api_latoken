"""Tests for LatokenExchangeData container."""

from __future__ import annotations

from bt_api_latoken.exchange_data import LatokenExchangeData


class TestLatokenExchangeData:
    """Tests for LatokenExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = LatokenExchangeData()

        assert exchange.exchange_name == "LATOKEN___SPOT"
