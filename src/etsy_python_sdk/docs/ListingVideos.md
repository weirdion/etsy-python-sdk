# ListingVideos

Represents a list of listing video resources, each of which contains the reference URLs for the videos.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of results. | [optional] 
**results** | [**List[ListingVideo]**](ListingVideo.md) | The list of requested resources. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_videos import ListingVideos

# TODO update the JSON string below
json = "{}"
# create an instance of ListingVideos from a JSON string
listing_videos_instance = ListingVideos.from_json(json)
# print the JSON string representation of the object
print(ListingVideos.to_json())

# convert the object into a dict
listing_videos_dict = listing_videos_instance.to_dict()
# create an instance of ListingVideos from a dict
listing_videos_from_dict = ListingVideos.from_dict(listing_videos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


