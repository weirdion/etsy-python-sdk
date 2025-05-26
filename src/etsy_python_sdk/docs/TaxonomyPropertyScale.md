# TaxonomyPropertyScale

A scale defnining the assignable increments for the property values available to specific product properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_id** | **int** | The unique numeric ID of a scale. | [optional] 
**display_name** | **str** | The name string for a scale. | [optional] 
**description** | **str** | The description string for a scale. | [optional] 

## Example

```python
from etsy_python_sdk.models.taxonomy_property_scale import TaxonomyPropertyScale

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyPropertyScale from a JSON string
taxonomy_property_scale_instance = TaxonomyPropertyScale.from_json(json)
# print the JSON string representation of the object
print(TaxonomyPropertyScale.to_json())

# convert the object into a dict
taxonomy_property_scale_dict = taxonomy_property_scale_instance.to_dict()
# create an instance of TaxonomyPropertyScale from a dict
taxonomy_property_scale_from_dict = TaxonomyPropertyScale.from_dict(taxonomy_property_scale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


