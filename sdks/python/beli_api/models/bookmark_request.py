from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookmarkRequest")


@_attrs_define
class BookmarkRequest:
    """Body for /api/add-bookmark/ and /api/remove-bookmark/. Verified live.

    Attributes:
        user_id (UUID):
        business_id (int):
        category (str | Unset): 3-letter category code, e.g. RES, DES, BAR
    """

    user_id: UUID
    business_id: int
    category: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = str(self.user_id)

        business_id = self.business_id

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "business_id": business_id,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = UUID(d.pop("user_id"))

        business_id = d.pop("business_id")

        category = d.pop("category", UNSET)

        bookmark_request = cls(
            user_id=user_id,
            business_id=business_id,
            category=category,
        )

        bookmark_request.additional_properties = d
        return bookmark_request

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
