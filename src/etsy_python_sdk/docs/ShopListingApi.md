# etsy_python_sdk.ShopListingApi

All URIs are relative to *https://openapi.etsy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_draft_listing**](ShopListingApi.md#create_draft_listing) | **POST** /v3/application/shops/{shop_id}/listings | 
[**delete_listing**](ShopListingApi.md#delete_listing) | **DELETE** /v3/application/listings/{listing_id} | 
[**delete_listing_property**](ShopListingApi.md#delete_listing_property) | **DELETE** /v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id} | 
[**find_all_active_listings_by_shop**](ShopListingApi.md#find_all_active_listings_by_shop) | **GET** /v3/application/shops/{shop_id}/listings/active | 
[**find_all_listings_active**](ShopListingApi.md#find_all_listings_active) | **GET** /v3/application/listings/active | 
[**get_featured_listings_by_shop**](ShopListingApi.md#get_featured_listings_by_shop) | **GET** /v3/application/shops/{shop_id}/listings/featured | 
[**get_listing**](ShopListingApi.md#get_listing) | **GET** /v3/application/listings/{listing_id} | 
[**get_listing_properties**](ShopListingApi.md#get_listing_properties) | **GET** /v3/application/shops/{shop_id}/listings/{listing_id}/properties | 
[**get_listing_property**](ShopListingApi.md#get_listing_property) | **GET** /v3/application/listings/{listing_id}/properties/{property_id} | 
[**get_listings_by_listing_ids**](ShopListingApi.md#get_listings_by_listing_ids) | **GET** /v3/application/listings/batch | 
[**get_listings_by_shop**](ShopListingApi.md#get_listings_by_shop) | **GET** /v3/application/shops/{shop_id}/listings | 
[**get_listings_by_shop_receipt**](ShopListingApi.md#get_listings_by_shop_receipt) | **GET** /v3/application/shops/{shop_id}/receipts/{receipt_id}/listings | 
[**get_listings_by_shop_return_policy**](ShopListingApi.md#get_listings_by_shop_return_policy) | **GET** /v3/application/shops/{shop_id}/policies/return/{return_policy_id}/listings | 
[**get_listings_by_shop_section_id**](ShopListingApi.md#get_listings_by_shop_section_id) | **GET** /v3/application/shops/{shop_id}/shop-sections/listings | 
[**update_listing**](ShopListingApi.md#update_listing) | **PATCH** /v3/application/shops/{shop_id}/listings/{listing_id} | 
[**update_listing_deprecated**](ShopListingApi.md#update_listing_deprecated) | **PUT** /v3/application/shops/{shop_id}/listings/{listing_id} | 
[**update_listing_property**](ShopListingApi.md#update_listing_property) | **PUT** /v3/application/shops/{shop_id}/listings/{listing_id}/properties/{property_id} | 


# **create_draft_listing**
> ShopListing create_draft_listing(shop_id, quantity, title, description, price, who_made, when_made, taxonomy_id, shipping_profile_id=shipping_profile_id, return_policy_id=return_policy_id, materials=materials, shop_section_id=shop_section_id, processing_min=processing_min, processing_max=processing_max, tags=tags, styles=styles, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, production_partner_ids=production_partner_ids, image_ids=image_ids, is_supply=is_supply, is_customizable=is_customizable, should_auto_renew=should_auto_renew, is_taxable=is_taxable, type=type)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Creates a physical draft [listing](/documentation/reference#tag/ShopListing) product in a shop on the Etsy channel.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing import ShopListing
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    quantity = 56 # int | The positive non-zero number of products available for purchase in the listing. Note: The listing quantity is the sum of available offering quantities. You can request the quantities for individual offerings from the ListingInventory resource using the [getListingInventory](/documentation/reference#operation/getListingInventory) endpoint.
    title = 'title_example' # str | The listing's title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, & and + characters once each.
    description = 'description_example' # str | A description string of the product for sale in the listing.
    price = 3.4 # float | The positive non-zero price of the product. (Sold product listings are private) Note: The price is the minimum possible price. The [`getListingInventory`](/documentation/reference/#operation/getListingInventory) method requests exact prices for available offerings.
    who_made = 'who_made_example' # str | An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires 'is_supply' and 'when_made'.
    when_made = 'when_made_example' # str | An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires 'is_supply' and 'who_made'.
    taxonomy_id = 56 # int | The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information.
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`. (optional)
    return_policy_id = 56 # int | The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). (optional)
    materials = ['materials_example'] # List[str] | A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. (optional)
    shop_section_id = 56 # int | The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. (optional)
    processing_min = 56 # int | The minimum number of days required to process this listing. Default value is null. (optional)
    processing_max = 56 # int | The maximum number of days required to process this listing. Default value is null. (optional)
    tags = ['tags_example'] # List[str] | A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, ', ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-'™©®]/u) Default value is null. (optional)
    styles = ['styles_example'] # List[str] | An array of style strings for this listing, each of which is free-form text string such as \\\"Formal\\\", or \\\"Steampunk\\\". When creating or updating a listing, the listing may have up to two styles. Valid style strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. (optional)
    item_weight = 3.4 # float | The numeric weight of the product measured in units set in 'item_weight_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_length = 3.4 # float | The numeric length of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_width = 3.4 # float | The numeric width of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_height = 3.4 # float | The numeric height of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_weight_unit = 'item_weight_unit_example' # str | A string defining the units used to measure the weight of the product. Default value is null. (optional)
    item_dimensions_unit = 'item_dimensions_unit_example' # str | A string defining the units used to measure the dimensions of the product. Default value is null. (optional)
    is_personalizable = True # bool | When true, this listing is personalizable. The default value is null. (optional)
    personalization_is_required = True # bool | When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is 'true'. (optional)
    personalization_char_count_max = 56 # int | This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is 'true'. (optional)
    personalization_instructions = 'personalization_instructions_example' # str | A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is 'true'. (optional)
    production_partner_ids = [56] # List[int] | An array of unique IDs of production partner ids. (optional)
    image_ids = [56] # List[int] | An array of numeric image IDs of the images in a listing, which can include up to 10 images. (optional)
    is_supply = True # bool | When true, tags the listing as a supply product, else indicates that it's a finished product. Helps buyers locate the listing under the Supplies heading. Requires 'who_made' and 'when_made'. (optional)
    is_customizable = True # bool | When true, a buyer may contact the seller for a customized order. The default value is true when a shop accepts custom orders. Does not apply to shops that do not accept custom orders. (optional)
    should_auto_renew = True # bool | When true, renews a listing for four months upon expiration. (optional)
    is_taxable = True # bool | When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. (optional)
    type = 'type_example' # str | An enumerated type string that indicates whether the listing is physical or a digital download. (optional)

    try:
        api_response = api_instance.create_draft_listing(shop_id, quantity, title, description, price, who_made, when_made, taxonomy_id, shipping_profile_id=shipping_profile_id, return_policy_id=return_policy_id, materials=materials, shop_section_id=shop_section_id, processing_min=processing_min, processing_max=processing_max, tags=tags, styles=styles, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, production_partner_ids=production_partner_ids, image_ids=image_ids, is_supply=is_supply, is_customizable=is_customizable, should_auto_renew=should_auto_renew, is_taxable=is_taxable, type=type)
        print("The response of ShopListingApi->create_draft_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->create_draft_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **quantity** | **int**| The positive non-zero number of products available for purchase in the listing. Note: The listing quantity is the sum of available offering quantities. You can request the quantities for individual offerings from the ListingInventory resource using the [getListingInventory](/documentation/reference#operation/getListingInventory) endpoint. | 
 **title** | **str**| The listing&#39;s title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, &amp; and + characters once each. | 
 **description** | **str**| A description string of the product for sale in the listing. | 
 **price** | **float**| The positive non-zero price of the product. (Sold product listings are private) Note: The price is the minimum possible price. The [&#x60;getListingInventory&#x60;](/documentation/reference/#operation/getListingInventory) method requests exact prices for available offerings. | 
 **who_made** | **str**| An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires &#39;is_supply&#39; and &#39;when_made&#39;. | 
 **when_made** | **str**| An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires &#39;is_supply&#39; and &#39;who_made&#39;. | 
 **taxonomy_id** | **int**| The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. | 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | [optional] 
 **return_policy_id** | **int**| The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). | [optional] 
 **materials** | [**List[str]**](str.md)| A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
 **shop_section_id** | **int**| The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. | [optional] 
 **processing_min** | **int**| The minimum number of days required to process this listing. Default value is null. | [optional] 
 **processing_max** | **int**| The maximum number of days required to process this listing. Default value is null. | [optional] 
 **tags** | [**List[str]**](str.md)| A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, &#39;, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-&#39;™©®]/u) Default value is null. | [optional] 
 **styles** | [**List[str]**](str.md)| An array of style strings for this listing, each of which is free-form text string such as \\\&quot;Formal\\\&quot;, or \\\&quot;Steampunk\\\&quot;. When creating or updating a listing, the listing may have up to two styles. Valid style strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
 **item_weight** | **float**| The numeric weight of the product measured in units set in &#39;item_weight_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_length** | **float**| The numeric length of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_width** | **float**| The numeric width of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_height** | **float**| The numeric height of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_weight_unit** | **str**| A string defining the units used to measure the weight of the product. Default value is null. | [optional] 
 **item_dimensions_unit** | **str**| A string defining the units used to measure the dimensions of the product. Default value is null. | [optional] 
 **is_personalizable** | **bool**| When true, this listing is personalizable. The default value is null. | [optional] 
 **personalization_is_required** | **bool**| When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_char_count_max** | **int**| This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_instructions** | **str**| A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **production_partner_ids** | [**List[int]**](int.md)| An array of unique IDs of production partner ids. | [optional] 
 **image_ids** | [**List[int]**](int.md)| An array of numeric image IDs of the images in a listing, which can include up to 10 images. | [optional] 
 **is_supply** | **bool**| When true, tags the listing as a supply product, else indicates that it&#39;s a finished product. Helps buyers locate the listing under the Supplies heading. Requires &#39;who_made&#39; and &#39;when_made&#39;. | [optional] 
 **is_customizable** | **bool**| When true, a buyer may contact the seller for a customized order. The default value is true when a shop accepts custom orders. Does not apply to shops that do not accept custom orders. | [optional] 
 **should_auto_renew** | **bool**| When true, renews a listing for four months upon expiration. | [optional] 
 **is_taxable** | **bool**| When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. | [optional] 
 **type** | **str**| An enumerated type string that indicates whether the listing is physical or a digital download. | [optional] 

### Return type

[**ShopListing**](ShopListing.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A single ShopListing |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_listing**
> delete_listing(listing_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Open API V3 endpoint to delete a ShopListing. A ShopListing can be deleted only if the state is one of the following:  SOLD_OUT, DRAFT, EXPIRED, INACTIVE, ACTIVE and is_available or ACTIVE and has seller flags:  SUPRESSED (frozen), VACATION, CUSTOM_SHOPS (pattern), SELL_ON_FACEBOOK

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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.

    try:
        api_instance.delete_listing(listing_id)
    except Exception as e:
        print("Exception when calling ShopListingApi->delete_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 

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
**409** | There was a request conflict with the current state of the target resource. See the error message for details. |  -  |
**204** | The Listing resource was correctly deleted |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_listing_property**
> delete_listing_property(shop_id, listing_id, property_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Deletes a property for a Listing.

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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    property_id = 56 # int | The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties).

    try:
        api_instance.delete_listing_property(shop_id, listing_id, property_id)
    except Exception as e:
        print("Exception when calling ShopListingApi->delete_listing_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **property_id** | **int**| The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties). | 

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
**204** | The ListingProperty resource was correctly deleted |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_active_listings_by_shop**
> ShopListings find_all_active_listings_by_shop(shop_id, limit=limit, sort_on=sort_on, sort_order=sort_order, offset=offset, keywords=keywords)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a list of all active listings on Etsy in a specific shop, paginated by listing creation date.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    sort_on = created # str | The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter. (optional) (default to created)
    sort_order = desc # str | The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). (optional) (default to desc)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)
    keywords = 'keywords_example' # str | Search term or phrase that must appear in all results. (optional)

    try:
        api_response = api_instance.find_all_active_listings_by_shop(shop_id, limit=limit, sort_on=sort_on, sort_order=sort_order, offset=offset, keywords=keywords)
        print("The response of ShopListingApi->find_all_active_listings_by_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->find_all_active_listings_by_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **sort_on** | **str**| The value to sort a search result of listings on. NOTES: a) &#x60;sort_on&#x60; only works when combined with one of the search options (keywords, region, etc.). b) when using &#x60;score&#x60; the returned results will always be in _descending_ order, regardless of the &#x60;sort_order&#x60; parameter. | [optional] [default to created]
 **sort_order** | **str**| The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). | [optional] [default to desc]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]
 **keywords** | **str**| Search term or phrase that must appear in all results. | [optional] 

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves a list of all active listings on Etsy in a specific shop, paginated by listing creation date. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_listings_active**
> ShopListings find_all_listings_active(limit=limit, offset=offset, keywords=keywords, sort_on=sort_on, sort_order=sort_order, min_price=min_price, max_price=max_price, taxonomy_id=taxonomy_id, shop_location=shop_location)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

A list of all active listings on Etsy paginated by their creation date. Without sort_order listings will be returned newest-first by default.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)
    keywords = 'keywords_example' # str | Search term or phrase that must appear in all results. (optional)
    sort_on = created # str | The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter. (optional) (default to created)
    sort_order = desc # str | The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). (optional) (default to desc)
    min_price = 3.4 # float | The minimum price of listings to be returned by a search result. (optional)
    max_price = 3.4 # float | The maximum price of listings to be returned by a search result. (optional)
    taxonomy_id = 56 # int | The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. (optional)
    shop_location = 'shop_location_example' # str | Filters by shop location. If location cannot be parsed, Etsy responds with an error. (optional)

    try:
        api_response = api_instance.find_all_listings_active(limit=limit, offset=offset, keywords=keywords, sort_on=sort_on, sort_order=sort_order, min_price=min_price, max_price=max_price, taxonomy_id=taxonomy_id, shop_location=shop_location)
        print("The response of ShopListingApi->find_all_listings_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->find_all_listings_active: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]
 **keywords** | **str**| Search term or phrase that must appear in all results. | [optional] 
 **sort_on** | **str**| The value to sort a search result of listings on. NOTES: a) &#x60;sort_on&#x60; only works when combined with one of the search options (keywords, region, etc.). b) when using &#x60;score&#x60; the returned results will always be in _descending_ order, regardless of the &#x60;sort_order&#x60; parameter. | [optional] [default to created]
 **sort_order** | **str**| The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). | [optional] [default to desc]
 **min_price** | **float**| The minimum price of listings to be returned by a search result. | [optional] 
 **max_price** | **float**| The maximum price of listings to be returned by a search result. | [optional] 
 **taxonomy_id** | **int**| The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. | [optional] 
 **shop_location** | **str**| Filters by shop location. If location cannot be parsed, Etsy responds with an error. | [optional] 

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of all active listings on Etsy paginated by their creation date. Without sort_order listings will be returned newest-first by default. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_featured_listings_by_shop**
> ShopListings get_featured_listings_by_shop(shop_id, limit=limit, offset=offset)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves Listings associated to a Shop that are featured.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)

    try:
        api_response = api_instance.get_featured_listings_by_shop(shop_id, limit=limit, offset=offset)
        print("The response of ShopListingApi->get_featured_listings_by_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_featured_listings_by_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Listings |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing**
> ShopListingWithAssociations get_listing(listing_id, includes=includes, language=language)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves a listing record by listing ID.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing_with_associations import ShopListingWithAssociations
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    includes = ['includes_example'] # List[str] | An enumerated string that attaches a valid association. Acceptable inputs are 'Shipping', 'Shop', 'Images', 'User', 'Translations' and 'Inventory'. (optional)
    language = 'language_example' # str | The IETF language tag for the language of this translation. Ex: `de`, `en`, `es`, `fr`, `it`, `ja`, `nl`, `pl`, `pt`. (optional)

    try:
        api_response = api_instance.get_listing(listing_id, includes=includes, language=language)
        print("The response of ShopListingApi->get_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **includes** | [**List[str]**](str.md)| An enumerated string that attaches a valid association. Acceptable inputs are &#39;Shipping&#39;, &#39;Shop&#39;, &#39;Images&#39;, &#39;User&#39;, &#39;Translations&#39; and &#39;Inventory&#39;. | [optional] 
 **language** | **str**| The IETF language tag for the language of this translation. Ex: &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;. | [optional] 

### Return type

[**ShopListingWithAssociations**](ShopListingWithAssociations.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single Listing. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_properties**
> ListingPropertyValues get_listing_properties(shop_id, listing_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Get a listing's properties

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_property_values import ListingPropertyValues
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.

    try:
        api_response = api_instance.get_listing_properties(shop_id, listing_id)
        print("The response of ShopListingApi->get_listing_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listing_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 

### Return type

[**ListingPropertyValues**](ListingPropertyValues.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Listing&#39;s Properties |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listing_property**
> ListingPropertyValue get_listing_property(listing_id, property_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationTertiary wt-mr-xs-2"> Feedback only </span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Give feedback</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">Development for this endpoint is in progress. It will only return a 501 response.</p></div>

Retrieves a listing's property

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_property_value import ListingPropertyValue
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    property_id = 56 # int | The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties).

    try:
        api_response = api_instance.get_listing_property(listing_id, property_id)
        print("The response of ShopListingApi->get_listing_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listing_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **property_id** | **int**| The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties). | 

### Return type

[**ListingPropertyValue**](ListingPropertyValue.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ListingProperty. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**501** | This endpoint is not functional at this time. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_by_listing_ids**
> ShopListingsWithAssociations get_listings_by_listing_ids(listing_ids, includes=includes)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Allows to query multiple listing ids at once. Limit 100 ids maximum per query.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings_with_associations import ShopListingsWithAssociations
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    listing_ids = [56] # List[int] | The list of numeric IDS for the listings in a specific Etsy shop.
    includes = ['includes_example'] # List[str] | An enumerated string that attaches a valid association. Acceptable inputs are 'Shipping', 'Shop', 'Images', 'User', 'Translations' and 'Inventory'. (optional)

    try:
        api_response = api_instance.get_listings_by_listing_ids(listing_ids, includes=includes)
        print("The response of ShopListingApi->get_listings_by_listing_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listings_by_listing_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listing_ids** | [**List[int]**](int.md)| The list of numeric IDS for the listings in a specific Etsy shop. | 
 **includes** | [**List[str]**](str.md)| An enumerated string that attaches a valid association. Acceptable inputs are &#39;Shipping&#39;, &#39;Shop&#39;, &#39;Images&#39;, &#39;User&#39;, &#39;Translations&#39; and &#39;Inventory&#39;. | [optional] 

### Return type

[**ShopListingsWithAssociations**](ShopListingsWithAssociations.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Listings |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_by_shop**
> ShopListingsWithAssociations get_listings_by_shop(shop_id, state=state, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order, includes=includes)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Endpoint to list Listings that belong to a Shop. Listings can be filtered using the 'state' param.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings_with_associations import ShopListingsWithAssociations
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    state = active # str | When _updating_ a listing, this value can be either `active` or `inactive`. Note: Setting a `draft` listing to `active` will also publish the listing on etsy.com and requires that the listing have an image set. Setting a `sold_out` listing to active will update the quantity to 1 and renew the listing on etsy.com. (optional) (default to active)
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)
    sort_on = created # str | The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter. (optional) (default to created)
    sort_order = desc # str | The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). (optional) (default to desc)
    includes = ['includes_example'] # List[str] | An enumerated string that attaches a valid association. Acceptable inputs are 'Shipping', 'Shop', 'Images', 'User', 'Translations' and 'Inventory'. (optional)

    try:
        api_response = api_instance.get_listings_by_shop(shop_id, state=state, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order, includes=includes)
        print("The response of ShopListingApi->get_listings_by_shop:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listings_by_shop: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **state** | **str**| When _updating_ a listing, this value can be either &#x60;active&#x60; or &#x60;inactive&#x60;. Note: Setting a &#x60;draft&#x60; listing to &#x60;active&#x60; will also publish the listing on etsy.com and requires that the listing have an image set. Setting a &#x60;sold_out&#x60; listing to active will update the quantity to 1 and renew the listing on etsy.com. | [optional] [default to active]
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]
 **sort_on** | **str**| The value to sort a search result of listings on. NOTES: a) &#x60;sort_on&#x60; only works when combined with one of the search options (keywords, region, etc.). b) when using &#x60;score&#x60; the returned results will always be in _descending_ order, regardless of the &#x60;sort_order&#x60; parameter. | [optional] [default to created]
 **sort_order** | **str**| The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). | [optional] [default to desc]
 **includes** | [**List[str]**](str.md)| An enumerated string that attaches a valid association. Acceptable inputs are &#39;Shipping&#39;, &#39;Shop&#39;, &#39;Images&#39;, &#39;User&#39;, &#39;Translations&#39; and &#39;Inventory&#39;. | [optional] 

### Return type

[**ShopListingsWithAssociations**](ShopListingsWithAssociations.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Listings |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_by_shop_receipt**
> ShopListings get_listings_by_shop_receipt(receipt_id, shop_id, limit=limit, offset=offset)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Gets all listings associated with a receipt.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    receipt_id = 56 # int | The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction.
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)

    try:
        api_response = api_instance.get_listings_by_shop_receipt(receipt_id, shop_id, limit=limit, offset=offset)
        print("The response of ShopListingApi->get_listings_by_shop_receipt:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listings_by_shop_receipt: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt_id** | **int**| The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction. | 
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of ShopListing resources. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_by_shop_return_policy**
> ShopListings get_listings_by_shop_return_policy(return_policy_id, shop_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Gets all listings associated with a Return Policy.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    return_policy_id = 56 # int | The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies).
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.

    try:
        api_response = api_instance.get_listings_by_shop_return_policy(return_policy_id, shop_id)
        print("The response of ShopListingApi->get_listings_by_shop_return_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listings_by_shop_return_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_policy_id** | **int**| The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). | 
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A set of ShopListing resources. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_listings_by_shop_section_id**
> ShopListings get_listings_by_shop_section_id(shop_id, shop_section_ids, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Retrieves all the listings from the section of a specific shop.

### Example

* Api Key Authentication (api_key):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listings import ShopListings
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    shop_section_ids = [56] # List[int] | A list of numeric IDS for all sections in a specific Etsy shop.
    limit = 25 # int | The maximum number of results to return. (optional) (default to 25)
    offset = 0 # int | The number of records to skip before selecting the first result. (optional) (default to 0)
    sort_on = created # str | The value to sort a search result of listings on. NOTES: a) `sort_on` only works when combined with one of the search options (keywords, region, etc.). b) when using `score` the returned results will always be in _descending_ order, regardless of the `sort_order` parameter. (optional) (default to created)
    sort_order = desc # str | The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). (optional) (default to desc)

    try:
        api_response = api_instance.get_listings_by_shop_section_id(shop_id, shop_section_ids, limit=limit, offset=offset, sort_on=sort_on, sort_order=sort_order)
        print("The response of ShopListingApi->get_listings_by_shop_section_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->get_listings_by_shop_section_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **shop_section_ids** | [**List[int]**](int.md)| A list of numeric IDS for all sections in a specific Etsy shop. | 
 **limit** | **int**| The maximum number of results to return. | [optional] [default to 25]
 **offset** | **int**| The number of records to skip before selecting the first result. | [optional] [default to 0]
 **sort_on** | **str**| The value to sort a search result of listings on. NOTES: a) &#x60;sort_on&#x60; only works when combined with one of the search options (keywords, region, etc.). b) when using &#x60;score&#x60; the returned results will always be in _descending_ order, regardless of the &#x60;sort_order&#x60; parameter. | [optional] [default to created]
 **sort_order** | **str**| The ascending(up) or descending(down) order to sort listings by. NOTE: sort_order only works when combined with one of the search options (keywords, region, etc.). | [optional] [default to desc]

### Return type

[**ShopListings**](ShopListings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of listings from a shop section. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_listing**
> ShopListing update_listing(shop_id, listing_id, image_ids=image_ids, title=title, description=description, materials=materials, should_auto_renew=should_auto_renew, shipping_profile_id=shipping_profile_id, return_policy_id=return_policy_id, shop_section_id=shop_section_id, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_taxable=is_taxable, taxonomy_id=taxonomy_id, tags=tags, who_made=who_made, when_made=when_made, featured_rank=featured_rank, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, state=state, is_supply=is_supply, production_partner_ids=production_partner_ids, type=type)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates a listing, identified by a listing ID, for a specific shop identified by a shop ID. Note that this is a PATCH method type. When activating, or manually renewing a physical listing, the shipping profile referenced by the `shipping_profile_id`, and all of its fields, along with its entries and upgrades must be complete and valid. If the shipping profile is not complete and valid, we will throw an exception with an error message that guides the request sender to update whatever data is bad.  Draft digital listings that are not made to order must have a file upload associated with it to be activated. If the listing is made to order, the file upload is not required.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing import ShopListing
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    image_ids = [56] # List[int] | An array of numeric image IDs of the images in a listing, which can include up to 10 images. (optional)
    title = 'title_example' # str | The listing's title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, & and + characters once each. (optional)
    description = 'description_example' # str | A description string of the product for sale in the listing. (optional)
    materials = ['materials_example'] # List[str] | A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. (optional)
    should_auto_renew = True # bool | When true, renews a listing for four months upon expiration. (optional)
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`. (optional)
    return_policy_id = 56 # int | The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). Required for active physical listings. This requirement does not apply to listings of EU-based shops. (optional)
    shop_section_id = 56 # int | The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. (optional)
    item_weight = 3.4 # float | The numeric weight of the product measured in units set in 'item_weight_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_length = 3.4 # float | The numeric length of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_width = 3.4 # float | The numeric width of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_height = 3.4 # float | The numeric height of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_weight_unit = 'item_weight_unit_example' # str | A string defining the units used to measure the weight of the product. Default value is null. (optional)
    item_dimensions_unit = 'item_dimensions_unit_example' # str | A string defining the units used to measure the dimensions of the product. Default value is null. (optional)
    is_taxable = True # bool | When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. (optional)
    taxonomy_id = 56 # int | The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. (optional)
    tags = ['tags_example'] # List[str] | A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, ', ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-'™©®]/u) Default value is null. (optional)
    who_made = 'who_made_example' # str | An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires 'is_supply' and 'when_made'. (optional)
    when_made = 'when_made_example' # str | An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires 'is_supply' and 'who_made'. (optional)
    featured_rank = 56 # int | The positive non-zero numeric position in the featured listings of the shop, with rank 1 listings appearing in the left-most position in featured listing on a shop’s home page. (optional)
    is_personalizable = True # bool | When true, this listing is personalizable. The default value is null. (optional)
    personalization_is_required = True # bool | When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is 'true'. (optional)
    personalization_char_count_max = 56 # int | This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is 'true'. (optional)
    personalization_instructions = 'personalization_instructions_example' # str | A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is 'true'. (optional)
    state = 'state_example' # str | When _updating_ a listing, this value can be either `active` or `inactive`. Note: Setting a `draft` listing to `active` will also publish the listing on etsy.com and requires that the listing have an image set. Setting a `sold_out` listing to active will update the quantity to 1 and renew the listing on etsy.com. (optional)
    is_supply = True # bool | When true, tags the listing as a supply product, else indicates that it's a finished product. Helps buyers locate the listing under the Supplies heading. Requires 'who_made' and 'when_made'. (optional)
    production_partner_ids = [56] # List[int] | An array of unique IDs of production partner ids. (optional)
    type = 'type_example' # str | An enumerated type string that indicates whether the listing is physical or a digital download. (optional)

    try:
        api_response = api_instance.update_listing(shop_id, listing_id, image_ids=image_ids, title=title, description=description, materials=materials, should_auto_renew=should_auto_renew, shipping_profile_id=shipping_profile_id, return_policy_id=return_policy_id, shop_section_id=shop_section_id, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_taxable=is_taxable, taxonomy_id=taxonomy_id, tags=tags, who_made=who_made, when_made=when_made, featured_rank=featured_rank, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, state=state, is_supply=is_supply, production_partner_ids=production_partner_ids, type=type)
        print("The response of ShopListingApi->update_listing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->update_listing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **image_ids** | [**List[int]**](int.md)| An array of numeric image IDs of the images in a listing, which can include up to 10 images. | [optional] 
 **title** | **str**| The listing&#39;s title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, &amp; and + characters once each. | [optional] 
 **description** | **str**| A description string of the product for sale in the listing. | [optional] 
 **materials** | [**List[str]**](str.md)| A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
 **should_auto_renew** | **bool**| When true, renews a listing for four months upon expiration. | [optional] 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | [optional] 
 **return_policy_id** | **int**| The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). Required for active physical listings. This requirement does not apply to listings of EU-based shops. | [optional] 
 **shop_section_id** | **int**| The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. | [optional] 
 **item_weight** | **float**| The numeric weight of the product measured in units set in &#39;item_weight_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_length** | **float**| The numeric length of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_width** | **float**| The numeric width of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_height** | **float**| The numeric height of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_weight_unit** | **str**| A string defining the units used to measure the weight of the product. Default value is null. | [optional] 
 **item_dimensions_unit** | **str**| A string defining the units used to measure the dimensions of the product. Default value is null. | [optional] 
 **is_taxable** | **bool**| When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. | [optional] 
 **taxonomy_id** | **int**| The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. | [optional] 
 **tags** | [**List[str]**](str.md)| A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, &#39;, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-&#39;™©®]/u) Default value is null. | [optional] 
 **who_made** | **str**| An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires &#39;is_supply&#39; and &#39;when_made&#39;. | [optional] 
 **when_made** | **str**| An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires &#39;is_supply&#39; and &#39;who_made&#39;. | [optional] 
 **featured_rank** | **int**| The positive non-zero numeric position in the featured listings of the shop, with rank 1 listings appearing in the left-most position in featured listing on a shop’s home page. | [optional] 
 **is_personalizable** | **bool**| When true, this listing is personalizable. The default value is null. | [optional] 
 **personalization_is_required** | **bool**| When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_char_count_max** | **int**| This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_instructions** | **str**| A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **state** | **str**| When _updating_ a listing, this value can be either &#x60;active&#x60; or &#x60;inactive&#x60;. Note: Setting a &#x60;draft&#x60; listing to &#x60;active&#x60; will also publish the listing on etsy.com and requires that the listing have an image set. Setting a &#x60;sold_out&#x60; listing to active will update the quantity to 1 and renew the listing on etsy.com. | [optional] 
 **is_supply** | **bool**| When true, tags the listing as a supply product, else indicates that it&#39;s a finished product. Helps buyers locate the listing under the Supplies heading. Requires &#39;who_made&#39; and &#39;when_made&#39;. | [optional] 
 **production_partner_ids** | [**List[int]**](int.md)| An array of unique IDs of production partner ids. | [optional] 
 **type** | **str**| An enumerated type string that indicates whether the listing is physical or a digital download. | [optional] 

### Return type

[**ShopListing**](ShopListing.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ShopListing |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**409** | There was a request conflict with the current state of the target resource. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_listing_deprecated**
> ShopListing update_listing_deprecated(shop_id, listing_id, image_ids=image_ids, title=title, description=description, materials=materials, should_auto_renew=should_auto_renew, shipping_profile_id=shipping_profile_id, shop_section_id=shop_section_id, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_taxable=is_taxable, taxonomy_id=taxonomy_id, tags=tags, who_made=who_made, when_made=when_made, featured_rank=featured_rank, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, state=state, is_supply=is_supply, production_partner_ids=production_partner_ids, type=type)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates a listing, identified by a listing ID, for a specific shop identified by a shop ID. This endpoint will be removed in the near future in favor of `updateListing` PATCH version.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.shop_listing import ShopListing
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    image_ids = [56] # List[int] | An array of numeric image IDs of the images in a listing, which can include up to 10 images. (optional)
    title = 'title_example' # str | The listing's title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, & and + characters once each. (optional)
    description = 'description_example' # str | A description string of the product for sale in the listing. (optional)
    materials = ['materials_example'] # List[str] | A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. (optional)
    should_auto_renew = True # bool | When true, renews a listing for four months upon expiration. (optional)
    shipping_profile_id = 56 # int | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is `physical`. (optional)
    shop_section_id = 56 # int | The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. (optional)
    item_weight = 3.4 # float | The numeric weight of the product measured in units set in 'item_weight_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_length = 3.4 # float | The numeric length of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_width = 3.4 # float | The numeric width of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_height = 3.4 # float | The numeric height of the product measured in units set in 'item_dimensions_unit'. Default value is null. If set, the value must be greater than 0. (optional)
    item_weight_unit = 'item_weight_unit_example' # str | A string defining the units used to measure the weight of the product. Default value is null. (optional)
    item_dimensions_unit = 'item_dimensions_unit_example' # str | A string defining the units used to measure the dimensions of the product. Default value is null. (optional)
    is_taxable = True # bool | When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. (optional)
    taxonomy_id = 56 # int | The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. (optional)
    tags = ['tags_example'] # List[str] | A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, ', ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-'™©®]/u) Default value is null. (optional)
    who_made = 'who_made_example' # str | An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires 'is_supply' and 'when_made'. (optional)
    when_made = 'when_made_example' # str | An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires 'is_supply' and 'who_made'. (optional)
    featured_rank = 56 # int | The positive non-zero numeric position in the featured listings of the shop, with rank 1 listings appearing in the left-most position in featured listing on a shop’s home page. (optional)
    is_personalizable = True # bool | When true, this listing is personalizable. The default value is null. (optional)
    personalization_is_required = True # bool | When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is 'true'. (optional)
    personalization_char_count_max = 56 # int | This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is 'true'. (optional)
    personalization_instructions = 'personalization_instructions_example' # str | A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is 'true'. (optional)
    state = 'state_example' # str | When _updating_ a listing, this value can be either `active` or `inactive`. Note: Setting a `draft` listing to `active` will also publish the listing on etsy.com and requires that the listing have an image set. Setting a `sold_out` listing to active will update the quantity to 1 and renew the listing on etsy.com. (optional)
    is_supply = True # bool | When true, tags the listing as a supply product, else indicates that it's a finished product. Helps buyers locate the listing under the Supplies heading. Requires 'who_made' and 'when_made'. (optional)
    production_partner_ids = [56] # List[int] | An array of unique IDs of production partner ids. (optional)
    type = 'type_example' # str | An enumerated type string that indicates whether the listing is physical or a digital download. (optional)

    try:
        api_response = api_instance.update_listing_deprecated(shop_id, listing_id, image_ids=image_ids, title=title, description=description, materials=materials, should_auto_renew=should_auto_renew, shipping_profile_id=shipping_profile_id, shop_section_id=shop_section_id, item_weight=item_weight, item_length=item_length, item_width=item_width, item_height=item_height, item_weight_unit=item_weight_unit, item_dimensions_unit=item_dimensions_unit, is_taxable=is_taxable, taxonomy_id=taxonomy_id, tags=tags, who_made=who_made, when_made=when_made, featured_rank=featured_rank, is_personalizable=is_personalizable, personalization_is_required=personalization_is_required, personalization_char_count_max=personalization_char_count_max, personalization_instructions=personalization_instructions, state=state, is_supply=is_supply, production_partner_ids=production_partner_ids, type=type)
        print("The response of ShopListingApi->update_listing_deprecated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->update_listing_deprecated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **image_ids** | [**List[int]**](int.md)| An array of numeric image IDs of the images in a listing, which can include up to 10 images. | [optional] 
 **title** | **str**| The listing&#39;s title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, &amp; and + characters once each. | [optional] 
 **description** | **str**| A description string of the product for sale in the listing. | [optional] 
 **materials** | [**List[str]**](str.md)| A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
 **should_auto_renew** | **bool**| When true, renews a listing for four months upon expiration. | [optional] 
 **shipping_profile_id** | **int**| The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | [optional] 
 **shop_section_id** | **int**| The numeric ID of the [shop section](/documentation/reference#tag/Shop-Section) for this listing. Default value is null. | [optional] 
 **item_weight** | **float**| The numeric weight of the product measured in units set in &#39;item_weight_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_length** | **float**| The numeric length of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_width** | **float**| The numeric width of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_height** | **float**| The numeric height of the product measured in units set in &#39;item_dimensions_unit&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
 **item_weight_unit** | **str**| A string defining the units used to measure the weight of the product. Default value is null. | [optional] 
 **item_dimensions_unit** | **str**| A string defining the units used to measure the dimensions of the product. Default value is null. | [optional] 
 **is_taxable** | **bool**| When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. | [optional] 
 **taxonomy_id** | **int**| The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. | [optional] 
 **tags** | [**List[str]**](str.md)| A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, &#39;, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-&#39;™©®]/u) Default value is null. | [optional] 
 **who_made** | **str**| An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires &#39;is_supply&#39; and &#39;when_made&#39;. | [optional] 
 **when_made** | **str**| An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires &#39;is_supply&#39; and &#39;who_made&#39;. | [optional] 
 **featured_rank** | **int**| The positive non-zero numeric position in the featured listings of the shop, with rank 1 listings appearing in the left-most position in featured listing on a shop’s home page. | [optional] 
 **is_personalizable** | **bool**| When true, this listing is personalizable. The default value is null. | [optional] 
 **personalization_is_required** | **bool**| When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_char_count_max** | **int**| This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **personalization_instructions** | **str**| A string representing instructions for the buyer to enter the personalization. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
 **state** | **str**| When _updating_ a listing, this value can be either &#x60;active&#x60; or &#x60;inactive&#x60;. Note: Setting a &#x60;draft&#x60; listing to &#x60;active&#x60; will also publish the listing on etsy.com and requires that the listing have an image set. Setting a &#x60;sold_out&#x60; listing to active will update the quantity to 1 and renew the listing on etsy.com. | [optional] 
 **is_supply** | **bool**| When true, tags the listing as a supply product, else indicates that it&#39;s a finished product. Helps buyers locate the listing under the Supplies heading. Requires &#39;who_made&#39; and &#39;when_made&#39;. | [optional] 
 **production_partner_ids** | [**List[int]**](int.md)| An array of unique IDs of production partner ids. | [optional] 
 **type** | **str**| An enumerated type string that indicates whether the listing is physical or a digital download. | [optional] 

### Return type

[**ShopListing**](ShopListing.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single ShopListing |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**409** | There was a request conflict with the current state of the target resource. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_listing_property**
> ListingPropertyValue update_listing_property(shop_id, listing_id, property_id, value_ids, values, scale_id=scale_id)

<div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><span class="wt-badge wt-badge--notificationPrimary wt-bg-slime-tint wt-mr-xs-2">General Release</span><a class="wt-text-link" href="https://github.com/etsy/open-api/discussions" target="_blank" rel="noopener noreferrer">Report bug</a></div><div class="wt-display-flex-xs wt-align-items-center wt-mt-xs-2 wt-mb-xs-3"><p class="wt-text-body-01 banner-text">This endpoint is ready for production use.</p></div>

Updates or populates the properties list defining product offerings for a listing. Each offering requires both a `value` and a `value_id` that are valid for a `scale_id` assigned to the listing or that you assign to the listing with this request.

### Example

* Api Key Authentication (api_key):
* OAuth Authentication (oauth2):

```python
import etsy_python_sdk
from etsy_python_sdk.models.listing_property_value import ListingPropertyValue
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
    api_instance = etsy_python_sdk.ShopListingApi(api_client)
    shop_id = 56 # int | The unique positive non-zero numeric ID for an Etsy Shop.
    listing_id = 56 # int | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction.
    property_id = 56 # int | The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties).
    value_ids = [56] # List[int] | An array of unique IDs of multiple Etsy [listing property](/documentation/reference#operation/getListingProperties) values. For example, if your listing offers different sizes of a product, then the value ID list contains value IDs for each size.
    values = ['values_example'] # List[str] | An array of value strings for multiple Etsy [listing property](/documentation/reference#operation/getListingProperties) values. For example, if your listing offers different colored products, then the values array contains the color strings for each color. Note: parenthesis characters (`(` and `)`) are not allowed.
    scale_id = 56 # int | The numeric ID of a single Etsy.com measurement scale. For example, for shoe size, there are three `scale_id`s available - `UK`, `US/Canada`, and `EU`, where `US/Canada` has `scale_id` 19. (optional)

    try:
        api_response = api_instance.update_listing_property(shop_id, listing_id, property_id, value_ids, values, scale_id=scale_id)
        print("The response of ShopListingApi->update_listing_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShopListingApi->update_listing_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shop_id** | **int**| The unique positive non-zero numeric ID for an Etsy Shop. | 
 **listing_id** | **int**| The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | 
 **property_id** | **int**| The unique ID of an Etsy [listing property](/documentation/reference#operation/getListingProperties). | 
 **value_ids** | [**List[int]**](int.md)| An array of unique IDs of multiple Etsy [listing property](/documentation/reference#operation/getListingProperties) values. For example, if your listing offers different sizes of a product, then the value ID list contains value IDs for each size. | 
 **values** | [**List[str]**](str.md)| An array of value strings for multiple Etsy [listing property](/documentation/reference#operation/getListingProperties) values. For example, if your listing offers different colored products, then the values array contains the color strings for each color. Note: parenthesis characters (&#x60;(&#x60; and &#x60;)&#x60;) are not allowed. | 
 **scale_id** | **int**| The numeric ID of a single Etsy.com measurement scale. For example, for shoe size, there are three &#x60;scale_id&#x60;s available - &#x60;UK&#x60;, &#x60;US/Canada&#x60;, and &#x60;EU&#x60;, where &#x60;US/Canada&#x60; has &#x60;scale_id&#x60; 19. | [optional] 

### Return type

[**ListingPropertyValue**](ListingPropertyValue.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A single listing property. |  -  |
**403** | The request attempted to perform an operation it is not allowed to. See the error message for details. |  -  |
**404** | A resource could not be found. See the error message for details. |  -  |
**400** | There was a problem with the request data. See the error message for details. |  -  |
**401** | The request lacks valid authentication credentials. See the error message for details. |  -  |
**500** | The server encountered an internal error. See the error message for details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

