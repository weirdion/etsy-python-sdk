# ShopShippingProfile

Represents a profile used to set a listing's shipping information. Please note that it's not possible to create calculated shipping templates via the API. However, you can associate calculated shipping profiles created from Shop Manager with listings using the API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_profile_id** | **int** | The numeric ID of the shipping profile. | [optional] 
**title** | **str** | The name string of this shipping profile. | [optional] 
**user_id** | **int** | The numeric ID for the [user](/documentation/reference#tag/User) who owns the shipping profile. | [optional] 
**min_processing_days** | **int** | The minimum number of days for processing the listing. | [optional] 
**max_processing_days** | **int** | The maximum number of days for processing the listing. | [optional] 
**processing_days_display_label** | **str** | Translated display label string for processing days. | [optional] 
**origin_country_iso** | **str** | The ISO code of the country from which the listing ships. | [optional] 
**is_deleted** | **bool** | When true, someone deleted this shipping profile. | [optional] 
**shipping_profile_destinations** | [**List[ShopShippingProfileDestination]**](ShopShippingProfileDestination.md) | A list of [shipping profile destinations](/documentation/reference/#operation/createShopShippingProfileDestination) available for this shipping profile. | [optional] 
**shipping_profile_upgrades** | [**List[ShopShippingProfileUpgrade]**](ShopShippingProfileUpgrade.md) | A list of [shipping profile upgrades](/documentation/reference/#operation/createShopShippingProfileUpgrade) available for this shipping profile. | [optional] 
**origin_postal_code** | **str** | The postal code string (not necessarily a number) for the location from which the listing ships. Required if the &#x60;origin_country_iso&#x60; supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info | [optional] 
**profile_type** | **str** |  | [optional] [default to 'manual']
**domestic_handling_fee** | **float** | The domestic handling fee added to buyer&#39;s shipping total - only available for calculated shipping profiles. | [optional] [default to 0]
**international_handling_fee** | **float** | The international handling fee added to buyer&#39;s shipping total - only available for calculated shipping profiles. | [optional] [default to 0]

## Example

```python
from etsy_python_sdk.models.shop_shipping_profile import ShopShippingProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ShopShippingProfile from a JSON string
shop_shipping_profile_instance = ShopShippingProfile.from_json(json)
# print the JSON string representation of the object
print(ShopShippingProfile.to_json())

# convert the object into a dict
shop_shipping_profile_dict = shop_shipping_profile_instance.to_dict()
# create an instance of ShopShippingProfile from a dict
shop_shipping_profile_from_dict = ShopShippingProfile.from_dict(shop_shipping_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


