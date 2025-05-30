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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ShopReturnPolicy(BaseModel):
    """
    Represents a listing-level return policy.
    """ # noqa: E501
    return_policy_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies).")
    shop_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The unique positive non-zero numeric ID for an Etsy Shop.")
    accepts_returns: Optional[StrictBool] = Field(default=None, description="return_policy_accepts_returns")
    accepts_exchanges: Optional[StrictBool] = Field(default=None, description="return_policy_accepts_exchanges")
    return_deadline: Optional[StrictInt] = Field(default=None, description="The deadline for the Return Policy, measured in days. The value must be one of the following: [7, 14, 21, 30, 45, 60, 90].")
    __properties: ClassVar[List[str]] = ["return_policy_id", "shop_id", "accepts_returns", "accepts_exchanges", "return_deadline"]

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
        """Create an instance of ShopReturnPolicy from a JSON string"""
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
        # set to None if return_deadline (nullable) is None
        # and model_fields_set contains the field
        if self.return_deadline is None and "return_deadline" in self.model_fields_set:
            _dict['return_deadline'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShopReturnPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "return_policy_id": obj.get("return_policy_id"),
            "shop_id": obj.get("shop_id"),
            "accepts_returns": obj.get("accepts_returns"),
            "accepts_exchanges": obj.get("accepts_exchanges"),
            "return_deadline": obj.get("return_deadline")
        })
        return _obj


