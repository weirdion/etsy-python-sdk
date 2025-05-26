# Payments

Represents several payments made with Etsy Payments. All monetary amounts are in USD pennies unless otherwise specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of payments in the response. | [optional] 
**results** | [**List[Payment]**](Payment.md) | A list of payments. | [optional] 

## Example

```python
from etsy_python_sdk.models.payments import Payments

# TODO update the JSON string below
json = "{}"
# create an instance of Payments from a JSON string
payments_instance = Payments.from_json(json)
# print the JSON string representation of the object
print(Payments.to_json())

# convert the object into a dict
payments_dict = payments_instance.to_dict()
# create an instance of Payments from a dict
payments_from_dict = Payments.from_dict(payments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


