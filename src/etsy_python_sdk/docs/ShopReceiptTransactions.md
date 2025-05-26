# ShopReceiptTransactions

A set of ShopReceiptTransaction resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of ShopReceiptTransaction resources found. | [optional] 
**results** | [**List[ShopReceiptTransaction]**](ShopReceiptTransaction.md) | The ShopReceiptTransaction resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_receipt_transactions import ShopReceiptTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReceiptTransactions from a JSON string
shop_receipt_transactions_instance = ShopReceiptTransactions.from_json(json)
# print the JSON string representation of the object
print(ShopReceiptTransactions.to_json())

# convert the object into a dict
shop_receipt_transactions_dict = shop_receipt_transactions_instance.to_dict()
# create an instance of ShopReceiptTransactions from a dict
shop_receipt_transactions_from_dict = ShopReceiptTransactions.from_dict(shop_receipt_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


