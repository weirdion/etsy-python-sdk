# ListingTranslations

Container for all current supported translations of a listing. Note that Etsy periodically adds/removes languages, so this list may change in the future.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**de** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**en_gb** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**en_in** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**en_us** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**es** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**fr** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**it** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**ja** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**nl** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**pl** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**pt** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 
**ru** | [**ListingTranslation**](ListingTranslation.md) |  | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_translations import ListingTranslations

# TODO update the JSON string below
json = "{}"
# create an instance of ListingTranslations from a JSON string
listing_translations_instance = ListingTranslations.from_json(json)
# print the JSON string representation of the object
print(ListingTranslations.to_json())

# convert the object into a dict
listing_translations_dict = listing_translations_instance.to_dict()
# create an instance of ListingTranslations from a dict
listing_translations_from_dict = ListingTranslations.from_dict(listing_translations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


