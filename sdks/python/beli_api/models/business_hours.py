from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessHours")


@_attrs_define
class BusinessHours:
    """
    Attributes:
        open_day (int | Unset):
        close_day (int | Unset):
        open_time (str | Unset):
        close_time (str | Unset):
    """

    open_day: int | Unset = UNSET
    close_day: int | Unset = UNSET
    open_time: str | Unset = UNSET
    close_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_day = self.open_day

        close_day = self.close_day

        open_time = self.open_time

        close_time = self.close_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_day is not UNSET:
            field_dict["open_day"] = open_day
        if close_day is not UNSET:
            field_dict["close_day"] = close_day
        if open_time is not UNSET:
            field_dict["open_time"] = open_time
        if close_time is not UNSET:
            field_dict["close_time"] = close_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_day = d.pop("open_day", UNSET)

        close_day = d.pop("close_day", UNSET)

        open_time = d.pop("open_time", UNSET)

        close_time = d.pop("close_time", UNSET)

        business_hours = cls(
            open_day=open_day,
            close_day=close_day,
            open_time=open_time,
            close_time=close_time,
        )

        business_hours.additional_properties = d
        return business_hours

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
