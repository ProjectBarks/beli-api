from enum import Enum


class ReservationOfferReservationPlatformsAdditionalPropertyName(str, Enum):
    OPENTABLE = "OPENTABLE"
    SEVENROOMS = "SEVENROOMS"

    def __str__(self) -> str:
        return str(self.value)
