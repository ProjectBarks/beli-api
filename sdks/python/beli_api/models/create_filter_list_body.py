from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_filter_list_body_bounds_type_0 import CreateFilterListBodyBoundsType0
    from ..models.create_filter_list_body_filters_item import CreateFilterListBodyFiltersItem


T = TypeVar("T", bound="CreateFilterListBody")


@_attrs_define
class CreateFilterListBody:
    """
    Attributes:
        filters (list[CreateFilterListBodyFiltersItem] | Unset):
        list_field (str | Unset):
        user (str | Unset):
        user2 (str | Unset):
        category (str | Unset):
        bounds (CreateFilterListBodyBoundsType0 | None | Unset):
        sort_method (str | Unset):
        coords (str | Unset):
        ids (list[int] | Unset):
    """

    filters: list[CreateFilterListBodyFiltersItem] | Unset = UNSET
    list_field: str | Unset = UNSET
    user: str | Unset = UNSET
    user2: str | Unset = UNSET
    category: str | Unset = UNSET
    bounds: CreateFilterListBodyBoundsType0 | None | Unset = UNSET
    sort_method: str | Unset = UNSET
    coords: str | Unset = UNSET
    ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_filter_list_body_bounds_type_0 import CreateFilterListBodyBoundsType0

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        list_field = self.list_field

        user = self.user

        user2 = self.user2

        category = self.category

        bounds: dict[str, Any] | None | Unset
        if isinstance(self.bounds, Unset):
            bounds = UNSET
        elif isinstance(self.bounds, CreateFilterListBodyBoundsType0):
            bounds = self.bounds.to_dict()
        else:
            bounds = self.bounds

        sort_method = self.sort_method

        coords = self.coords

        ids: list[int] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filters is not UNSET:
            field_dict["filters"] = filters
        if list_field is not UNSET:
            field_dict["list_field"] = list_field
        if user is not UNSET:
            field_dict["user"] = user
        if user2 is not UNSET:
            field_dict["user2"] = user2
        if category is not UNSET:
            field_dict["category"] = category
        if bounds is not UNSET:
            field_dict["bounds"] = bounds
        if sort_method is not UNSET:
            field_dict["sort_method"] = sort_method
        if coords is not UNSET:
            field_dict["coords"] = coords
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_filter_list_body_bounds_type_0 import CreateFilterListBodyBoundsType0
        from ..models.create_filter_list_body_filters_item import CreateFilterListBodyFiltersItem

        d = dict(src_dict)
        _filters = d.pop("filters", UNSET)
        filters: list[CreateFilterListBodyFiltersItem] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = CreateFilterListBodyFiltersItem.from_dict(filters_item_data)

                filters.append(filters_item)

        list_field = d.pop("list_field", UNSET)

        user = d.pop("user", UNSET)

        user2 = d.pop("user2", UNSET)

        category = d.pop("category", UNSET)

        def _parse_bounds(data: object) -> CreateFilterListBodyBoundsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bounds_type_0 = CreateFilterListBodyBoundsType0.from_dict(data)

                return bounds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateFilterListBodyBoundsType0 | None | Unset, data)

        bounds = _parse_bounds(d.pop("bounds", UNSET))

        sort_method = d.pop("sort_method", UNSET)

        coords = d.pop("coords", UNSET)

        ids = cast(list[int], d.pop("ids", UNSET))

        create_filter_list_body = cls(
            filters=filters,
            list_field=list_field,
            user=user,
            user2=user2,
            category=category,
            bounds=bounds,
            sort_method=sort_method,
            coords=coords,
            ids=ids,
        )

        create_filter_list_body.additional_properties = d
        return create_filter_list_body

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
