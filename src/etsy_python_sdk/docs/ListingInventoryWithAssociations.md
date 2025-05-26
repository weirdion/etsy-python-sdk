# ListingInventoryWithAssociations

A representation of a single listing's inventory record with associations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ListingInventoryProduct]**](ListingInventoryProduct.md) | A JSON array of products available in a listing, even if only one product. All field names in the JSON blobs are lowercase. | [optional] 
**price_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change product prices, if any. For example, if you charge specific prices for different sized products in the same listing, then this array contains the property ID for size. | [optional] 
**quantity_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the quantity of the products, if any. For example, if you stock specific quantities of different colored products in the same listing, then this array contains the property ID for color. | [optional] 
**sku_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the product SKU, if any. For example, if you use specific skus for different colored products in the same listing, then this array contains the property ID for color. | [optional] 
**listing** | [**ShopListing**](ShopListing.md) | An enumerated string that attaches a valid association. Default value is null. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_inventory_with_associations import ListingInventoryWithAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ListingInventoryWithAssociations from a JSON string
listing_inventory_with_associations_instance = ListingInventoryWithAssociations.from_json(json)
# print the JSON string representation of the object
print(ListingInventoryWithAssociations.to_json())

# convert the object into a dict
listing_inventory_with_associations_dict = listing_inventory_with_associations_instance.to_dict()
# create an instance of ListingInventoryWithAssociations from a dict
listing_inventory_with_associations_from_dict = ListingInventoryWithAssociations.from_dict(listing_inventory_with_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


