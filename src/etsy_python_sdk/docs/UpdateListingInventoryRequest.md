# UpdateListingInventoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[UpdateListingInventoryRequestProductsInner]**](UpdateListingInventoryRequestProductsInner.md) | A JSON array of products available in a listing, even if only one product. All field names in the JSON blobs are lowercase. | 
**price_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change product prices, if any. For example, if you charge specific prices for different sized products in the same listing, then this array contains the property ID for size. | [optional] 
**quantity_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the quantity of the products, if any. For example, if you stock specific quantities of different colored products in the same listing, then this array contains the property ID for color. | [optional] 
**sku_on_property** | **List[int]** | An array of unique [listing property](/documentation/reference#operation/getListingProperties) ID integers for the properties that change the product SKU, if any. For example, if you use specific skus for different colored products in the same listing, then this array contains the property ID for color. | [optional] 

## Example

```python
from etsy_python_sdk.models.update_listing_inventory_request import UpdateListingInventoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListingInventoryRequest from a JSON string
update_listing_inventory_request_instance = UpdateListingInventoryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateListingInventoryRequest.to_json())

# convert the object into a dict
update_listing_inventory_request_dict = update_listing_inventory_request_instance.to_dict()
# create an instance of UpdateListingInventoryRequest from a dict
update_listing_inventory_request_from_dict = UpdateListingInventoryRequest.from_dict(update_listing_inventory_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


