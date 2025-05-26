# ListingPropertyValue

A representation of structured data values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The numeric ID of the Property. | [optional] 
**property_name** | **str** | The name of the Property. | [optional] 
**scale_id** | **int** | The numeric ID of the scale (if any). | [optional] 
**scale_name** | **str** | The label used to describe the chosen scale (if any). | [optional] 
**value_ids** | **List[int]** | The numeric IDs of the Property values | [optional] 
**values** | **List[str]** | The Property values | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_property_value import ListingPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of ListingPropertyValue from a JSON string
listing_property_value_instance = ListingPropertyValue.from_json(json)
# print the JSON string representation of the object
print(ListingPropertyValue.to_json())

# convert the object into a dict
listing_property_value_dict = listing_property_value_instance.to_dict()
# create an instance of ListingPropertyValue from a dict
listing_property_value_from_dict = ListingPropertyValue.from_dict(listing_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


