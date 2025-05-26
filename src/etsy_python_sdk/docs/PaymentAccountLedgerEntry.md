# PaymentAccountLedgerEntry

Represents an entry in a shop's ledger.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **int** | The ledger entry&#39;s numeric ID. | [optional] 
**ledger_id** | **int** | The ledger&#39;s numeric ID. | [optional] 
**sequence_number** | **int** | The sequence allows ledger entries to be sorted chronologically. The higher the sequence, the more recent the entry. | [optional] 
**amount** | **int** | The amount of money credited to the ledger. | [optional] 
**currency** | **str** | The currency of the entry on the ledger. | [optional] 
**description** | **str** | Details what kind of ledger entry this is: a payment, refund, reversal of a failed refund, disbursement, returned disbursement, recoupment, miscellaneous credit, miscellaneous debit, or bill payment. | [optional] 
**balance** | **int** | The amount of money in the shop&#39;s ledger the moment after this entry was applied. | [optional] 
**create_date** | **int** | The date and time the ledger entry was created in Epoch seconds. | [optional] 
**created_timestamp** | **int** | The date and time the ledger entry was created in Epoch seconds. | [optional] 
**ledger_type** | **str** | The original reference type for the ledger entry. | [optional] 
**reference_type** | **str** | The object type the ledger entry refers to. | [optional] 
**reference_id** | **str** | The object id the ledger entry refers to. | [optional] 
**payment_adjustments** | [**List[PaymentAdjustment]**](PaymentAdjustment.md) | List of refund objects on an Etsy Payments transaction. All monetary amounts are in USD pennies unless otherwise specified. | [optional] 

## Example

```python
from etsy_python_sdk.models.payment_account_ledger_entry import PaymentAccountLedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountLedgerEntry from a JSON string
payment_account_ledger_entry_instance = PaymentAccountLedgerEntry.from_json(json)
# print the JSON string representation of the object
print(PaymentAccountLedgerEntry.to_json())

# convert the object into a dict
payment_account_ledger_entry_dict = payment_account_ledger_entry_instance.to_dict()
# create an instance of PaymentAccountLedgerEntry from a dict
payment_account_ledger_entry_from_dict = PaymentAccountLedgerEntry.from_dict(payment_account_ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


