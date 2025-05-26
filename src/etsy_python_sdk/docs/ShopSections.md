# ShopSections

All the sections in a sprecific Shop.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ShopSection]**](ShopSection.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_sections import ShopSections

# TODO update the JSON string below
json = "{}"
# create an instance of ShopSections from a JSON string
shop_sections_instance = ShopSections.from_json(json)
# print the JSON string representation of the object
print(ShopSections.to_json())

# convert the object into a dict
shop_sections_dict = shop_sections_instance.to_dict()
# create an instance of ShopSections from a dict
shop_sections_from_dict = ShopSections.from_dict(shop_sections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


