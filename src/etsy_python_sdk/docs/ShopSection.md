# ShopSection

A section within a shop, into which a user can sort listings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_section_id** | **int** | The numeric ID of a section in a specific Etsy shop. | [optional] 
**title** | **str** | The title string for a shop section. | [optional] 
**rank** | **int** | The positive non-zero numeric position of this section in the section display order for a shop, with rank 1 sections appearing first. | [optional] 
**user_id** | **int** | The numeric ID of the [user](/documentation/reference#tag/User) who owns this shop section. | [optional] 
**active_listing_count** | **int** | The number of active listings in one section of a specific Etsy shop. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_section import ShopSection

# TODO update the JSON string below
json = "{}"
# create an instance of ShopSection from a JSON string
shop_section_instance = ShopSection.from_json(json)
# print the JSON string representation of the object
print(ShopSection.to_json())

# convert the object into a dict
shop_section_dict = shop_section_instance.to_dict()
# create an instance of ShopSection from a dict
shop_section_from_dict = ShopSection.from_dict(shop_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


