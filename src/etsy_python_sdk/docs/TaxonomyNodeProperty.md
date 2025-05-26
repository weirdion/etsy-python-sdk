# TaxonomyNodeProperty

A product property definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The unique numeric ID of this product property. | [optional] 
**name** | **str** | The name string for this taxonomy node. | [optional] 
**display_name** | **str** | The human-readable product property name string. | [optional] 
**scales** | [**List[TaxonomyPropertyScale]**](TaxonomyPropertyScale.md) | A list of available scales. | [optional] 
**is_required** | **bool** | When true, listings assigned eligible taxonomy IDs require this property. | [optional] 
**supports_attributes** | **bool** | When true, you can use this property in listing attributes. | [optional] 
**supports_variations** | **bool** | When true, you can use this property in listing variations. | [optional] 
**is_multivalued** | **bool** | When true, you can assign multiple property values to this property | [optional] 
**max_values_allowed** | **int** | When true, you can assign multiple property values to this property | [optional] 
**possible_values** | [**List[TaxonomyPropertyValue]**](TaxonomyPropertyValue.md) | A list of supported property value strings for this property. | [optional] 
**selected_values** | [**List[TaxonomyPropertyValue]**](TaxonomyPropertyValue.md) | A list of property value strings automatically and always selected for the given property. | [optional] 

## Example

```python
from etsy_python_sdk.models.taxonomy_node_property import TaxonomyNodeProperty

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyNodeProperty from a JSON string
taxonomy_node_property_instance = TaxonomyNodeProperty.from_json(json)
# print the JSON string representation of the object
print(TaxonomyNodeProperty.to_json())

# convert the object into a dict
taxonomy_node_property_dict = taxonomy_node_property_instance.to_dict()
# create an instance of TaxonomyNodeProperty from a dict
taxonomy_node_property_from_dict = TaxonomyNodeProperty.from_dict(taxonomy_node_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


