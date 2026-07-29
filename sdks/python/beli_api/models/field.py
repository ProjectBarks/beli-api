from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Field")


@_attrs_define
class Field:
    """
    Attributes:
        id (int):
        name (str):
        display (None | str | Unset):
        table (None | str | Unset):
        category (None | str | Unset):
        is_filter (bool | Unset):
    """

    id: int
    name: str
    display: None | str | Unset = UNSET
    table: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    is_filter: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        display: None | str | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        else:
            display = self.display

        table: None | str | Unset
        if isinstance(self.table, Unset):
            table = UNSET
        else:
            table = self.table

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_filter = self.is_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if display is not UNSET:
            field_dict["display"] = display
        if table is not UNSET:
            field_dict["table"] = table
        if category is not UNSET:
            field_dict["category"] = category
        if is_filter is not UNSET:
            field_dict["is_filter"] = is_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_table(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table = _parse_table(d.pop("table", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        is_filter = d.pop("is_filter", UNSET)

        field = cls(
            id=id,
            name=name,
            display=display,
            table=table,
            category=category,
            is_filter=is_filter,
        )

        field.additional_properties = d
        return field

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
