from enum import Enum


class FollowEdgeStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
