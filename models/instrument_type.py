from __future__ import annotations

import enum


class InstrumentType(enum.Enum):
    STOCK = 'Stock'
    CURRENCY = 'Currency'
    BOND = 'Bond'
    ETF = 'Etf'
