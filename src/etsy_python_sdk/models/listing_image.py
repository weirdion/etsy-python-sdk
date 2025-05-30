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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ListingImage(BaseModel):
    """
    Reference urls and metadata for an image associated with a specific listing. The `url_fullxfull` parameter contains the URL for full-sized binary image file.
    """ # noqa: E501
    listing_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.")
    listing_image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The numeric ID of the primary [listing image](/documentation/reference#tag/ShopListing-Image) for this transaction.")
    hex_code: Optional[StrictStr] = Field(default=None, description="The webhex string for the image's average color, in webhex notation.")
    red: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric red value equal to the image's average red value, from 0-255 (RGB color).")
    green: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric red value equal to the image's average red value, from 0-255 (RGB color).")
    blue: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric red value equal to the image's average red value, from 0-255 (RGB color).")
    hue: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric hue equal to the image's average hue, from 0-360 (HSV color).")
    saturation: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric saturation equal to the image's average saturation, from 0-100 (HSV color).")
    brightness: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric brightness equal to the image's average brightness, from 0-100 (HSV color).")
    is_black_and_white: Optional[StrictBool] = Field(default=None, description="When true, the image is in black & white.")
    creation_tsz: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The listing image\\'s creation time, in epoch seconds.")
    created_timestamp: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The listing image\\'s creation time, in epoch seconds.")
    rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The positive non-zero numeric position in the images displayed in a listing, with rank 1 images appearing in the left-most position in a listing.")
    url_75x75: Optional[StrictStr] = Field(default=None, description="The url string for a 75x75 pixel thumbnail of the image.")
    url_170x135: Optional[StrictStr] = Field(default=None, description="The url string for a 170x135 pixel thumbnail of the image.")
    url_570x_n: Optional[StrictStr] = Field(default=None, description="The url string for a thumbnail of the image, no more than 570 pixels wide with variable height.", alias="url_570xN")
    url_fullxfull: Optional[StrictStr] = Field(default=None, description="The url string for the full-size image, up to 3000 pixels in each dimension.")
    full_height: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric height, measured in pixels, of the full-sized image referenced in url_fullxfull.")
    full_width: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The numeric width, measured in pixels, of the full-sized image referenced in url_fullxfull.")
    alt_text: Optional[StrictStr] = Field(default=None, description="Alt text for the listing image. Max length 500 characters.")
    __properties: ClassVar[List[str]] = ["listing_id", "listing_image_id", "hex_code", "red", "green", "blue", "hue", "saturation", "brightness", "is_black_and_white", "creation_tsz", "created_timestamp", "rank", "url_75x75", "url_170x135", "url_570xN", "url_fullxfull", "full_height", "full_width", "alt_text"]

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
        """Create an instance of ListingImage from a JSON string"""
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
        # set to None if hex_code (nullable) is None
        # and model_fields_set contains the field
        if self.hex_code is None and "hex_code" in self.model_fields_set:
            _dict['hex_code'] = None

        # set to None if red (nullable) is None
        # and model_fields_set contains the field
        if self.red is None and "red" in self.model_fields_set:
            _dict['red'] = None

        # set to None if green (nullable) is None
        # and model_fields_set contains the field
        if self.green is None and "green" in self.model_fields_set:
            _dict['green'] = None

        # set to None if blue (nullable) is None
        # and model_fields_set contains the field
        if self.blue is None and "blue" in self.model_fields_set:
            _dict['blue'] = None

        # set to None if hue (nullable) is None
        # and model_fields_set contains the field
        if self.hue is None and "hue" in self.model_fields_set:
            _dict['hue'] = None

        # set to None if saturation (nullable) is None
        # and model_fields_set contains the field
        if self.saturation is None and "saturation" in self.model_fields_set:
            _dict['saturation'] = None

        # set to None if brightness (nullable) is None
        # and model_fields_set contains the field
        if self.brightness is None and "brightness" in self.model_fields_set:
            _dict['brightness'] = None

        # set to None if is_black_and_white (nullable) is None
        # and model_fields_set contains the field
        if self.is_black_and_white is None and "is_black_and_white" in self.model_fields_set:
            _dict['is_black_and_white'] = None

        # set to None if full_height (nullable) is None
        # and model_fields_set contains the field
        if self.full_height is None and "full_height" in self.model_fields_set:
            _dict['full_height'] = None

        # set to None if full_width (nullable) is None
        # and model_fields_set contains the field
        if self.full_width is None and "full_width" in self.model_fields_set:
            _dict['full_width'] = None

        # set to None if alt_text (nullable) is None
        # and model_fields_set contains the field
        if self.alt_text is None and "alt_text" in self.model_fields_set:
            _dict['alt_text'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListingImage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "listing_id": obj.get("listing_id"),
            "listing_image_id": obj.get("listing_image_id"),
            "hex_code": obj.get("hex_code"),
            "red": obj.get("red"),
            "green": obj.get("green"),
            "blue": obj.get("blue"),
            "hue": obj.get("hue"),
            "saturation": obj.get("saturation"),
            "brightness": obj.get("brightness"),
            "is_black_and_white": obj.get("is_black_and_white"),
            "creation_tsz": obj.get("creation_tsz"),
            "created_timestamp": obj.get("created_timestamp"),
            "rank": obj.get("rank"),
            "url_75x75": obj.get("url_75x75"),
            "url_170x135": obj.get("url_170x135"),
            "url_570xN": obj.get("url_570xN"),
            "url_fullxfull": obj.get("url_fullxfull"),
            "full_height": obj.get("full_height"),
            "full_width": obj.get("full_width"),
            "alt_text": obj.get("alt_text")
        })
        return _obj


