# User

Represents a single user of the site

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The numeric ID of a user. This number is also a valid shop ID for the user\\&#39;s shop. | [optional] 
**primary_email** | **str** | An email address string for the user\\&#39;s primary email address. Access to this field is granted on a case by case basis for third-party integrations that require full access | [optional] 
**first_name** | **str** | The user\\&#39;s first name. | [optional] 
**last_name** | **str** | The user\\&#39;s last name. | [optional] 
**image_url_75x75** | **str** | The user\\&#39;s avatar URL. | [optional] 

## Example

```python
from etsy_python_sdk.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


