# ShopRefund

The refund record for a receipt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Money**](Money.md) | A number equal to the refund total. | [optional] 
**created_timestamp** | **int** | The date &amp; time of the refund, in epoch seconds. | [optional] 
**reason** | **str** | The reason string given for the refund. | [optional] 
**note_from_issuer** | **str** | The note string created by the refund issuer. | [optional] 
**status** | **str** | The status indication string for the refund. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_refund import ShopRefund

# TODO update the JSON string below
json = "{}"
# create an instance of ShopRefund from a JSON string
shop_refund_instance = ShopRefund.from_json(json)
# print the JSON string representation of the object
print(ShopRefund.to_json())

# convert the object into a dict
shop_refund_dict = shop_refund_instance.to_dict()
# create an instance of ShopRefund from a dict
shop_refund_from_dict = ShopRefund.from_dict(shop_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


