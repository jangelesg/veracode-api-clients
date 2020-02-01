# swagger_client.V1AnalysisApiApi

All URIs are relative to *https://api.veracode.com/was/configservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scans_to_analysis_using_post**](V1AnalysisApiApi.md#add_scans_to_analysis_using_post) | **POST** /analyses/{analysis_id}/scans | Adds one or more new URLs to the Dynamic Analysis. You can also add URLs by updating the analysis.
[**create_analysis_using_post**](V1AnalysisApiApi.md#create_analysis_using_post) | **POST** /analyses | Creates a new Dynamic Analysis for the account, if the user has access to the account. Returns the URL of the  new analysis in the HTTP response header. 
[**delete_analysis_using_delete**](V1AnalysisApiApi.md#delete_analysis_using_delete) | **DELETE** /analyses/{analysis_id} | Deletes the Dynamic Analysis for the provided identifier. You can only hard-delete an analysis if it has never run.
[**delete_scan_using_delete**](V1AnalysisApiApi.md#delete_scan_using_delete) | **DELETE** /scans/{scan_id} | Deletes the URL scan with the specified dentifier. You can only delete scans that have never run.
[**find_all_scans_for_analysis_using_get**](V1AnalysisApiApi.md#find_all_scans_for_analysis_using_get) | **GET** /analyses/{analysis_id}/scans | Returns a list of all occurrences of the Dynamic Analysis.
[**find_analysis_audits_by_id_using_get**](V1AnalysisApiApi.md#find_analysis_audits_by_id_using_get) | **GET** /analyses/{analysis_id}/audits | Returns a list of audit logs for the specified Dynamic Analysis.
[**find_analysis_by_id_using_get**](V1AnalysisApiApi.md#find_analysis_by_id_using_get) | **GET** /analyses/{analysis_id} | Returns the Dynamic Analysis for the provided identifier.
[**find_analysis_summaries_using_get**](V1AnalysisApiApi.md#find_analysis_summaries_using_get) | **GET** /analyses | Returns a list of Dynamic Analyses for the current organization or a specified, alternate organization.
[**find_platform_applications_using_get**](V1AnalysisApiApi.md#find_platform_applications_using_get) | **GET** /platform_applications | Returns a list of applications in the Veracode Platform.
[**find_scan_audits_by_id_using_get**](V1AnalysisApiApi.md#find_scan_audits_by_id_using_get) | **GET** /scans/{scan_id}/audits | Returns a list of audits (activity logs) for the provided URL scan identifier.
[**find_scan_by_id_using_get**](V1AnalysisApiApi.md#find_scan_by_id_using_get) | **GET** /scans/{scan_id} | Returns a URL scan.
[**get_scan_configuration_using_get**](V1AnalysisApiApi.md#get_scan_configuration_using_get) | **GET** /scans/{scan_id}/configuration | Returns the configuration for the specified URL scan.
[**update_analysis_using_put**](V1AnalysisApiApi.md#update_analysis_using_put) | **PUT** /analyses/{analysis_id} | Updates a Dynamic Analysis for the provided identifier.
[**update_scan_configuration_using_put**](V1AnalysisApiApi.md#update_scan_configuration_using_put) | **PUT** /scans/{scan_id}/configuration | Updates the configuration for the specified URL scan.
[**update_scan_using_put**](V1AnalysisApiApi.md#update_scan_using_put) | **PUT** /scans/{scan_id} | Updates the URL scan request.


# **add_scans_to_analysis_using_post**
> add_scans_to_analysis_using_post(analysis_id, scans)

Adds one or more new URLs to the Dynamic Analysis. You can also add URLs by updating the analysis.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Dynamic Analysis identifier.
scans = [swagger_client.ScanRequest()] # list[ScanRequest] | scans

try:
    # Adds one or more new URLs to the Dynamic Analysis. You can also add URLs by updating the analysis.
    api_instance.add_scans_to_analysis_using_post(analysis_id, scans)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->add_scans_to_analysis_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Dynamic Analysis identifier. | 
 **scans** | [**list[ScanRequest]**](ScanRequest.md)| scans | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_analysis_using_post**
> create_analysis_using_post(analysis, run_verification=run_verification, validate_only=validate_only)

Creates a new Dynamic Analysis for the account, if the user has access to the account. Returns the URL of the  new analysis in the HTTP response header. 

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis = swagger_client.AnalysisRequest() # AnalysisRequest | Details of the Dynamic Analysis request.
run_verification = true # bool | If true, then the Dynamic Analysis is created and a verification scan starts immediately. (optional)
validate_only = false # bool | If true, the request is only validated and run_verification is ignored. (optional) (default to false)

try:
    # Creates a new Dynamic Analysis for the account, if the user has access to the account. Returns the URL of the  new analysis in the HTTP response header. 
    api_instance.create_analysis_using_post(analysis, run_verification=run_verification, validate_only=validate_only)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->create_analysis_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis** | [**AnalysisRequest**](AnalysisRequest.md)| Details of the Dynamic Analysis request. | 
 **run_verification** | **bool**| If true, then the Dynamic Analysis is created and a verification scan starts immediately. | [optional] 
 **validate_only** | **bool**| If true, the request is only validated and run_verification is ignored. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_analysis_using_delete**
> delete_analysis_using_delete(analysis_id)

Deletes the Dynamic Analysis for the provided identifier. You can only hard-delete an analysis if it has never run.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Identifier of the Dynamic Analysis.

try:
    # Deletes the Dynamic Analysis for the provided identifier. You can only hard-delete an analysis if it has never run.
    api_instance.delete_analysis_using_delete(analysis_id)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->delete_analysis_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Identifier of the Dynamic Analysis. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scan_using_delete**
> object delete_scan_using_delete(scan_id)

Deletes the URL scan with the specified dentifier. You can only delete scans that have never run.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.

try:
    # Deletes the URL scan with the specified dentifier. You can only delete scans that have never run.
    api_response = api_instance.delete_scan_using_delete(scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->delete_scan_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_all_scans_for_analysis_using_get**
> PagedDetailedScan find_all_scans_for_analysis_using_get(analysis_id, page=page, size=size)

Returns a list of all occurrences of the Dynamic Analysis.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Dynamic Analysis identifier.
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)

try:
    # Returns a list of all occurrences of the Dynamic Analysis.
    api_response = api_instance.find_all_scans_for_analysis_using_get(analysis_id, page=page, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_all_scans_for_analysis_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Dynamic Analysis identifier. | 
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 

### Return type

[**PagedDetailedScan**](PagedDetailedScan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_analysis_audits_by_id_using_get**
> PagedAuditData find_analysis_audits_by_id_using_get(analysis_id, page=page, size=size, sort=sort)

Returns a list of audit logs for the specified Dynamic Analysis.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Identifier of the Dynamic Analysis.
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property(,asc|desc). The default sort order is ascending. The supported sort criteria are event_type and audited_on. (optional)

try:
    # Returns a list of audit logs for the specified Dynamic Analysis.
    api_response = api_instance.find_analysis_audits_by_id_using_get(analysis_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_analysis_audits_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Identifier of the Dynamic Analysis. | 
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). The default sort order is ascending. The supported sort criteria are event_type and audited_on. | [optional] 

### Return type

[**PagedAuditData**](PagedAuditData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_analysis_by_id_using_get**
> Analysis find_analysis_by_id_using_get(analysis_id)

Returns the Dynamic Analysis for the provided identifier.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Identifier of the Dynamic Analysis.

try:
    # Returns the Dynamic Analysis for the provided identifier.
    api_response = api_instance.find_analysis_by_id_using_get(analysis_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_analysis_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Identifier of the Dynamic Analysis. | 

### Return type

[**Analysis**](Analysis.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_analysis_summaries_using_get**
> PagedAnalysisSummary find_analysis_summaries_using_get(page=page, size=size, sort=sort, name=name, status=status)

Returns a list of Dynamic Analyses for the current organization or a specified, alternate organization.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)
sort = ['sort_example'] # list[str] | Sorting criteria in the format: property(,asc|desc). The default sort order is ascending. The following sort criteria are supported: name, status, number_of_scans, latest_occurrence_date_time.  (optional)
name = 'name_example' # str | Filter by the Dynamic Analysis name. (optional)
status = ['status_example'] # list[str] | Filter by the Dynamic Analysis status. (optional)

try:
    # Returns a list of Dynamic Analyses for the current organization or a specified, alternate organization.
    api_response = api_instance.find_analysis_summaries_using_get(page=page, size=size, sort=sort, name=name, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_analysis_summaries_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 
 **sort** | [**list[str]**](str.md)| Sorting criteria in the format: property(,asc|desc). The default sort order is ascending. The following sort criteria are supported: name, status, number_of_scans, latest_occurrence_date_time.  | [optional] 
 **name** | **str**| Filter by the Dynamic Analysis name. | [optional] 
 **status** | [**list[str]**](str.md)| Filter by the Dynamic Analysis status. | [optional] 

### Return type

[**PagedAnalysisSummary**](PagedAnalysisSummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_platform_applications_using_get**
> PagedPlatformApplication find_platform_applications_using_get(page=page, size=size, sort=sort, application_name=application_name)

Returns a list of applications in the Veracode Platform.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)
sort = 'sort_example' # str | Use this parameter to sort the results in the format: property(,asc|desc). The default sort order is ascending. The following sort criteria are supported: name, id (optional)
application_name = 'application_name_example' # str | Application name-based search parameter. (optional)

try:
    # Returns a list of applications in the Veracode Platform.
    api_response = api_instance.find_platform_applications_using_get(page=page, size=size, sort=sort, application_name=application_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_platform_applications_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 
 **sort** | **str**| Use this parameter to sort the results in the format: property(,asc|desc). The default sort order is ascending. The following sort criteria are supported: name, id | [optional] 
 **application_name** | **str**| Application name-based search parameter. | [optional] 

### Return type

[**PagedPlatformApplication**](PagedPlatformApplication.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scan_audits_by_id_using_get**
> PagedAuditData find_scan_audits_by_id_using_get(scan_id, page=page, size=size, sort=sort)

Returns a list of audits (activity logs) for the provided URL scan identifier.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.
page = 56 # int | The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. (optional)
size = 56 # int | The number of records you want to display per page. The maximum is 100 and the default is 20. (optional)
sort = ['sort_example'] # list[str] | Use sort criteria in the format: property(,asc|desc). The default sort order is ascending. Supported sort  criteria are event_type and audited_on.  (optional)

try:
    # Returns a list of audits (activity logs) for the provided URL scan identifier.
    api_response = api_instance.find_scan_audits_by_id_using_get(scan_id, page=page, size=size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_scan_audits_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 
 **page** | **int**| The number of the results page you want to retrieve (0..N), where the default is 0 if you do not specify a page. | [optional] 
 **size** | **int**| The number of records you want to display per page. The maximum is 100 and the default is 20. | [optional] 
 **sort** | [**list[str]**](str.md)| Use sort criteria in the format: property(,asc|desc). The default sort order is ascending. Supported sort  criteria are event_type and audited_on.  | [optional] 

### Return type

[**PagedAuditData**](PagedAuditData.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_scan_by_id_using_get**
> DetailedScan find_scan_by_id_using_get(scan_id)

Returns a URL scan.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.

try:
    # Returns a URL scan.
    api_response = api_instance.find_scan_by_id_using_get(scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->find_scan_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 

### Return type

[**DetailedScan**](DetailedScan.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scan_configuration_using_get**
> ScanConfiguration get_scan_configuration_using_get(scan_id, runtime=runtime)

Returns the configuration for the specified URL scan.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.
runtime = false # bool | If true, this call returns the configuration that applies to the specified URL scan as well as the Dynamic  Analysis configuration and the system defaults.  (optional) (default to false)

try:
    # Returns the configuration for the specified URL scan.
    api_response = api_instance.get_scan_configuration_using_get(scan_id, runtime=runtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->get_scan_configuration_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 
 **runtime** | **bool**| If true, this call returns the configuration that applies to the specified URL scan as well as the Dynamic  Analysis configuration and the system defaults.  | [optional] [default to false]

### Return type

[**ScanConfiguration**](ScanConfiguration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_analysis_using_put**
> update_analysis_using_put(analysis_id, analysis=analysis, run_verification=run_verification, method=method)

Updates a Dynamic Analysis for the provided identifier.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
analysis_id = 'analysis_id_example' # str | Identifier of the Dynamic Analysis.
analysis = swagger_client.AnalysisRequest() # AnalysisRequest | Details of the Dynamic Analysis. (optional)
run_verification = true # bool | If true, then Veracode updates the Dynamic Analysis and starts a verification scan immediately if no other  occurrences of the Dynamic Analysis are in progress.  (optional)
method = 'method_example' # str | If set to PATCH, Veracode replaces the content, except for the list of URLs in the Dynamic Analysis.  The list of URLs are partially updated based on the action_type attribute for each individual analysis  update request.'  (optional)

try:
    # Updates a Dynamic Analysis for the provided identifier.
    api_instance.update_analysis_using_put(analysis_id, analysis=analysis, run_verification=run_verification, method=method)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->update_analysis_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **analysis_id** | **str**| Identifier of the Dynamic Analysis. | 
 **analysis** | [**AnalysisRequest**](AnalysisRequest.md)| Details of the Dynamic Analysis. | [optional] 
 **run_verification** | **bool**| If true, then Veracode updates the Dynamic Analysis and starts a verification scan immediately if no other  occurrences of the Dynamic Analysis are in progress.  | [optional] 
 **method** | **str**| If set to PATCH, Veracode replaces the content, except for the list of URLs in the Dynamic Analysis.  The list of URLs are partially updated based on the action_type attribute for each individual analysis  update request.&#39;  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_configuration_using_put**
> object update_scan_configuration_using_put(scan_id, configuration=configuration, method=method)

Updates the configuration for the specified URL scan.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.
configuration = swagger_client.ScanConfigurationRequest() # ScanConfigurationRequest | URL scan configuration. (optional)
method = 'method_example' # str | When set to PATCH, the configuration content is partially updated. (optional)

try:
    # Updates the configuration for the specified URL scan.
    api_response = api_instance.update_scan_configuration_using_put(scan_id, configuration=configuration, method=method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->update_scan_configuration_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 
 **configuration** | [**ScanConfigurationRequest**](ScanConfigurationRequest.md)| URL scan configuration. | [optional] 
 **method** | **str**| When set to PATCH, the configuration content is partially updated. | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scan_using_put**
> object update_scan_using_put(scan_id, scan=scan, scanner_version=scanner_version, method=method)

Updates the URL scan request.

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
api_instance = swagger_client.V1AnalysisApiApi(swagger_client.ApiClient(configuration))
scan_id = 'scan_id_example' # str | Identifier of the URL scan.
scan = swagger_client.ScanRequest() # ScanRequest | The URL scan data. (optional)
scanner_version = 'scanner_version_example' # str | Version of scan engine. (optional)
method = 'method_example' # str | If set to PATCH, this call partially replaces the content. The update does not affect the list of scans in the  Dynamic Analysis request.  (optional)

try:
    # Updates the URL scan request.
    api_response = api_instance.update_scan_using_put(scan_id, scan=scan, scanner_version=scanner_version, method=method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1AnalysisApiApi->update_scan_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_id** | **str**| Identifier of the URL scan. | 
 **scan** | [**ScanRequest**](ScanRequest.md)| The URL scan data. | [optional] 
 **scanner_version** | **str**| Version of scan engine. | [optional] 
 **method** | **str**| If set to PATCH, this call partially replaces the content. The update does not affect the list of scans in the  Dynamic Analysis request.  | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

