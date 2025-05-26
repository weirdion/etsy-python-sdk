# UserAddress

Represents a user's address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_address_id** | **int** | The numeric ID of the user&#39;s address. | [optional] 
**user_id** | **int** | The user&#39;s numeric ID. | [optional] 
**name** | **str** | The user&#39;s name for this address. | [optional] 
**first_line** | **str** | The first line of the user&#39;s address. | [optional] 
**second_line** | **str** | The second line of the user&#39;s address. | [optional] 
**city** | **str** | The city field of the user&#39;s address. | [optional] 
**state** | **str** | The state field of the user&#39;s address. | [optional] 
**zip** | **str** | The zip code field of the user&#39;s address. | [optional] 
**iso_country_code** | **str** | The ISO code of the country in this address. | [optional] 
**country_name** | **str** | The name of the user&#39;s country. | [optional] 
**is_default_shipping_address** | **bool** | Is this the user&#39;s default shipping address. | [optional] 

## Example

```python
from etsy_python_sdk.models.user_address import UserAddress

# TODO update the JSON string below
json = "{}"
# create an instance of UserAddress from a JSON string
user_address_instance = UserAddress.from_json(json)
# print the JSON string representation of the object
print(UserAddress.to_json())

# convert the object into a dict
user_address_dict = user_address_instance.to_dict()
# create an instance of UserAddress from a dict
user_address_from_dict = UserAddress.from_dict(user_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


