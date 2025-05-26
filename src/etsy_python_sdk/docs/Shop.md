# Shop

A shop created by an Etsy user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shop_id** | **int** | The unique positive non-zero numeric ID for an Etsy Shop. | [optional] 
**user_id** | **int** | The numeric user ID of the [user](/documentation/reference#tag/User) who owns this shop. | [optional] 
**shop_name** | **str** | The shop&#39;s name string. | [optional] 
**create_date** | **int** | The date and time this shop was created, in epoch seconds. | [optional] 
**created_timestamp** | **int** | The date and time this shop was created, in epoch seconds. | [optional] 
**title** | **str** | A brief heading string for the shop\\&#39;s main page. | [optional] 
**announcement** | **str** | An announcement string to buyers that displays on the shop&#39;s homepage. | [optional] 
**currency_code** | **str** | The ISO (alphabetic) code for the shop&#39;s currency. The shop displays all prices in this currency by default. | [optional] 
**is_vacation** | **bool** | When true, this shop is not accepting purchases. | [optional] 
**vacation_message** | **str** | The shop&#39;s message string displayed when &#x60;is_vacation&#x60; is true. | [optional] 
**sale_message** | **str** | A message string sent to users who complete a purchase from this shop. | [optional] 
**digital_sale_message** | **str** | A message string sent to users who purchase a digital item from this shop. | [optional] 
**update_date** | **int** | The date and time of the last update to the shop, in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The date and time of the last update to the shop, in epoch seconds. | [optional] 
**listing_active_count** | **int** | The number of active listings in the shop. | [optional] 
**digital_listing_count** | **int** | The number of digital listings in the shop. | [optional] 
**login_name** | **str** | The shop owner\\&#39;s login name string. | [optional] 
**accepts_custom_requests** | **bool** | When true, the shop accepts customization requests. | [optional] 
**policy_welcome** | **str** | The shop&#39;s policy welcome string (may be blank). | [optional] 
**policy_payment** | **str** | The shop&#39;s payment policy string (may be blank). | [optional] 
**policy_shipping** | **str** | The shop&#39;s shipping policy string (may be blank). | [optional] 
**policy_refunds** | **str** | The shop&#39;s refund policy string (may be blank). | [optional] 
**policy_additional** | **str** | The shop&#39;s additional policies string (may be blank). | [optional] 
**policy_seller_info** | **str** | The shop&#39;s seller information string (may be blank). | [optional] 
**policy_update_date** | **int** | The date and time of the last update to the shop&#39;s policies, in epoch seconds. | [optional] 
**policy_has_private_receipt_info** | **bool** | When true, EU receipts display private info. | [optional] 
**has_unstructured_policies** | **bool** | When true, the shop displays additional unstructured policy fields. | [optional] 
**policy_privacy** | **str** | The shop&#39;s privacy policy string (may be blank). | [optional] 
**vacation_autoreply** | **str** | The shop&#39;s automatic reply string displayed in new conversations when &#x60;is_vacation&#x60; is true. | [optional] 
**url** | **str** | The URL string for this shop. | [optional] 
**image_url_760x100** | **str** | The URL string for this shop&#39;s banner image. | [optional] 
**num_favorers** | **int** | The number of users who marked this shop a favorite. | [optional] 
**languages** | **List[str]** | A list of language strings for the shop&#39;s enrolled languages where the default shop language is the first element in the array. | [optional] 
**icon_url_fullxfull** | **str** | The URL string for this shop&#39;s icon image. | [optional] 
**is_using_structured_policies** | **bool** | When true, the shop accepted using structured policies. | [optional] 
**has_onboarded_structured_policies** | **bool** | When true, the shop accepted OR declined after viewing structured policies onboarding. | [optional] 
**include_dispute_form_link** | **bool** | When true, this shop\\&#39;s policies include a link to an EU online dispute form. | [optional] 
**is_direct_checkout_onboarded** | **bool** | (**DEPRECATED: Replaced by _is_etsy_payments_onboarded_.) When true, the shop has onboarded onto Etsy Payments. | [optional] 
**is_etsy_payments_onboarded** | **bool** | When true, the shop has onboarded onto Etsy Payments. | [optional] 
**is_calculated_eligible** | **bool** | When true, the shop is eligible for calculated shipping profiles. (Only available in the US and Canada) | [optional] 
**is_opted_in_to_buyer_promise** | **bool** | When true, the shop opted in to buyer promise. | [optional] 
**is_shop_us_based** | **bool** | When true, the shop is based in the US. | [optional] 
**transaction_sold_count** | **int** | The total number of sales ([transactions](/documentation/reference#tag/Shop-Receipt-Transactions)) for this shop. | [optional] 
**shipping_from_country_iso** | **str** | The country iso the shop is shipping from. | [optional] 
**shop_location_country_iso** | **str** | The country iso where the shop is located. | [optional] 
**review_count** | **int** | Number of reviews of shop listings in the past year. | [optional] 
**review_average** | **float** | Average rating based on reviews of shop listings in the past year. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop import Shop

# TODO update the JSON string below
json = "{}"
# create an instance of Shop from a JSON string
shop_instance = Shop.from_json(json)
# print the JSON string representation of the object
print(Shop.to_json())

# convert the object into a dict
shop_dict = shop_instance.to_dict()
# create an instance of Shop from a dict
shop_from_dict = Shop.from_dict(shop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


