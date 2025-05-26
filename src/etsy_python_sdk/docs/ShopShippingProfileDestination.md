# ShopShippingProfileDestination

Represents a shipping destination assigned to a shipping profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_profile_destination_id** | **int** | The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing. | [optional] 
**shipping_profile_id** | **int** | The numeric ID of the shipping profile. | [optional] 
**origin_country_iso** | **str** | The ISO code of the country from which the listing ships. | [optional] 
**destination_country_iso** | **str** | The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. | [optional] 
**destination_region** | **str** | The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If \\&#x60;none\\&#x60;, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. | [optional] 
**primary_cost** | [**Money**](Money.md) | The cost of shipping to this country/region alone, measured in the store&#39;s default currency. | [optional] 
**secondary_cost** | [**Money**](Money.md) | The cost of shipping to this country/region with another item, measured in the store&#39;s default currency. | [optional] 
**shipping_carrier_id** | **int** | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
**mail_class** | **str** | The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
**min_delivery_days** | **int** | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
**max_delivery_days** | **int** | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_shipping_profile_destination import ShopShippingProfileDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ShopShippingProfileDestination from a JSON string
shop_shipping_profile_destination_instance = ShopShippingProfileDestination.from_json(json)
# print the JSON string representation of the object
print(ShopShippingProfileDestination.to_json())

# convert the object into a dict
shop_shipping_profile_destination_dict = shop_shipping_profile_destination_instance.to_dict()
# create an instance of ShopShippingProfileDestination from a dict
shop_shipping_profile_destination_from_dict = ShopShippingProfileDestination.from_dict(shop_shipping_profile_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


