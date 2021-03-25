from __future__ import annotations

import enum


class TradeStatus(enum.Enum):
    NORMALTRADING = "NormalTrading"
    NOTAVAILABLEFORTRADING = "NotAvailableForTrading"
