# ConnectionAttemptData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_initiated** | **float** | The UTC time in milliseconds when the connection attempt was initiated. | [optional] 
**response_time** | **float** | The UTC elapsed time for the completion of the request, in milliseconds, nullable. | [optional] 
**scope** | **str** | The scopr of the request as evaluated by the scanner based on target URL, whitelist and blacklist. | [optional] 
**request** | [**HttpRequestData**](HttpRequestData.md) | Details of the HTTP Request that was sent.  | [optional] 
**response** | [**HttpResponseData**](HttpResponseData.md) | Details of the HTTP Request that was sent.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


