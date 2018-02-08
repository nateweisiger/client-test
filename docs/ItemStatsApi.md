# swagger_client.ItemStatsApi

All URIs are relative to *https://api.planet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stats**](ItemStatsApi.md#stats) | **POST** /data/v1/stats | Search Stats


# **stats**
> StatsResults stats(search)

Search Stats

Returns a date bucketed histogram of items matching a filter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.ItemStatsApi(swagger_client.ApiClient(configuration))
search = swagger_client.Stats() # Stats | The structured search criteria.

try:
    # Search Stats
    api_response = api_instance.stats(search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemStatsApi->stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**Stats**](Stats.md)| The structured search criteria. | 

### Return type

[**StatsResults**](StatsResults.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

