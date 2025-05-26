# ShopListings

A set of ShopListing resources.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of ShopListing resources found. | [optional] 
**results** | [**List[ShopListing]**](ShopListing.md) | The ShopListing resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_listings import ShopListings

# TODO update the JSON string below
json = "{}"
# create an instance of ShopListings from a JSON string
shop_listings_instance = ShopListings.from_json(json)
# print the JSON string representation of the object
print(ShopListings.to_json())

# convert the object into a dict
shop_listings_dict = shop_listings_instance.to_dict()
# create an instance of ShopListings from a dict
shop_listings_from_dict = ShopListings.from_dict(shop_listings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


