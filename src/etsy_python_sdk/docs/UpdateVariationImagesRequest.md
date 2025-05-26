# UpdateVariationImagesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variation_images** | [**List[UpdateVariationImagesRequestVariationImagesInner]**](UpdateVariationImagesRequestVariationImagesInner.md) | A list of variation image data. | 

## Example

```python
from etsy_python_sdk.models.update_variation_images_request import UpdateVariationImagesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVariationImagesRequest from a JSON string
update_variation_images_request_instance = UpdateVariationImagesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVariationImagesRequest.to_json())

# convert the object into a dict
update_variation_images_request_dict = update_variation_images_request_instance.to_dict()
# create an instance of UpdateVariationImagesRequest from a dict
update_variation_images_request_from_dict = UpdateVariationImagesRequest.from_dict(update_variation_images_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


