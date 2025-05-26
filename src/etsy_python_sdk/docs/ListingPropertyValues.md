# ListingPropertyValues

Represents several ListingPropertyValues.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[ListingPropertyValue]**](ListingPropertyValue.md) |  | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_property_values import ListingPropertyValues

# TODO update the JSON string below
json = "{}"
# create an instance of ListingPropertyValues from a JSON string
listing_property_values_instance = ListingPropertyValues.from_json(json)
# print the JSON string representation of the object
print(ListingPropertyValues.to_json())

# convert the object into a dict
listing_property_values_dict = listing_property_values_instance.to_dict()
# create an instance of ListingPropertyValues from a dict
listing_property_values_from_dict = ListingPropertyValues.from_dict(listing_property_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


