# ShopProductionPartners

Represents a list of shop production partners.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ShopProductionPartner]**](ShopProductionPartner.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_production_partners import ShopProductionPartners

# TODO update the JSON string below
json = "{}"
# create an instance of ShopProductionPartners from a JSON string
shop_production_partners_instance = ShopProductionPartners.from_json(json)
# print the JSON string representation of the object
print(ShopProductionPartners.to_json())

# convert the object into a dict
shop_production_partners_dict = shop_production_partners_instance.to_dict()
# create an instance of ShopProductionPartners from a dict
shop_production_partners_from_dict = ShopProductionPartners.from_dict(shop_production_partners_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


