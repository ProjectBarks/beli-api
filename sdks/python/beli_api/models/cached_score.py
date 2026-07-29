from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CachedScore")


@_attrs_define
class CachedScore:
    """
    Attributes:
        user_id (UUID | Unset):
        business_id (int | Unset):
        value (float | Unset):
        category (str | Unset):
        labels (list[str] | Unset):
    """

    user_id: UUID | Unset = UNSET
    business_id: int | Unset = UNSET
    value: float | Unset = UNSET
    category: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        business_id = self.business_id

        value = self.value

        category = self.category

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

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
        if labels is not UNSET:
            field_dict["labels"] = labels

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

        labels = cast(list[str], d.pop("labels", UNSET))

        cached_score = cls(
            user_id=user_id,
            business_id=business_id,
            value=value,
            category=category,
            labels=labels,
        )

        cached_score.additional_properties = d
        return cached_score

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
