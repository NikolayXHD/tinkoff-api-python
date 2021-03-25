from __future__ import annotations

import enum


class OperationStatus(enum.Enum):
    DONE = "Done"
    DECLINE = "Decline"
    PROGRESS = "Progress"
