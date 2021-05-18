from __future__ import annotations

import enum


class CandleResolution(enum.Enum):
    MIN_1 = '1min'
    MIN_2 = '2min'
    MIN_3 = '3min'
    MIN_5 = '5min'
    MIN_10 = '10min'
    MIN_15 = '15min'
    MIN_30 = '30min'
    HOUR = 'hour'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
