# ShopListingFiles

Represents several ShopListingFiles.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of ShopListingFiles being returned.. | [optional] 
**results** | [**List[ShopListingFile]**](ShopListingFile.md) | An array of ShopListingFile resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_listing_files import ShopListingFiles

# TODO update the JSON string below
json = "{}"
# create an instance of ShopListingFiles from a JSON string
shop_listing_files_instance = ShopListingFiles.from_json(json)
# print the JSON string representation of the object
print(ShopListingFiles.to_json())

# convert the object into a dict
shop_listing_files_dict = shop_listing_files_instance.to_dict()
# create an instance of ShopListingFiles from a dict
shop_listing_files_from_dict = ShopListingFiles.from_dict(shop_listing_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


