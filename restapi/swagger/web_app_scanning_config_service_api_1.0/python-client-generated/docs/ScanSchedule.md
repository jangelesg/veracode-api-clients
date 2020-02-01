# ScanSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | [**ScanDuration**](ScanDuration.md) | Duration of the URL scan. | [optional] 
**effective_end_date** | **str** | Present only in responses. The effective end date in ISO-8601 format of the URL scan as calculated from the specified schedule. | [optional] 
**effective_start_date** | **str** | Present only in responses. The effective start date in ISO-8601 format of the URL scan as calculated from the specified schedule. | [optional] 
**end_date** | **str** | If the URL scan duration is zero or less, you must specify the end date as a date and time in future,  and it must be later than the startDate. Must be in ISO-8601 format, for example: 2016-12-03T10:15+01:00.  You can include seconds and milliseconds but are ignored.  | [optional] 
**now** | **bool** | Indicates that the URL scan should start as soon as possible. | [optional] 
**scan_blackout_schedule** | [**ScanBlackoutSchedule**](ScanBlackoutSchedule.md) | URL scan blackout configuration to schedule auto-pause and resume. | [optional] 
**scan_recurrence_schedule** | [**ScanRecurrenceSchedule**](ScanRecurrenceSchedule.md) | URL scan recurrence configuration to schedule batch scans on a recurring basis. | [optional] 
**schedule_status** | **str** | The status of the current schedule, whether active, completed, or canceled. | [optional] 
**start_date** | **str** | The date and time the URL scan should start. Must be in ISO-8601 format, for example:  2016-12-03T10:15+01:00. You can include seconds and milliseconds but they are ignored. If now is set to true, this value is calcuated  as the current time, unless already specified.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


