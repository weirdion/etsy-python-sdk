# PaymentAccountLedgerEntries

A set of PaymentAccountLedgerEntry resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of PaymentAccountLedgerEntry resources found. | [optional] 
**results** | [**List[PaymentAccountLedgerEntry]**](PaymentAccountLedgerEntry.md) | The PaymentAccountLedgerEntry resources found. | [optional] 

## Example

```python
from etsy_python_sdk.models.payment_account_ledger_entries import PaymentAccountLedgerEntries

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountLedgerEntries from a JSON string
payment_account_ledger_entries_instance = PaymentAccountLedgerEntries.from_json(json)
# print the JSON string representation of the object
print(PaymentAccountLedgerEntries.to_json())

# convert the object into a dict
payment_account_ledger_entries_dict = payment_account_ledger_entries_instance.to_dict()
# create an instance of PaymentAccountLedgerEntries from a dict
payment_account_ledger_entries_from_dict = PaymentAccountLedgerEntries.from_dict(payment_account_ledger_entries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


