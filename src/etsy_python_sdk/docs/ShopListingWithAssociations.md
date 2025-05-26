# ShopListingWithAssociations

A listing from a shop, which contains a product quantity, title, description, price, etc. and additional fields which represent associations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **int** | The numeric ID for the [listing](/documentation/reference#tag/ShopListing) associated to this transaction. | [optional] 
**user_id** | **int** | The numeric ID for the [user](/documentation/reference#tag/User) posting the listing. | [optional] 
**shop_id** | **int** | The unique positive non-zero numeric ID for an Etsy Shop. | [optional] 
**title** | **str** | The listing&#39;s title string. When creating or updating a listing, valid title strings contain only letters, numbers, punctuation marks, mathematical symbols, whitespace characters, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{P}\\\\p{Sm}\\\\p{Zs}™©®]/u) You can only use the %, :, &amp; and + characters once each. | [optional] 
**description** | **str** | A description string of the product for sale in the listing. | [optional] 
**state** | **str** | When _updating_ a listing, this value can be either &#x60;active&#x60; or &#x60;inactive&#x60;. Note: Setting a &#x60;draft&#x60; listing to &#x60;active&#x60; will also publish the listing on etsy.com and requires that the listing have an image set. Setting a &#x60;sold_out&#x60; listing to active will update the quantity to 1 and renew the listing on etsy.com. | [optional] 
**creation_timestamp** | **int** | The listing\\&#39;s creation time, in epoch seconds. | [optional] 
**created_timestamp** | **int** | The listing\\&#39;s creation time, in epoch seconds. | [optional] 
**ending_timestamp** | **int** | The listing\\&#39;s expiration time, in epoch seconds. | [optional] 
**original_creation_timestamp** | **int** | The listing\\&#39;s creation time, in epoch seconds. | [optional] 
**last_modified_timestamp** | **int** | The time of the last update to the listing, in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The time of the last update to the listing, in epoch seconds. | [optional] 
**state_timestamp** | **int** | The date and time of the last state change of this listing. | [optional] 
**quantity** | **int** | The positive non-zero number of products available for purchase in the listing. Note: The listing quantity is the sum of available offering quantities. You can request the quantities for individual offerings from the ListingInventory resource using the [getListingInventory](/documentation/reference#operation/getListingInventory) endpoint. | [optional] 
**shop_section_id** | **int** | The numeric ID of a section in a specific Etsy shop. | [optional] 
**featured_rank** | **int** | The positive non-zero numeric position in the featured listings of the shop, with rank 1 listings appearing in the left-most position in featured listing on a shop’s home page. | [optional] 
**url** | **str** | The full URL to the listing&#39;s page on Etsy. | [optional] 
**num_favorers** | **int** | The number of users who marked this Listing a favorite. | [optional] 
**non_taxable** | **bool** | When true, applicable [shop](/documentation/reference#tag/Shop) tax rates do not apply to this listing at checkout. | [optional] 
**is_taxable** | **bool** | When true, applicable [shop](/documentation/reference#tag/Shop) tax rates apply to this listing at checkout. | [optional] 
**is_customizable** | **bool** | When true, a buyer may contact the seller for a customized order. The default value is true when a shop accepts custom orders. Does not apply to shops that do not accept custom orders. | [optional] 
**is_personalizable** | **bool** | When true, this listing is personalizable. The default value is null. | [optional] 
**personalization_is_required** | **bool** | When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
**personalization_char_count_max** | **int** | This is an integer value representing the maximum length for the personalization message entered by the buyer. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
**personalization_instructions** | **str** | When true, this listing requires personalization. The default value is null. Will only change if is_personalizable is &#39;true&#39;. | [optional] 
**listing_type** | **str** | An enumerated type string that indicates whether the listing is physical or a digital download. | [optional] 
**tags** | **List[str]** | A comma-separated list of tag strings for the listing. When creating or updating a listing, valid tag strings contain only letters, numbers, whitespace characters, -, &#39;, ™, ©, and ®. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}\\\\-&#39;™©®]/u) Default value is null. | [optional] 
**materials** | **List[str]** | A list of material strings for materials used in the product. Valid materials strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
**shipping_profile_id** | **int** | The numeric ID of the [shipping profile](/documentation/reference#operation/getShopShippingProfile) associated with the listing. Required when listing type is &#x60;physical&#x60;. | [optional] 
**return_policy_id** | **int** | The numeric ID of the [Return Policy](/documentation/reference#operation/getShopReturnPolicies). | [optional] 
**processing_min** | **int** | The minimum number of days required to process this listing. Default value is null. | [optional] 
**processing_max** | **int** | The maximum number of days required to process this listing. Default value is null. | [optional] 
**who_made** | **str** | An enumerated string indicating who made the product. Helps buyers locate the listing under the Handmade heading. Requires &#39;is_supply&#39; and &#39;when_made&#39;. | [optional] 
**when_made** | **str** | An enumerated string for the era in which the maker made the product in this listing. Helps buyers locate the listing under the Vintage heading. Requires &#39;is_supply&#39; and &#39;who_made&#39;. | [optional] 
**is_supply** | **bool** | When true, tags the listing as a supply product, else indicates that it&#39;s a finished product. Helps buyers locate the listing under the Supplies heading. Requires &#39;who_made&#39; and &#39;when_made&#39;. | [optional] 
**item_weight** | **float** | The numeric weight of the product measured in units set in \\&#39;item_weight_unit\\&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
**item_weight_unit** | **str** | A string defining the units used to measure the weight of the product. Default value is null. | [optional] 
**item_length** | **float** | The numeric length of the product measured in units set in \\&#39;item_dimensions_unit\\&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
**item_width** | **float** | The numeric width of the product measured in units set in \\&#39;item_dimensions_unit\\&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
**item_height** | **float** | The numeric length of the product measured in units set in \\&#39;item_dimensions_unit\\&#39;. Default value is null. If set, the value must be greater than 0. | [optional] 
**item_dimensions_unit** | **str** | A string defining the units used to measure the dimensions of the product. Default value is null. | [optional] 
**is_private** | **bool** | When true, this is a private listing intended for a specific buyer and hidden from shop view. | [optional] 
**style** | **List[str]** | An array of style strings for this listing, each of which is free-form text string such as \\\&quot;Formal\\\&quot;, or \\\&quot;Steampunk\\\&quot;. When creating or updating a listing, the listing may have up to two styles. Valid style strings contain only letters, numbers, and whitespace characters. (regex: /[^\\\\p{L}\\\\p{Nd}\\\\p{Zs}]/u) Default value is null. | [optional] 
**file_data** | **str** | A string describing the files attached to a digital listing. | [optional] 
**has_variations** | **bool** | When true, the listing has variations. | [optional] 
**should_auto_renew** | **bool** | When true, renews a listing for four months upon expiration. | [optional] 
**language** | **str** | The IETF language tag for the default language of the listing. Ex: &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;ja&#x60;, &#x60;nl&#x60;, &#x60;pl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;. | [optional] 
**price** | [**Money**](Money.md) | The positive non-zero price of the product. (Sold product listings are private) Note: The price is the minimum possible price. The [&#x60;getListingInventory&#x60;](/documentation/reference/#operation/getListingInventory) method requests exact prices for available offerings. | [optional] 
**taxonomy_id** | **int** | The numerical taxonomy ID of the listing. See [SellerTaxonomy](/documentation/reference#tag/SellerTaxonomy) and [BuyerTaxonomy](/documentation/reference#tag/BuyerTaxonomy) for more information. | [optional] 
**shipping_profile** | [**ShopShippingProfile**](ShopShippingProfile.md) | An array of data representing the shipping profile resource. | [optional] 
**user** | [**User**](User.md) | Represents a single user of the site | [optional] 
**shop** | [**Shop**](Shop.md) | A shop created by an Etsy user. | [optional] 
**images** | [**List[ListingImage]**](ListingImage.md) | Represents a list of listing image resources, each of which contains the reference URLs and metadata for an image | [optional] 
**videos** | [**List[ListingVideo]**](ListingVideo.md) | The single video associated with a listing. | [optional] 
**inventory** | [**ListingInventory**](ListingInventory.md) | An enumerated string that attaches a valid association. Default value is null. | [optional] 
**production_partners** | [**List[ShopProductionPartner]**](ShopProductionPartner.md) | Represents a list of production partners for a shop. | [optional] 
**skus** | **List[str]** | A list of SKU strings for the listing. SKUs will only appear if the requesting user owns the shop and a valid matching OAuth 2 token is provided. When requested without the token it will be an empty array. | [optional] 
**translations** | [**ListingTranslations**](ListingTranslations.md) | A map of translations for the listing. Default value is a map of all supported languages keyed to null. | [optional] 
**views** | **int** | The number of times the listing has been viewed. This value is tabulated once per day and **only for active listings**, so the value is not real-time. If &#x60;0&#x60;, the listing has either not been viewed, not yet tabulated, was not active during the last tabulation or there was an error fetching the value. If a value is expected, call &#x60;getListing&#x60; to confirm the value. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_listing_with_associations import ShopListingWithAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ShopListingWithAssociations from a JSON string
shop_listing_with_associations_instance = ShopListingWithAssociations.from_json(json)
# print the JSON string representation of the object
print(ShopListingWithAssociations.to_json())

# convert the object into a dict
shop_listing_with_associations_dict = shop_listing_with_associations_instance.to_dict()
# create an instance of ShopListingWithAssociations from a dict
shop_listing_with_associations_from_dict = ShopListingWithAssociations.from_dict(shop_listing_with_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


