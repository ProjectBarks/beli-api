from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_ranking_response_results import AddRankingResponseResults


T = TypeVar("T", bound="AddRankingResponse")


@_attrs_define
class AddRankingResponse:
    """
    Attributes:
        results (AddRankingResponseResults | Unset):
        feed_item_id (int | None | Unset):
        score (float | None | Unset):
    """

    results: AddRankingResponseResults | Unset = UNSET
    feed_item_id: int | None | Unset = UNSET
    score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results: dict[str, Any] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

        feed_item_id: int | None | Unset
        if isinstance(self.feed_item_id, Unset):
            feed_item_id = UNSET
        else:
            feed_item_id = self.feed_item_id

        score: float | None | Unset
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results
        if feed_item_id is not UNSET:
            field_dict["feed_item_id"] = feed_item_id
        if score is not UNSET:
            field_dict["score"] = score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_ranking_response_results import AddRankingResponseResults

        d = dict(src_dict)
        _results = d.pop("results", UNSET)
        results: AddRankingResponseResults | Unset
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = AddRankingResponseResults.from_dict(_results)

        def _parse_feed_item_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        feed_item_id = _parse_feed_item_id(d.pop("feed_item_id", UNSET))

        def _parse_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        score = _parse_score(d.pop("score", UNSET))

        add_ranking_response = cls(
            results=results,
            feed_item_id=feed_item_id,
            score=score,
        )

        add_ranking_response.additional_properties = d
        return add_ranking_response

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
