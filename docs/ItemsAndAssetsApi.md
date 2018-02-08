# swagger_client.ItemsAndAssetsApi

All URIs are relative to *https://api.planet.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_type**](ItemsAndAssetsApi.md#get_asset_type) | **GET** /data/v1/asset-types/{asset_type_id} | Get Asset Type
[**get_item**](ItemsAndAssetsApi.md#get_item) | **GET** /data/v1/item-types/{item_type_id}/items/{item_id} | Get Item
[**get_item_type**](ItemsAndAssetsApi.md#get_item_type) | **GET** /data/v1/item-types/{item_type_id} | Get Item Type
[**list_asset_types**](ItemsAndAssetsApi.md#list_asset_types) | **GET** /data/v1/asset-types | List Asset Types
[**list_item_assets**](ItemsAndAssetsApi.md#list_item_assets) | **GET** /data/v1/item-types/{item_type_id}/items/{item_id}/assets | List Item Assets
[**list_item_types**](ItemsAndAssetsApi.md#list_item_types) | **GET** /data/v1/item-types | List Item Types


# **get_asset_type**
> AssetType get_asset_type(asset_type_id)

Get Asset Type

Get an asset type by id. An `asset` describes a product that can be derived from an item's source data, and can be used for various analytic, visual or other purposes. These are referred to as `assets_types`.  [Learn more about asset types](/docs/items-assets#section-assets) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))
asset_type_id = 'asset_type_id_example' # str | Asset type identifier.

try:
    # Get Asset Type
    api_response = api_instance.get_asset_type(asset_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->get_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | **str**| Asset type identifier. | 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item**
> Item get_item(item_type_id, item_id)

Get Item

Get an item by id and item type.  In the Planet API, an `item` is an entry in our catalog, and generally represents a single logical observation (or scene) captured by a satellite. Each `item` is defined by an `item_type`, which represents the class of spacecraft and/or processing level of the item. Assets (or products, such as visual or analytic) can be derived from the item's source data.  [Learn more about items](/docs/items-assets#section-items) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))
item_type_id = 'item_type_id_example' # str | Item type identifier.
item_id = 'item_id_example' # str | Item identifier.

try:
    # Get Item
    api_response = api_instance.get_item(item_type_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->get_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_type_id** | **str**| Item type identifier. | 
 **item_id** | **str**| Item identifier. | 

### Return type

[**Item**](Item.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_type**
> ItemType get_item_type(item_type_id)

Get Item Type

Get an item type by id.  An `item_type` represents the class of spacecraft and/or processing level of an item. All items have an associated `item_type`. Each `item_type` has a specific list of `assets_types` that can be derived from the item's source data.  [Learn more about item types](/docs/items-assets#section-item-types) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))
item_type_id = 'item_type_id_example' # str | Item type identifier.

try:
    # Get Item Type
    api_response = api_instance.get_item_type(item_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->get_item_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_type_id** | **str**| Item type identifier. | 

### Return type

[**ItemType**](ItemType.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_types**
> AssetTypePage list_asset_types()

List Asset Types

List all asset types available to the authenticated user.  An `asset` describes a product that can be derived from an item's source data, and can be used for various analytic, visual or other purposes. These are referred to as `assets_types`.    [Learn more about asset types](/docs/items-assets#section-assets) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))

try:
    # List Asset Types
    api_response = api_instance.list_asset_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->list_asset_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AssetTypePage**](AssetTypePage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_assets**
> Asset list_item_assets(item_type_id, item_id)

List Item Assets

List all assets available for an item. An `asset` describes a product that can be derived from an item's source data, and can be used for various analytic, visual or other purposes. These are referred to as `assets_types`.  [Learn more about asset types](/docs/items-assets#section-assets) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))
item_type_id = 'item_type_id_example' # str | Item type identifier.
item_id = 'item_id_example' # str | Item identifier.

try:
    # List Item Assets
    api_response = api_instance.list_item_assets(item_type_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->list_item_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_type_id** | **str**| Item type identifier. | 
 **item_id** | **str**| Item identifier. | 

### Return type

[**Asset**](Asset.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_item_types**
> ItemTypePage list_item_types()

List Item Types

List all item types available to the authenticated user.  An `item_type` represents the class of spacecraft and/or processing level of an item. All items have an associated `item_type`. Each `item_type` has a specific list of `assets_types` that can be derived from the item's source data.  [Learn more about item types](/docs/items-assets#section-item-types) 

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
api_instance = swagger_client.ItemsAndAssetsApi(swagger_client.ApiClient(configuration))

try:
    # List Item Types
    api_response = api_instance.list_item_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsAndAssetsApi->list_item_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ItemTypePage**](ItemTypePage.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

