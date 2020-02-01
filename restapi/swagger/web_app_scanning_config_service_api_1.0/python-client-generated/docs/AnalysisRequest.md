# AnalysisRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Dynamic Analysis. The name must be unique to the application porfolio of the organization and the  length must be between 6 and 256 characters.  | [optional] 
**org_info** | [**OrgInformation**](OrgInformation.md) | Organization information. | [optional] 
**scan_setting** | [**ScanSetting**](ScanSetting.md) | The Dynamic Analysis scan level setting that applies to all URL scans in this analysis. | [optional] 
**scans** | [**list[ScanRequest]**](ScanRequest.md) | The list of URL scans included in the analysis. | [optional] 
**schedule** | [**ScanSchedule**](ScanSchedule.md) | The schedule for the URL scan. This is optional. If not specified, no URL scans will run. You can still run verification scans.  | [optional] 
**special_instructions** | **str** | Special instructions related to the Dynamic Analysis. Can be null. Instructions can delay the analysis. | [optional] 
**visibility** | [**VisibilitySetup**](VisibilitySetup.md) | Visibility setup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


