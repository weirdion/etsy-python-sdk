# UpdateListingInventoryRequestProductsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | The SKU string for the product | [optional] 
**property_values** | [**List[UpdateListingInventoryRequestProductsInnerPropertyValuesInner]**](UpdateListingInventoryRequestProductsInnerPropertyValuesInner.md) | A list of property value entries for this product. Note: parenthesis characters (&#x60;(&#x60; and &#x60;)&#x60;) are not allowed. | [optional] 
**offerings** | [**List[UpdateListingInventoryRequestProductsInnerOfferingsInner]**](UpdateListingInventoryRequestProductsInnerOfferingsInner.md) | A list of product offering entries for this product. | 

## Example

```python
from etsy_python_sdk.models.update_listing_inventory_request_products_inner import UpdateListingInventoryRequestProductsInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListingInventoryRequestProductsInner from a JSON string
update_listing_inventory_request_products_inner_instance = UpdateListingInventoryRequestProductsInner.from_json(json)
# print the JSON string representation of the object
print(UpdateListingInventoryRequestProductsInner.to_json())

# convert the object into a dict
update_listing_inventory_request_products_inner_dict = update_listing_inventory_request_products_inner_instance.to_dict()
# create an instance of UpdateListingInventoryRequestProductsInner from a dict
update_listing_inventory_request_products_inner_from_dict = UpdateListingInventoryRequestProductsInner.from_dict(update_listing_inventory_request_products_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


