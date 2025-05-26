# BuyerTaxonomyNodes

A list of taxonomy nodes from the buyer taxonomy tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[BuyerTaxonomyNode]**](BuyerTaxonomyNode.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.buyer_taxonomy_nodes import BuyerTaxonomyNodes

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerTaxonomyNodes from a JSON string
buyer_taxonomy_nodes_instance = BuyerTaxonomyNodes.from_json(json)
# print the JSON string representation of the object
print(BuyerTaxonomyNodes.to_json())

# convert the object into a dict
buyer_taxonomy_nodes_dict = buyer_taxonomy_nodes_instance.to_dict()
# create an instance of BuyerTaxonomyNodes from a dict
buyer_taxonomy_nodes_from_dict = BuyerTaxonomyNodes.from_dict(buyer_taxonomy_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


