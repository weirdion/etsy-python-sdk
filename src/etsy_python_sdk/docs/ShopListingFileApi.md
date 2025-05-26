# etsy_python_sdk.ShopListingFileApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_listing_file**](ShopListingFileApi.md#delete_listing_file) | **DELETE** /v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id} | 
[**get_all_listing_files**](ShopListingFileApi.md#get_all_listing_files) | **GET** /v3/application/shops/{shop_id}/listings/{listing_id}/files | 
[**get_listing_file**](ShopListingFileApi.md#get_listing_file) | **GET** /v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id} | 
[**upload_listing_file**](ShopListingFileApi.md#upload_listing_file) | **POST** /v3/application/shops/{shop_id}/listings/{listing_id}/files | 


# **delete_listing_file**
> delete_listing_file(shop_id, listing_id, listing_file_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Deletes a file from a specific listing. When you delete the final file for a digital listing, the listing converts into a physical listing. The response to a delete request returns a list of the remaining file records associated with the given listing.

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
    api_instance = etsy_python_sdk.ShopListingFileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    listing_file_id = 56 # int | The unique numeric ID of a file associated with a digital listing.

    try:
        api_instance.delete_listing_file(shop_id, listing_id, listing_file_id)
    except Exception as e:
        print("Exception when calling ShopListingFileApi->delete_listing_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **listing_file_id** | **int**| The unique numeric ID of a file associated with a digital listing. | 

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
**409** | There was a request conflict with the current state of the target resource. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**204** | The ShopListingFile resource was correctly deleted |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_listing_files**
> ShopListingFiles get_all_listing_files(listing_id, shop_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves all the files associated with the given digital listing. Requesting files from a physical listing returns an empty result.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing_files import ShopListingFiles
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
    api_instance = etsy_python_sdk.ShopListingFileApi(api_client)
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.

    try:
        api_response = api_instance.get_all_listing_files(listing_id, shop_id)
        print("The response of ShopListingFileApi->get_all_listing_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingFileApi->get_all_listing_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 

### Return type

[**ShopListingFiles**](ShopListingFiles.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of metadata objects for the file resources associated with a listing. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_file**
> ShopListingFile get_listing_file(shop_id, listing_id, listing_file_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a single file associated with the given digital listing. Requesting a file from a physical listing returns an empty result.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing_file import ShopListingFile
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
    api_instance = etsy_python_sdk.ShopListingFileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    listing_file_id = 56 # int | The unique numeric ID of a file associated with a digital listing.

    try:
        api_response = api_instance.get_listing_file(shop_id, listing_id, listing_file_id)
        print("The response of ShopListingFileApi->get_listing_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingFileApi->get_listing_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **listing_file_id** | **int**| The unique numeric ID of a file associated with a digital listing. | 

### Return type

[**ShopListingFile**](ShopListingFile.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The metatdata for a file associated with a digital listing. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_listing_file**
> ShopListingFile upload_listing_file(shop_id, listing_id, listing_file_id=listing_file_id, file=file, name=name, rank=rank)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Uploads a new file for a digital listing, or associates an existing file with a specific listing. You must either provide the `listing_file_id` of an existing file, or the name and binary file data for a file to upload. Associating an existing file to a physical listing converts the physical listing into a digital listing, which removes all shipping costs and any product and inventory variations.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing_file import ShopListingFile
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
    api_instance = etsy_python_sdk.ShopListingFileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    listing_file_id = 56 # int | The unique numeric ID of a file associated with a digital listing. (optional)
    file = None # bytearray | A binary file to upload. (optional)
    name = 'name_example' # str | The file name string of a file to upload (optional)
    rank = 1 # int | The positive non-zero numeric position in the images displayed in a listing, with rank 1 images appearing in the left-most position in a listing. (optional) (default to 1)

    try:
        api_response = api_instance.upload_listing_file(shop_id, listing_id, listing_file_id=listing_file_id, file=file, name=name, rank=rank)
        print("The response of ShopListingFileApi->upload_listing_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingFileApi->upload_listing_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **listing_file_id** | **int**| The unique numeric ID of a file associated with a digital listing. | [optional] 
 **file** | **bytearray**| A binary file to upload. | [optional] 
 **name** | **str**| The file name string of a file to upload | [optional] 
 **rank** | **int**| The positive non-zero numeric position in the images displayed in a listing, with rank 1 images appearing in the left-most position in a listing. | [optional] [default to 1]

### Return type

[**ShopListingFile**](ShopListingFile.md)

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

