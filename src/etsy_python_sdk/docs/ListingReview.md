# ListingReview

A listing review record left by a User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** | The shop&#39;s numeric ID. | [optional] 
**listing_id** | **int** | The ID of the ShopListing that the TransactionReview belongs to. | [optional] 
**rating** | **int** | Rating value on scale from 1 to 5 | [optional] 
**review** | **str** | A message left by the author, explaining the feedback, if provided. | [optional] 
**language** | **str** | The language of the TransactionReview | [optional] 
**image_url_fullxfull** | **str** | The url to a photo provided with the feedback, dimensions fullxfull. Note: This field may be absent, depending on the buyer&#39;s privacy settings. | [optional] 
**create_timestamp** | **int** | The date and time the TransactionReview was created in epoch seconds. | [optional] 
**created_timestamp** | **int** | The date and time the TransactionReview was created in epoch seconds. | [optional] 
**update_timestamp** | **int** | The date and time the TransactionReview was updated in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The date and time the TransactionReview was updated in epoch seconds. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_review import ListingReview

# TODO update the JSON string below
json = "{}"
# create an instance of ListingReview from a JSON string
listing_review_instance = ListingReview.from_json(json)
# print the JSON string representation of the object
print(ListingReview.to_json())

# convert the object into a dict
listing_review_dict = listing_review_instance.to_dict()
# create an instance of ListingReview from a dict
listing_review_from_dict = ListingReview.from_dict(listing_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


