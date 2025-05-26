# ListingInventoryProductOffering

A representation of an offering for a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offering_id** | **int** | The ID for the ProductOffering | [optional] 
**quantity** | **int** | The quantity the ProductOffering | [optional] 
**is_enabled** | **bool** | Whether or not the offering can be shown to buyers. | [optional] 
**is_deleted** | **bool** | Whether or not the offering has been deleted. | [optional] 
**price** | [**Money**](Money.md) | Price data for this ProductOffering | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_inventory_product_offering import ListingInventoryProductOffering

# TODO update the JSON string below
json = "{}"
# create an instance of ListingInventoryProductOffering from a JSON string
listing_inventory_product_offering_instance = ListingInventoryProductOffering.from_json(json)
# print the JSON string representation of the object
print(ListingInventoryProductOffering.to_json())

# convert the object into a dict
listing_inventory_product_offering_dict = listing_inventory_product_offering_instance.to_dict()
# create an instance of ListingInventoryProductOffering from a dict
listing_inventory_product_offering_from_dict = ListingInventoryProductOffering.from_dict(listing_inventory_product_offering_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


