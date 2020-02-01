# AuditData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audited_on** | **str** | The date and time in ISO-8601 format when this activity log audit entry was created. | [optional] 
**event_type** | **str** | The event type that triggered the activity log audit entry. | [optional] 
**details** | **str** | Additional details about the activity log audit entry. | [optional] 
**new_value** | **str** | The new activity log audit entry value after update. Note: Sensitive values like passwords are not recorded in the activity log but the event entry is.  | [optional] 
**old_value** | **str** | The new activity log audit entry value before update. Note: Sensitive values like passwords are not recorded in the activity log but the event entry is.  | [optional] 
**parent_record_id** | **str** | The identity of the parent entity whose change triggered the activity log audit entry. | [optional] 
**parent_record_type** | **str** | The type of the parent entity whose change triggred the activity log audit entry. | [optional] 
**proxy_user** | **bool** | If true, this was created by a user who was proxied. | [optional] 
**system_user** | **bool** | If true, this was created by a system-automated process. | [optional] 
**user_display_name** | **str** | Display name of the user that created the activity log audit event, typically concatenated from the first and last names. | [optional] 
**user_id** | **str** | Identity of the user who created the activity log audit event. | [optional] 
**username** | **str** | Username of the user who created the activity log audit event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


