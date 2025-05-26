# SellerTaxonomyNode

A taxonomy node in the seller taxonomy tree.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique numeric ID of an Etsy taxonomy node, which is a metadata category for listings organized into the seller taxonomy hierarchy tree. For example, the \\\&quot;shoes\\\&quot; taxonomy node (ID: 1429, level: 1) is higher in the hierarchy than \\\&quot;girls&#39; shoes\\\&quot; (ID: 1440, level: 2). The taxonomy nodes assigned to a listing support access to specific standardized product scales and properties. For example, listings assigned the taxonomy nodes \\\&quot;shoes\\\&quot; or \\\&quot;girls&#39; shoes\\\&quot; support access to the \\\&quot;EU\\\&quot; shoe size scale with its associated property names and IDs for EU shoe sizes, such as property &#x60;value_id&#x60;:\\\&quot;1394\\\&quot;, and &#x60;name&#x60;:\\\&quot;38\\\&quot;. | [optional] 
**level** | **int** | The integer depth of this taxonomy node in the seller taxonomy tree, with roots at level 0. | [optional] 
**name** | **str** | The name string for this taxonomy node. | [optional] 
**parent_id** | **int** | The numeric taxonomy ID of the parent of this node. | [optional] 
**children** | [**List[SellerTaxonomyNode]**](SellerTaxonomyNode.md) | An array of taxonomy nodes for all the direct children of this taxonomy node in the seller taxonomy tree. | [optional] 
**full_path_taxonomy_ids** | **List[int]** | An array of &#x60;taxonomy_id&#x60;s including this node and all of its direct parents in the seller taxonomy tree up to a root node. They are listed in order from root to leaf. | [optional] 

## Example

```python
from etsy_python_sdk.models.seller_taxonomy_node import SellerTaxonomyNode

# TODO update the JSON string below
json = "{}"
# create an instance of SellerTaxonomyNode from a JSON string
seller_taxonomy_node_instance = SellerTaxonomyNode.from_json(json)
# print the JSON string representation of the object
print(SellerTaxonomyNode.to_json())

# convert the object into a dict
seller_taxonomy_node_dict = seller_taxonomy_node_instance.to_dict()
# create an instance of SellerTaxonomyNode from a dict
seller_taxonomy_node_from_dict = SellerTaxonomyNode.from_dict(seller_taxonomy_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


