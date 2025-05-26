# TransactionReviews

A set of transaction review records left by Users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of TransactionReview resources found. | [optional] 
**results** | [**List[TransactionReview]**](TransactionReview.md) | The TransactionReview resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.transaction_reviews import TransactionReviews

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionReviews from a JSON string
transaction_reviews_instance = TransactionReviews.from_json(json)
# print the JSON string representation of the object
print(TransactionReviews.to_json())

# convert the object into a dict
transaction_reviews_dict = transaction_reviews_instance.to_dict()
# create an instance of TransactionReviews from a dict
transaction_reviews_from_dict = TransactionReviews.from_dict(transaction_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


