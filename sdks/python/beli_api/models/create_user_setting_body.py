from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateUserSettingBody")


@_attrs_define
class CreateUserSettingBody:
    """
    Attributes:
        user (UUID):
        field_name (str):
        value (Any):
    """

    user: UUID
    field_name: str
    value: Any
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = str(self.user)

        field_name = self.field_name

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "field_name": field_name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user = UUID(d.pop("user"))

        field_name = d.pop("field_name")

        value = d.pop("value")

        create_user_setting_body = cls(
            user=user,
            field_name=field_name,
            value=value,
        )

        create_user_setting_body.additional_properties = d
        return create_user_setting_body

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
