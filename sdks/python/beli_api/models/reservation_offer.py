from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business import Business
    from ..models.reservation_offer_reservation_platforms import ReservationOfferReservationPlatforms
    from ..models.user import User


T = TypeVar("T", bound="ReservationOffer")


@_attrs_define
class ReservationOffer:
    """Slot metadata and availability keys vary by query/platform; treat as a partial contract beyond the fields listed
    here.

        Attributes:
            id (int | Unset):
            user (User | Unset):
            business (Business | Unset):
            reservation_platforms (ReservationOfferReservationPlatforms | Unset):
    """

    id: int | Unset = UNSET
    user: User | Unset = UNSET
    business: Business | Unset = UNSET
    reservation_platforms: ReservationOfferReservationPlatforms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        business: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business, Unset):
            business = self.business.to_dict()

        reservation_platforms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservation_platforms, Unset):
            reservation_platforms = self.reservation_platforms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user
        if business is not UNSET:
            field_dict["business"] = business
        if reservation_platforms is not UNSET:
            field_dict["reservation_platforms"] = reservation_platforms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business import Business
        from ..models.reservation_offer_reservation_platforms import ReservationOfferReservationPlatforms
        from ..models.user import User

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _business = d.pop("business", UNSET)
        business: Business | Unset
        if isinstance(_business, Unset):
            business = UNSET
        else:
            business = Business.from_dict(_business)

        _reservation_platforms = d.pop("reservation_platforms", UNSET)
        reservation_platforms: ReservationOfferReservationPlatforms | Unset
        if isinstance(_reservation_platforms, Unset):
            reservation_platforms = UNSET
        else:
            reservation_platforms = ReservationOfferReservationPlatforms.from_dict(_reservation_platforms)

        reservation_offer = cls(
            id=id,
            user=user,
            business=business,
            reservation_platforms=reservation_platforms,
        )

        reservation_offer.additional_properties = d
        return reservation_offer

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
