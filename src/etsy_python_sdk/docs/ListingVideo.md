# ListingVideo

Reference urls and metadata for a video associated with a specific listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**video_id** | **int** | The unique ID of a video associated with a listing. | [optional] 
**height** | **int** | The video height dimension in pixels. | [optional] 
**width** | **int** | The video width dimension in pixels. | [optional] 
**thumbnail_url** | **str** | The url of the video thumbnail. | [optional] 
**video_url** | **str** | The url of the video file. | [optional] 
**video_state** | **str** | The current state of a given video. Value is one of &#x60;active&#x60;, &#x60;inactive&#x60;, &#x60;deleted&#x60; or &#x60;flagged&#x60;. | [optional] 

## Example

```python
from etsy_python_sdk.models.listing_video import ListingVideo

# TODO update the JSON string below
json = "{}"
# create an instance of ListingVideo from a JSON string
listing_video_instance = ListingVideo.from_json(json)
# print the JSON string representation of the object
print(ListingVideo.to_json())

# convert the object into a dict
listing_video_dict = listing_video_instance.to_dict()
# create an instance of ListingVideo from a dict
listing_video_from_dict = ListingVideo.from_dict(listing_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


