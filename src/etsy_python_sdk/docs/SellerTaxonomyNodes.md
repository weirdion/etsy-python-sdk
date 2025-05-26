# SellerTaxonomyNodes

A list of taxonomy nodes from the seller taxonomy tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[SellerTaxonomyNode]**](SellerTaxonomyNode.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.seller_taxonomy_nodes import SellerTaxonomyNodes

# TODO update the JSON string below
json = "{}"
# create an instance of SellerTaxonomyNodes from a JSON string
seller_taxonomy_nodes_instance = SellerTaxonomyNodes.from_json(json)
# print the JSON string representation of the object
print(SellerTaxonomyNodes.to_json())

# convert the object into a dict
seller_taxonomy_nodes_dict = seller_taxonomy_nodes_instance.to_dict()
# create an instance of SellerTaxonomyNodes from a dict
seller_taxonomy_nodes_from_dict = SellerTaxonomyNodes.from_dict(seller_taxonomy_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


