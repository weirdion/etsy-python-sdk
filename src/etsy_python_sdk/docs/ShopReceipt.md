# ShopReceipt

The record of a purchase from a shop. Shop receipts display monetary values using the shop's currency.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receipt_id** | **int** | The numeric ID for the [receipt](/documentation/reference#tag/Shop-Receipt) associated to this transaction. | [optional] 
**receipt_type** | **int** | The numeric value for the Etsy channel that serviced the purchase: 0 for Etsy.com, 1 for a Pattern shop. | [optional] 
**seller_user_id** | **int** | The numeric ID for the [user](/documentation/reference#tag/User) (seller) fulfilling the purchase. | [optional] 
**seller_email** | **str** | The email address string for the seller of the listing. | [optional] 
**buyer_user_id** | **int** | The numeric ID for the [user](/documentation/reference#tag/User) making the purchase. | [optional] 
**buyer_email** | **str** | The email address string for the buyer of the listing. It will be null if access hasn&#39;t been granted. Access is case-by-case and subject to approval. | [optional] 
**name** | **str** | The name string for the recipient in the shipping address. | [optional] 
**first_line** | **str** | The first address line string for the recipient in the shipping address. | [optional] 
**second_line** | **str** | The optional second address line string for the recipient in the shipping address. | [optional] 
**city** | **str** | The city string for the recipient in the shipping address. | [optional] 
**state** | **str** | The state string for the recipient in the shipping address. | [optional] 
**zip** | **str** | The zip code string (not necessarily a number) for the recipient in the shipping address. | [optional] 
**status** | **str** | The current order status string. One of: &#x60;paid&#x60;, &#x60;completed&#x60;, &#x60;open&#x60;, &#x60;payment processing&#x60; or &#x60;canceled&#x60;. | [optional] 
**formatted_address** | **str** | The formatted shipping address string for the recipient in the shipping address. | [optional] 
**country_iso** | **str** | The ISO-3166 alpha-2 country code string for the recipient in the shipping address. | [optional] 
**payment_method** | **str** | The payment method string identifying purchaser&#39;s payment method, which must be one of: \\&#39;cc\\&#39; (credit card), \\&#39;paypal\\&#39;, \\&#39;check\\&#39;, \\&#39;mo\\&#39; (money order), \\&#39;bt\\&#39; (bank transfer), \\&#39;other\\&#39;, \\&#39;ideal\\&#39;, \\&#39;sofort\\&#39;, \\&#39;apple_pay\\&#39;, \\&#39;google\\&#39;, \\&#39;android_pay\\&#39;, \\&#39;google_pay\\&#39;, \\&#39;klarna\\&#39;, \\&#39;k_pay_in_4\\&#39; (klarna), \\&#39;k_pay_in_3\\&#39; (klarna), or \\&#39;k_financing\\&#39; (klarna). | [optional] 
**payment_email** | **str** | The email address string for the email address to which to send payment confirmation | [optional] 
**message_from_seller** | **str** | An optional message string from the seller. | [optional] 
**message_from_buyer** | **str** | An optional message string from the buyer. | [optional] 
**message_from_payment** | **str** | The machine-generated acknowledgement string from the payment system. | [optional] 
**is_paid** | **bool** | When true, buyer paid for this purchase. | [optional] 
**is_shipped** | **bool** | When true, seller shipped the products. | [optional] 
**create_timestamp** | **int** | The receipt\\&#39;s creation time, in epoch seconds. | [optional] 
**created_timestamp** | **int** | The receipt\\&#39;s creation time, in epoch seconds. | [optional] 
**update_timestamp** | **int** | The time of the last update to the receipt, in epoch seconds. | [optional] 
**updated_timestamp** | **int** | The time of the last update to the receipt, in epoch seconds. | [optional] 
**is_gift** | **bool** | When true, the buyer indicated this purchase is a gift. | [optional] 
**gift_message** | **str** | A gift message string the buyer requests delivered with the product. | [optional] 
**gift_sender** | **str** | The name of the person who sent the gift. | [optional] 
**grandtotal** | [**Money**](Money.md) | A number equal to the total_price minus the coupon discount plus tax and shipping costs. | [optional] 
**subtotal** | [**Money**](Money.md) | A number equal to the total_price minus coupon discounts. Does not included tax or shipping costs. | [optional] 
**total_price** | [**Money**](Money.md) | A number equal to the sum of the individual listings\\&#39; (price * quantity). Does not included tax or shipping costs. | [optional] 
**total_shipping_cost** | [**Money**](Money.md) | A number equal to the total shipping cost of the receipt. | [optional] 
**total_tax_cost** | [**Money**](Money.md) | The total sales tax of the receipt. | [optional] 
**total_vat_cost** | [**Money**](Money.md) | A number equal to the total value-added tax (VAT) of the receipt. | [optional] 
**discount_amt** | [**Money**](Money.md) | The numeric total discounted price for the receipt when using a discount (percent or fixed) coupon. Free shipping coupons are not included in this discount amount. | [optional] 
**gift_wrap_price** | [**Money**](Money.md) | The numeric price of gift wrap for this receipt. | [optional] 
**shipments** | [**List[ShopReceiptShipment]**](ShopReceiptShipment.md) | A list of shipment statements for this receipt. | [optional] 
**transactions** | [**List[ShopReceiptTransaction]**](ShopReceiptTransaction.md) | Array of transactions for the receipt. | [optional] 
**refunds** | [**List[ShopRefund]**](ShopRefund.md) | Refunds for a given receipt. | [optional] 

## Example

```python
from etsy_python_sdk.models.shop_receipt import ShopReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of ShopReceipt from a JSON string
shop_receipt_instance = ShopReceipt.from_json(json)
# print the JSON string representation of the object
print(ShopReceipt.to_json())

# convert the object into a dict
shop_receipt_dict = shop_receipt_instance.to_dict()
# create an instance of ShopReceipt from a dict
shop_receipt_from_dict = ShopReceipt.from_dict(shop_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


