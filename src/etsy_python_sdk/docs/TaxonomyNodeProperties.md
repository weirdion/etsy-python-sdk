# TaxonomyNodeProperties

A list of product property definitions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[TaxonomyNodeProperty]**](TaxonomyNodeProperty.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.taxonomy_node_properties import TaxonomyNodeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TaxonomyNodeProperties from a JSON string
taxonomy_node_properties_instance = TaxonomyNodeProperties.from_json(json)
# print the JSON string representation of the object
print(TaxonomyNodeProperties.to_json())

# convert the object into a dict
taxonomy_node_properties_dict = taxonomy_node_properties_instance.to_dict()
# create an instance of TaxonomyNodeProperties from a dict
taxonomy_node_properties_from_dict = TaxonomyNodeProperties.from_dict(taxonomy_node_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


