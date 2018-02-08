# ItemProperties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquired** | **datetime** | Timestamp that the item was captured. | [optional] 
**anomalous_pixels** | **float** | The percentage of pixels that may have errors. | [optional] 
**black_fill** | **float** | The percentage of the item containing black fill. | [optional] 
**cloud_cover** | **float** | Average percentage of cloud coverage throughout the item. | [optional] 
**columns** | **int** | The number of columns in the item. | [optional] 
**epsg_code** | **int** | The unique code that identifies the spatial reference system for the item. | [optional] 
**gsd** | **float** | Ground sample distance - the distance between pixel centers as measured on the ground. | [optional] 
**item_type** | **str** | The planet item type. | [optional] 
**origin_x** | **int** | ULX coordinate of the extent of the data. The coordinate references the top left corner of the top left pixel. | [optional] 
**origin_y** | **int** | ULY coordinate of the extent of the data. The coordinate references the top left corner of the top left pixel. | [optional] 
**pixel_resolution** | **int** | Pixel resolution of the item in meters. | [optional] 
**provider** | **str** | Name of the item provider. | [optional] 
**published** | **datetime** | Timestamp that the item was published to the Planet API. | [optional] 
**rows** | **int** | The number of rows in the item | [optional] 
**satellite_id** | **str** | Globally unique identifier of the satellite that acquired the item. | [optional] 
**sun_azimuth** | **float** | The angle of the sun, as seen by the observer, measured clockwise from the north. | [optional] 
**sun_elevation** | **float** | The angle of the sun above the horizon. | [optional] 
**updated** | **datetime** | Timestamp that the item record was last updated. | [optional] 
**usable_data** | **float** | The percentage of pixels that are usable. | [optional] 
**view_angle** | **float** | The satellite&#39;s across-track, off-nadir viewing angle. Positive numbers denote east, negitive numbers denote west. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


