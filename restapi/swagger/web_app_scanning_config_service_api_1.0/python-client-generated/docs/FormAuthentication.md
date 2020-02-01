# FormAuthentication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authtype** | **str** | The type of authentication. Only the value FORM is expected. | [optional] 
**authentication_id** | **str** | Unique identifier locator. | [optional] 
**login_script_data** | [**Script**](Script.md) | The login script. | [optional] 
**logout_script_data** | [**Script**](Script.md) | The logout script, which is required if advanced mode scanning is configured. | [optional] 
**verification** | [**LoginVerification**](LoginVerification.md) | The verification to use, which is not required if advanced mode scanning is configured. | [optional] 
**logout_detection** | [**LogoutDetection**](LogoutDetection.md) | The type of logout detection to use. If verification is already specified, this is ignored. It is not required if advanced mode scanning is configured. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


