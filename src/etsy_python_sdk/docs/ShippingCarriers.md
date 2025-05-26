# ShippingCarriers

Represents several ShippingCarriers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**results** | [**List[ShippingCarrier]**](ShippingCarrier.md) |  | [optional] 

## Example

```python
from etsy_python_sdk.models.shipping_carriers import ShippingCarriers

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingCarriers from a JSON string
shipping_carriers_instance = ShippingCarriers.from_json(json)
# print the JSON string representation of the object
print(ShippingCarriers.to_json())

# convert the object into a dict
shipping_carriers_dict = shipping_carriers_instance.to_dict()
# create an instance of ShippingCarriers from a dict
shipping_carriers_from_dict = ShippingCarriers.from_dict(shipping_carriers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


