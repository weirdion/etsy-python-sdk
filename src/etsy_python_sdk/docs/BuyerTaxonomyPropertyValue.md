# BuyerTaxonomyPropertyValue

A property value for a specific product property, which may also employ a specific scale.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_id** | **int** | The numeric ID of this property value. | [optional] 
**name** | **str** | The name string of this property value. | [optional] 
**scale_id** | **int** | The numeric scale ID of the scale to which this property value belongs. | [optional] 
**equal_to** | **List[int]** | A list of numeric property value IDs this property value is equal to (if any). | [optional] 

## Example

```python
from etsy_python_sdk.models.buyer_taxonomy_property_value import BuyerTaxonomyPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of BuyerTaxonomyPropertyValue from a JSON string
buyer_taxonomy_property_value_instance = BuyerTaxonomyPropertyValue.from_json(json)
# print the JSON string representation of the object
print(BuyerTaxonomyPropertyValue.to_json())

# convert the object into a dict
buyer_taxonomy_property_value_dict = buyer_taxonomy_property_value_instance.to_dict()
# create an instance of BuyerTaxonomyPropertyValue from a dict
buyer_taxonomy_property_value_from_dict = BuyerTaxonomyPropertyValue.from_dict(buyer_taxonomy_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


