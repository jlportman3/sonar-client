# Scheduled Events Endpoints

## Create a new scheduled event (POST)
- **Version**: 1.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/scheduled_events`
- **Description**: Create a new scheduled event.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `event_type` (String, required): The type of scheduled event this is (`"add_service"`, `"remove_service"`, `"change_status"`, `"price_override_service"`, `"remove_price_override_from_service"`, `"add_package"`, `"remove_package"`)
    - `scheduled_datetime` (DateTime, required): The scheduled date and time for this event to occur, in UTC (YYYY-MM-DD HH:mm:ss format, in 24 hour time.)
    - `primary_value` (String, required): The primary value for the event. The primary value corresponds to the event. For add_service, it is the service ID to add to the account. For remove_service, it is the unique_service_relationship_id for the service currently on the account. For change_status, it is the ID of the account status to change the account to. For price_override_service, it is the unique_service_relationship_id for the service on the account that you want to price override. For remove_price_override_from_service, it is the unique_service_relationship_id for the service you want to remove the price override from.
    - `secondary_value` (String, optional): The secondary value for the event. This is currently only used for the event price_override_service, and it is the amount, as a decimal, that you want to price override the service to.
    - `proration_override` (Boolean, optional): Whether or not to override the default system proration for this event. Only valid if proration is valid for this event, and can only be set if you have account superuser permissions. If this is false, the system default price override selection will be used.
    - `prorate` (Boolean, optional): Whether or not to prorate this event, if proration is valid. This value is only checked if proration_override is true, and can only be set if you have account superuser permissions.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "event_type": "add_service",
        "scheduled_datetime": "2016-10-25 07:00:00",
        "primary_value": "1",
        "secondary_value": null,
        "proration_override": false,
        "prorate": false,
        "completed": false,
        "user_id": 1
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "scheduled_datetime": "The scheduled datetime cannot be in the past."
         },
         "status_code": 422
       }
    }
    ```

## Delete a scheduled event (DELETE)
- **Version**: 0.7.6
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/scheduled_events/:id`
- **Description**: Delete a scheduled event
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `id` (Integer, required): The ID of the scheduled event
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "success": true
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "scheduled event does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all scheduled events (GET)
- **Version**: 1.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/scheduled_events`
- **Description**: Get all scheduled events
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
    - `account_id` (Integer, required): The ID of the account to get events for
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "event_type": "add_service",
          "scheduled_datetime": "2016-10-25 07:00:00",
          "primary_value": "1",
          "secondary_value": null,
          "proration_override": false,
          "prorate": false,
          "completed": false,
          "user_id": 1
        }
      ],
      "paginator": {
        "total_count": 1,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get an individual scheduled event (GET)
- **Version**: 1.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/scheduled_events/:id`
- **Description**: Get an individual scheduled event
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account to get events for
    - `id` (Integer, required): The ID of the scheduled event
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "event_type": "add_service",
        "scheduled_datetime": "2016-10-25 07:00:00",
        "primary_value": "1",
        "secondary_value": null,
        "proration_override": false,
        "prorate": false,
        "completed": false,
        "user_id": 1
      }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
       "error": {
         "message": "No item with that ID found.",
         "status_code": 404
       }
    }
    ```

## Update scheduled event (PATCH)
- **Version**: 1.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/scheduled_events/:id`
- **Description**: Update an existing scheduled event.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `id` (Integer, required): The ID of the scheduled event
    - `event_type` (String, optional): The type of scheduled event this is (`"add_service"`, `"remove_service"`, `"change_status"`, `"price_override_service"`, `"remove_price_override_from_service"`, `"add_package"`, `"remove_package"`)
    - `scheduled_datetime` (DateTime, optional): The scheduled date and time for this event to occur, in UTC (YYYY-MM-DD HH:mm:ss format, in 24 hour time.)
    - `primary_value` (String, optional): The primary value for the event. The primary value corresponds to the event. For add_service, it is the service ID to add to the account. For remove_service, it is the unique_service_relationship_id for the service currently on the account. For change_status, it is the ID of the account status to change the account to. For price_override_service, it is the unique_service_relationship_id for the service on the account that you want to price override. For remove_price_override_from_service, it is the unique_service_relationship_id for the service you want to remove the price override from. For add_package, it is the package ID. For remove_package it is the unique_package_id from the account to service relationship.
    - `secondary_value` (String, optional): The secondary value for the event. This is currently only used for the event price_override_service, and it is the amount, as a decimal, that you want to price override the service to.
    - `proration_override` (Boolean, optional): Whether or not to override the default system proration for this event. Only valid if proration is valid for this event, and can only be set if you have account superuser permissions. If this is false, the system default price override selection will be used.
    - `prorate` (Boolean, optional): Whether or not to prorate this event, if proration is valid. This value is only checked if proration_override is true, and can only be set if you have account superuser permissions.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2
      }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
       "error": {
         "message": "No item with that ID found.",
         "status_code": 404
       }
    }
    ```
```
