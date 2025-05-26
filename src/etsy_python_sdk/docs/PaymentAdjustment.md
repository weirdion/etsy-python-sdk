# PaymentAdjustment

Represents a refund, which applies to a prior Etsy payment. All monetary amounts are in USD pennies unless otherwise specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_adjustment_id** | **int** | The numeric ID for a payment adjustment. | [optional] 
**payment_id** | **int** | A unique numeric ID for a payment to a specific Etsy [shop](/documentation/reference#tag/Shop). | [optional] 
**status** | **str** | The status string of the payment adjustment. | [optional] 
**is_success** | **bool** | When true, the payment adjustment was or is likely to complete successfully. | [optional] 
**user_id** | **int** | The numeric ID for the [user](/documentation/reference#tag/User) (seller) fulfilling the purchase. | [optional] 
**reason_code** | **str** | A human-readable string describing the reason for the refund. | [optional] 
**total_adjustment_amount** | **int** | The total numeric amount of the refund in the payment currency. | [optional] 
**shop_total_adjustment_amount** | **int** | The numeric amount of the refund in the shop currency. | [optional] 
**buyer_total_adjustment_amount** | **int** | The numeric amount of the refund in the buyer currency. | [optional] 
**total_fee_adjustment_amount** | **int** | The numeric amount of card processing fees associated with a payment adjustment. | [optional] 
**create_timestamp** | **int** | The transaction\\&#39;s creation date and time, in epoch seconds. | [optional] 
**created_timestamp** | **int** | The transaction\\&#39;s creation date and time, in epoch seconds. | [optional] 
**update_timestamp** | **int** | The date and time of the last change to the payment adjustment in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The date and time of the last change to the payment adjustment in epoch seconds. | [optional] 
**payment_adjustment_items** | [**List[PaymentAdjustmentItem]**](PaymentAdjustmentItem.md) | List of payment adjustment line items. | [optional] 

## Example

```python
from etsy_python_sdk.models.payment_adjustment import PaymentAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAdjustment from a JSON string
payment_adjustment_instance = PaymentAdjustment.from_json(json)
# print the JSON string representation of the object
print(PaymentAdjustment.to_json())

# convert the object into a dict
payment_adjustment_dict = payment_adjustment_instance.to_dict()
# create an instance of PaymentAdjustment from a dict
payment_adjustment_from_dict = PaymentAdjustment.from_dict(payment_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


