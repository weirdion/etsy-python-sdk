# ShopShippingProfileDestinations

Represents a list of shipping destination objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ShopShippingProfileDestination]**](ShopShippingProfileDestination.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_shipping_profile_destinations import ShopShippingProfileDestinations

# TODO update the JSON string below
json = "{}"
# create an instance of ShopShippingProfileDestinations from a JSON string
shop_shipping_profile_destinations_instance = ShopShippingProfileDestinations.from_json(json)
# print the JSON string representation of the object
print(ShopShippingProfileDestinations.to_json())

# convert the object into a dict
shop_shipping_profile_destinations_dict = shop_shipping_profile_destinations_instance.to_dict()
# create an instance of ShopShippingProfileDestinations from a dict
shop_shipping_profile_destinations_from_dict = ShopShippingProfileDestinations.from_dict(shop_shipping_profile_destinations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


