# AnalysisSummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org** | **str** | Organization identifier. | [optional] 
**analysis_id** | **str** | Unique identifier of the Dynamic Analysis. | [optional] 
**name** | **str** | Name of the Dynamic Analysis. | [optional] 
**number_of_scans** | **int** | Number of URL scans in the Dynamic Analysis. | [optional] 
**schedule_summary** | [**ScanSchedule**](ScanSchedule.md) | Summary of the schedule for this Dynamic Analysis. | [optional] 
**latest_occurrence_id** | **str** | Identifier of the latest occurrence of this Dynamic Analysis. | [optional] 
**latest_occurrence_date_time** | **str** | Start date and time in ISO-8601 format for the latest occurrence of this Dynamic Analysis. | [optional] 
**latest_occurrence_status** | [**AnalysisOccurrenceStatus**](AnalysisOccurrenceStatus.md) | Status of the latest occurrence of this Dynamic Analysis. | [optional] 
**latest_verification_occurrence_id** | **str** | Identifier of the latest verification-only occurrence of this Dynamic Analysis. | [optional] 
**latest_verification_occurrence_status** | [**AnalysisOccurrenceStatus**](AnalysisOccurrenceStatus.md) | Status of the latest verification-only occurrence of this Dynamic Analysis. | [optional] 
**next_occurrence_date_time** | **str** | Date and time in ISO-8601 format for the next scheduled occurrence of this Dynamic Analysis. | [optional] 
**has_verification_failures** | **bool** | If this value is true, one or more URL scans in the analysis has failed verification. | [optional] 
**has_result_import_in_progress** | **bool** | If true, indicates one or more URL scans are having their results imported into corresponding linked application profiles. | [optional] 
**throttled** | **bool** | This value indicates that one or more URL scans of the latest occurrence of the Dynamic Analysis were throttled  because the maximum number of URL scans was reached.  | [optional] 
**actions** | **list[str]** | The list of actions that can be performed to this Dynamic Analysis based on the status of its latest occurrence. | [optional] 
**created_on** | **str** | The UTC-format date and time of when the Dynamic Analysis occurrence was created. | [optional] 
**last_modified_on** | **str** | The UTC-format date and time when the Dynamic Analysis occurrence was last modified. | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 
**capabilities** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


