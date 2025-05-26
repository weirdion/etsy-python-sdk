# ListingInventory

A representation of a single listing's inventory record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ListingInventoryProduct]**](ListingInventoryProduct.md) | A JSON array of products available in a listing, even if only one product. All field names in the JSON blobs are lowercase. | [optional] 
**price_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change product prices, if any. For example, if you charge specific prices for different sized products in the same listing, then this array contains the property ID for size. | [optional] 
**quantity_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the quantity of the products, if any. For example, if you stock specific quantities of different colored products in the same listing, then this array contains the property ID for color. | [optional] 
**sku_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the product SKU, if any. For example, if you use specific skus for different colored products in the same listing, then this array contains the property ID for color. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_inventory import ListingInventory

# TODO update the JSON string below
json = "{}"
# create an instance of ListingInventory from a JSON string
listing_inventory_instance = ListingInventory.from_json(json)
# print the JSON string representation of the object
print(ListingInventory.to_json())

# convert the object into a dict
listing_inventory_dict = listing_inventory_instance.to_dict()
# create an instance of ListingInventory from a dict
listing_inventory_from_dict = ListingInventory.from_dict(listing_inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


