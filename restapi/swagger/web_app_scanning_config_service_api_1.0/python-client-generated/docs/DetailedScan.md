# DetailedScan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_id** | **str** | Identifier of the URL scan. | [optional] 
**org** | **str** | Organization identifier. | [optional] 
**target_url** | **str** | Target URL of the scan. | [optional] 
**analysis_id** | **str** | Identifier of the Dynamic Analysis this URL scan is a part of. | [optional] 
**analysis_name** | **str** | Name of the Dynamic Analysis this URL scan is a part of. | [optional] 
**internal_scan_configuration** | [**InternalScanConfiguration**](InternalScanConfiguration.md) | Configuration data for the internal scanning gateway and endpoint, if this scan is an internal scan. | [optional] 
**last_verified_by_prescan** | **bool** | True, if the last verification was done using a prescan. | [optional] 
**last_verified_on** | **str** | Date and time this configuration was last verified using a prescan occurrence. | [optional] 
**latest_occurrence_status** | [**ScanOccurrenceStatus**](ScanOccurrenceStatus.md) | Status of the latest occurrence of this URL scan. | [optional] 
**latest_occurrence_verifications** | [**list[ScanVerification]**](ScanVerification.md) | List of the verifications completed for this URL scan in the latest occurrence. | [optional] 
**linked_platform_app_uuid** | **str** | UUID of the Veracode Platform application linked to the URL scan. | [optional] 
**linked_platform_app_name** | **str** | Name of the linked application in the application portfoliio in the Veracode Platform, if this URL scan is  linked to an application.   | [optional] 
**scan_contact_info** | [**ContactInformation**](ContactInformation.md) | Contact information for the user to receive information about this URL scan. | [optional] 
**scan_locked** | **bool** | If true, the URL scan is locked by Veracode and can only be edited or resubmitted by Veracode. | [optional] 
**scan_locked_on** | **str** | Date and time the URL scan was locked. | [optional] 
**created_on** | **str** | UTC-format date and time when the URL scan was created. | [optional] 
**last_modified_on** | **str** | UTC-format date and time when the URL scan was last modified. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**capabilities** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


