from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Photo")


@_attrs_define
class Photo:
    """
    Attributes:
        id (int):
        image (str | Unset):
        thumbnail (None | str | Unset):
        bb_image (None | str | Unset):
        bb_thumbnail (None | str | Unset):
        description (None | str | Unset):
        order (int | Unset):
        favorite_dish (None | str | Unset):
        created_dt (datetime.datetime | Unset):
        status (str | Unset):
        likes (list[UUID] | Unset):
        user (UUID | Unset):
        business (int | Unset):
    """

    id: int
    image: str | Unset = UNSET
    thumbnail: None | str | Unset = UNSET
    bb_image: None | str | Unset = UNSET
    bb_thumbnail: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    order: int | Unset = UNSET
    favorite_dish: None | str | Unset = UNSET
    created_dt: datetime.datetime | Unset = UNSET
    status: str | Unset = UNSET
    likes: list[UUID] | Unset = UNSET
    user: UUID | Unset = UNSET
    business: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        image = self.image

        thumbnail: None | str | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

        bb_image: None | str | Unset
        if isinstance(self.bb_image, Unset):
            bb_image = UNSET
        else:
            bb_image = self.bb_image

        bb_thumbnail: None | str | Unset
        if isinstance(self.bb_thumbnail, Unset):
            bb_thumbnail = UNSET
        else:
            bb_thumbnail = self.bb_thumbnail

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        order = self.order

        favorite_dish: None | str | Unset
        if isinstance(self.favorite_dish, Unset):
            favorite_dish = UNSET
        else:
            favorite_dish = self.favorite_dish

        created_dt: str | Unset = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        status = self.status

        likes: list[str] | Unset = UNSET
        if not isinstance(self.likes, Unset):
            likes = []
            for likes_item_data in self.likes:
                likes_item = str(likes_item_data)
                likes.append(likes_item)

        user: str | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = str(self.user)

        business = self.business

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if image is not UNSET:
            field_dict["image"] = image
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if bb_image is not UNSET:
            field_dict["bb_image"] = bb_image
        if bb_thumbnail is not UNSET:
            field_dict["bb_thumbnail"] = bb_thumbnail
        if description is not UNSET:
            field_dict["description"] = description
        if order is not UNSET:
            field_dict["order"] = order
        if favorite_dish is not UNSET:
            field_dict["favorite_dish"] = favorite_dish
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if status is not UNSET:
            field_dict["status"] = status
        if likes is not UNSET:
            field_dict["likes"] = likes
        if user is not UNSET:
            field_dict["user"] = user
        if business is not UNSET:
            field_dict["business"] = business

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        image = d.pop("image", UNSET)

        def _parse_thumbnail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))

        def _parse_bb_image(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bb_image = _parse_bb_image(d.pop("bb_image", UNSET))

        def _parse_bb_thumbnail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bb_thumbnail = _parse_bb_thumbnail(d.pop("bb_thumbnail", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        order = d.pop("order", UNSET)

        def _parse_favorite_dish(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        favorite_dish = _parse_favorite_dish(d.pop("favorite_dish", UNSET))

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime | Unset
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = datetime.datetime.fromisoformat(_created_dt)

        status = d.pop("status", UNSET)

        _likes = d.pop("likes", UNSET)
        likes: list[UUID] | Unset = UNSET
        if _likes is not UNSET:
            likes = []
            for likes_item_data in _likes:
                likes_item = UUID(likes_item_data)

                likes.append(likes_item)

        _user = d.pop("user", UNSET)
        user: UUID | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UUID(_user)

        business = d.pop("business", UNSET)

        photo = cls(
            id=id,
            image=image,
            thumbnail=thumbnail,
            bb_image=bb_image,
            bb_thumbnail=bb_thumbnail,
            description=description,
            order=order,
            favorite_dish=favorite_dish,
            created_dt=created_dt,
            status=status,
            likes=likes,
            user=user,
            business=business,
        )

        photo.additional_properties = d
        return photo

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
