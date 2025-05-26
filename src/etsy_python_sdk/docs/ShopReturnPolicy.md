# ShopReturnPolicy

Represents a listing-level return policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_policy_id** | **int** | The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). | [optional] 
**shop_id** | **int** | The unique positive non-zero numeric ID for an Etsy Shop. | [optional] 
**accepts_returns** | **bool** | return_policy_accepts_returns | [optional] 
**accepts_exchanges** | **bool** | return_policy_accepts_exchanges | [optional] 
**return_deadline** | **int** | The deadline for the Return Policy, measured in days. The value must be one of the following: [7, 14, 21, 30, 45, 60, 90]. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_return_policy import ShopReturnPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReturnPolicy from a JSON string
shop_return_policy_instance = ShopReturnPolicy.from_json(json)
# print the JSON string representation of the object
print(ShopReturnPolicy.to_json())

# convert the object into a dict
shop_return_policy_dict = shop_return_policy_instance.to_dict()
# create an instance of ShopReturnPolicy from a dict
shop_return_policy_from_dict = ShopReturnPolicy.from_dict(shop_return_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


