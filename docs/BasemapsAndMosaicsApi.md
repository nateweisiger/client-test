# swagger_client.BasemapsAndMosaicsApi

All URIs are relative to *https://api.planet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mosaic**](BasemapsAndMosaicsApi.md#get_mosaic) | **GET** /basemaps/v1/mosaics/{mosaic_id} | Get Mosaic
[**get_mosaic_grid**](BasemapsAndMosaicsApi.md#get_mosaic_grid) | **GET** /basemaps/v1/mosaics/{mosaic_id}/grid | Get Mosaic Grid
[**get_mosaic_tile_json**](BasemapsAndMosaicsApi.md#get_mosaic_tile_json) | **GET** /basemaps/v1/mosaics/{mosaic_id}/tiles | Get Mosaic TileJSON
[**get_quad**](BasemapsAndMosaicsApi.md#get_quad) | **GET** /basemaps/v1/mosaics/{mosaic_id}/quads/{quad_id} | Get Mosaic Quad
[**get_quad_download**](BasemapsAndMosaicsApi.md#get_quad_download) | **GET** /basemaps/v1/mosaics/{mosaic_id}/quads/{quad_id}/full | Get Mosaic Quad URL
[**get_quad_download_links**](BasemapsAndMosaicsApi.md#get_quad_download_links) | **GET** /basemaps/v1/mosaics/{mosaic_id}/quads | List Mosaic Quads
[**get_quad_items**](BasemapsAndMosaicsApi.md#get_quad_items) | **GET** /basemaps/v1/mosaics/{mosaic_id}/quads/{quad_id}/items | List Mosaic Quad Items
[**get_series**](BasemapsAndMosaicsApi.md#get_series) | **GET** /basemaps/v1/series/{series_id} | Get Mosaic Series
[**get_series_mosaics**](BasemapsAndMosaicsApi.md#get_series_mosaics) | **GET** /basemaps/v1/series/{series_id}/mosaics | List Series&#39; Mosaics
[**list_mosaics**](BasemapsAndMosaicsApi.md#list_mosaics) | **GET** /basemaps/v1/mosaics | List Mosaics
[**list_series**](BasemapsAndMosaicsApi.md#list_series) | **GET** /basemaps/v1/series | List Mosaic Series


# **get_mosaic**
> Mosaic get_mosaic(mosaic_id)

Get Mosaic

Get a mosaic by id.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.

try:
    # Get Mosaic
    api_response = api_instance.get_mosaic(mosaic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_mosaic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 

### Return type

[**Mosaic**](Mosaic.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mosaic_grid**
> GridContext get_mosaic_grid(mosaic_id)

Get Mosaic Grid

Get extended mosaic metadata by id.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.

try:
    # Get Mosaic Grid
    api_response = api_instance.get_mosaic_grid(mosaic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_mosaic_grid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 

### Return type

[**GridContext**](GridContext.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mosaic_tile_json**
> object get_mosaic_tile_json(mosaic_id)

Get Mosaic TileJSON

Get TileJSON for Mosaic. See https://github.com/mapbox/tilejson-spec

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.

try:
    # Get Mosaic TileJSON
    api_response = api_instance.get_mosaic_tile_json(mosaic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_mosaic_tile_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quad**
> Quad get_quad(mosaic_id, quad_id)

Get Mosaic Quad

Get mosaic quad by id.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
quad_id = 'quad_id_example' # str | Quad identifier.

try:
    # Get Mosaic Quad
    api_response = api_instance.get_quad(mosaic_id, quad_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_quad: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **quad_id** | **str**| Quad identifier. | 

### Return type

[**Quad**](Quad.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quad_download**
> Error get_quad_download(mosaic_id, quad_id)

Get Mosaic Quad URL

Get a full quad download URL quad id.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
quad_id = 'quad_id_example' # str | Quad identifier.

try:
    # Get Mosaic Quad URL
    api_response = api_instance.get_quad_download(mosaic_id, quad_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_quad_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **quad_id** | **str**| Quad identifier. | 

### Return type

[**Error**](Error.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quad_download_links**
> QuadListPage get_quad_download_links(mosaic_id, bbox, minimal=minimal, page=page, page_size=page_size)

List Mosaic Quads

List of quad download links for a mosaic.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
bbox = 'bbox_example' # str | Comma separated bounding box in degrees as lx,ly,ux,uy.
minimal = true # bool | If true, only return quad download links. (optional)
page = 'page_example' # str | Integer representing a specific page of results. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # List Mosaic Quads
    api_response = api_instance.get_quad_download_links(mosaic_id, bbox, minimal=minimal, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_quad_download_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **bbox** | **str**| Comma separated bounding box in degrees as lx,ly,ux,uy. | 
 **minimal** | **bool**| If true, only return quad download links. | [optional] 
 **page** | **str**| Integer representing a specific page of results. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**QuadListPage**](QuadListPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quad_items**
> QuadItems get_quad_items(mosaic_id, quad_id)

List Mosaic Quad Items

List items that contributed to a quad.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
quad_id = 'quad_id_example' # str | Quad identifier.

try:
    # List Mosaic Quad Items
    api_response = api_instance.get_quad_items(mosaic_id, quad_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_quad_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **quad_id** | **str**| Quad identifier. | 

### Return type

[**QuadItems**](QuadItems.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series**
> MosaicSeries get_series(series_id)

Get Mosaic Series

Get a mosaic series by id.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
series_id = 'series_id_example' # str | Series identifier.

try:
    # Get Mosaic Series
    api_response = api_instance.get_series(series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Series identifier. | 

### Return type

[**MosaicSeries**](MosaicSeries.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_series_mosaics**
> MosaicSeriesMosaicsListPage get_series_mosaics(series_id)

List Series' Mosaics

List mosaics in this series.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
series_id = 'series_id_example' # str | Series identifier.

try:
    # List Series' Mosaics
    api_response = api_instance.get_series_mosaics(series_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->get_series_mosaics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **series_id** | **str**| Series identifier. | 

### Return type

[**MosaicSeriesMosaicsListPage**](MosaicSeriesMosaicsListPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mosaics**
> MosaicListPage list_mosaics(page=page, page_size=page_size)

List Mosaics

List all accessible mosaics. For non authenticated users, this returns public mosaics.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
page = 56 # int | Integer representing a specific page of results. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # List Mosaics
    api_response = api_instance.list_mosaics(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->list_mosaics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Integer representing a specific page of results. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**MosaicListPage**](MosaicListPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_series**
> MosaicSeriesListPage list_series(page=page, page_size=page_size)

List Mosaic Series

List all mosaic series available to the authenticated user.

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
api_instance = swagger_client.BasemapsAndMosaicsApi(swagger_client.ApiClient(configuration))
page = 56 # int | Integer representing a specific page of results. (optional)
page_size = 56 # int | Number of results to return per page. (optional)

try:
    # List Mosaic Series
    api_response = api_instance.list_series(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasemapsAndMosaicsApi->list_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Integer representing a specific page of results. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 

### Return type

[**MosaicSeriesListPage**](MosaicSeriesListPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

