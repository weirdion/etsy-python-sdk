# ModelSelf

Represents a single user of the site

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | The numeric ID of a user. This number is also a valid shop ID for the user\\&#39;s shop. | [optional] 
**shop_id** | **int** | The unique positive non-zero numeric ID for an Etsy Shop. | [optional] 

## Example

```python
from etsy_python_sdk.models.model_self import ModelSelf

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSelf from a JSON string
model_self_instance = ModelSelf.from_json(json)
# print the JSON string representation of the object
print(ModelSelf.to_json())

# convert the object into a dict
model_self_dict = model_self_instance.to_dict()
# create an instance of ModelSelf from a dict
model_self_from_dict = ModelSelf.from_dict(model_self_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


