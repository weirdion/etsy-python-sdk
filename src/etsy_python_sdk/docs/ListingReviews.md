# ListingReviews

A set of listing review records left by Users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of TransactionReview resources found. | [optional] 
**results** | [**List[ListingReview]**](ListingReview.md) | The TransactionReview resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_reviews import ListingReviews

# TODO update the JSON string below
json = "{}"
# create an instance of ListingReviews from a JSON string
listing_reviews_instance = ListingReviews.from_json(json)
# print the JSON string representation of the object
print(ListingReviews.to_json())

# convert the object into a dict
listing_reviews_dict = listing_reviews_instance.to_dict()
# create an instance of ListingReviews from a dict
listing_reviews_from_dict = ListingReviews.from_dict(listing_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


