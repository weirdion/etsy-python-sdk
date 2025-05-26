# UpdateListingInventoryRequestProductsInnerPropertyValuesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties). | 
**value_ids** | **List[int]** | An array of unique IDs of multiple Etsy [listing property](/documentation/reference#operation/getListingProperties) values. For example, if your listing offers different sizes of a product, then the value ID list contains value IDs for each size. | 
**scale_id** | **int** | The numeric ID of a single Etsy.com measurement scale. For example, for shoe size, there are three &#x60;scale_id&#x60;s available - &#x60;UK&#x60;, &#x60;US/Canada&#x60;, and &#x60;EU&#x60;, where &#x60;US/Canada&#x60; has &#x60;scale_id&#x60; 19. | [optional] 
**property_name** | **str** | The name of the property, in the requested locale language. | [optional] 
**values** | **List[str]** | A list of property value entries for this product. Note: parenthesis characters (&#x60;(&#x60; and &#x60;)&#x60;) are not allowed. | 

## Example

```python
from etsy_python_sdk.models.update_listing_inventory_request_products_inner_property_values_inner import UpdateListingInventoryRequestProductsInnerPropertyValuesInner

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateListingInventoryRequestProductsInnerPropertyValuesInner from a JSON string
update_listing_inventory_request_products_inner_property_values_inner_instance = UpdateListingInventoryRequestProductsInnerPropertyValuesInner.from_json(json)
# print the JSON string representation of the object
print(UpdateListingInventoryRequestProductsInnerPropertyValuesInner.to_json())

# convert the object into a dict
update_listing_inventory_request_products_inner_property_values_inner_dict = update_listing_inventory_request_products_inner_property_values_inner_instance.to_dict()
# create an instance of UpdateListingInventoryRequestProductsInnerPropertyValuesInner from a dict
update_listing_inventory_request_products_inner_property_values_inner_from_dict = UpdateListingInventoryRequestProductsInnerPropertyValuesInner.from_dict(update_listing_inventory_request_products_inner_property_values_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


