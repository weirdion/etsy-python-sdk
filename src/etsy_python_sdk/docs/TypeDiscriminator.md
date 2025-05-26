# TypeDiscriminator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | field used to determine the type of the object when deserializing union type responses | 

## Example

```python
from etsy_python_sdk.models.type_discriminator import TypeDiscriminator

# TODO update the JSON string below
json = "{}"
# create an instance of TypeDiscriminator from a JSON string
type_discriminator_instance = TypeDiscriminator.from_json(json)
# print the JSON string representation of the object
print(TypeDiscriminator.to_json())

# convert the object into a dict
type_discriminator_dict = type_discriminator_instance.to_dict()
# create an instance of TypeDiscriminator from a dict
type_discriminator_from_dict = TypeDiscriminator.from_dict(type_discriminator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


