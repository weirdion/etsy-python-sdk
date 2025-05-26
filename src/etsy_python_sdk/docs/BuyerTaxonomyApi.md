# etsy_python_sdk.BuyerTaxonomyApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_buyer_taxonomy_nodes**](BuyerTaxonomyApi.md#get_buyer_taxonomy_nodes) | **GET** /v3/application/buyer-taxonomy/nodes | 
[**get_properties_by_buyer_taxonomy_id**](BuyerTaxonomyApi.md#get_properties_by_buyer_taxonomy_id) | **GET** /v3/application/buyer-taxonomy/nodes/{taxonomy_id}/properties | 


# **get_buyer_taxonomy_nodes**
> BuyerTaxonomyNodes get_buyer_taxonomy_nodes()

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves the full hierarchy tree of buyer taxonomy nodes.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.buyer_taxonomy_nodes import BuyerTaxonomyNodes
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
    api_instance = etsy_python_sdk.BuyerTaxonomyApi(api_client)

    try:
        api_response = api_instance.get_buyer_taxonomy_nodes()
        print("The response of BuyerTaxonomyApi->get_buyer_taxonomy_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerTaxonomyApi->get_buyer_taxonomy_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BuyerTaxonomyNodes**](BuyerTaxonomyNodes.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the full hierarchy tree of buyer taxonomy nodes. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties_by_buyer_taxonomy_id**
> BuyerTaxonomyNodeProperties get_properties_by_buyer_taxonomy_id(taxonomy_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a list of product properties, with applicable scales and values, supported for a specific buyer taxonomy ID.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.buyer_taxonomy_node_properties import BuyerTaxonomyNodeProperties
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
    api_instance = etsy_python_sdk.BuyerTaxonomyApi(api_client)
    taxonomy_id = 56 # int | The unique numeric ID of an Etsy taxonomy node, which is a metadata category for listings organized into the seller taxonomy hierarchy tree. For example, the \"shoes\" taxonomy node (ID: 1429, level: 1) is higher in the hierarchy than \"girls' shoes\" (ID: 1440, level: 2). The taxonomy nodes assigned to a listing support access to specific standardized product scales and properties. For example, listings assigned the taxonomy nodes \"shoes\" or \"girls' shoes\" support access to the \"EU\" shoe size scale with its associated property names and IDs for EU shoe sizes, such as property `value_id`:\"1394\", and `name`:\"38\".

    try:
        api_response = api_instance.get_properties_by_buyer_taxonomy_id(taxonomy_id)
        print("The response of BuyerTaxonomyApi->get_properties_by_buyer_taxonomy_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BuyerTaxonomyApi->get_properties_by_buyer_taxonomy_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **taxonomy_id** | **int**| The unique numeric ID of an Etsy taxonomy node, which is a metadata category for listings organized into the seller taxonomy hierarchy tree. For example, the \&quot;shoes\&quot; taxonomy node (ID: 1429, level: 1) is higher in the hierarchy than \&quot;girls&#39; shoes\&quot; (ID: 1440, level: 2). The taxonomy nodes assigned to a listing support access to specific standardized product scales and properties. For example, listings assigned the taxonomy nodes \&quot;shoes\&quot; or \&quot;girls&#39; shoes\&quot; support access to the \&quot;EU\&quot; shoe size scale with its associated property names and IDs for EU shoe sizes, such as property &#x60;value_id&#x60;:\&quot;1394\&quot;, and &#x60;name&#x60;:\&quot;38\&quot;. | 

### Return type

[**BuyerTaxonomyNodeProperties**](BuyerTaxonomyNodeProperties.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of product properties, with applicable scales and values. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

