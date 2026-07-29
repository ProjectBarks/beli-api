from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserBody")


@_attrs_define
class UpdateUserBody:
    """
    Attributes:
        fcm_token (None | str | Unset):
        live_activity_token (None | str | Unset):
        sessions (Any | Unset):
        last_login (datetime.datetime | None | Unset):
        version (None | str | Unset):
    """

    fcm_token: None | str | Unset = UNSET
    live_activity_token: None | str | Unset = UNSET
    sessions: Any | Unset = UNSET
    last_login: datetime.datetime | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fcm_token: None | str | Unset
        if isinstance(self.fcm_token, Unset):
            fcm_token = UNSET
        else:
            fcm_token = self.fcm_token

        live_activity_token: None | str | Unset
        if isinstance(self.live_activity_token, Unset):
            live_activity_token = UNSET
        else:
            live_activity_token = self.live_activity_token

        sessions = self.sessions

        last_login: None | str | Unset
        if isinstance(self.last_login, Unset):
            last_login = UNSET
        elif isinstance(self.last_login, datetime.datetime):
            last_login = self.last_login.isoformat()
        else:
            last_login = self.last_login

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fcm_token is not UNSET:
            field_dict["fcm_token"] = fcm_token
        if live_activity_token is not UNSET:
            field_dict["live_activity_token"] = live_activity_token
        if sessions is not UNSET:
            field_dict["sessions"] = sessions
        if last_login is not UNSET:
            field_dict["last_login"] = last_login
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_fcm_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fcm_token = _parse_fcm_token(d.pop("fcm_token", UNSET))

        def _parse_live_activity_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        live_activity_token = _parse_live_activity_token(d.pop("live_activity_token", UNSET))

        sessions = d.pop("sessions", UNSET)

        def _parse_last_login(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_login_type_0 = datetime.datetime.fromisoformat(data)

                return last_login_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_login = _parse_last_login(d.pop("last_login", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        update_user_body = cls(
            fcm_token=fcm_token,
            live_activity_token=live_activity_token,
            sessions=sessions,
            last_login=last_login,
            version=version,
        )

        update_user_body.additional_properties = d
        return update_user_body

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
