# ShopListingFile

A file associated with a digital listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_file_id** | **int** | The unique numeric ID of a file associated with a digital listing. | [optional] 
**listing_id** | **int** | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | [optional] 
**rank** | **int** | The numeric index of the display order position of this file in the listing, starting at 1. | [optional] 
**filename** | **str** | The file name string for a file associated with a digital listing. | [optional] 
**filesize** | **str** | A human-readable format size string for the size of a file. | [optional] 
**size_bytes** | **int** | A number indicating the size of a file, measured in bytes. | [optional] 
**filetype** | **str** | A type string indicating a file&#39;s MIME type. | [optional] 
**create_timestamp** | **int** | The unique numeric ID of a file associated with a digital listing. | [optional] 
**created_timestamp** | **int** | The unique numeric ID of a file associated with a digital listing. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_listing_file import ShopListingFile

# TODO update the JSON string below
json = "{}"
# create an instance of ShopListingFile from a JSON string
shop_listing_file_instance = ShopListingFile.from_json(json)
# print the JSON string representation of the object
print(ShopListingFile.to_json())

# convert the object into a dict
shop_listing_file_dict = shop_listing_file_instance.to_dict()
# create an instance of ShopListingFile from a dict
shop_listing_file_from_dict = ShopListingFile.from_dict(shop_listing_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


