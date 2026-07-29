from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """
    Attributes:
        id (UUID):
        username (str):
        first_name (str | Unset):
        last_name (str | Unset):
        full_name (str | Unset):
        created_dt (datetime.datetime | Unset):
        instagram_url (None | str | Unset):
        tiktok_url (None | str | Unset):
        photo (None | str | Unset):
        profile_photo (None | str | Unset):
        public (bool | Unset):
        school (None | str | Unset):
        company (None | str | Unset):
        has_supper_club (bool | Unset):
        has_vip (bool | Unset):
        is_playlist_eligible (bool | Unset):
    """

    id: UUID
    username: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    full_name: str | Unset = UNSET
    created_dt: datetime.datetime | Unset = UNSET
    instagram_url: None | str | Unset = UNSET
    tiktok_url: None | str | Unset = UNSET
    photo: None | str | Unset = UNSET
    profile_photo: None | str | Unset = UNSET
    public: bool | Unset = UNSET
    school: None | str | Unset = UNSET
    company: None | str | Unset = UNSET
    has_supper_club: bool | Unset = UNSET
    has_vip: bool | Unset = UNSET
    is_playlist_eligible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        full_name = self.full_name

        created_dt: str | Unset = UNSET
        if not isinstance(self.created_dt, Unset):
            created_dt = self.created_dt.isoformat()

        instagram_url: None | str | Unset
        if isinstance(self.instagram_url, Unset):
            instagram_url = UNSET
        else:
            instagram_url = self.instagram_url

        tiktok_url: None | str | Unset
        if isinstance(self.tiktok_url, Unset):
            tiktok_url = UNSET
        else:
            tiktok_url = self.tiktok_url

        photo: None | str | Unset
        if isinstance(self.photo, Unset):
            photo = UNSET
        else:
            photo = self.photo

        profile_photo: None | str | Unset
        if isinstance(self.profile_photo, Unset):
            profile_photo = UNSET
        else:
            profile_photo = self.profile_photo

        public = self.public

        school: None | str | Unset
        if isinstance(self.school, Unset):
            school = UNSET
        else:
            school = self.school

        company: None | str | Unset
        if isinstance(self.company, Unset):
            company = UNSET
        else:
            company = self.company

        has_supper_club = self.has_supper_club

        has_vip = self.has_vip

        is_playlist_eligible = self.is_playlist_eligible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if full_name is not UNSET:
            field_dict["full_name"] = full_name
        if created_dt is not UNSET:
            field_dict["created_dt"] = created_dt
        if instagram_url is not UNSET:
            field_dict["instagram_url"] = instagram_url
        if tiktok_url is not UNSET:
            field_dict["tiktok_url"] = tiktok_url
        if photo is not UNSET:
            field_dict["photo"] = photo
        if profile_photo is not UNSET:
            field_dict["profile_photo"] = profile_photo
        if public is not UNSET:
            field_dict["public"] = public
        if school is not UNSET:
            field_dict["school"] = school
        if company is not UNSET:
            field_dict["company"] = company
        if has_supper_club is not UNSET:
            field_dict["has_supper_club"] = has_supper_club
        if has_vip is not UNSET:
            field_dict["has_vip"] = has_vip
        if is_playlist_eligible is not UNSET:
            field_dict["is_playlist_eligible"] = is_playlist_eligible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        username = d.pop("username")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        full_name = d.pop("full_name", UNSET)

        _created_dt = d.pop("created_dt", UNSET)
        created_dt: datetime.datetime | Unset
        if isinstance(_created_dt, Unset):
            created_dt = UNSET
        else:
            created_dt = datetime.datetime.fromisoformat(_created_dt)

        def _parse_instagram_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instagram_url = _parse_instagram_url(d.pop("instagram_url", UNSET))

        def _parse_tiktok_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tiktok_url = _parse_tiktok_url(d.pop("tiktok_url", UNSET))

        def _parse_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo = _parse_photo(d.pop("photo", UNSET))

        def _parse_profile_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_photo = _parse_profile_photo(d.pop("profile_photo", UNSET))

        public = d.pop("public", UNSET)

        def _parse_school(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        school = _parse_school(d.pop("school", UNSET))

        def _parse_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company = _parse_company(d.pop("company", UNSET))

        has_supper_club = d.pop("has_supper_club", UNSET)

        has_vip = d.pop("has_vip", UNSET)

        is_playlist_eligible = d.pop("is_playlist_eligible", UNSET)

        user = cls(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            created_dt=created_dt,
            instagram_url=instagram_url,
            tiktok_url=tiktok_url,
            photo=photo,
            profile_photo=profile_photo,
            public=public,
            school=school,
            company=company,
            has_supper_club=has_supper_club,
            has_vip=has_vip,
            is_playlist_eligible=is_playlist_eligible,
        )

        user.additional_properties = d
        return user

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
