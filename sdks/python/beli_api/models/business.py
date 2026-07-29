from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.business_business_hours_config import BusinessBusinessHoursConfig
    from ..models.business_businessdistinction_set_item import BusinessBusinessdistinctionSetItem
    from ..models.business_hours import BusinessHours


T = TypeVar("T", bound="Business")


@_attrs_define
class Business:
    """
    Attributes:
        id (int):
        name (str):
        place_id (None | str | Unset):
        status (str | Unset):
        city (None | str | Unset):
        borough (None | str | Unset):
        lat (float | Unset):
        lng (float | Unset):
        price (int | None | Unset):
        price_key (None | str | Unset):
        neighborhood (None | str | Unset):
        country (None | str | Unset):
        website (None | str | Unset):
        phone_number (None | str | Unset):
        cuisines (list[str] | Unset):
        default_category (None | str | Unset):
        quick_link (None | str | Unset):
        tz (None | str | Unset):
        has_cover_photo (bool | Unset):
        has_res_links (bool | Unset):
        has_delivery_links (bool | Unset):
        has_no_show_fee (bool | Unset):
        reservation_venue_id (int | None | Unset):
        businesshours_set (list[BusinessHours] | Unset):
        businessdistinction_set (list[BusinessBusinessdistinctionSetItem] | Unset): Shape not pinned down by reference
            §8.
        business_hours_config (BusinessBusinessHoursConfig | Unset): Shape not pinned down by reference §8.
    """

    id: int
    name: str
    place_id: None | str | Unset = UNSET
    status: str | Unset = UNSET
    city: None | str | Unset = UNSET
    borough: None | str | Unset = UNSET
    lat: float | Unset = UNSET
    lng: float | Unset = UNSET
    price: int | None | Unset = UNSET
    price_key: None | str | Unset = UNSET
    neighborhood: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    website: None | str | Unset = UNSET
    phone_number: None | str | Unset = UNSET
    cuisines: list[str] | Unset = UNSET
    default_category: None | str | Unset = UNSET
    quick_link: None | str | Unset = UNSET
    tz: None | str | Unset = UNSET
    has_cover_photo: bool | Unset = UNSET
    has_res_links: bool | Unset = UNSET
    has_delivery_links: bool | Unset = UNSET
    has_no_show_fee: bool | Unset = UNSET
    reservation_venue_id: int | None | Unset = UNSET
    businesshours_set: list[BusinessHours] | Unset = UNSET
    businessdistinction_set: list[BusinessBusinessdistinctionSetItem] | Unset = UNSET
    business_hours_config: BusinessBusinessHoursConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        place_id: None | str | Unset
        if isinstance(self.place_id, Unset):
            place_id = UNSET
        else:
            place_id = self.place_id

        status = self.status

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        borough: None | str | Unset
        if isinstance(self.borough, Unset):
            borough = UNSET
        else:
            borough = self.borough

        lat = self.lat

        lng = self.lng

        price: int | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        price_key: None | str | Unset
        if isinstance(self.price_key, Unset):
            price_key = UNSET
        else:
            price_key = self.price_key

        neighborhood: None | str | Unset
        if isinstance(self.neighborhood, Unset):
            neighborhood = UNSET
        else:
            neighborhood = self.neighborhood

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        phone_number: None | str | Unset
        if isinstance(self.phone_number, Unset):
            phone_number = UNSET
        else:
            phone_number = self.phone_number

        cuisines: list[str] | Unset = UNSET
        if not isinstance(self.cuisines, Unset):
            cuisines = self.cuisines

        default_category: None | str | Unset
        if isinstance(self.default_category, Unset):
            default_category = UNSET
        else:
            default_category = self.default_category

        quick_link: None | str | Unset
        if isinstance(self.quick_link, Unset):
            quick_link = UNSET
        else:
            quick_link = self.quick_link

        tz: None | str | Unset
        if isinstance(self.tz, Unset):
            tz = UNSET
        else:
            tz = self.tz

        has_cover_photo = self.has_cover_photo

        has_res_links = self.has_res_links

        has_delivery_links = self.has_delivery_links

        has_no_show_fee = self.has_no_show_fee

        reservation_venue_id: int | None | Unset
        if isinstance(self.reservation_venue_id, Unset):
            reservation_venue_id = UNSET
        else:
            reservation_venue_id = self.reservation_venue_id

        businesshours_set: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.businesshours_set, Unset):
            businesshours_set = []
            for businesshours_set_item_data in self.businesshours_set:
                businesshours_set_item = businesshours_set_item_data.to_dict()
                businesshours_set.append(businesshours_set_item)

        businessdistinction_set: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.businessdistinction_set, Unset):
            businessdistinction_set = []
            for businessdistinction_set_item_data in self.businessdistinction_set:
                businessdistinction_set_item = businessdistinction_set_item_data.to_dict()
                businessdistinction_set.append(businessdistinction_set_item)

        business_hours_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.business_hours_config, Unset):
            business_hours_config = self.business_hours_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
            }
        )
        if place_id is not UNSET:
            field_dict["place_id"] = place_id
        if status is not UNSET:
            field_dict["status"] = status
        if city is not UNSET:
            field_dict["city"] = city
        if borough is not UNSET:
            field_dict["borough"] = borough
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if price is not UNSET:
            field_dict["price"] = price
        if price_key is not UNSET:
            field_dict["price_key"] = price_key
        if neighborhood is not UNSET:
            field_dict["neighborhood"] = neighborhood
        if country is not UNSET:
            field_dict["country"] = country
        if website is not UNSET:
            field_dict["website"] = website
        if phone_number is not UNSET:
            field_dict["phone_number"] = phone_number
        if cuisines is not UNSET:
            field_dict["cuisines"] = cuisines
        if default_category is not UNSET:
            field_dict["default_category"] = default_category
        if quick_link is not UNSET:
            field_dict["quick_link"] = quick_link
        if tz is not UNSET:
            field_dict["tz"] = tz
        if has_cover_photo is not UNSET:
            field_dict["has_cover_photo"] = has_cover_photo
        if has_res_links is not UNSET:
            field_dict["has_res_links"] = has_res_links
        if has_delivery_links is not UNSET:
            field_dict["has_delivery_links"] = has_delivery_links
        if has_no_show_fee is not UNSET:
            field_dict["has_no_show_fee"] = has_no_show_fee
        if reservation_venue_id is not UNSET:
            field_dict["reservation_venue_id"] = reservation_venue_id
        if businesshours_set is not UNSET:
            field_dict["businesshours_set"] = businesshours_set
        if businessdistinction_set is not UNSET:
            field_dict["businessdistinction_set"] = businessdistinction_set
        if business_hours_config is not UNSET:
            field_dict["businessHoursConfig"] = business_hours_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.business_business_hours_config import BusinessBusinessHoursConfig
        from ..models.business_businessdistinction_set_item import BusinessBusinessdistinctionSetItem
        from ..models.business_hours import BusinessHours

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_place_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        place_id = _parse_place_id(d.pop("place_id", UNSET))

        status = d.pop("status", UNSET)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_borough(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        borough = _parse_borough(d.pop("borough", UNSET))

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        def _parse_price(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_price_key(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_key = _parse_price_key(d.pop("price_key", UNSET))

        def _parse_neighborhood(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        neighborhood = _parse_neighborhood(d.pop("neighborhood", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_phone_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        phone_number = _parse_phone_number(d.pop("phone_number", UNSET))

        cuisines = cast(list[str], d.pop("cuisines", UNSET))

        def _parse_default_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_category = _parse_default_category(d.pop("default_category", UNSET))

        def _parse_quick_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quick_link = _parse_quick_link(d.pop("quick_link", UNSET))

        def _parse_tz(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tz = _parse_tz(d.pop("tz", UNSET))

        has_cover_photo = d.pop("has_cover_photo", UNSET)

        has_res_links = d.pop("has_res_links", UNSET)

        has_delivery_links = d.pop("has_delivery_links", UNSET)

        has_no_show_fee = d.pop("has_no_show_fee", UNSET)

        def _parse_reservation_venue_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_venue_id = _parse_reservation_venue_id(d.pop("reservation_venue_id", UNSET))

        _businesshours_set = d.pop("businesshours_set", UNSET)
        businesshours_set: list[BusinessHours] | Unset = UNSET
        if _businesshours_set is not UNSET:
            businesshours_set = []
            for businesshours_set_item_data in _businesshours_set:
                businesshours_set_item = BusinessHours.from_dict(businesshours_set_item_data)

                businesshours_set.append(businesshours_set_item)

        _businessdistinction_set = d.pop("businessdistinction_set", UNSET)
        businessdistinction_set: list[BusinessBusinessdistinctionSetItem] | Unset = UNSET
        if _businessdistinction_set is not UNSET:
            businessdistinction_set = []
            for businessdistinction_set_item_data in _businessdistinction_set:
                businessdistinction_set_item = BusinessBusinessdistinctionSetItem.from_dict(
                    businessdistinction_set_item_data
                )

                businessdistinction_set.append(businessdistinction_set_item)

        _business_hours_config = d.pop("businessHoursConfig", UNSET)
        business_hours_config: BusinessBusinessHoursConfig | Unset
        if isinstance(_business_hours_config, Unset):
            business_hours_config = UNSET
        else:
            business_hours_config = BusinessBusinessHoursConfig.from_dict(_business_hours_config)

        business = cls(
            id=id,
            name=name,
            place_id=place_id,
            status=status,
            city=city,
            borough=borough,
            lat=lat,
            lng=lng,
            price=price,
            price_key=price_key,
            neighborhood=neighborhood,
            country=country,
            website=website,
            phone_number=phone_number,
            cuisines=cuisines,
            default_category=default_category,
            quick_link=quick_link,
            tz=tz,
            has_cover_photo=has_cover_photo,
            has_res_links=has_res_links,
            has_delivery_links=has_delivery_links,
            has_no_show_fee=has_no_show_fee,
            reservation_venue_id=reservation_venue_id,
            businesshours_set=businesshours_set,
            businessdistinction_set=businessdistinction_set,
            business_hours_config=business_hours_config,
        )

        business.additional_properties = d
        return business

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
