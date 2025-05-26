# BuyerTaxonomyNodeProperties

A list of product property definitions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[BuyerTaxonomyNodeProperty]**](BuyerTaxonomyNodeProperty.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.buyer_taxonomy_node_properties import BuyerTaxonomyNodeProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerTaxonomyNodeProperties from a JSON string
buyer_taxonomy_node_properties_instance = BuyerTaxonomyNodeProperties.from_json(json)
# print the JSON string representation of the object
print(BuyerTaxonomyNodeProperties.to_json())

# convert the object into a dict
buyer_taxonomy_node_properties_dict = buyer_taxonomy_node_properties_instance.to_dict()
# create an instance of BuyerTaxonomyNodeProperties from a dict
buyer_taxonomy_node_properties_from_dict = BuyerTaxonomyNodeProperties.from_dict(buyer_taxonomy_node_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


