# UserAddresses

Represents several UserAddress records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of UserAddress records being returned. | [optional] 
**results** | [**List[UserAddress]**](UserAddress.md) | An array of UserAddress resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.user_addresses import UserAddresses

# TODO update the JSON string below
json = "{}"
# create an instance of UserAddresses from a JSON string
user_addresses_instance = UserAddresses.from_json(json)
# print the JSON string representation of the object
print(UserAddresses.to_json())

# convert the object into a dict
user_addresses_dict = user_addresses_instance.to_dict()
# create an instance of UserAddresses from a dict
user_addresses_from_dict = UserAddresses.from_dict(user_addresses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


