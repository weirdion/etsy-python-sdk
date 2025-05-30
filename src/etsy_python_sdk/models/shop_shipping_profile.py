# coding: utf-8

"""
    Etsy Open API v3

    <div class=\"wt-text-body-01\"><p class=\"wt-pt-xs-2 wt-pb-xs-2\">Etsy's Open API provides a simple RESTful interface for various Etsy.com features. The API endpoints are meant to replace Etsy's Open API v2, which is scheduled to end service in 2022.</p><p class=\"wt-pb-xs-2\">All of the endpoints are callable and the majority of the API endpoints are now in a beta phase. This means we do not expect to make any breaking changes before our general release. A handful of endpoints are currently interface stubs (labeled “Feedback Only”) and returns a \"501 Not Implemented\" response code when called.</p><p class=\"wt-pb-xs-2\">If you'd like to report an issue or provide feedback on the API design, <a target=\"_blank\" class=\"wt-text-link wt-p-xs-0\" href=\"https://github.com/etsy/open-api/discussions\">please add an issue in Github</a>.</p></div>&copy; 2021-2025 Etsy, Inc. All Rights Reserved. Use of this code is subject to Etsy's <a class='wt-text-link wt-p-xs-0' target='_blank' href='https://www.etsy.com/legal/api'>API Developer Terms of Use</a>.

    The version of the OpenAPI document: 3.0.0
    Contact: developers@etsy.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from etsy_python_sdk.models.shop_shipping_profile_destination import ShopShippingProfileDestination
from etsy_python_sdk.models.shop_shipping_profile_upgrade import ShopShippingProfileUpgrade
from typing import Optional, Set
from typing_extensions import Self

class ShopShippingProfile(BaseModel):
    """
    Represents a profile used to set a listing's shipping information. Please note that it's not possible to create calculated shipping templates via the API. However, you can associate calculated shipping profiles created from Shop Manager with listings using the API.
    """ # noqa: E501
    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID of the shipping profile.")
    title: Optional[StrictStr] = Field(default=None, description="The name string of this shipping profile.")
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID for the [user](/documentation/reference#tag/User) who owns the shipping profile.")
    min_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The minimum number of days for processing the listing.")
    max_processing_days: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The maximum number of days for processing the listing.")
    processing_days_display_label: Optional[StrictStr] = Field(default=None, description="Translated display label string for processing days.")
    origin_country_iso: Optional[StrictStr] = Field(default=None, description="The ISO code of the country from which the listing ships.")
    is_deleted: Optional[StrictBool] = Field(default=None, description="When true, someone deleted this shipping profile.")
    shipping_profile_destinations: Optional[List[ShopShippingProfileDestination]] = Field(default=None, description="A list of [shipping profile destinations](/documentation/reference/#operation/createShopShippingProfileDestination) available for this shipping profile.")
    shipping_profile_upgrades: Optional[List[ShopShippingProfileUpgrade]] = Field(default=None, description="A list of [shipping profile upgrades](/documentation/reference/#operation/createShopShippingProfileUpgrade) available for this shipping profile.")
    origin_postal_code: Optional[StrictStr] = Field(default=None, description="The postal code string (not necessarily a number) for the location from which the listing ships. Required if the `origin_country_iso` supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info")
    profile_type: Optional[StrictStr] = 'manual'
    domestic_handling_fee: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=0, description="The domestic handling fee added to buyer's shipping total - only available for calculated shipping profiles.")
    international_handling_fee: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=0, description="The international handling fee added to buyer's shipping total - only available for calculated shipping profiles.")
    __properties: ClassVar[List[str]] = ["shipping_profile_id", "title", "user_id", "min_processing_days", "max_processing_days", "processing_days_display_label", "origin_country_iso", "is_deleted", "shipping_profile_destinations", "shipping_profile_upgrades", "origin_postal_code", "profile_type", "domestic_handling_fee", "international_handling_fee"]

    @field_validator('profile_type')
    def profile_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['manual', 'calculated']):
            raise ValueError("must be one of enum values ('manual', 'calculated')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ShopShippingProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_profile_destinations (list)
        _items = []
        if self.shipping_profile_destinations:
            for _item_shipping_profile_destinations in self.shipping_profile_destinations:
                if _item_shipping_profile_destinations:
                    _items.append(_item_shipping_profile_destinations.to_dict())
            _dict['shipping_profile_destinations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_profile_upgrades (list)
        _items = []
        if self.shipping_profile_upgrades:
            for _item_shipping_profile_upgrades in self.shipping_profile_upgrades:
                if _item_shipping_profile_upgrades:
                    _items.append(_item_shipping_profile_upgrades.to_dict())
            _dict['shipping_profile_upgrades'] = _items
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if min_processing_days (nullable) is None
        # and model_fields_set contains the field
        if self.min_processing_days is None and "min_processing_days" in self.model_fields_set:
            _dict['min_processing_days'] = None

        # set to None if max_processing_days (nullable) is None
        # and model_fields_set contains the field
        if self.max_processing_days is None and "max_processing_days" in self.model_fields_set:
            _dict['max_processing_days'] = None

        # set to None if origin_postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.origin_postal_code is None and "origin_postal_code" in self.model_fields_set:
            _dict['origin_postal_code'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShopShippingProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipping_profile_id": obj.get("shipping_profile_id"),
            "title": obj.get("title"),
            "user_id": obj.get("user_id"),
            "min_processing_days": obj.get("min_processing_days"),
            "max_processing_days": obj.get("max_processing_days"),
            "processing_days_display_label": obj.get("processing_days_display_label"),
            "origin_country_iso": obj.get("origin_country_iso"),
            "is_deleted": obj.get("is_deleted"),
            "shipping_profile_destinations": [ShopShippingProfileDestination.from_dict(_item) for _item in obj["shipping_profile_destinations"]] if obj.get("shipping_profile_destinations") is not None else None,
            "shipping_profile_upgrades": [ShopShippingProfileUpgrade.from_dict(_item) for _item in obj["shipping_profile_upgrades"]] if obj.get("shipping_profile_upgrades") is not None else None,
            "origin_postal_code": obj.get("origin_postal_code"),
            "profile_type": obj.get("profile_type") if obj.get("profile_type") is not None else 'manual',
            "domestic_handling_fee": obj.get("domestic_handling_fee") if obj.get("domestic_handling_fee") is not None else 0,
            "international_handling_fee": obj.get("international_handling_fee") if obj.get("international_handling_fee") is not None else 0
        })
        return _obj


