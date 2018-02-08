# Mosaic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**MosaicLinks**](MosaicLinks.md) |  | [optional] 
**bands** | **int** | The number of bands in this mosaic. | [optional] 
**bbox** | **list[float]** | The bounding box representing the extent of the mosaic. | 
**coordinate_system** | **str** | The coordinate system of this mosaic. | 
**datatype** | **str** | The type of data (byte, uint16, float32, etc). | [optional] 
**first_acquired** | **datetime** | The acquisition date of the oldest scene that contributed to this mosaic. | 
**grid** | [**GridContext**](GridContext.md) |  | [optional] 
**id** | **str** | Mosaic identifier. | [optional] 
**interval** | **str** | The interval of the mosaic. | [optional] 
**item_types** | **list[str]** | The item types in this mosaic. | [optional] 
**last_acquired** | **datetime** | The acquisition date of the newest scene that contributed to this mosaic. | 
**level** | **int** | The maximum zoom level in XYZ scheme. | [optional] 
**name** | **str** | A unique name for this mosaic. | 
**product_type** | **str** | The product type of this mosaics, currently supported is \&quot;timelapse\&quot;, \&quot;basemap\&quot;. | 
**quad_download** | **bool** | Your quad download permission for this mosaic. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


