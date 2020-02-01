# ScanRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | **str** | Optional action type for when bulk scan requests are being modified for a single Dynamic Analysis. | [optional] 
**scan_id** | **str** | Unique identifier of the URL scan. Only necessary for updates. | [optional] 
**scan_contact_info** | [**ContactInformation**](ContactInformation.md) |  | [optional] 
**scan_config_request** | [**ScanConfigurationRequest**](ScanConfigurationRequest.md) |  | [optional] 
**linked_platform_app_uuid** | **str** | UUID of the Veracode Platform application to which this URL scan should link. Optional. | [optional] 
**internal_scan_configuration** | [**InternalScanConfiguration**](InternalScanConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


