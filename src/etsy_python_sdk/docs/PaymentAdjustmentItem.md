# PaymentAdjustmentItem

A payemnt adjustment line item for a payment adjustment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_adjustment_id** | **int** | The numeric ID for a payment adjustment. | [optional] 
**payment_adjustment_item_id** | **int** | Unique ID for the adjustment line item. | [optional] 
**adjustment_type** | **str** | String indicating the type of adjustment for this line item. | [optional] 
**amount** | **int** | Integer value for the amount of the adjustment in original currency. | [optional] [default to 0]
**shop_amount** | **int** | Integer value for the amount of the adjustment in currency for the shop. | [optional] [default to 0]
**transaction_id** | **int** | The unique numeric ID for a transaction. | [optional] 
**bill_payment_id** | **int** | Unique ID for the bill payment adjustment. | [optional] 
**created_timestamp** | **int** | The transaction\\&#39;s creation date and time, in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The update date and time the payment adjustment in epoch seconds. | [optional] 

## Example

```python
from etsy_python_sdk.models.payment_adjustment_item import PaymentAdjustmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAdjustmentItem from a JSON string
payment_adjustment_item_instance = PaymentAdjustmentItem.from_json(json)
# print the JSON string representation of the object
print(PaymentAdjustmentItem.to_json())

# convert the object into a dict
payment_adjustment_item_dict = payment_adjustment_item_instance.to_dict()
# create an instance of PaymentAdjustmentItem from a dict
payment_adjustment_item_from_dict = PaymentAdjustmentItem.from_dict(payment_adjustment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


