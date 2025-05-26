# Pong

A confirmation that the current application has access to the Open API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **int** | The authenticated application&#39;s ID | [optional] 

## Example

```python
from etsy_python_sdk.models.pong import Pong

# TODO update the JSON string below
json = "{}"
# create an instance of Pong from a JSON string
pong_instance = Pong.from_json(json)
# print the JSON string representation of the object
print(Pong.to_json())

# convert the object into a dict
pong_dict = pong_instance.to_dict()
# create an instance of Pong from a dict
pong_from_dict = Pong.from_dict(pong_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


