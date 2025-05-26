# ShopListingsWithAssociations

A set of ShopListing resources with associations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of ShopListing resources found. | [optional] 
**results** | [**List[ShopListingWithAssociations]**](ShopListingWithAssociations.md) | The ShopListing resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_listings_with_associations import ShopListingsWithAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ShopListingsWithAssociations from a JSON string
shop_listings_with_associations_instance = ShopListingsWithAssociations.from_json(json)
# print the JSON string representation of the object
print(ShopListingsWithAssociations.to_json())

# convert the object into a dict
shop_listings_with_associations_dict = shop_listings_with_associations_instance.to_dict()
# create an instance of ShopListingsWithAssociations from a dict
shop_listings_with_associations_from_dict = ShopListingsWithAssociations.from_dict(shop_listings_with_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


