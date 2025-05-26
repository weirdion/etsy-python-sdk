# etsy_python_sdk.ShopShippingProfileApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shop_shipping_profile**](ShopShippingProfileApi.md#create_shop_shipping_profile) | **POST** /v3/application/shops/{shop_id}/shipping-profiles | 
[**create_shop_shipping_profile_destination**](ShopShippingProfileApi.md#create_shop_shipping_profile_destination) | **POST** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations | 
[**create_shop_shipping_profile_upgrade**](ShopShippingProfileApi.md#create_shop_shipping_profile_upgrade) | **POST** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades | 
[**delete_shop_shipping_profile**](ShopShippingProfileApi.md#delete_shop_shipping_profile) | **DELETE** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id} | 
[**delete_shop_shipping_profile_destination**](ShopShippingProfileApi.md#delete_shop_shipping_profile_destination) | **DELETE** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id} | 
[**delete_shop_shipping_profile_upgrade**](ShopShippingProfileApi.md#delete_shop_shipping_profile_upgrade) | **DELETE** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id} | 
[**get_shipping_carriers**](ShopShippingProfileApi.md#get_shipping_carriers) | **GET** /v3/application/shipping-carriers | 
[**get_shop_shipping_profile**](ShopShippingProfileApi.md#get_shop_shipping_profile) | **GET** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id} | 
[**get_shop_shipping_profile_destinations_by_shipping_profile**](ShopShippingProfileApi.md#get_shop_shipping_profile_destinations_by_shipping_profile) | **GET** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations | 
[**get_shop_shipping_profile_upgrades**](ShopShippingProfileApi.md#get_shop_shipping_profile_upgrades) | **GET** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades | 
[**get_shop_shipping_profiles**](ShopShippingProfileApi.md#get_shop_shipping_profiles) | **GET** /v3/application/shops/{shop_id}/shipping-profiles | 
[**update_shop_shipping_profile**](ShopShippingProfileApi.md#update_shop_shipping_profile) | **PUT** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id} | 
[**update_shop_shipping_profile_destination**](ShopShippingProfileApi.md#update_shop_shipping_profile_destination) | **PUT** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/destinations/{shipping_profile_destination_id} | 
[**update_shop_shipping_profile_upgrade**](ShopShippingProfileApi.md#update_shop_shipping_profile_upgrade) | **PUT** /v3/application/shops/{shop_id}/shipping-profiles/{shipping_profile_id}/upgrades/{upgrade_id} | 


# **create_shop_shipping_profile**
> ShopShippingProfile create_shop_shipping_profile(shop_id, title, origin_country_iso, primary_cost, secondary_cost, min_processing_time, max_processing_time, processing_time_unit=processing_time_unit, destination_country_iso=destination_country_iso, destination_region=destination_region, origin_postal_code=origin_postal_code, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Creates a new ShippingProfile. You can pass a country iso code or a region when creating a ShippingProfile, but not both. Only one is required. You must pass either a shipping_carrier_id AND mail_class, or both min and max_delivery_days.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile import ShopShippingProfile
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    title = 'title_example' # str | The name string of this shipping profile.
    origin_country_iso = 'origin_country_iso_example' # str | The ISO code of the country from which the listing ships.
    primary_cost = 3.4 # float | The cost of shipping to this country/region alone, measured in the store's default currency.
    secondary_cost = 3.4 # float | The cost of shipping to this country/region with another item, measured in the store's default currency.
    min_processing_time = 56 # int | The minimum time required to process to ship listings with this shipping profile.
    max_processing_time = 56 # int | The maximum processing time the listing needs to ship.
    processing_time_unit = business_days # str | The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to \\\"business_days\\\". (optional) (default to business_days)
    destination_country_iso = 'destination_country_iso_example' # str | The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. (optional)
    destination_region = none # str | The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. (optional) (default to none)
    origin_postal_code = '' # str | The postal code string (not necessarily a number) for the location from which the listing ships. Required if the `origin_country_iso` supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info (optional) (default to '')
    shipping_carrier_id = 0 # int | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null. (optional) (default to 0)
    mail_class = 'mail_class_example' # str | The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    min_delivery_days = 56 # int | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null. (optional)
    max_delivery_days = 56 # int | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null. (optional)

    try:
        api_response = api_instance.create_shop_shipping_profile(shop_id, title, origin_country_iso, primary_cost, secondary_cost, min_processing_time, max_processing_time, processing_time_unit=processing_time_unit, destination_country_iso=destination_country_iso, destination_region=destination_region, origin_postal_code=origin_postal_code, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)
        print("The response of ShopShippingProfileApi->create_shop_shipping_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->create_shop_shipping_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **title** | **str**| The name string of this shipping profile. | 
 **origin_country_iso** | **str**| The ISO code of the country from which the listing ships. | 
 **primary_cost** | **float**| The cost of shipping to this country/region alone, measured in the store&#39;s default currency. | 
 **secondary_cost** | **float**| The cost of shipping to this country/region with another item, measured in the store&#39;s default currency. | 
 **min_processing_time** | **int**| The minimum time required to process to ship listings with this shipping profile. | 
 **max_processing_time** | **int**| The maximum processing time the listing needs to ship. | 
 **processing_time_unit** | **str**| The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to \\\&quot;business_days\\\&quot;. | [optional] [default to business_days]
 **destination_country_iso** | **str**| The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. | [optional] 
 **destination_region** | **str**| The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If &#x60;none&#x60;, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. | [optional] [default to none]
 **origin_postal_code** | **str**| The postal code string (not necessarily a number) for the location from which the listing ships. Required if the &#x60;origin_country_iso&#x60; supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info | [optional] [default to &#39;&#39;]
 **shipping_carrier_id** | **int**| The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] [default to 0]
 **mail_class** | **str**| The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **min_delivery_days** | **int**| The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
 **max_delivery_days** | **int**| The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

### Return type

[**ShopShippingProfile**](ShopShippingProfile.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ShippingProfile |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shop_shipping_profile_destination**
> ShopShippingProfileDestination create_shop_shipping_profile_destination(shop_id, shipping_profile_id, primary_cost, secondary_cost, destination_country_iso=destination_country_iso, destination_region=destination_region, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Creates a new shipping destination, which sets the shipping cost, carrier, and class for a destination in a [shipping profile](/documentation/reference/#tag/Shop-ShippingProfile). createShopShippingProfileDestination assigns costs using the currency of the associated shop. Set the destination using either `destination_country_iso` or `destination_region`; `destination_country_iso` and `destination_region` are mutually exclusive — set one or the other. Setting both triggers error 400. If the request sets neither `destination_country_iso` nor `destination_region`, the default destination is "everywhere". You must also either assign both a `shipping_carrier_id` AND `mail_class` or both `min_delivery_days` AND `max_delivery_days`.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_destination import ShopShippingProfileDestination
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    primary_cost = 3.4 # float | The cost of shipping to this country/region alone, measured in the store's default currency.
    secondary_cost = 3.4 # float | The cost of shipping to this country/region with another item, measured in the store's default currency.
    destination_country_iso = 'destination_country_iso_example' # str | The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. (optional)
    destination_region = none # str | The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. (optional) (default to none)
    shipping_carrier_id = 0 # int | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null. (optional) (default to 0)
    mail_class = 'mail_class_example' # str | The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    min_delivery_days = 56 # int | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null. (optional)
    max_delivery_days = 56 # int | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null. (optional)

    try:
        api_response = api_instance.create_shop_shipping_profile_destination(shop_id, shipping_profile_id, primary_cost, secondary_cost, destination_country_iso=destination_country_iso, destination_region=destination_region, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)
        print("The response of ShopShippingProfileApi->create_shop_shipping_profile_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->create_shop_shipping_profile_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **primary_cost** | **float**| The cost of shipping to this country/region alone, measured in the store&#39;s default currency. | 
 **secondary_cost** | **float**| The cost of shipping to this country/region with another item, measured in the store&#39;s default currency. | 
 **destination_country_iso** | **str**| The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. | [optional] 
 **destination_region** | **str**| The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If &#x60;none&#x60;, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. | [optional] [default to none]
 **shipping_carrier_id** | **int**| The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] [default to 0]
 **mail_class** | **str**| The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **min_delivery_days** | **int**| The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
 **max_delivery_days** | **int**| The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

### Return type

[**ShopShippingProfileDestination**](ShopShippingProfileDestination.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A single shipping destination. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shop_shipping_profile_upgrade**
> ShopShippingProfileUpgrade create_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, type, upgrade_name, price, secondary_price, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Creates a new shipping profile upgrade, which can establish a price for a shipping option, such as an alternate carrier or faster delivery.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_upgrade import ShopShippingProfileUpgrade
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    type = 'type_example' # str | The type of the shipping upgrade. Domestic (0) or international (1).
    upgrade_name = 'upgrade_name_example' # str | Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority.
    price = 3.4 # float | Additional cost of adding the shipping upgrade.
    secondary_price = 3.4 # float | Additional cost of adding the shipping upgrade for each additional item.
    shipping_carrier_id = 0 # int | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null. (optional) (default to 0)
    mail_class = 'mail_class_example' # str | The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    min_delivery_days = 56 # int | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null. (optional)
    max_delivery_days = 56 # int | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null. (optional)

    try:
        api_response = api_instance.create_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, type, upgrade_name, price, secondary_price, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)
        print("The response of ShopShippingProfileApi->create_shop_shipping_profile_upgrade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->create_shop_shipping_profile_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **type** | **str**| The type of the shipping upgrade. Domestic (0) or international (1). | 
 **upgrade_name** | **str**| Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority. | 
 **price** | **float**| Additional cost of adding the shipping upgrade. | 
 **secondary_price** | **float**| Additional cost of adding the shipping upgrade for each additional item. | 
 **shipping_carrier_id** | **int**| The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] [default to 0]
 **mail_class** | **str**| The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **min_delivery_days** | **int**| The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
 **max_delivery_days** | **int**| The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

### Return type

[**ShopShippingProfileUpgrade**](ShopShippingProfileUpgrade.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single shipping profile upgrade. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shop_shipping_profile**
> delete_shop_shipping_profile(shop_id, shipping_profile_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Deletes a ShippingProfile by given id.

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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.

    try:
        api_instance.delete_shop_shipping_profile(shop_id, shipping_profile_id)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->delete_shop_shipping_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 

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
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**204** | The ShopShippingProfile resource was correctly deleted |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shop_shipping_profile_destination**
> delete_shop_shipping_profile_destination(shop_id, shipping_profile_id, shipping_profile_destination_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Deletes a shipping destination and removes the destination option from every listing that uses the associated shipping profile. A shipping profile requires at least one shipping destination, so this endpoint cannot delete the final shipping destination for any shipping profile. To delete the final shipping destination from a shipping profile, you must [delete the entire shipping profile](/documentation/reference/#operation/deleteShopShippingProfile).

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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    shipping_profile_destination_id = 56 # int | The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing.

    try:
        api_instance.delete_shop_shipping_profile_destination(shop_id, shipping_profile_id, shipping_profile_destination_id)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->delete_shop_shipping_profile_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **shipping_profile_destination_id** | **int**| The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing. | 

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
**204** | Etsy deleted the shipping profile destination. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shop_shipping_profile_upgrade**
> delete_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, upgrade_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Deletes a shipping profile upgrade and removes the upgrade option from every listing that uses the associated shipping profile.

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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the shipping profile.
    upgrade_id = 56 # int | The numeric ID that is associated with a shipping upgrade

    try:
        api_instance.delete_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, upgrade_id)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->delete_shop_shipping_profile_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the shipping profile. | 
 **upgrade_id** | **int**| The numeric ID that is associated with a shipping upgrade | 

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
**204** | Etsy deleted the shipping profile upgrade. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_carriers**
> ShippingCarriers get_shipping_carriers(origin_country_iso)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a list of available shipping carriers and the mail classes associated with them for a given country

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shipping_carriers import ShippingCarriers
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    origin_country_iso = 'origin_country_iso_example' # str | The ISO code of the country from which the listing ships.

    try:
        api_response = api_instance.get_shipping_carriers(origin_country_iso)
        print("The response of ShopShippingProfileApi->get_shipping_carriers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->get_shipping_carriers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_country_iso** | **str**| The ISO code of the country from which the listing ships. | 

### Return type

[**ShippingCarriers**](ShippingCarriers.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of ShippingCarriers |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_shipping_profile**
> ShopShippingProfile get_shop_shipping_profile(shop_id, shipping_profile_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a Shipping Profile referenced by shipping profile ID.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile import ShopShippingProfile
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.

    try:
        api_response = api_instance.get_shop_shipping_profile(shop_id, shipping_profile_id)
        print("The response of ShopShippingProfileApi->get_shop_shipping_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->get_shop_shipping_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 

### Return type

[**ShopShippingProfile**](ShopShippingProfile.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ShippingProfile |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_shipping_profile_destinations_by_shipping_profile**
> ShopShippingProfileDestinations get_shop_shipping_profile_destinations_by_shipping_profile(shop_id, shipping_profile_id, limit=limit, offset=offset)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a list of shipping destination objects associated with a shipping profile.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_destinations import ShopShippingProfileDestinations
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)

    try:
        api_response = api_instance.get_shop_shipping_profile_destinations_by_shipping_profile(shop_id, shipping_profile_id, limit=limit, offset=offset)
        print("The response of ShopShippingProfileApi->get_shop_shipping_profile_destinations_by_shipping_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->get_shop_shipping_profile_destinations_by_shipping_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]

### Return type

[**ShopShippingProfileDestinations**](ShopShippingProfileDestinations.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of shipping destination objects. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_shipping_profile_upgrades**
> ShopShippingProfileUpgrades get_shop_shipping_profile_upgrades(shop_id, shipping_profile_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves the list of shipping profile upgrades assigned to a specific shipping profile.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_upgrades import ShopShippingProfileUpgrades
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.

    try:
        api_response = api_instance.get_shop_shipping_profile_upgrades(shop_id, shipping_profile_id)
        print("The response of ShopShippingProfileApi->get_shop_shipping_profile_upgrades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->get_shop_shipping_profile_upgrades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 

### Return type

[**ShopShippingProfileUpgrades**](ShopShippingProfileUpgrades.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of shipping profile upgrades. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shop_shipping_profiles**
> ShopShippingProfiles get_shop_shipping_profiles(shop_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a list of shipping profiles available in the specific Etsy shop identified by its shop ID.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profiles import ShopShippingProfiles
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.

    try:
        api_response = api_instance.get_shop_shipping_profiles(shop_id)
        print("The response of ShopShippingProfileApi->get_shop_shipping_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->get_shop_shipping_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 

### Return type

[**ShopShippingProfiles**](ShopShippingProfiles.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of shipping profiles |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_shipping_profile**
> ShopShippingProfile update_shop_shipping_profile(shop_id, shipping_profile_id, title=title, origin_country_iso=origin_country_iso, min_processing_time=min_processing_time, max_processing_time=max_processing_time, processing_time_unit=processing_time_unit, origin_postal_code=origin_postal_code)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Changes the settings in a shipping profile. You can pass a country iso code or a region when updating a ShippingProfile, but not both. Only one is required. You must pass either a shipping_carrier_id AND mail_class, or both min and max_delivery_days.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile import ShopShippingProfile
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    title = 'title_example' # str | The name string of this shipping profile. (optional)
    origin_country_iso = 'origin_country_iso_example' # str | The ISO code of the country from which the listing ships. (optional)
    min_processing_time = 56 # int | The minimum time required to process to ship listings with this shipping profile. (optional)
    max_processing_time = 56 # int | The maximum processing time the listing needs to ship. (optional)
    processing_time_unit = business_days # str | The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to \\\"business_days\\\". (optional) (default to business_days)
    origin_postal_code = 'origin_postal_code_example' # str | The postal code string (not necessarily a number) for the location from which the listing ships. Required if the `origin_country_iso` supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info (optional)

    try:
        api_response = api_instance.update_shop_shipping_profile(shop_id, shipping_profile_id, title=title, origin_country_iso=origin_country_iso, min_processing_time=min_processing_time, max_processing_time=max_processing_time, processing_time_unit=processing_time_unit, origin_postal_code=origin_postal_code)
        print("The response of ShopShippingProfileApi->update_shop_shipping_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->update_shop_shipping_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **title** | **str**| The name string of this shipping profile. | [optional] 
 **origin_country_iso** | **str**| The ISO code of the country from which the listing ships. | [optional] 
 **min_processing_time** | **int**| The minimum time required to process to ship listings with this shipping profile. | [optional] 
 **max_processing_time** | **int**| The maximum processing time the listing needs to ship. | [optional] 
 **processing_time_unit** | **str**| The unit used to represent how long a processing time is. A week is equivalent to the set processing schedule (default to 5 business days). If none is provided, the unit is set to \\\&quot;business_days\\\&quot;. | [optional] [default to business_days]
 **origin_postal_code** | **str**| The postal code string (not necessarily a number) for the location from which the listing ships. Required if the &#x60;origin_country_iso&#x60; supports postal codes. See the [Fulfillment Tutorial docs](https://developer.etsy.com/documentation/tutorials/fulfillment/#countries-requiring-postal-codes) for more info | [optional] 

### Return type

[**ShopShippingProfile**](ShopShippingProfile.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated shipping profile. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**503** | This function is temporarily unavailable. Please try again later. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_shipping_profile_destination**
> ShopShippingProfileDestination update_shop_shipping_profile_destination(shop_id, shipping_profile_id, shipping_profile_destination_id, primary_cost=primary_cost, secondary_cost=secondary_cost, destination_country_iso=destination_country_iso, destination_region=destination_region, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates an existing shipping destination, which can set or reassign the shipping cost, carrier, and class for a destination.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_destination import ShopShippingProfileDestination
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    shipping_profile_destination_id = 56 # int | The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing.
    primary_cost = 3.4 # float | The cost of shipping to this country/region alone, measured in the store's default currency. (optional)
    secondary_cost = 3.4 # float | The cost of shipping to this country/region with another item, measured in the store's default currency. (optional)
    destination_country_iso = 'destination_country_iso_example' # str | The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. (optional)
    destination_region = none # str | The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If `none`, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. (optional) (default to none)
    shipping_carrier_id = 56 # int | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    mail_class = 'mail_class_example' # str | The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    min_delivery_days = 56 # int | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null. (optional)
    max_delivery_days = 56 # int | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null. (optional)

    try:
        api_response = api_instance.update_shop_shipping_profile_destination(shop_id, shipping_profile_id, shipping_profile_destination_id, primary_cost=primary_cost, secondary_cost=secondary_cost, destination_country_iso=destination_country_iso, destination_region=destination_region, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)
        print("The response of ShopShippingProfileApi->update_shop_shipping_profile_destination:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->update_shop_shipping_profile_destination: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **shipping_profile_destination_id** | **int**| The numeric ID of the shipping profile destination in the [shipping profile](/documentation/reference#tag/Shop-ShippingProfile) associated with the listing. | 
 **primary_cost** | **float**| The cost of shipping to this country/region alone, measured in the store&#39;s default currency. | [optional] 
 **secondary_cost** | **float**| The cost of shipping to this country/region with another item, measured in the store&#39;s default currency. | [optional] 
 **destination_country_iso** | **str**| The ISO code of the country to which the listing ships. If null, request sets destination to destination_region. Required if destination_region is null or not provided. | [optional] 
 **destination_region** | **str**| The code of the region to which the listing ships. A region represents a set of countries. Supported regions are Europe Union and Non-Europe Union (countries in Europe not in EU). If &#x60;none&#x60;, request sets destination to destination_country_iso. Required if destination_country_iso is null or not provided. | [optional] [default to none]
 **shipping_carrier_id** | **int**| The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **mail_class** | **str**| The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **min_delivery_days** | **int**| The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
 **max_delivery_days** | **int**| The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

### Return type

[**ShopShippingProfileDestination**](ShopShippingProfileDestination.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single shipping destination. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**503** | This function is temporarily unavailable. Please try again later. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shop_shipping_profile_upgrade**
> ShopShippingProfileUpgrade update_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, upgrade_id, upgrade_name=upgrade_name, type=type, price=price, secondary_price=secondary_price, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates a shipping profile upgrade and updates any listings that use the shipping profile.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_shipping_profile_upgrade import ShopShippingProfileUpgrade
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
    api_instance = etsy_python_sdk.ShopShippingProfileApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`.
    upgrade_id = 56 # int | The numeric ID that is associated with a shipping upgrade
    upgrade_name = 'upgrade_name_example' # str | Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority. (optional)
    type = 'type_example' # str | The type of the shipping upgrade. Domestic (0) or international (1). (optional)
    price = 3.4 # float | Additional cost of adding the shipping upgrade. (optional)
    secondary_price = 3.4 # float | Additional cost of adding the shipping upgrade for each additional item. (optional)
    shipping_carrier_id = 56 # int | The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with `mail_class`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    mail_class = 'mail_class_example' # str | The unique ID string of a shipping carrier's mail class, which is used to calculate an estimated delivery date. **Required with `shipping_carrier_id`** if `min_delivery_days` and `max_delivery_days` are null. (optional)
    min_delivery_days = 56 # int | The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `max_delivery_days`** if `mail_class` is null. (optional)
    max_delivery_days = 56 # int | The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with `min_delivery_days`** if `mail_class` is null. (optional)

    try:
        api_response = api_instance.update_shop_shipping_profile_upgrade(shop_id, shipping_profile_id, upgrade_id, upgrade_name=upgrade_name, type=type, price=price, secondary_price=secondary_price, shipping_carrier_id=shipping_carrier_id, mail_class=mail_class, min_delivery_days=min_delivery_days, max_delivery_days=max_delivery_days)
        print("The response of ShopShippingProfileApi->update_shop_shipping_profile_upgrade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopShippingProfileApi->update_shop_shipping_profile_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | 
 **upgrade_id** | **int**| The numeric ID that is associated with a shipping upgrade | 
 **upgrade_name** | **str**| Name for the shipping upgrade shown to shoppers at checkout, e.g. USPS Priority. | [optional] 
 **type** | **str**| The type of the shipping upgrade. Domestic (0) or international (1). | [optional] 
 **price** | **float**| Additional cost of adding the shipping upgrade. | [optional] 
 **secondary_price** | **float**| Additional cost of adding the shipping upgrade for each additional item. | [optional] 
 **shipping_carrier_id** | **int**| The unique ID of a supported shipping carrier, which is used to calculate an Estimated Delivery Date. **Required with &#x60;mail_class&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **mail_class** | **str**| The unique ID string of a shipping carrier&#39;s mail class, which is used to calculate an estimated delivery date. **Required with &#x60;shipping_carrier_id&#x60;** if &#x60;min_delivery_days&#x60; and &#x60;max_delivery_days&#x60; are null. | [optional] 
 **min_delivery_days** | **int**| The minimum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;max_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 
 **max_delivery_days** | **int**| The maximum number of business days a buyer can expect to wait to receive their purchased item once it has shipped. **Required with &#x60;min_delivery_days&#x60;** if &#x60;mail_class&#x60; is null. | [optional] 

### Return type

[**ShopShippingProfileUpgrade**](ShopShippingProfileUpgrade.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single shipping profile upgrade. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**503** | This function is temporarily unavailable. Please try again later. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

