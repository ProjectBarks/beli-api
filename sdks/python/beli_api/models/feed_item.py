from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business import Business


T = TypeVar("T", bound="FeedItem")


@_attrs_define
class FeedItem:
    """
    Attributes:
        id (int):
        event_type (str | Unset): e.g. ADD, BOOKMARK, … (not exhaustively observed)
        sent_dt (datetime.datetime | Unset):
        user1 (UUID | Unset):
        title (None | str | Unset):
        body (None | str | Unset):
        business (int | Unset):
        category (None | str | Unset):
        score (float | None | Unset):
        num_visits (int | None | Unset):
        business_full (Business | Unset):
    """

    id: int
    event_type: str | Unset = UNSET
    sent_dt: datetime.datetime | Unset = UNSET
    user1: UUID | Unset = UNSET
    title: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    business: int | Unset = UNSET
    category: None | str | Unset = UNSET
    score: float | None | Unset = UNSET
    num_visits: int | None | Unset = UNSET
    business_full: Business | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event_type = self.event_type

        sent_dt: str | Unset = UNSET
        if not isinstance(self.sent_dt, Unset):
            sent_dt = self.sent_dt.isoformat()

        user1: str | Unset = UNSET
        if not isinstance(self.user1, Unset):
            user1 = str(self.user1)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        business = self.business

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        num_visits: int | None | Unset
        if isinstance(self.num_visits, Unset):
            num_visits = UNSET
        else:
            num_visits = self.num_visits

        business_full: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_full, Unset):
            business_full = self.business_full.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if sent_dt is not UNSET:
            field_dict["sent_dt"] = sent_dt
        if user1 is not UNSET:
            field_dict["user1"] = user1
        if title is not UNSET:
            field_dict["title"] = title
        if body is not UNSET:
            field_dict["body"] = body
        if business is not UNSET:
            field_dict["business"] = business
        if category is not UNSET:
            field_dict["category"] = category
        if score is not UNSET:
            field_dict["score"] = score
        if num_visits is not UNSET:
            field_dict["num_visits"] = num_visits
        if business_full is not UNSET:
            field_dict["business_full"] = business_full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business import Business

        d = dict(src_dict)
        id = d.pop("id")

        event_type = d.pop("event_type", UNSET)

        _sent_dt = d.pop("sent_dt", UNSET)
        sent_dt: datetime.datetime | Unset
        if isinstance(_sent_dt, Unset):
            sent_dt = UNSET
        else:
            sent_dt = datetime.datetime.fromisoformat(_sent_dt)

        _user1 = d.pop("user1", UNSET)
        user1: UUID | Unset
        if isinstance(_user1, Unset):
            user1 = UNSET
        else:
            user1 = UUID(_user1)

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        business = d.pop("business", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_num_visits(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        num_visits = _parse_num_visits(d.pop("num_visits", UNSET))

        _business_full = d.pop("business_full", UNSET)
        business_full: Business | Unset
        if isinstance(_business_full, Unset):
            business_full = UNSET
        else:
            business_full = Business.from_dict(_business_full)

        feed_item = cls(
            id=id,
            event_type=event_type,
            sent_dt=sent_dt,
            user1=user1,
            title=title,
            body=body,
            business=business,
            category=category,
            score=score,
            num_visits=num_visits,
            business_full=business_full,
        )

        feed_item.additional_properties = d
        return feed_item

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
