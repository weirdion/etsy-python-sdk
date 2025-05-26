# ListingVariationImage

A representation of the associations of variations and images on a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The numeric ID of the Property. | [optional] 
**value_id** | **int** | The numeric ID of the Value. | [optional] 
**value** | **str** | The string value of the property. | [optional] 
**image_id** | **int** | The numeric ID of the Image. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_variation_image import ListingVariationImage

# TODO update the JSON string below
json = "{}"
# create an instance of ListingVariationImage from a JSON string
listing_variation_image_instance = ListingVariationImage.from_json(json)
# print the JSON string representation of the object
print(ListingVariationImage.to_json())

# convert the object into a dict
listing_variation_image_dict = listing_variation_image_instance.to_dict()
# create an instance of ListingVariationImage from a dict
listing_variation_image_from_dict = ListingVariationImage.from_dict(listing_variation_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


