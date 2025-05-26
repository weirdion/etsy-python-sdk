# etsy_python_sdk.ShopListingVideoApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_listing_video**](ShopListingVideoApi.md#delete_listing_video) | **DELETE** /v3/application/shops/{shop_id}/listings/{listing_id}/videos/{video_id} | 
[**get_listing_video**](ShopListingVideoApi.md#get_listing_video) | **GET** /v3/application/listings/{listing_id}/videos/{video_id} | 
[**get_listing_videos**](ShopListingVideoApi.md#get_listing_videos) | **GET** /v3/application/listings/{listing_id}/videos | 
[**upload_listing_video**](ShopListingVideoApi.md#upload_listing_video) | **POST** /v3/application/shops/{shop_id}/listings/{listing_id}/videos | 


# **delete_listing_video**
> delete_listing_video(shop_id, listing_id, video_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Open API V3 endpoint to delete a listing video. A copy of the video remains on our servers, and so a deleted video may be re-associated with the listing without re-uploading the original video; see uploadListingVideo.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.etsy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = etsy_python_sdk.Configuration(
    host = "https://openapi.etsy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with etsy_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = etsy_python_sdk.ShopListingVideoApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    video_id = 56 # int | The unique ID of a video associated with a listing.

    try:
        api_instance.delete_listing_video(shop_id, listing_id, video_id)
    except Exception as e:
        print("Exception when calling ShopListingVideoApi->delete_listing_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **video_id** | **int**| The unique ID of a video associated with a listing. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**204** | The ListingVideo resource was correctly deleted |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_video**
> ListingVideo get_listing_video(video_id, listing_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a single video associated with the given listing. Requesting a video from a listing returns an empty result.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_video import ListingVideo
from etsy_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.etsy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = etsy_python_sdk.Configuration(
    host = "https://openapi.etsy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with etsy_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = etsy_python_sdk.ShopListingVideoApi(api_client)
    video_id = 56 # int | The unique ID of a video associated with a listing.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.

    try:
        api_response = api_instance.get_listing_video(video_id, listing_id)
        print("The response of ShopListingVideoApi->get_listing_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingVideoApi->get_listing_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| The unique ID of a video associated with a listing. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 

### Return type

[**ListingVideo**](ListingVideo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metatdata for a video associated with a listing. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_videos**
> ListingVideos get_listing_videos(listing_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves all listing video resources for a listing with a specific listing ID.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_videos import ListingVideos
from etsy_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.etsy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = etsy_python_sdk.Configuration(
    host = "https://openapi.etsy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with etsy_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = etsy_python_sdk.ShopListingVideoApi(api_client)
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.

    try:
        api_response = api_instance.get_listing_videos(listing_id)
        print("The response of ShopListingVideoApi->get_listing_videos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingVideoApi->get_listing_videos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 

### Return type

[**ListingVideos**](ListingVideos.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of videos for a listing |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_listing_video**
> ListingVideo upload_listing_video(shop_id, listing_id, video_id=video_id, video=video, name=name)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Uploads a new video for a listing, or associates an existing video with a specific listing. You must either provide the `video_id` of an existing video, or the name and binary file data for a video to upload.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_video import ListingVideo
from etsy_python_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi.etsy.com
# See configuration.py for a list of all supported configuration parameters.
configuration = etsy_python_sdk.Configuration(
    host = "https://openapi.etsy.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with etsy_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = etsy_python_sdk.ShopListingVideoApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    video_id = 56 # int | The unique ID of a video associated with a listing. (optional)
    video = None # bytearray | A video file to upload. (optional)
    name = 'name_example' # str | The file name string for the video to upload. (optional)

    try:
        api_response = api_instance.upload_listing_video(shop_id, listing_id, video_id=video_id, video=video, name=name)
        print("The response of ShopListingVideoApi->upload_listing_video:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingVideoApi->upload_listing_video: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **video_id** | **int**| The unique ID of a video associated with a listing. | [optional] 
 **video** | **bytearray**| A video file to upload. | [optional] 
 **name** | **str**| The file name string for the video to upload. | [optional] 

### Return type

[**ListingVideo**](ListingVideo.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The metadata for a file associated with a digital listing. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

