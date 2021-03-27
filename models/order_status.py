from __future__ import annotations

import enum


class OrderStatus(enum.Enum):
    NEW = 'New'
    PARTIALLYFILL = 'PartiallyFill'
    FILL = 'Fill'
    CANCELLED = 'Cancelled'
    REPLACED = 'Replaced'
    PENDINGCANCEL = 'PendingCancel'
    REJECTED = 'Rejected'
    PENDINGREPLACE = 'PendingReplace'
    PENDINGNEW = 'PendingNew'
