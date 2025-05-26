# TaxonomyPropertyValue

A property value for a specific product property, which may also employ a specific scale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_id** | **int** | The numeric ID of this property value. | [optional] 
**name** | **str** | The name string of this property value. | [optional] 
**scale_id** | **int** | The numeric scale ID of the scale to which this property value belongs. | [optional] 
**equal_to** | **List[int]** | A list of numeric property value IDs this property value is equal to (if any). | [optional] 

## Example

```python
from etsy_python_sdk.models.taxonomy_property_value import TaxonomyPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyPropertyValue from a JSON string
taxonomy_property_value_instance = TaxonomyPropertyValue.from_json(json)
# print the JSON string representation of the object
print(TaxonomyPropertyValue.to_json())

# convert the object into a dict
taxonomy_property_value_dict = taxonomy_property_value_instance.to_dict()
# create an instance of TaxonomyPropertyValue from a dict
taxonomy_property_value_from_dict = TaxonomyPropertyValue.from_dict(taxonomy_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


