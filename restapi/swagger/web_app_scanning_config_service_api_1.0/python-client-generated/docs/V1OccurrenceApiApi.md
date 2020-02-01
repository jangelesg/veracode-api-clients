# swagger_client.V1OccurrenceApiApi

All URIs are relative to *https://api.veracode.com/was/configservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_analysis_occurrence_by_analysis_occurrence_id_using_get**](V1OccurrenceApiApi.md#find_analysis_occurrence_by_analysis_occurrence_id_using_get) | **GET** /analysis_occurrences/{analysis_occurrence_id} | Returns the Dynamic Analysis occurrence for the specified identifier.
[**find_analysis_occurrences_by_analysis_id_using_get**](V1OccurrenceApiApi.md#find_analysis_occurrences_by_analysis_id_using_get) | **GET** /analysis_occurrences | Returns a list of occurrences of the Dynamic Analysis. By default, Veracode only returns the occurrences that  started earlier than todays date. Optionally, you can use the status parameter to only return a list of  occurrences of the provided Dynamic Analysis identifier with the specified status(es). 
[**find_scan_occurence_by_occurrence_id_using_get**](V1OccurrenceApiApi.md#find_scan_occurence_by_occurrence_id_using_get) | **GET** /scan_occurrences/{scan_occurrence_id} | Returns the URL scan occurrence for the provided URL scan occurrence identifier.
[**find_scan_occurrences_by_analysis_occurrence_id_using_get**](V1OccurrenceApiApi.md#find_scan_occurrences_by_analysis_occurrence_id_using_get) | **GET** /analysis_occurrences/{analysis_occurrence_id}/scan_occurrences | Returns a list of completed URL scan occurrences for the specified Dynamic Analysis occurrence.
[**find_verification_report_using_get**](V1OccurrenceApiApi.md#find_verification_report_using_get) | **GET** /scan_occurrences/{scan_occurrence_id}/verification_report | Returns the Verification Report, which contains connection and authentication details for the specified scan occurrence ID.
[**get_runtime_scan_configuration_using_get**](V1OccurrenceApiApi.md#get_runtime_scan_configuration_using_get) | **GET** /scan_occurrences/{scan_occurrence_id}/configuration | Returns the configuration for the specified URL scan occurrence.
[**perform_analysis_occurrence_action_using_put**](V1OccurrenceApiApi.md#perform_analysis_occurrence_action_using_put) | **PUT** /analysis_occurrences/{analysis_occurrence_id} | Performs the specified action on the specified occurrence.
[**perform_scan_occurrence_action_using_put**](V1OccurrenceApiApi.md#perform_scan_occurrence_action_using_put) | **PUT** /scan_occurrences/{scan_occurrence_id} | Performs the specified action on the URL scan occurrence.


# **find_analysis_occurrence_by_analysis_occurrence_id_using_get**
> AnalysisOccurrence find_analysis_occurrence_by_analysis_occurrence_id_using_get(analysis_occurrence_id)

Returns the Dynamic Analysis occurrence for the specified identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
analysis_occurrence_id = 'analysis_occurrence_id_example' # str | Identifier of the Dynamic Analysis occurrence.

try:
    # Returns the Dynamic Analysis occurrence for the specified identifier.
    api_response = api_instance.find_analysis_occurrence_by_analysis_occurrence_id_using_get(analysis_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->find_analysis_occurrence_by_analysis_occurrence_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_occurrence_id** | **str**| Identifier of the Dynamic Analysis occurrence. | 

### Return type

[**AnalysisOccurrence**](AnalysisOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_analysis_occurrences_by_analysis_id_using_get**
> PagedAnalysisOccurrence find_analysis_occurrences_by_analysis_id_using_get(include_verification=include_verification, analysis_id=analysis_id, status=status, start_date_after=start_date_after, start_date_before=start_date_before, page=page, size=size)

Returns a list of occurrences of the Dynamic Analysis. By default, Veracode only returns the occurrences that  started earlier than todays date. Optionally, you can use the status parameter to only return a list of  occurrences of the provided Dynamic Analysis identifier with the specified status(es). 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
include_verification = false # bool | Set the parameter to true if you want the results to include the verification details of the returned occurrences. (optional) (default to false)
analysis_id = 'analysis_id_example' # str | Dynamic Analysis identifier. (optional)
status = ['status_example'] # list[str] | The status of the Dynamic Analysis occurrences. (optional)
start_date_after = 'start_date_after_example' # str | The date from when you want the date range to start. The date should be ISO-8601 format or specify the exact  duration, such as: 2h (2 hours ago) 2d (2 days ago) or 2m (2 minutes ago).  (optional)
start_date_before = 'start_date_before_example' # str | The date when you want the date range to finish. The date should be ISO-8601 format or specify the exact duration,  such as: 2h (2 hours in the future) -2d (2 days in the future) or 2m (2 minutes in the future).  (optional)
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page.  (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)

try:
    # Returns a list of occurrences of the Dynamic Analysis. By default, Veracode only returns the occurrences that  started earlier than todays date. Optionally, you can use the status parameter to only return a list of  occurrences of the provided Dynamic Analysis identifier with the specified status(es). 
    api_response = api_instance.find_analysis_occurrences_by_analysis_id_using_get(include_verification=include_verification, analysis_id=analysis_id, status=status, start_date_after=start_date_after, start_date_before=start_date_before, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->find_analysis_occurrences_by_analysis_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_verification** | **bool**| Set the parameter to true if you want the results to include the verification details of the returned occurrences. | [optional] [default to false]
 **analysis_id** | **str**| Dynamic Analysis identifier. | [optional] 
 **status** | [**list[str]**](str.md)| The status of the Dynamic Analysis occurrences. | [optional] 
 **start_date_after** | **str**| The date from when you want the date range to start. The date should be ISO-8601 format or specify the exact  duration, such as: 2h (2 hours ago) 2d (2 days ago) or 2m (2 minutes ago).  | [optional] 
 **start_date_before** | **str**| The date when you want the date range to finish. The date should be ISO-8601 format or specify the exact duration,  such as: 2h (2 hours in the future) -2d (2 days in the future) or 2m (2 minutes in the future).  | [optional] 
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page.  | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 

### Return type

[**PagedAnalysisOccurrence**](PagedAnalysisOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scan_occurence_by_occurrence_id_using_get**
> DetailedScanOccurrence find_scan_occurence_by_occurrence_id_using_get(scan_occurrence_id)

Returns the URL scan occurrence for the provided URL scan occurrence identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
scan_occurrence_id = 'scan_occurrence_id_example' # str | Identifier of the URL scan occurrence.

try:
    # Returns the URL scan occurrence for the provided URL scan occurrence identifier.
    api_response = api_instance.find_scan_occurence_by_occurrence_id_using_get(scan_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->find_scan_occurence_by_occurrence_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_occurrence_id** | **str**| Identifier of the URL scan occurrence. | 

### Return type

[**DetailedScanOccurrence**](DetailedScanOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scan_occurrences_by_analysis_occurrence_id_using_get**
> PagedDetailedScanOccurrence find_scan_occurrences_by_analysis_occurrence_id_using_get(analysis_occurrence_id, page=page, size=size, sort=sort, url=url, linked_platform_app_name=linked_platform_app_name, scan_locked=scan_locked)

Returns a list of completed URL scan occurrences for the specified Dynamic Analysis occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
analysis_occurrence_id = 'analysis_occurrence_id_example' # str | Identifier of the Dynamic Analysis occurrence.
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)
sort = ['sort_example'] # list[str] | The sort criteria you want to use in the format: property(,asc|desc). The default sort order is ascending.  The following sort criteria are supported: linked_platform_app_name, status, scheduled_date, start_date,  total_flaw_count, count_of_failed_verifications, count_of_very_high_sev_flaws, count_of_high_sev_flaws,  count_of_medium_sev_flaws, count_of_low_sev_flaws.  (optional)
url = 'url_example' # str | Filter the results by the specified URL. (optional)
linked_platform_app_name = ['linked_platform_app_name_example'] # list[str] | Filter by the application linked to the Dynamic Analysis. (optional)
scan_locked = true # bool | Filter by URL scan locked status. A URL scan is locked when Veracode is reviewing it. (optional)

try:
    # Returns a list of completed URL scan occurrences for the specified Dynamic Analysis occurrence.
    api_response = api_instance.find_scan_occurrences_by_analysis_occurrence_id_using_get(analysis_occurrence_id, page=page, size=size, sort=sort, url=url, linked_platform_app_name=linked_platform_app_name, scan_locked=scan_locked)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->find_scan_occurrences_by_analysis_occurrence_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_occurrence_id** | **str**| Identifier of the Dynamic Analysis occurrence. | 
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 
 **sort** | [**list[str]**](str.md)| The sort criteria you want to use in the format: property(,asc|desc). The default sort order is ascending.  The following sort criteria are supported: linked_platform_app_name, status, scheduled_date, start_date,  total_flaw_count, count_of_failed_verifications, count_of_very_high_sev_flaws, count_of_high_sev_flaws,  count_of_medium_sev_flaws, count_of_low_sev_flaws.  | [optional] 
 **url** | **str**| Filter the results by the specified URL. | [optional] 
 **linked_platform_app_name** | [**list[str]**](str.md)| Filter by the application linked to the Dynamic Analysis. | [optional] 
 **scan_locked** | **bool**| Filter by URL scan locked status. A URL scan is locked when Veracode is reviewing it. | [optional] 

### Return type

[**PagedDetailedScanOccurrence**](PagedDetailedScanOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_verification_report_using_get**
> VerificationReport find_verification_report_using_get(scan_occurrence_id)

Returns the Verification Report, which contains connection and authentication details for the specified scan occurrence ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
scan_occurrence_id = 'scan_occurrence_id_example' # str | Identifier of the URL scan occurrence.

try:
    # Returns the Verification Report, which contains connection and authentication details for the specified scan occurrence ID.
    api_response = api_instance.find_verification_report_using_get(scan_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->find_verification_report_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_occurrence_id** | **str**| Identifier of the URL scan occurrence. | 

### Return type

[**VerificationReport**](VerificationReport.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_runtime_scan_configuration_using_get**
> ScanConfiguration get_runtime_scan_configuration_using_get(scan_occurrence_id)

Returns the configuration for the specified URL scan occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
scan_occurrence_id = 'scan_occurrence_id_example' # str | Identifier of the URL scan occurrence.

try:
    # Returns the configuration for the specified URL scan occurrence.
    api_response = api_instance.get_runtime_scan_configuration_using_get(scan_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->get_runtime_scan_configuration_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_occurrence_id** | **str**| Identifier of the URL scan occurrence. | 

### Return type

[**ScanConfiguration**](ScanConfiguration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_analysis_occurrence_action_using_put**
> AnalysisOccurrence perform_analysis_occurrence_action_using_put(analysis_occurrence_id, action)

Performs the specified action on the specified occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
analysis_occurrence_id = 'analysis_occurrence_id_example' # str | Identifier of the occurrence.
action = 'action_example' # str | Action to perform.

try:
    # Performs the specified action on the specified occurrence.
    api_response = api_instance.perform_analysis_occurrence_action_using_put(analysis_occurrence_id, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->perform_analysis_occurrence_action_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_occurrence_id** | **str**| Identifier of the occurrence. | 
 **action** | **str**| Action to perform. | 

### Return type

[**AnalysisOccurrence**](AnalysisOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_scan_occurrence_action_using_put**
> DetailedScanOccurrence perform_scan_occurrence_action_using_put(scan_occurrence_id, action)

Performs the specified action on the URL scan occurrence.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.V1OccurrenceApiApi(swagger_client.ApiClient(configuration))
scan_occurrence_id = 'scan_occurrence_id_example' # str | Identifier of the URL scan occurrence.
action = 'action_example' # str | Action to be performed.

try:
    # Performs the specified action on the URL scan occurrence.
    api_response = api_instance.perform_scan_occurrence_action_using_put(scan_occurrence_id, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1OccurrenceApiApi->perform_scan_occurrence_action_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_occurrence_id** | **str**| Identifier of the URL scan occurrence. | 
 **action** | **str**| Action to be performed. | 

### Return type

[**DetailedScanOccurrence**](DetailedScanOccurrence.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

