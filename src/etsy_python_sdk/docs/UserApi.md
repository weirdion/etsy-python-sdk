# etsy_python_sdk.UserApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_me**](UserApi.md#get_me) | **GET** /v3/application/users/me | 
[**get_user**](UserApi.md#get_user) | **GET** /v3/application/users/{user_id} | 


# **get_me**
> ModelSelf get_me()

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Returns basic info for the user making the request.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.model_self import ModelSelf
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
    api_instance = etsy_python_sdk.UserApi(api_client)

    try:
        api_response = api_instance.get_me()
        print("The response of UserApi->get_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelSelf**](ModelSelf.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Fetches basic info about the requesting user |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a user profile based on a unique user ID.                  Access is limited to profiles of the authenticated user                  or linked buyers. For the primary_email field, specific                  app-based permissions are required and granted case-by-case.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.user import User
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
    api_instance = etsy_python_sdk.UserApi(api_client)
    user_id = 56 # int | 

    try:
        api_response = api_instance.get_user(user_id)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single User |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

