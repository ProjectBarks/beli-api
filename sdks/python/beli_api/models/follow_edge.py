from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.follow_edge_status import FollowEdgeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="FollowEdge")


@_attrs_define
class FollowEdge:
    """
    Attributes:
        id (int):
        status (FollowEdgeStatus):
        request_dt (datetime.datetime | None | Unset):
        accept_dt (datetime.datetime | None | Unset):
        unfollow_dt (datetime.datetime | None | Unset):
        unaccept_dt (datetime.datetime | None | Unset):
        follower (UUID | Unset):
        followed (UUID | Unset):
    """

    id: int
    status: FollowEdgeStatus
    request_dt: datetime.datetime | None | Unset = UNSET
    accept_dt: datetime.datetime | None | Unset = UNSET
    unfollow_dt: datetime.datetime | None | Unset = UNSET
    unaccept_dt: datetime.datetime | None | Unset = UNSET
    follower: UUID | Unset = UNSET
    followed: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        request_dt: None | str | Unset
        if isinstance(self.request_dt, Unset):
            request_dt = UNSET
        elif isinstance(self.request_dt, datetime.datetime):
            request_dt = self.request_dt.isoformat()
        else:
            request_dt = self.request_dt

        accept_dt: None | str | Unset
        if isinstance(self.accept_dt, Unset):
            accept_dt = UNSET
        elif isinstance(self.accept_dt, datetime.datetime):
            accept_dt = self.accept_dt.isoformat()
        else:
            accept_dt = self.accept_dt

        unfollow_dt: None | str | Unset
        if isinstance(self.unfollow_dt, Unset):
            unfollow_dt = UNSET
        elif isinstance(self.unfollow_dt, datetime.datetime):
            unfollow_dt = self.unfollow_dt.isoformat()
        else:
            unfollow_dt = self.unfollow_dt

        unaccept_dt: None | str | Unset
        if isinstance(self.unaccept_dt, Unset):
            unaccept_dt = UNSET
        elif isinstance(self.unaccept_dt, datetime.datetime):
            unaccept_dt = self.unaccept_dt.isoformat()
        else:
            unaccept_dt = self.unaccept_dt

        follower: str | Unset = UNSET
        if not isinstance(self.follower, Unset):
            follower = str(self.follower)

        followed: str | Unset = UNSET
        if not isinstance(self.followed, Unset):
            followed = str(self.followed)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
            }
        )
        if request_dt is not UNSET:
            field_dict["request_dt"] = request_dt
        if accept_dt is not UNSET:
            field_dict["accept_dt"] = accept_dt
        if unfollow_dt is not UNSET:
            field_dict["unfollow_dt"] = unfollow_dt
        if unaccept_dt is not UNSET:
            field_dict["unaccept_dt"] = unaccept_dt
        if follower is not UNSET:
            field_dict["follower"] = follower
        if followed is not UNSET:
            field_dict["followed"] = followed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = FollowEdgeStatus(d.pop("status"))

        def _parse_request_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                request_dt_type_0 = datetime.datetime.fromisoformat(data)

                return request_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        request_dt = _parse_request_dt(d.pop("request_dt", UNSET))

        def _parse_accept_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accept_dt_type_0 = datetime.datetime.fromisoformat(data)

                return accept_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        accept_dt = _parse_accept_dt(d.pop("accept_dt", UNSET))

        def _parse_unfollow_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unfollow_dt_type_0 = datetime.datetime.fromisoformat(data)

                return unfollow_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        unfollow_dt = _parse_unfollow_dt(d.pop("unfollow_dt", UNSET))

        def _parse_unaccept_dt(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unaccept_dt_type_0 = datetime.datetime.fromisoformat(data)

                return unaccept_dt_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        unaccept_dt = _parse_unaccept_dt(d.pop("unaccept_dt", UNSET))

        _follower = d.pop("follower", UNSET)
        follower: UUID | Unset
        if isinstance(_follower, Unset):
            follower = UNSET
        else:
            follower = UUID(_follower)

        _followed = d.pop("followed", UNSET)
        followed: UUID | Unset
        if isinstance(_followed, Unset):
            followed = UNSET
        else:
            followed = UUID(_followed)

        follow_edge = cls(
            id=id,
            status=status,
            request_dt=request_dt,
            accept_dt=accept_dt,
            unfollow_dt=unfollow_dt,
            unaccept_dt=unaccept_dt,
            follower=follower,
            followed=followed,
        )

        follow_edge.additional_properties = d
        return follow_edge

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
