# ConnectionVerificationData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_type** | **str** | The context of the URL. Currently, Veracode only verifies the target URL, therefore the only value is TARGET_URL. | [optional] 
**url** | **str** | The URL being verified. | [optional] 
**resolved_ip_address** | **str** | IP address for the URL as resolved by the dynamic scanner. | [optional] 
**browser_used** | **bool** | If true, a browser was used to verify the existence and accessibility of the URL. If false, the URL was accessed directly from the scanner.  | [optional] 
**attempts** | [**list[ConnectionAttemptData]**](ConnectionAttemptData.md) | Details on each attempt made to verify. For a direct request sent by scanner this will likely have only one entry. if the request is made from a browser it will capture all requests made to load the page.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


