# Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | **object** | Links to related endpoints. | 
**permissions** | **list[str]** | An array of permissons the authenticated user has to the item. | 
**expires_at** | **datetime** | If present, RFC 3339 timestamp indicating when this asset will become inactive and will require reactivation. | [optional] 
**location** | **str** | If present, RFC 3986 URI that indicates a location that will yield image data. Consult the documentation of the asset type to understand how to use this URI. | [optional] 
**status** | **str** | Current status of the asset.  Inactive - Asset is not currently available for download, but may be after activation.  Activating - Asset is currently undergoing activation, and may be available for download shortly.  Active - Asset has been activated, and may currently be available for download if the authentication context permits. | 
**type** | **str** | Type identifier of the asset. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


