# swagger_client.ClipAndShipApi

All URIs are relative to *https://api.planet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clip_scene**](ClipAndShipApi.md#clip_scene) | **POST** /compute/ops/clips/v1 | List Clips
[**get_clip**](ClipAndShipApi.md#get_clip) | **GET** /compute/ops/clips/v1/{clip_id} | Get Clip
[**list_clips**](ClipAndShipApi.md#list_clips) | **GET** /compute/ops/clips/v1 | List Clips


# **clip_scene**
> Clip clip_scene(body)

List Clips

Clips a scene.

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
api_instance = swagger_client.ClipAndShipApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClipRequest() # ClipRequest | Clip details.

try:
    # List Clips
    api_response = api_instance.clip_scene(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClipAndShipApi->clip_scene: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClipRequest**](ClipRequest.md)| Clip details. | 

### Return type

[**Clip**](Clip.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clip**
> Clip get_clip(clip_id)

Get Clip

Get clip request details by Id.

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
api_instance = swagger_client.ClipAndShipApi(swagger_client.ApiClient(configuration))
clip_id = 'clip_id_example' # str | The Clip ID (a UUID).

try:
    # Get Clip
    api_response = api_instance.get_clip(clip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClipAndShipApi->get_clip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clip_id** | [**str**](.md)| The Clip ID (a UUID). | 

### Return type

[**Clip**](Clip.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_clips**
> ClipListPage list_clips(page_marker=page_marker)

List Clips

Returns all pending clip requests.

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
api_instance = swagger_client.ClipAndShipApi(swagger_client.ApiClient(configuration))
page_marker = 'page_marker_example' # str | Paging marker (optional)

try:
    # List Clips
    api_response = api_instance.list_clips(page_marker=page_marker)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClipAndShipApi->list_clips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_marker** | **str**| Paging marker | [optional] 

### Return type

[**ClipListPage**](ClipListPage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

