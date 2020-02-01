# ScanConfigurationRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_hosts** | [**list[ScanURL]**](ScanURL.md) | Additional allowed hosts for the URL scan with rules, such as a scan of both HTTP and HTTPS protocols or the restriction of the URL scan to a specific directory type. | [optional] 
**auth_configuration** | [**AuthenticationConfiguration**](AuthenticationConfiguration.md) | Authentication configuration for the URL scan. | [optional] 
**crawl_configuration** | [**CrawlConfiguration**](CrawlConfiguration.md) | Crawl configuration for the URL scan. | [optional] 
**scan_setting** | [**ScanSetting**](ScanSetting.md) | URL scan setting. Not mandatory and not everything must be specified. | [optional] 
**target_url** | [**ScanURL**](ScanURL.md) | Target URL for the scan with rules such as a scan of both HTTP and HTTPS protocols or the restriction of the URL scan to a specific directory type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


