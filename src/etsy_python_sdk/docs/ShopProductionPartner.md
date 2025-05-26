# ShopProductionPartner

Represents a description of a shop production partner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**production_partner_id** | **int** | The numeric ID of a production partner. | [optional] 
**partner_name** | **str** | The name or title of the production partner. | [optional] 
**location** | **str** | A string representing the production partner location. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_production_partner import ShopProductionPartner

# TODO update the JSON string below
json = "{}"
# create an instance of ShopProductionPartner from a JSON string
shop_production_partner_instance = ShopProductionPartner.from_json(json)
# print the JSON string representation of the object
print(ShopProductionPartner.to_json())

# convert the object into a dict
shop_production_partner_dict = shop_production_partner_instance.to_dict()
# create an instance of ShopProductionPartner from a dict
shop_production_partner_from_dict = ShopProductionPartner.from_dict(shop_production_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


