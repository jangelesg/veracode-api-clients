# AnalysisOccurrence

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_end_date** | **str** | The date and time the Dynamic Analysis ended. | [optional] 
**actual_start_date** | **str** | The date and time the Dynamic Analysis started. | [optional] 
**all_scans_passed_verification** | **bool** |  | [optional] 
**analysis_id** | **str** | Identifier of the Dynamic Analysis an occurrence is based on. This field cannot be null or empty. | [optional] 
**analysis_occurrence_id** | **str** | Unique identifier for an occurrence of a Dynamic Analysis. This field cannot be null or empty. | [optional] 
**count_of_failed_verifications** | **int** | Number of URL scan occurrences that failed verifications. | [optional] 
**duration** | **str** | Duration of the Dynamic Analysis occurrence. | [optional] 
**end_date** | **str** | The date and time when the Dynamic Analysis is scheduled to end. | [optional] 
**percent_scanned** | **int** | The percentage of URL scans completed. | [optional] 
**start_date** | **str** | The date and time when the Dynamic Analysis is scheduled to start. | [optional] 
**status** | [**AnalysisOccurrenceStatus**](AnalysisOccurrenceStatus.md) | The status of the Dynamic Analysis occurrence. This field cannot be null or empty. | [optional] 
**verification_only** | **bool** | Set this value to true if you want this analysis occurrence to only run for verification purposes. | [optional] 
**created_on** | **str** | The UTC-format for the date and time when the Dynamic Analysis was created. | [optional] 
**last_modified_on** | **str** | The UTC-format for the date and time when the Dynamic Analysis was last modified. | [optional] 
**capabilities** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


