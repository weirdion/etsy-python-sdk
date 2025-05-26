# etsy_python_sdk.ShopListingOfferingApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_listing_offering**](ShopListingOfferingApi.md#get_listing_offering) | **GET** /v3/application/listings/{listing_id}/products/{product_id}/offerings/{product_offering_id} | 


# **get_listing_offering**
> ListingInventoryProductOffering get_listing_offering(listing_id, product_id, product_offering_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Get an Offering for a Listing

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_inventory_product_offering import ListingInventoryProductOffering
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
    api_instance = etsy_python_sdk.ShopListingOfferingApi(api_client)
    listing_id = 56 # int | 
    product_id = 56 # int | 
    product_offering_id = 56 # int | 

    try:
        api_response = api_instance.get_listing_offering(listing_id, product_id, product_offering_id)
        print("The response of ShopListingOfferingApi->get_listing_offering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingOfferingApi->get_listing_offering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**|  | 
 **product_id** | **int**|  | 
 **product_offering_id** | **int**|  | 

### Return type

[**ListingInventoryProductOffering**](ListingInventoryProductOffering.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ListingInventoryProductOffering |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

