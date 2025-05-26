# ShippingCarrier

A supported shipping carrier, which is used to calculate an Estimated Delivery Date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_carrier_id** | **int** | The numeric ID of this shipping carrier. | [optional] 
**name** | **str** | The name of this shipping carrier. | [optional] 
**domestic_classes** | [**List[ShippingCarrierMailClass]**](ShippingCarrierMailClass.md) | Set of domestic mail classes of this shipping carrier. | [optional] 
**international_classes** | [**List[ShippingCarrierMailClass]**](ShippingCarrierMailClass.md) | Set of international mail classes of this shipping carrier. | [optional] 

## Example

```python
from etsy_python_sdk.models.shipping_carrier import ShippingCarrier

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCarrier from a JSON string
shipping_carrier_instance = ShippingCarrier.from_json(json)
# print the JSON string representation of the object
print(ShippingCarrier.to_json())

# convert the object into a dict
shipping_carrier_dict = shipping_carrier_instance.to_dict()
# create an instance of ShippingCarrier from a dict
shipping_carrier_from_dict = ShippingCarrier.from_dict(shipping_carrier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


