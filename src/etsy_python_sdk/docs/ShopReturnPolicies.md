# ShopReturnPolicies

Represents a shop's listing-level return policies list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[ShopReturnPolicy]**](ShopReturnPolicy.md) |  | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_return_policies import ShopReturnPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReturnPolicies from a JSON string
shop_return_policies_instance = ShopReturnPolicies.from_json(json)
# print the JSON string representation of the object
print(ShopReturnPolicies.to_json())

# convert the object into a dict
shop_return_policies_dict = shop_return_policies_instance.to_dict()
# create an instance of ShopReturnPolicies from a dict
shop_return_policies_from_dict = ShopReturnPolicies.from_dict(shop_return_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


