# DetailedScanOccurrence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scan_occurrence_id** | **str** | Unique identifier and locator of the URL scan occurrence. | [optional] 
**org** | **str** | Unique identifier of the organization. | [optional] 
**analysis_id** | **str** | Identifier of the Dynamic Analysis containing the URL scan of which the current scan occurrence is an instance. | [optional] 
**analysis_name** | **str** | Name of the related Dynamic Analysis. | [optional] 
**analysis_occurrence_id** | **str** | Identifer of the Dynamic Analysis occurrence of which this URL scan occurrence is part. | [optional] 
**count_of_failed_verifications** | **int** | Count of failed verifications. | [optional] 
**count_of_high_sev_flaws** | **int** | Count of high-severity flaws found in the URL scan. | [optional] 
**count_of_low_sev_flaws** | **int** | Count of low-severity flaws found in the URL scan. | [optional] 
**count_of_medium_sev_flaws** | **int** | Count of medium-severity flaws found in the scan. | [optional] 
**count_of_very_high_sev_flaws** | **int** | Count of very high-severity flaws found in the URL scan. | [optional] 
**duration** | **str** | The duration of the URL scan occurrence. If null, no occurrence has run. | [optional] 
**expected_publish_date** | **str** | Date (In ISO-8601 format) when the URL scan occurrence is expected to be published. | [optional] 
**has_custom_configuration** | **bool** | If true, this URL scan has a custom scan configuration. A custom URL scan configuration scan only be specified by Veracode and overrides the current configuration of the URL scan.   | [optional] 
**internal_scan_configuration** | [**InternalScanConfiguration**](InternalScanConfiguration.md) | Internal scan configuration data, if the URL scan is configured as an internal scan. | [optional] 
**extended_status** | **str** | Additional status information available for this URL scan occurrence. | [optional] 
**linked_platform_app_name** | **str** | Name of the Veracode Platform application linked to the URL scan. | [optional] 
**linked_platform_app_uuid** | **str** | UUID of the Veracode Platform application linked to the URL scan. | [optional] 
**linked_platform_app_id** | **int** | The numeric identifier of the Veracode Platform application linked to the scan. | [optional] 
**linked_app_info** | [**LinkedAppInfo**](LinkedAppInfo.md) | Additional Veracode Platform application information, including the results import status. | [optional] 
**result_import_status** | **str** | The status of the import task, if this occurrence results should be sent to an application if the URL scan is linked. | [optional] 
**scan_contact_info** | [**ContactInformation**](ContactInformation.md) | Contact information for the person to received information about the URL scan. | [optional] 
**scan_id** | **str** | Identifier of the URL scan on which this occurrence is based. | [optional] 
**scan_locked** | **bool** | If true, this scan occurrence is locked by Veracode and can be edited and resubmitted by Veracode. | [optional] 
**scan_locked_on** | **str** | Time the scan of this URL scan occurrence was locked. | [optional] 
**scheduled_start_date** | **str** | Date and time in ISO-8601 format when the occurrence is scheduled to start. | [optional] 
**scheduled_end_date** | **str** | Date and time in ISO-8601format when the occurrence is scheduled to end. | [optional] 
**start_date** | **str** | Actual start date and time, in ISO-8601 format. | [optional] 
**end_date** | **str** | Actual end date and time, in ISO-8601 format. | [optional] 
**status** | [**ScanOccurrenceStatus**](ScanOccurrenceStatus.md) | The status of the URL scan occurrence. Cannot be null or empty. | [optional] 
**summary** | [**ScanOccurrenceRuntimeSummary**](ScanOccurrenceRuntimeSummary.md) | A summary of the current URL scan occurrence results. | [optional] 
**target_url** | **str** | The target URL of the scan occurrence. | [optional] 
**total_flaw_count** | **int** | Total count of flaws found in the URL scan occurrence. | [optional] 
**verification_only** | **bool** | If true, this is a verification-only or prescan occurrence. | [optional] 
**verifications** | [**list[ScanVerification]**](ScanVerification.md) | List of verifications done on the scan. | [optional] 
**created_on** | **str** | The UTC-format date and time when URL scan was created. | [optional] 
**last_modified_on** | **str** | The UTC-format date and when the URL scan was last modified. | [optional] 
**app_link_type** | **str** | The type of application linking of the scan. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**capabilities** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


