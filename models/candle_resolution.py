from __future__ import annotations

import enum


class CandleResolution(enum.Enum):
    _1MIN = "1min"
    _2MIN = "2min"
    _3MIN = "3min"
    _5MIN = "5min"
    _10MIN = "10min"
    _15MIN = "15min"
    _30MIN = "30min"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
