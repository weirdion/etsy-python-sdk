# ListingImages

Represents a list of listing image resources, each of which contains the reference URLs and metadata for an image.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ListingImage]**](ListingImage.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_images import ListingImages

# TODO update the JSON string below
json = "{}"
# create an instance of ListingImages from a JSON string
listing_images_instance = ListingImages.from_json(json)
# print the JSON string representation of the object
print(ListingImages.to_json())

# convert the object into a dict
listing_images_dict = listing_images_instance.to_dict()
# create an instance of ListingImages from a dict
listing_images_from_dict = ListingImages.from_dict(listing_images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


