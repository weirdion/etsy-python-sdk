# BuyerTaxonomyNodeProperty

A product property definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The unique numeric ID of this product property. | [optional] 
**name** | **str** | The name string for this taxonomy node. | [optional] 
**display_name** | **str** | The human-readable product property name string. | [optional] 
**scales** | [**List[BuyerTaxonomyPropertyScale]**](BuyerTaxonomyPropertyScale.md) | A list of available scales. | [optional] 
**is_required** | **bool** | When true, listings assigned eligible taxonomy IDs require this property. | [optional] 
**supports_attributes** | **bool** | When true, you can use this property in listing attributes. | [optional] 
**supports_variations** | **bool** | When true, you can use this property in listing variations. | [optional] 
**is_multivalued** | **bool** | When true, you can assign multiple property values to this property | [optional] 
**max_values_allowed** | **int** | When true, you can assign multiple property values to this property | [optional] 
**possible_values** | [**List[BuyerTaxonomyPropertyValue]**](BuyerTaxonomyPropertyValue.md) | A list of supported property value strings for this property. | [optional] 
**selected_values** | [**List[BuyerTaxonomyPropertyValue]**](BuyerTaxonomyPropertyValue.md) | A list of property value strings automatically and always selected for the given property. | [optional] 

## Example

```python
from etsy_python_sdk.models.buyer_taxonomy_node_property import BuyerTaxonomyNodeProperty

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerTaxonomyNodeProperty from a JSON string
buyer_taxonomy_node_property_instance = BuyerTaxonomyNodeProperty.from_json(json)
# print the JSON string representation of the object
print(BuyerTaxonomyNodeProperty.to_json())

# convert the object into a dict
buyer_taxonomy_node_property_dict = buyer_taxonomy_node_property_instance.to_dict()
# create an instance of BuyerTaxonomyNodeProperty from a dict
buyer_taxonomy_node_property_from_dict = BuyerTaxonomyNodeProperty.from_dict(buyer_taxonomy_node_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


