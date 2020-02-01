# ScanConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | [**ScanURL**](ScanURL.md) | Target URL for the scan with rules, such as a scan of both HTTP and HTTPS protocols or the restriction of the URL scan to a specific directory type. | [optional] 
**allowed_hosts** | [**list[ScanURL]**](ScanURL.md) | Additional allowed hosts for the URL scan with rules, such as a scan of both HTTP and HTTPS protocols or the restriction of the URL scan to a specific directory type. | [optional] 
**auth_configuration** | [**AuthenticationConfiguration**](AuthenticationConfiguration.md) | Authentication configuration for the URL scan. | [optional] 
**crawl_configuration** | [**CrawlConfiguration**](CrawlConfiguration.md) | Crawl configuration for the URL scan. | [optional] 
**scan_setting** | [**ScanSetting**](ScanSetting.md) | Settings for the URL scan. You do not have to specify all the settings. Any settings you do specificy at the  URL scan configuration level override or add to the Dynamic Analysis configuration level.  | [optional] 
**capabilities** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


