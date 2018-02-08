# swagger_client.ItemSearchApi

All URIs are relative to *https://api.planet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_search**](ItemSearchApi.md#create_search) | **POST** /data/v1/searches | Create Saved Search
[**list_searches**](ItemSearchApi.md#list_searches) | **GET** /data/v1/searches | List Saved Searches
[**quick_search**](ItemSearchApi.md#quick_search) | **POST** /data/v1/quick-search | Quick Search
[**search_delete**](ItemSearchApi.md#search_delete) | **DELETE** /data/v1/searches/{search_id} | Delete Saved Search
[**search_detail**](ItemSearchApi.md#search_detail) | **GET** /data/v1/searches/{search_id} | Get Saved Search
[**search_results**](ItemSearchApi.md#search_results) | **GET** /data/v1/searches/{search_id}/results | Run Saved Search
[**search_update**](ItemSearchApi.md#search_update) | **PUT** /data/v1/searches/{search_id} | Update Saved Search


# **create_search**
> Search create_search(search, strict=strict)

Create Saved Search

Create a new saved search.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search = swagger_client.SavedSearch() # SavedSearch | The structured search criteria.
strict = false # bool | Strictly remove false positives from geo intersection. (optional) (default to false)

try:
    # Create Saved Search
    api_response = api_instance.create_search(search, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->create_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**SavedSearch**](SavedSearch.md)| The structured search criteria. | 
 **strict** | **bool**| Strictly remove false positives from geo intersection. | [optional] [default to false]

### Return type

[**Search**](Search.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_searches**
> SearchPage list_searches(page=page, page_size=page_size, sort=sort, search_type=search_type)

List Saved Searches

List all saved searches available to the authenticated user.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
page = 'page_example' # str | Token representing a specific page of results. This should never be constructed manually. (optional)
page_size = 250 # int | Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \"_page\" parameter. (optional) (default to 250)
sort = 'created desc' # str | Field and direction to order results by. This may not be provided with the \"_page\" parameter. (optional) (default to created desc)
search_type = 'any' # str | Search type filter. (optional) (default to any)

try:
    # List Saved Searches
    api_response = api_instance.list_searches(page=page, page_size=page_size, sort=sort, search_type=search_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->list_searches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| Token representing a specific page of results. This should never be constructed manually. | [optional] 
 **page_size** | **int**| Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to 250]
 **sort** | **str**| Field and direction to order results by. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to created desc]
 **search_type** | **str**| Search type filter. | [optional] [default to any]

### Return type

[**SearchPage**](SearchPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quick_search**
> ItemPage quick_search(search, page_size=page_size, sort=sort, strict=strict)

Quick Search

Executes a structured item search.  The search APIs allow for both simple and complex `item` searches. Complex searches support boolean conditions, multiple values, geometries using GeoJSON and others. You can also save, retrieve and execute searches that you use frequently for easy use later.  [Learn more about searching](/docs/searches-filtering) 

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search = swagger_client.QuickSearch() # QuickSearch | The structured search criteria.
page_size = 250 # int | Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \"_page\" parameter. (optional) (default to 250)
sort = 'published desc' # str | Field and direction to order results by. This may not be provided with the \"_page\" parameter. (optional) (default to published desc)
strict = false # bool | Strictly remove false positives from geo intersection. (optional) (default to false)

try:
    # Quick Search
    api_response = api_instance.quick_search(search, page_size=page_size, sort=sort, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->quick_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**QuickSearch**](QuickSearch.md)| The structured search criteria. | 
 **page_size** | **int**| Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to 250]
 **sort** | **str**| Field and direction to order results by. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to published desc]
 **strict** | **bool**| Strictly remove false positives from geo intersection. | [optional] [default to false]

### Return type

[**ItemPage**](ItemPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_delete**
> search_delete(search_id)

Delete Saved Search

Delete an existing saved search.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search_id = 'search_id_example' # str | Saved search identifier.

try:
    # Delete Saved Search
    api_instance.search_delete(search_id)
except ApiException as e:
    print("Exception when calling ItemSearchApi->search_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Saved search identifier. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_detail**
> Search search_detail(search_id)

Get Saved Search

Get a saved search by id.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search_id = 'search_id_example' # str | Saved search identifier.

try:
    # Get Saved Search
    api_response = api_instance.search_detail(search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->search_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Saved search identifier. | 

### Return type

[**Search**](Search.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_results**
> ItemPage search_results(search_id, page=page, page_size=page_size, sort=sort, strict=strict)

Run Saved Search

Executes a saved search.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search_id = 'search_id_example' # str | Saved search identifier.
page = 'page_example' # str | Token representing a specific page of results. This should never be constructed manually. (optional)
page_size = 250 # int | Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \"_page\" parameter. (optional) (default to 250)
sort = 'published desc' # str | Field and direction to order results by. This may not be provided with the \"_page\" parameter. (optional) (default to published desc)
strict = false # bool | Strictly remove false positives from geo intersection. (optional) (default to false)

try:
    # Run Saved Search
    api_response = api_instance.search_results(search_id, page=page, page_size=page_size, sort=sort, strict=strict)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->search_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Saved search identifier. | 
 **page** | **str**| Token representing a specific page of results. This should never be constructed manually. | [optional] 
 **page_size** | **int**| Number of results to return per page. This may only be used at the start of pagination. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to 250]
 **sort** | **str**| Field and direction to order results by. This may not be provided with the \&quot;_page\&quot; parameter. | [optional] [default to published desc]
 **strict** | **bool**| Strictly remove false positives from geo intersection. | [optional] [default to false]

### Return type

[**ItemPage**](ItemPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_update**
> Search search_update(search_id, search)

Update Saved Search

Update an existing saved search.

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
api_instance = swagger_client.ItemSearchApi(swagger_client.ApiClient(configuration))
search_id = 'search_id_example' # str | Saved search identifier.
search = swagger_client.SavedSearch() # SavedSearch | The structured search criteria.

try:
    # Update Saved Search
    api_response = api_instance.search_update(search_id, search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemSearchApi->search_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Saved search identifier. | 
 **search** | [**SavedSearch**](SavedSearch.md)| The structured search criteria. | 

### Return type

[**Search**](Search.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

