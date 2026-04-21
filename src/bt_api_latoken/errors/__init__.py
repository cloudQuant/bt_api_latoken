from __future__ import annotations

from typing import Any

from bt_api_base.error import ErrorCategory, ErrorTranslator, UnifiedError, UnifiedErrorCode


class LatokenErrorTranslator(ErrorTranslator):
    @classmethod
    def translate(cls, raw_error: dict[str, Any], venue: str) -> UnifiedError | None:
        message = str(raw_error.get("message", raw_error.get("error", "")))
        message_lower = message.lower()
        if "balance" in message_lower or "insufficient" in message_lower:
            return cls._build_error(UnifiedErrorCode.INSUFFICIENT_BALANCE, venue, raw_error)
        if "order" in message_lower and "not found" in message_lower:
            return cls._build_error(UnifiedErrorCode.ORDER_NOT_FOUND, venue, raw_error)
        if "order" in message_lower and "duplicate" in message_lower:
            return cls._build_error(UnifiedErrorCode.DUPLICATE_ORDER, venue, raw_error)
        if "rate" in message_lower or "limit" in message_lower:
            return cls._build_error(UnifiedErrorCode.RATE_LIMIT_EXCEEDED, venue, raw_error)
        if "auth" in message_lower or "key" in message_lower or "signature" in message_lower:
            return cls._build_error(UnifiedErrorCode.INVALID_API_KEY, venue, raw_error)
        return super().translate(raw_error, venue)

    @staticmethod
    def _build_error(code: UnifiedErrorCode, venue: str, raw_error: dict[str, Any]) -> UnifiedError:
        message = str(raw_error.get("message", raw_error.get("error", code.name)))
        return UnifiedError(
            code=code,
            category=ErrorCategory.BUSINESS,
            venue=venue,
            message=message,
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )
