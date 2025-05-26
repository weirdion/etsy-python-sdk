# ShopShippingProfileUpgrades

A list of shipping upgrade options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ShopShippingProfileUpgrade]**](ShopShippingProfileUpgrade.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_shipping_profile_upgrades import ShopShippingProfileUpgrades

# TODO update the JSON string below
json = "{}"
# create an instance of ShopShippingProfileUpgrades from a JSON string
shop_shipping_profile_upgrades_instance = ShopShippingProfileUpgrades.from_json(json)
# print the JSON string representation of the object
print(ShopShippingProfileUpgrades.to_json())

# convert the object into a dict
shop_shipping_profile_upgrades_dict = shop_shipping_profile_upgrades_instance.to_dict()
# create an instance of ShopShippingProfileUpgrades from a dict
shop_shipping_profile_upgrades_from_dict = ShopShippingProfileUpgrades.from_dict(shop_shipping_profile_upgrades_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


