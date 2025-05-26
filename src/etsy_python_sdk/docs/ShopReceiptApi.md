# etsy_python_sdk.ShopReceiptApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_receipt_shipment**](ShopReceiptApi.md#create_receipt_shipment) | **POST** /v3/application/shops/{shop_id}/receipts/{receipt_id}/tracking | 
[**get_shop_receipt**](ShopReceiptApi.md#get_shop_receipt) | **GET** /v3/application/shops/{shop_id}/receipts/{receipt_id} | 
[**get_shop_receipts**](ShopReceiptApi.md#get_shop_receipts) | **GET** /v3/application/shops/{shop_id}/receipts | 
[**update_shop_receipt**](ShopReceiptApi.md#update_shop_receipt) | **PUT** /v3/application/shops/{shop_id}/receipts/{receipt_id} | 


# **create_receipt_shipment**
> ShopReceipt create_receipt_shipment(shop_id, receipt_id, tracking_code=tracking_code, carrier_name=carrier_name, send_bcc=send_bcc, note_to_buyer=note_to_buyer)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Submits tracking information for a Shop Receipt, which creates a Shop Receipt Shipment entry for the given receipt_id. Each time you successfully submit tracking info, Etsy sends a notification email to the buyer User. When send_bcc is true, Etsy sends shipping notifications to the seller as well. When tracking_code and carrier_name aren't sent, the receipt is marked as shipped only. If the carrier is not supported, you may use `other` as the carrier name so you can provide the tracking code. **NOTES** When shipping within the United States AND the order is over $10 _or_ when shipping to India, tracking code and carrier name ARE required. Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_receipt import ShopReceipt
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
    api_instance = etsy_python_sdk.ShopReceiptApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    receipt_id = 56 # int | The receipt to submit tracking for.
    tracking_code = 'tracking_code_example' # str | The tracking code for this receipt. (optional)
    carrier_name = 'carrier_name_example' # str | The carrier name for this receipt. (optional)
    send_bcc = True # bool | If true, the shipping notification will be sent to the seller as well (optional)
    note_to_buyer = 'note_to_buyer_example' # str | Message to include in notification to the buyer. (optional)

    try:
        api_response = api_instance.create_receipt_shipment(shop_id, receipt_id, tracking_code=tracking_code, carrier_name=carrier_name, send_bcc=send_bcc, note_to_buyer=note_to_buyer)
        print("The response of ShopReceiptApi->create_receipt_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopReceiptApi->create_receipt_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **receipt_id** | **int**| The receipt to submit tracking for. | 
 **tracking_code** | **str**| The tracking code for this receipt. | [optional] 
 **carrier_name** | **str**| The carrier name for this receipt. | [optional] 
 **send_bcc** | **bool**| If true, the shipping notification will be sent to the seller as well | [optional] 
 **note_to_buyer** | **str**| Message to include in notification to the buyer. | [optional] 

### Return type

[**ShopReceipt**](ShopReceipt.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ShopReceipt |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**409** | There was a request conflict with the current state of the target resource. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_receipt**
> ShopReceipt get_shop_receipt(shop_id, receipt_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a receipt, identified by a receipt id, from an Etsy shop. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_receipt import ShopReceipt
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
    api_instance = etsy_python_sdk.ShopReceiptApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    receipt_id = 56 # int | The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction.

    try:
        api_response = api_instance.get_shop_receipt(shop_id, receipt_id)
        print("The response of ShopReceiptApi->get_shop_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopReceiptApi->get_shop_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **receipt_id** | **int**| The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction. | 

### Return type

[**ShopReceipt**](ShopReceipt.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single Shop Receipt |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_receipts**
> ShopReceipts get_shop_receipts(shop_id, min_created=min_created, max_created=max_created, min_last_modified=min_last_modified, max_last_modified=max_last_modified, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order, was_paid=was_paid, was_shipped=was_shipped, was_delivered=was_delivered, was_canceled=was_canceled)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Requests the Shop Receipts from a specific Shop, unfiltered or filtered by receipt id range or offset, date, paid, and/or shipped purchases. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_receipts import ShopReceipts
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
    api_instance = etsy_python_sdk.ShopReceiptApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    min_created = 56 # int | The earliest unix timestamp for when a record was created. (optional)
    max_created = 56 # int | The latest unix timestamp for when a record was created. (optional)
    min_last_modified = 56 # int | The earliest unix timestamp for when a record last changed. (optional)
    max_last_modified = 56 # int | The latest unix timestamp for when a record last changed. (optional)
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)
    sort_on = created # str | The value to sort a search result of listings on. (optional) (default to created)
    sort_order = desc # str | The ascending(up) or descending(down) order to sort receipts by. (optional) (default to desc)
    was_paid = True # bool | When `true`, returns receipts where the seller has recieved payment for the receipt. When `false`, returns receipts where payment has not been received. (optional)
    was_shipped = True # bool | When `true`, returns receipts where the seller shipped the product(s) in this receipt. When `false`, returns receipts where shipment has not been set. (optional)
    was_delivered = True # bool | When `true`, returns receipts that have been marked as delivered. When `false`, returns receipts where shipment has not been marked as delivered. (optional)
    was_canceled = True # bool | When `true`, the endpoint will only return the canceled receipts. When `false`, the endpoint will only return non-canceled receipts. (optional)

    try:
        api_response = api_instance.get_shop_receipts(shop_id, min_created=min_created, max_created=max_created, min_last_modified=min_last_modified, max_last_modified=max_last_modified, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order, was_paid=was_paid, was_shipped=was_shipped, was_delivered=was_delivered, was_canceled=was_canceled)
        print("The response of ShopReceiptApi->get_shop_receipts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopReceiptApi->get_shop_receipts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **min_created** | **int**| The earliest unix timestamp for when a record was created. | [optional] 
 **max_created** | **int**| The latest unix timestamp for when a record was created. | [optional] 
 **min_last_modified** | **int**| The earliest unix timestamp for when a record last changed. | [optional] 
 **max_last_modified** | **int**| The latest unix timestamp for when a record last changed. | [optional] 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]
 **sort_on** | **str**| The value to sort a search result of listings on. | [optional] [default to created]
 **sort_order** | **str**| The ascending(up) or descending(down) order to sort receipts by. | [optional] [default to desc]
 **was_paid** | **bool**| When &#x60;true&#x60;, returns receipts where the seller has recieved payment for the receipt. When &#x60;false&#x60;, returns receipts where payment has not been received. | [optional] 
 **was_shipped** | **bool**| When &#x60;true&#x60;, returns receipts where the seller shipped the product(s) in this receipt. When &#x60;false&#x60;, returns receipts where shipment has not been set. | [optional] 
 **was_delivered** | **bool**| When &#x60;true&#x60;, returns receipts that have been marked as delivered. When &#x60;false&#x60;, returns receipts where shipment has not been marked as delivered. | [optional] 
 **was_canceled** | **bool**| When &#x60;true&#x60;, the endpoint will only return the canceled receipts. When &#x60;false&#x60;, the endpoint will only return non-canceled receipts. | [optional] 

### Return type

[**ShopReceipts**](ShopReceipts.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Shop Receipts |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_receipt**
> ShopReceipt update_shop_receipt(shop_id, receipt_id, was_shipped=was_shipped, was_paid=was_paid)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates the status of a receipt, identified by a receipt id, from an Etsy shop. **NOTE** Access to ShopReceipt's first_line, second_line, city, state, zip, country_iso and formatted_address is contingent in some regions to a preferred partnership status with Etsy

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_receipt import ShopReceipt
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
    api_instance = etsy_python_sdk.ShopReceiptApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    receipt_id = 56 # int | The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction.
    was_shipped = True # bool | When `true`, returns receipts where the seller shipped the product(s) in this receipt. When `false`, returns receipts where shipment has not been set. (optional)
    was_paid = True # bool | When `true`, returns receipts where the seller has recieved payment for the receipt. When `false`, returns receipts where payment has not been received. (optional)

    try:
        api_response = api_instance.update_shop_receipt(shop_id, receipt_id, was_shipped=was_shipped, was_paid=was_paid)
        print("The response of ShopReceiptApi->update_shop_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopReceiptApi->update_shop_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **receipt_id** | **int**| The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction. | 
 **was_shipped** | **bool**| When &#x60;true&#x60;, returns receipts where the seller shipped the product(s) in this receipt. When &#x60;false&#x60;, returns receipts where shipment has not been set. | [optional] 
 **was_paid** | **bool**| When &#x60;true&#x60;, returns receipts where the seller has recieved payment for the receipt. When &#x60;false&#x60;, returns receipts where payment has not been received. | [optional] 

### Return type

[**ShopReceipt**](ShopReceipt.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update A Shop Receipt |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

