from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Score")


@_attrs_define
class Score:
    """
    Attributes:
        user_id (UUID | Unset):
        business_id (int | Unset):
        value (float | Unset):
        category (str | Unset):
        num_visits (int | None | Unset):
        notification_id (int | None | Unset):
        sent_dt (datetime.datetime | None | Unset):
    """

    user_id: UUID | Unset = UNSET
    business_id: int | Unset = UNSET
    value: float | Unset = UNSET
    category: str | Unset = UNSET
    num_visits: int | None | Unset = UNSET
    notification_id: int | None | Unset = UNSET
    sent_dt: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        business_id = self.business_id

        value = self.value

        category = self.category

        num_visits: int | None | Unset
        if isinstance(self.num_visits, Unset):
            num_visits = UNSET
        else:
            num_visits = self.num_visits

        notification_id: int | None | Unset
        if isinstance(self.notification_id, Unset):
            notification_id = UNSET
        else:
            notification_id = self.notification_id

        sent_dt: None | str | Unset
        if isinstance(self.sent_dt, Unset):
            sent_dt = UNSET
        elif isinstance(self.sent_dt, datetime.datetime):
            sent_dt = self.sent_dt.isoformat()
        else:
            sent_dt = self.sent_dt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if business_id is not UNSET:
            field_dict["business_id"] = business_id
        if value is not UNSET:
            field_dict["value"] = value
        if category is not UNSET:
            field_dict["category"] = category
        if num_visits is not UNSET:
            field_dict["num_visits"] = num_visits
        if notification_id is not UNSET:
            field_dict["notification_id"] = notification_id
        if sent_dt is not UNSET:
            field_dict["sent_dt"] = sent_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        business_id = d.pop("business_id", UNSET)

        value = d.pop("value", UNSET)

        category = d.pop("category", UNSET)

        def _parse_num_visits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_visits = _parse_num_visits(d.pop("num_visits", UNSET))

        def _parse_notification_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        notification_id = _parse_notification_id(d.pop("notification_id", UNSET))

        def _parse_sent_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sent_dt_type_0 = datetime.datetime.fromisoformat(data)

                return sent_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        sent_dt = _parse_sent_dt(d.pop("sent_dt", UNSET))

        score = cls(
            user_id=user_id,
            business_id=business_id,
            value=value,
            category=category,
            num_visits=num_visits,
            notification_id=notification_id,
            sent_dt=sent_dt,
        )

        score.additional_properties = d
        return score

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
