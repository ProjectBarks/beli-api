from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBusinessesResAvailabilityBody")


@_attrs_define
class CreateBusinessesResAvailabilityBody:
    """
    Attributes:
        business_ids (list[int] | Unset):
        date (datetime.date | Unset):
        table_size (int | Unset):
        time (str | Unset):
        use_now (bool | Unset):
        local_dt (datetime.datetime | Unset):
    """

    business_ids: list[int] | Unset = UNSET
    date: datetime.date | Unset = UNSET
    table_size: int | Unset = UNSET
    time: str | Unset = UNSET
    use_now: bool | Unset = UNSET
    local_dt: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_ids: list[int] | Unset = UNSET
        if not isinstance(self.business_ids, Unset):
            business_ids = self.business_ids

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        table_size = self.table_size

        time = self.time

        use_now = self.use_now

        local_dt: str | Unset = UNSET
        if not isinstance(self.local_dt, Unset):
            local_dt = self.local_dt.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_ids is not UNSET:
            field_dict["business_ids"] = business_ids
        if date is not UNSET:
            field_dict["date"] = date
        if table_size is not UNSET:
            field_dict["table_size"] = table_size
        if time is not UNSET:
            field_dict["time"] = time
        if use_now is not UNSET:
            field_dict["use_now"] = use_now
        if local_dt is not UNSET:
            field_dict["local_dt"] = local_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_ids = cast(list[int], d.pop("business_ids", UNSET))

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        table_size = d.pop("table_size", UNSET)

        time = d.pop("time", UNSET)

        use_now = d.pop("use_now", UNSET)

        _local_dt = d.pop("local_dt", UNSET)
        local_dt: datetime.datetime | Unset
        if isinstance(_local_dt, Unset):
            local_dt = UNSET
        else:
            local_dt = datetime.datetime.fromisoformat(_local_dt)

        create_businesses_res_availability_body = cls(
            business_ids=business_ids,
            date=date,
            table_size=table_size,
            time=time,
            use_now=use_now,
            local_dt=local_dt,
        )

        create_businesses_res_availability_body.additional_properties = d
        return create_businesses_res_availability_body

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
