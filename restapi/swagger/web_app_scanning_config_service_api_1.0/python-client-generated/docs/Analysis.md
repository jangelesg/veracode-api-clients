# Analysis

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **str** | Identifier of the Dynamic Analysis. | [optional] 
**name** | **str** | Name of the Dynamic Analysis. | [optional] 
**org** | **str** | Identifier of the organization. | [optional] 
**org_info** | [**OrgInformation**](OrgInformation.md) | Organization details. | [optional] 
**scan_setting** | [**ScanSetting**](ScanSetting.md) | Scan setting for the Dynamic Analysis that applies to all URL scans in analysis, unless overridden at the URL scan level. | [optional] 
**schedule** | [**ScanSchedule**](ScanSchedule.md) | The schedule for the Dynamic Analysis. | [optional] 
**special_instructions** | **str** | Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis. | [optional] 
**throttled** | **bool** |  | [optional] 
**visibility** | [**VisibilitySetup**](VisibilitySetup.md) | The setting that determines who can access the analysis. | [optional] 
**created_on** | **str** | The UTC-format date and time when the Dynamic Analysis was created. | [optional] 
**last_modified_on** | **str** | UTC-format date and time when the Dynamic Analysis was last modified. | [optional] 
**latest_occurrence_status** | [**AnalysisOccurrenceStatus**](AnalysisOccurrenceStatus.md) | Status of the latest occurrence of this Dynamic Analysis. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


