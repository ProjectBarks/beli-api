from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserExtended")


@_attrs_define
class UserExtended:
    """Extended profile shape returned by self/detail endpoints (adds contact + onboarding fields on top of the base User
    shape).

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
            phone_no (None | str | Unset):
            email (None | str | Unset):
            home_city (None | str | Unset):
            bio (None | str | Unset):
            referrer (Any | Unset):
            referral_link (None | str | Unset):
            sessions (Any | Unset):
            reservation_priority (Any | Unset):
            qr_code (None | str | Unset):
            following (bool | None | Unset): Present (bool) only in search-result contexts.
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
    phone_no: None | str | Unset = UNSET
    email: None | str | Unset = UNSET
    home_city: None | str | Unset = UNSET
    bio: None | str | Unset = UNSET
    referrer: Any | Unset = UNSET
    referral_link: None | str | Unset = UNSET
    sessions: Any | Unset = UNSET
    reservation_priority: Any | Unset = UNSET
    qr_code: None | str | Unset = UNSET
    following: bool | None | Unset = UNSET
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

        phone_no: None | str | Unset
        if isinstance(self.phone_no, Unset):
            phone_no = UNSET
        else:
            phone_no = self.phone_no

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        home_city: None | str | Unset
        if isinstance(self.home_city, Unset):
            home_city = UNSET
        else:
            home_city = self.home_city

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio

        referrer = self.referrer

        referral_link: None | str | Unset
        if isinstance(self.referral_link, Unset):
            referral_link = UNSET
        else:
            referral_link = self.referral_link

        sessions = self.sessions

        reservation_priority = self.reservation_priority

        qr_code: None | str | Unset
        if isinstance(self.qr_code, Unset):
            qr_code = UNSET
        else:
            qr_code = self.qr_code

        following: bool | None | Unset
        if isinstance(self.following, Unset):
            following = UNSET
        else:
            following = self.following

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
        if phone_no is not UNSET:
            field_dict["phone_no"] = phone_no
        if email is not UNSET:
            field_dict["email"] = email
        if home_city is not UNSET:
            field_dict["home_city"] = home_city
        if bio is not UNSET:
            field_dict["bio"] = bio
        if referrer is not UNSET:
            field_dict["referrer"] = referrer
        if referral_link is not UNSET:
            field_dict["referral_link"] = referral_link
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if reservation_priority is not UNSET:
            field_dict["reservation_priority"] = reservation_priority
        if qr_code is not UNSET:
            field_dict["qr_code"] = qr_code
        if following is not UNSET:
            field_dict["following"] = following

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

        def _parse_phone_no(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_no = _parse_phone_no(d.pop("phone_no", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_home_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        home_city = _parse_home_city(d.pop("home_city", UNSET))

        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))

        referrer = d.pop("referrer", UNSET)

        def _parse_referral_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_link = _parse_referral_link(d.pop("referral_link", UNSET))

        sessions = d.pop("sessions", UNSET)

        reservation_priority = d.pop("reservation_priority", UNSET)

        def _parse_qr_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        qr_code = _parse_qr_code(d.pop("qr_code", UNSET))

        def _parse_following(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        following = _parse_following(d.pop("following", UNSET))

        user_extended = cls(
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
            phone_no=phone_no,
            email=email,
            home_city=home_city,
            bio=bio,
            referrer=referrer,
            referral_link=referral_link,
            sessions=sessions,
            reservation_priority=reservation_priority,
            qr_code=qr_code,
            following=following,
        )

        user_extended.additional_properties = d
        return user_extended

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
