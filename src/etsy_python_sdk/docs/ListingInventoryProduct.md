# ListingInventoryProduct

A representation of a product for a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **int** | The numeric ID for a specific [product](/documentation/reference#tag/ShopListing-Product) purchased from a listing. | [optional] 
**sku** | **str** | The SKU string for the product | [optional] 
**is_deleted** | **bool** | When true, someone deleted this product. | [optional] 
**offerings** | [**List[ListingInventoryProductOffering]**](ListingInventoryProductOffering.md) | A list of product offering entries for this product. | [optional] 
**property_values** | [**List[ListingPropertyValue]**](ListingPropertyValue.md) | A list of property value entries for this product. Note: parenthesis characters (&#x60;(&#x60; and &#x60;)&#x60;) are not allowed. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_inventory_product import ListingInventoryProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ListingInventoryProduct from a JSON string
listing_inventory_product_instance = ListingInventoryProduct.from_json(json)
# print the JSON string representation of the object
print(ListingInventoryProduct.to_json())

# convert the object into a dict
listing_inventory_product_dict = listing_inventory_product_instance.to_dict()
# create an instance of ListingInventoryProduct from a dict
listing_inventory_product_from_dict = ListingInventoryProduct.from_dict(listing_inventory_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


