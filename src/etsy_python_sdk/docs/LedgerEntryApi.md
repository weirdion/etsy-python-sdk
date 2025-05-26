# etsy_python_sdk.LedgerEntryApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shop_payment_account_ledger_entries**](LedgerEntryApi.md#get_shop_payment_account_ledger_entries) | **GET** /v3/application/shops/{shop_id}/payment-account/ledger-entries | 
[**get_shop_payment_account_ledger_entry**](LedgerEntryApi.md#get_shop_payment_account_ledger_entry) | **GET** /v3/application/shops/{shop_id}/payment-account/ledger-entries/{ledger_entry_id} | 


# **get_shop_payment_account_ledger_entries**
> PaymentAccountLedgerEntries get_shop_payment_account_ledger_entries(shop_id, min_created, max_created, limit=limit, offset=offset)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Get a Shop Payment Account Ledger's Entries

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.payment_account_ledger_entries import PaymentAccountLedgerEntries
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
    api_instance = etsy_python_sdk.LedgerEntryApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    min_created = 56 # int | The earliest unix timestamp for when a record was created.
    max_created = 56 # int | The latest unix timestamp for when a record was created.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)

    try:
        api_response = api_instance.get_shop_payment_account_ledger_entries(shop_id, min_created, max_created, limit=limit, offset=offset)
        print("The response of LedgerEntryApi->get_shop_payment_account_ledger_entries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerEntryApi->get_shop_payment_account_ledger_entries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **min_created** | **int**| The earliest unix timestamp for when a record was created. | 
 **max_created** | **int**| The latest unix timestamp for when a record was created. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]

### Return type

[**PaymentAccountLedgerEntries**](PaymentAccountLedgerEntries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of PaymentAccountLedgerEntries |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_payment_account_ledger_entry**
> PaymentAccountLedgerEntry get_shop_payment_account_ledger_entry(shop_id, ledger_entry_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Get a single Shop Payment Account Ledger's Entry

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.payment_account_ledger_entry import PaymentAccountLedgerEntry
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
    api_instance = etsy_python_sdk.LedgerEntryApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    ledger_entry_id = 56 # int | The unique ID of the shop owner ledger entry.

    try:
        api_response = api_instance.get_shop_payment_account_ledger_entry(shop_id, ledger_entry_id)
        print("The response of LedgerEntryApi->get_shop_payment_account_ledger_entry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LedgerEntryApi->get_shop_payment_account_ledger_entry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **ledger_entry_id** | **int**| The unique ID of the shop owner ledger entry. | 

### Return type

[**PaymentAccountLedgerEntry**](PaymentAccountLedgerEntry.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single of PaymentAccountLedgerEntry |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

