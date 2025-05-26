# TransactionVariations

A list of variations chosen by the buyer during checkout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** | The variation property ID. | [optional] 
**value_id** | **int** | The ID of the variation value selected. | [optional] 
**formatted_name** | **str** | Formatted name of the variation. | [optional] 
**formatted_value** | **str** | Value of the variation entered by the buyer. | [optional] 

## Example

```python
from etsy_python_sdk.models.transaction_variations import TransactionVariations

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionVariations from a JSON string
transaction_variations_instance = TransactionVariations.from_json(json)
# print the JSON string representation of the object
print(TransactionVariations.to_json())

# convert the object into a dict
transaction_variations_dict = transaction_variations_instance.to_dict()
# create an instance of TransactionVariations from a dict
transaction_variations_from_dict = TransactionVariations.from_dict(transaction_variations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


