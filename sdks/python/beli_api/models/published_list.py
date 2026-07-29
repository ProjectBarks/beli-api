from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.published_list_challenge_info_type_0 import PublishedListChallengeInfoType0


T = TypeVar("T", bound="PublishedList")


@_attrs_define
class PublishedList:
    """
    Attributes:
        id (int):
        title (str):
        description (None | str | Unset):
        cover_photo (Any | Unset):
        ranked (bool | Unset):
        category (None | str | Unset):
        quick_link (None | str | Unset):
        challenge_info (None | PublishedListChallengeInfoType0 | Unset):
        status (str | Unset):
    """

    id: int
    title: str
    description: None | str | Unset = UNSET
    cover_photo: Any | Unset = UNSET
    ranked: bool | Unset = UNSET
    category: None | str | Unset = UNSET
    quick_link: None | str | Unset = UNSET
    challenge_info: None | PublishedListChallengeInfoType0 | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.published_list_challenge_info_type_0 import PublishedListChallengeInfoType0

        id = self.id

        title = self.title

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        cover_photo = self.cover_photo

        ranked = self.ranked

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        quick_link: None | str | Unset
        if isinstance(self.quick_link, Unset):
            quick_link = UNSET
        else:
            quick_link = self.quick_link

        challenge_info: dict[str, Any] | None | Unset
        if isinstance(self.challenge_info, Unset):
            challenge_info = UNSET
        elif isinstance(self.challenge_info, PublishedListChallengeInfoType0):
            challenge_info = self.challenge_info.to_dict()
        else:
            challenge_info = self.challenge_info

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if cover_photo is not UNSET:
            field_dict["cover_photo"] = cover_photo
        if ranked is not UNSET:
            field_dict["ranked"] = ranked
        if category is not UNSET:
            field_dict["category"] = category
        if quick_link is not UNSET:
            field_dict["quick_link"] = quick_link
        if challenge_info is not UNSET:
            field_dict["challenge_info"] = challenge_info
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.published_list_challenge_info_type_0 import PublishedListChallengeInfoType0

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        cover_photo = d.pop("cover_photo", UNSET)

        ranked = d.pop("ranked", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_quick_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_link = _parse_quick_link(d.pop("quick_link", UNSET))

        def _parse_challenge_info(data: object) -> None | PublishedListChallengeInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                challenge_info_type_0 = PublishedListChallengeInfoType0.from_dict(data)

                return challenge_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PublishedListChallengeInfoType0 | Unset, data)

        challenge_info = _parse_challenge_info(d.pop("challenge_info", UNSET))

        status = d.pop("status", UNSET)

        published_list = cls(
            id=id,
            title=title,
            description=description,
            cover_photo=cover_photo,
            ranked=ranked,
            category=category,
            quick_link=quick_link,
            challenge_info=challenge_info,
            status=status,
        )

        published_list.additional_properties = d
        return published_list

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
