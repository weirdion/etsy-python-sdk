# Shops

A set of Shop records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of Shops | [optional] 
**results** | [**List[Shop]**](Shop.md) | The Shop resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shops import Shops

# TODO update the JSON string below
json = "{}"
# create an instance of Shops from a JSON string
shops_instance = Shops.from_json(json)
# print the JSON string representation of the object
print(Shops.to_json())

# convert the object into a dict
shops_dict = shops_instance.to_dict()
# create an instance of Shops from a dict
shops_from_dict = Shops.from_dict(shops_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


