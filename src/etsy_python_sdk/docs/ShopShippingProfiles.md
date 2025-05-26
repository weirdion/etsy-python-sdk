# ShopShippingProfiles

Represents several ShopShippingProfiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[ShopShippingProfile]**](ShopShippingProfile.md) |  | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_shipping_profiles import ShopShippingProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of ShopShippingProfiles from a JSON string
shop_shipping_profiles_instance = ShopShippingProfiles.from_json(json)
# print the JSON string representation of the object
print(ShopShippingProfiles.to_json())

# convert the object into a dict
shop_shipping_profiles_dict = shop_shipping_profiles_instance.to_dict()
# create an instance of ShopShippingProfiles from a dict
shop_shipping_profiles_from_dict = ShopShippingProfiles.from_dict(shop_shipping_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


