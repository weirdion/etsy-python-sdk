# ShopHolidayPreference

Represents a shop's holiday preference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** | The unique positive non-zero numeric ID for an Etsy Shop. | [optional] 
**holiday_id** | **str** | The unique id that maps to the holiday a country observes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#country-holidays) for more info | [optional] 
**country_iso** | **str** | The country iso where the shop is located. | [optional] 
**is_working** | **bool** | A boolean value for whether the shop will process orders on a particular holiday. | [optional] 
**holiday_name** | **str** | The name of the holiday that a country observes. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_holiday_preference import ShopHolidayPreference

# TODO update the JSON string below
json = "{}"
# create an instance of ShopHolidayPreference from a JSON string
shop_holiday_preference_instance = ShopHolidayPreference.from_json(json)
# print the JSON string representation of the object
print(ShopHolidayPreference.to_json())

# convert the object into a dict
shop_holiday_preference_dict = shop_holiday_preference_instance.to_dict()
# create an instance of ShopHolidayPreference from a dict
shop_holiday_preference_from_dict = ShopHolidayPreference.from_dict(shop_holiday_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


