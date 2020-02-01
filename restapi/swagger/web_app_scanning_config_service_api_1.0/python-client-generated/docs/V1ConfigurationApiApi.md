# swagger_client.V1ConfigurationApiApi

All URIs are relative to *https://api.veracode.com/was/configservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_code_group_by_id_using_get**](V1ConfigurationApiApi.md#find_code_group_by_id_using_get) | **GET** /code_groups/{name} | Returns the details of a code group.
[**get_account_scan_capacity_summary_using_get**](V1ConfigurationApiApi.md#get_account_scan_capacity_summary_using_get) | **GET** /scan_capacity_summary | Returns the scan capacity summary for the organization.
[**get_code_groups_using_get**](V1ConfigurationApiApi.md#get_code_groups_using_get) | **GET** /code_groups | Returns a list of code groups
[**get_default_configuration_using_get**](V1ConfigurationApiApi.md#get_default_configuration_using_get) | **GET** /configuration | Returns the default Dynamic Analysis configuration for the organization.


# **find_code_group_by_id_using_get**
> ListedCode find_code_group_by_id_using_get(name)

Returns the details of a code group.

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
api_instance = swagger_client.V1ConfigurationApiApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name (identifier) of the code group.

try:
    # Returns the details of a code group.
    api_response = api_instance.find_code_group_by_id_using_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1ConfigurationApiApi->find_code_group_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name (identifier) of the code group. | 

### Return type

[**ListedCode**](ListedCode.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_scan_capacity_summary_using_get**
> ScanCapacitySummary get_account_scan_capacity_summary_using_get()

Returns the scan capacity summary for the organization.

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
api_instance = swagger_client.V1ConfigurationApiApi(swagger_client.ApiClient(configuration))

try:
    # Returns the scan capacity summary for the organization.
    api_response = api_instance.get_account_scan_capacity_summary_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1ConfigurationApiApi->get_account_scan_capacity_summary_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScanCapacitySummary**](ScanCapacitySummary.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_code_groups_using_get**
> list[InlineResponse200] get_code_groups_using_get()

Returns a list of code groups

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
api_instance = swagger_client.V1ConfigurationApiApi(swagger_client.ApiClient(configuration))

try:
    # Returns a list of code groups
    api_response = api_instance.get_code_groups_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1ConfigurationApiApi->get_code_groups_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InlineResponse200]**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_configuration_using_get**
> UserConfiguration get_default_configuration_using_get()

Returns the default Dynamic Analysis configuration for the organization.

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
api_instance = swagger_client.V1ConfigurationApiApi(swagger_client.ApiClient(configuration))

try:
    # Returns the default Dynamic Analysis configuration for the organization.
    api_response = api_instance.get_default_configuration_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1ConfigurationApiApi->get_default_configuration_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserConfiguration**](UserConfiguration.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

