# Clip

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ClipLinks**](ClipLinks.md) |  | [optional] 
**aoi** | **object** | The geojson representation of the clipped region that has either been requested to be performed on the set of targets, or has been depending on the state of the operation. | 
**created_on** | **datetime** | The UTC date this Clip request was created. | [optional] 
**id** | **str** | A UUID to uniquely identify this Clip request. | [optional] 
**last_modified** | **datetime** | The UTC date this Clip request was last modified. | [optional] 
**state** | **str** | The current state of this clip request. | [optional] 
**targets** | [**list[Product]**](Product.md) | The target imagery from the Data API to apply the Clip operation on. | 
**taskgroup** | **object** | Optional debugging information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


