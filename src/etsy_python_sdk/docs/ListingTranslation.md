# ListingTranslation

Represents the translation data for a Listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **int** | The numeric ID for the Listing. | [optional] 
**language** | **str** | The IETF language tag (e.g. &#39;fr&#39;) for the language of this translation. | [optional] 
**title** | **str** | The title of the Listing of this Translation. | [optional] 
**description** | **str** | The description of the Listing of this Translation. | [optional] 
**tags** | **List[str]** | The tags of the Listing of this Translation. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_translation import ListingTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of ListingTranslation from a JSON string
listing_translation_instance = ListingTranslation.from_json(json)
# print the JSON string representation of the object
print(ListingTranslation.to_json())

# convert the object into a dict
listing_translation_dict = listing_translation_instance.to_dict()
# create an instance of ListingTranslation from a dict
listing_translation_from_dict = ListingTranslation.from_dict(listing_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


