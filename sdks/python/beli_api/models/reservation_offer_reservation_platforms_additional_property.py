from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reservation_offer_reservation_platforms_additional_property_name import (
    ReservationOfferReservationPlatformsAdditionalPropertyName,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReservationOfferReservationPlatformsAdditionalProperty")


@_attrs_define
class ReservationOfferReservationPlatformsAdditionalProperty:
    """
    Attributes:
        name (ReservationOfferReservationPlatformsAdditionalPropertyName | Unset):
    """

    name: ReservationOfferReservationPlatformsAdditionalPropertyName | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: str | Unset = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: ReservationOfferReservationPlatformsAdditionalPropertyName | Unset
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ReservationOfferReservationPlatformsAdditionalPropertyName(_name)

        reservation_offer_reservation_platforms_additional_property = cls(
            name=name,
        )

        reservation_offer_reservation_platforms_additional_property.additional_properties = d
        return reservation_offer_reservation_platforms_additional_property

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
