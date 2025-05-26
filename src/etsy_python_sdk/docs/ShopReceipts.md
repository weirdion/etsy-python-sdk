# ShopReceipts

The receipts for a specific Shop.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of Shop Receipts found. | [optional] 
**results** | [**List[ShopReceipt]**](ShopReceipt.md) | List of Shop Receipt resources found, with all Shop Receipt fields for each resource. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_receipts import ShopReceipts

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReceipts from a JSON string
shop_receipts_instance = ShopReceipts.from_json(json)
# print the JSON string representation of the object
print(ShopReceipts.to_json())

# convert the object into a dict
shop_receipts_dict = shop_receipts_instance.to_dict()
# create an instance of ShopReceipts from a dict
shop_receipts_from_dict = ShopReceipts.from_dict(shop_receipts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


