# ShopReceiptShipment

The record of one shipment event for a ShopReceipt. A receipt may have many ShopReceiptShipment records.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt_shipping_id** | **int** | The unique numeric ID of a Shop Receipt Shipment record. | [optional] 
**shipment_notification_timestamp** | **int** | The time at which Etsy notified the buyer of the shipment event, in epoch seconds. | [optional] 
**carrier_name** | **str** | The name string for the carrier/company responsible for delivering the shipment. | [optional] 
**tracking_code** | **str** | The tracking code string provided by the carrier/company for the shipment. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_receipt_shipment import ShopReceiptShipment

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReceiptShipment from a JSON string
shop_receipt_shipment_instance = ShopReceiptShipment.from_json(json)
# print the JSON string representation of the object
print(ShopReceiptShipment.to_json())

# convert the object into a dict
shop_receipt_shipment_dict = shop_receipt_shipment_instance.to_dict()
# create an instance of ShopReceiptShipment from a dict
shop_receipt_shipment_from_dict = ShopReceiptShipment.from_dict(shop_receipt_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


