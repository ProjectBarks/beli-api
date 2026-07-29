from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field import Field


T = TypeVar("T", bound="UserSetting")


@_attrs_define
class UserSetting:
    """
    Attributes:
        user (UUID | Unset):
        field (Field | Unset):
        value (Any | Unset):
        start_dt (datetime.datetime | None | Unset):
        end_dt (datetime.datetime | None | Unset):
    """

    user: UUID | Unset = UNSET
    field: Field | Unset = UNSET
    value: Any | Unset = UNSET
    start_dt: datetime.datetime | None | Unset = UNSET
    end_dt: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user: str | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = str(self.user)

        field: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field, Unset):
            field = self.field.to_dict()

        value = self.value

        start_dt: None | str | Unset
        if isinstance(self.start_dt, Unset):
            start_dt = UNSET
        elif isinstance(self.start_dt, datetime.datetime):
            start_dt = self.start_dt.isoformat()
        else:
            start_dt = self.start_dt

        end_dt: None | str | Unset
        if isinstance(self.end_dt, Unset):
            end_dt = UNSET
        elif isinstance(self.end_dt, datetime.datetime):
            end_dt = self.end_dt.isoformat()
        else:
            end_dt = self.end_dt

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if field is not UNSET:
            field_dict["field"] = field
        if value is not UNSET:
            field_dict["value"] = value
        if start_dt is not UNSET:
            field_dict["start_dt"] = start_dt
        if end_dt is not UNSET:
            field_dict["end_dt"] = end_dt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.field import Field

        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: UUID | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UUID(_user)

        _field = d.pop("field", UNSET)
        field: Field | Unset
        if isinstance(_field, Unset):
            field = UNSET
        else:
            field = Field.from_dict(_field)

        value = d.pop("value", UNSET)

        def _parse_start_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_dt_type_0 = datetime.datetime.fromisoformat(data)

                return start_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_dt = _parse_start_dt(d.pop("start_dt", UNSET))

        def _parse_end_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_dt_type_0 = datetime.datetime.fromisoformat(data)

                return end_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_dt = _parse_end_dt(d.pop("end_dt", UNSET))

        user_setting = cls(
            user=user,
            field=field,
            value=value,
            start_dt=start_dt,
            end_dt=end_dt,
        )

        user_setting.additional_properties = d
        return user_setting

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
