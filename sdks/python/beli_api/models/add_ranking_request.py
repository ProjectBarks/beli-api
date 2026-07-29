from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddRankingRequest")


@_attrs_define
class AddRankingRequest:
    """
    Attributes:
        category (str):
        user_id (UUID):
        business_id (int):
        value (float | None | Unset):
        tagged_users (list[UUID] | Unset):
        local_datetime (datetime.datetime | Unset):
        utc_offset (int | Unset):
        visit_dates (list[datetime.date] | Unset):
        visit_date_on_rank (datetime.date | None | Unset):
        rank_button_source (None | str | Unset):
        overall_rank_count (int | Unset):
        version_supports_multi_category (bool | Unset):
        has_access_multi_category (bool | Unset):
        supports_featured_list_challenges (bool | Unset):
    """

    category: str
    user_id: UUID
    business_id: int
    value: float | None | Unset = UNSET
    tagged_users: list[UUID] | Unset = UNSET
    local_datetime: datetime.datetime | Unset = UNSET
    utc_offset: int | Unset = UNSET
    visit_dates: list[datetime.date] | Unset = UNSET
    visit_date_on_rank: datetime.date | None | Unset = UNSET
    rank_button_source: None | str | Unset = UNSET
    overall_rank_count: int | Unset = UNSET
    version_supports_multi_category: bool | Unset = UNSET
    has_access_multi_category: bool | Unset = UNSET
    supports_featured_list_challenges: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        user_id = str(self.user_id)

        business_id = self.business_id

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        tagged_users: list[str] | Unset = UNSET
        if not isinstance(self.tagged_users, Unset):
            tagged_users = []
            for tagged_users_item_data in self.tagged_users:
                tagged_users_item = str(tagged_users_item_data)
                tagged_users.append(tagged_users_item)

        local_datetime: str | Unset = UNSET
        if not isinstance(self.local_datetime, Unset):
            local_datetime = self.local_datetime.isoformat()

        utc_offset = self.utc_offset

        visit_dates: list[str] | Unset = UNSET
        if not isinstance(self.visit_dates, Unset):
            visit_dates = []
            for visit_dates_item_data in self.visit_dates:
                visit_dates_item = visit_dates_item_data.isoformat()
                visit_dates.append(visit_dates_item)

        visit_date_on_rank: None | str | Unset
        if isinstance(self.visit_date_on_rank, Unset):
            visit_date_on_rank = UNSET
        elif isinstance(self.visit_date_on_rank, datetime.date):
            visit_date_on_rank = self.visit_date_on_rank.isoformat()
        else:
            visit_date_on_rank = self.visit_date_on_rank

        rank_button_source: None | str | Unset
        if isinstance(self.rank_button_source, Unset):
            rank_button_source = UNSET
        else:
            rank_button_source = self.rank_button_source

        overall_rank_count = self.overall_rank_count

        version_supports_multi_category = self.version_supports_multi_category

        has_access_multi_category = self.has_access_multi_category

        supports_featured_list_challenges = self.supports_featured_list_challenges

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "user_id": user_id,
                "business_id": business_id,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if tagged_users is not UNSET:
            field_dict["tagged_users"] = tagged_users
        if local_datetime is not UNSET:
            field_dict["local_datetime"] = local_datetime
        if utc_offset is not UNSET:
            field_dict["utc_offset"] = utc_offset
        if visit_dates is not UNSET:
            field_dict["visit_dates"] = visit_dates
        if visit_date_on_rank is not UNSET:
            field_dict["visit_date_on_rank"] = visit_date_on_rank
        if rank_button_source is not UNSET:
            field_dict["rank_button_source"] = rank_button_source
        if overall_rank_count is not UNSET:
            field_dict["overall_rank_count"] = overall_rank_count
        if version_supports_multi_category is not UNSET:
            field_dict["version_supports_multi_category"] = version_supports_multi_category
        if has_access_multi_category is not UNSET:
            field_dict["has_access_multi_category"] = has_access_multi_category
        if supports_featured_list_challenges is not UNSET:
            field_dict["supports_featured_list_challenges"] = supports_featured_list_challenges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        user_id = UUID(d.pop("user_id"))

        business_id = d.pop("business_id")

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        _tagged_users = d.pop("tagged_users", UNSET)
        tagged_users: list[UUID] | Unset = UNSET
        if _tagged_users is not UNSET:
            tagged_users = []
            for tagged_users_item_data in _tagged_users:
                tagged_users_item = UUID(tagged_users_item_data)

                tagged_users.append(tagged_users_item)

        _local_datetime = d.pop("local_datetime", UNSET)
        local_datetime: datetime.datetime | Unset
        if isinstance(_local_datetime, Unset):
            local_datetime = UNSET
        else:
            local_datetime = datetime.datetime.fromisoformat(_local_datetime)

        utc_offset = d.pop("utc_offset", UNSET)

        _visit_dates = d.pop("visit_dates", UNSET)
        visit_dates: list[datetime.date] | Unset = UNSET
        if _visit_dates is not UNSET:
            visit_dates = []
            for visit_dates_item_data in _visit_dates:
                visit_dates_item = datetime.date.fromisoformat(visit_dates_item_data)

                visit_dates.append(visit_dates_item)

        def _parse_visit_date_on_rank(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                visit_date_on_rank_type_0 = datetime.date.fromisoformat(data)

                return visit_date_on_rank_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        visit_date_on_rank = _parse_visit_date_on_rank(d.pop("visit_date_on_rank", UNSET))

        def _parse_rank_button_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rank_button_source = _parse_rank_button_source(d.pop("rank_button_source", UNSET))

        overall_rank_count = d.pop("overall_rank_count", UNSET)

        version_supports_multi_category = d.pop("version_supports_multi_category", UNSET)

        has_access_multi_category = d.pop("has_access_multi_category", UNSET)

        supports_featured_list_challenges = d.pop("supports_featured_list_challenges", UNSET)

        add_ranking_request = cls(
            category=category,
            user_id=user_id,
            business_id=business_id,
            value=value,
            tagged_users=tagged_users,
            local_datetime=local_datetime,
            utc_offset=utc_offset,
            visit_dates=visit_dates,
            visit_date_on_rank=visit_date_on_rank,
            rank_button_source=rank_button_source,
            overall_rank_count=overall_rank_count,
            version_supports_multi_category=version_supports_multi_category,
            has_access_multi_category=has_access_multi_category,
            supports_featured_list_challenges=supports_featured_list_challenges,
        )

        add_ranking_request.additional_properties = d
        return add_ranking_request

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
