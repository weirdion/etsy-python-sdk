# ShippingCarrierMailClass

A shipping carrier's mail class, which is used to calculate an Estimated Delivery Date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mail_class_key** | **str** | The unique identifier of this mail class. | [optional] 
**name** | **str** | The name of this mail class. | [optional] 

## Example

```python
from etsy_python_sdk.models.shipping_carrier_mail_class import ShippingCarrierMailClass

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCarrierMailClass from a JSON string
shipping_carrier_mail_class_instance = ShippingCarrierMailClass.from_json(json)
# print the JSON string representation of the object
print(ShippingCarrierMailClass.to_json())

# convert the object into a dict
shipping_carrier_mail_class_dict = shipping_carrier_mail_class_instance.to_dict()
# create an instance of ShippingCarrierMailClass from a dict
shipping_carrier_mail_class_from_dict = ShippingCarrierMailClass.from_dict(shipping_carrier_mail_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


