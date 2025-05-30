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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_python_sdk.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class ShopShippingProfileDestination(BaseModel):
    """
    Represents a shipping destination assigned to a shipping profile.
    """ # noqa: E501
    shipping_profile_destination_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing.")
    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID of the shipping profile.")
    origin_country_iso: Optional[StrictStr] = Field(default=None, description="The ISO code of the country from which the listing ships.")
    destination_country_iso: Optional[StrictStr] = Field(default=None, description="The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided.")
    destination_region: Optional[StrictStr] = Field(default=None, description="The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If \\`none\\`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided.")
    primary_cost: Optional[Money] = Field(default=None, description="The cost of shipping to this country/region alone, measured in the store's default currency.")
    secondary_cost: Optional[Money] = Field(default=None, description="The cost of shipping to this country/region with another item, measured in the store's default currency.")
    shipping_carrier_id: Optional[StrictInt] = Field(default=None, description="The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null.")
    mail_class: Optional[StrictStr] = Field(default=None, description="The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null.")
    min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = Field(default=None, description="The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null.")
    max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = Field(default=None, description="The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null.")
    __properties: ClassVar[List[str]] = ["shipping_profile_destination_id", "shipping_profile_id", "origin_country_iso", "destination_country_iso", "destination_region", "primary_cost", "secondary_cost", "shipping_carrier_id", "mail_class", "min_delivery_days", "max_delivery_days"]

    @field_validator('destination_region')
    def destination_region_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['eu', 'non_eu', 'none']):
            raise ValueError("must be one of enum values ('eu', 'non_eu', 'none')")
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
        """Create an instance of ShopShippingProfileDestination from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of primary_cost
        if self.primary_cost:
            _dict['primary_cost'] = self.primary_cost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secondary_cost
        if self.secondary_cost:
            _dict['secondary_cost'] = self.secondary_cost.to_dict()
        # set to None if shipping_carrier_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_carrier_id is None and "shipping_carrier_id" in self.model_fields_set:
            _dict['shipping_carrier_id'] = None

        # set to None if mail_class (nullable) is None
        # and model_fields_set contains the field
        if self.mail_class is None and "mail_class" in self.model_fields_set:
            _dict['mail_class'] = None

        # set to None if min_delivery_days (nullable) is None
        # and model_fields_set contains the field
        if self.min_delivery_days is None and "min_delivery_days" in self.model_fields_set:
            _dict['min_delivery_days'] = None

        # set to None if max_delivery_days (nullable) is None
        # and model_fields_set contains the field
        if self.max_delivery_days is None and "max_delivery_days" in self.model_fields_set:
            _dict['max_delivery_days'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShopShippingProfileDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipping_profile_destination_id": obj.get("shipping_profile_destination_id"),
            "shipping_profile_id": obj.get("shipping_profile_id"),
            "origin_country_iso": obj.get("origin_country_iso"),
            "destination_country_iso": obj.get("destination_country_iso"),
            "destination_region": obj.get("destination_region"),
            "primary_cost": Money.from_dict(obj["primary_cost"]) if obj.get("primary_cost") is not None else None,
            "secondary_cost": Money.from_dict(obj["secondary_cost"]) if obj.get("secondary_cost") is not None else None,
            "shipping_carrier_id": obj.get("shipping_carrier_id"),
            "mail_class": obj.get("mail_class"),
            "min_delivery_days": obj.get("min_delivery_days"),
            "max_delivery_days": obj.get("max_delivery_days")
        })
        return _obj


