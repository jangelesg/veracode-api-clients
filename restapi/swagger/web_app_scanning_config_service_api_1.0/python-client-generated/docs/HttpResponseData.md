# HttpResponseData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_code** | **str** | HTTP Response code. | [optional] 
**redirect_url** | **str** | If the response code was one of 3xx, the redirect URL specified in response. | [optional] 
**response_truncated** | **bool** | If the response is too large, it will be trucated in the raw_response field below. The value of this field will be true in that case.  | [optional] 
**malformed** | **bool** | If true, the response was determined as malformed, e.g. not adhering to HTTP standards. | [optional] 
**raw_response** | **str** | The raw response bytes in the response, encoded in base64. The string may become truncated if it is too long. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


