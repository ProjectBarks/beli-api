from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PublishedListChallengeInfoType0")


@_attrs_define
class PublishedListChallengeInfoType0:
    """
    Attributes:
        is_joined (bool | Unset):
        progress (float | Unset):
        total (float | Unset):
        participant_count (int | Unset):
    """

    is_joined: bool | Unset = UNSET
    progress: float | Unset = UNSET
    total: float | Unset = UNSET
    participant_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_joined = self.is_joined

        progress = self.progress

        total = self.total

        participant_count = self.participant_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_joined is not UNSET:
            field_dict["is_joined"] = is_joined
        if progress is not UNSET:
            field_dict["progress"] = progress
        if total is not UNSET:
            field_dict["total"] = total
        if participant_count is not UNSET:
            field_dict["participant_count"] = participant_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_joined = d.pop("is_joined", UNSET)

        progress = d.pop("progress", UNSET)

        total = d.pop("total", UNSET)

        participant_count = d.pop("participant_count", UNSET)

        published_list_challenge_info_type_0 = cls(
            is_joined=is_joined,
            progress=progress,
            total=total,
            participant_count=participant_count,
        )

        published_list_challenge_info_type_0.additional_properties = d
        return published_list_challenge_info_type_0

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
