# UpdateListingInventoryRequestProductsInnerOfferingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** | The price of the product. | 
**quantity** | **int** | How many of this product are available? | 
**is_enabled** | **bool** | True if the offering is shown to buyers | 

## Example

```python
from etsy_python_sdk.models.update_listing_inventory_request_products_inner_offerings_inner import UpdateListingInventoryRequestProductsInnerOfferingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListingInventoryRequestProductsInnerOfferingsInner from a JSON string
update_listing_inventory_request_products_inner_offerings_inner_instance = UpdateListingInventoryRequestProductsInnerOfferingsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateListingInventoryRequestProductsInnerOfferingsInner.to_json())

# convert the object into a dict
update_listing_inventory_request_products_inner_offerings_inner_dict = update_listing_inventory_request_products_inner_offerings_inner_instance.to_dict()
# create an instance of UpdateListingInventoryRequestProductsInnerOfferingsInner from a dict
update_listing_inventory_request_products_inner_offerings_inner_from_dict = UpdateListingInventoryRequestProductsInnerOfferingsInner.from_dict(update_listing_inventory_request_products_inner_offerings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


