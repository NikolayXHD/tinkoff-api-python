from __future__ import annotations

import enum


class OrderType(enum.Enum):
    LIMIT = 'Limit'
    MARKET = 'Market'
