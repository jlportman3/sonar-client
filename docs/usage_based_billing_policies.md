# Usage Based Billing Policies Endpoints

## Create a new usage based billing free period (POST)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:usage_based_billing_policy_id/usage_based_billing_free_periods`
- **Description**: Create a new usage based billing free period.
- **Parameters**:
    - `usage_based_billing_policy_id` (Number, required): The ID of the usage based billing policy.
    - `day` (Number, required): The day of the week of the free period, where 0 is Sunday and 6 is Saturday
    - `start` (Time, required): The start of the free period in HH:MM:SS
    - `end` (Time, required): The end of the free period in HH:MM:SS
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "day": 0,
        "start": "00:00:00",
        "end": "02:30:00"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "This free period overlaps another defined free period from 09:00:00 to 21:32:00.",
         "status_code": 422
       }
    }
    ```

## Create a new usage based billing policy (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies`
- **Description**: Create a new usage based billing policy.
- **Parameters**:
    - `description` (String, required): A description of the policy.
    - `cap_in_gigabytes` (Number, required): The cap on the policy, in gigabytes.
    - `rollover_enabled` (Boolean, required): If rollover is enabled on this policy.
    - `rollover_expiration_enabled` (Boolean, required): If rollover data expires
    - `rollover_expires_after_months` (Number, optional): If rollover_expiration_enabled is true, then any unused data rolled over expires after this many months. This is required if rollover_expiration_enabled is true!
    - `assess_charges_at_end_of_billing_period` (Boolean, required): If this is true, then any data usage over cap_in_gigabytes will be charged at the rates defined in the overage service linked as service_id
    - `allow_user_to_purchase_capacity` (Boolean, required): If this is true, then a user can purchase additional data mid-billing period (referred to as a 'top off' inside Sonar) at the rates defined in the overage service linked as service_id
    - `service_id` (Number, optional): If either assess_charges_at_end_of_billing_period or allow_user_to_purchase_capacity are true, then this is the ID of the overage service used to determine the rates for those functions. This is required if either of the aforementioned properties are true!
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 9,
        "description": "Test 123",
        "cap_in_gigabytes": 150,
        "rollover_enabled": false,
        "rollover_expiration_enabled": false,
        "rollover_expires_after_months": 0,
        "assess_charges_at_end_of_billing_period": false,
        "allow_user_to_purchase_capacity": false,
        "service_id": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "description": "The description must be unique."
         },
         "status_code": 422
       }
    }
    ```

## Delete a usage based billing free period (DELETE)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:usage_based_billing_policy_id/usage_based_billing_free_periods/:id`
- **Description**: Delete a usage based billing free period
- **Parameters**:
    - `usage_based_billing_policy_id` (Number, required): The ID of the usage based billing policy
    - `id` (Number, required): The ID of the usage based billing free period
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
            "message": "Usage based billing free period does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a usage based billing policy (DELETE)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:id`
- **Description**: Delete a usage based billing policy. If this is currently on any services, it will be removed from the services, and all users with those services will no longer have a usage cap.
- **Parameters**:
    - `id` (Number, required): The ID of the usage based billing policy
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
            "message": "Usage based billing policy does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all usage based billing free periods (GET)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:usage_based_billing_policy_id/usage_based_billing_free_periods`
- **Description**: Get all usage based billing free periods for a specific policy.
- **Parameters**:
    - `usage_based_billing_policy_id` (Number, required): The ID of the usage based billing policy the free period is attached to
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "day": 0,
          "start": "00:00:00",
          "end": "02:30:00"
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

## Get all usage based billing policies (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies`
- **Description**: Get all usage based billing policies
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "description": "No Rollover",
          "cap_in_gigabytes": 5,
          "rollover_enabled": false,
          "rollover_expiration_enabled": false,
          "rollover_expires_after_months": 0,
          "assess_charges_at_end_of_billing_period": false,
          "allow_user_to_purchase_capacity": false,
          "service_id": null
        },
        {
          "id": 3,
          "description": "Rollover No Expiration",
          "cap_in_gigabytes": 1,
          "rollover_enabled": true,
          "rollover_expiration_enabled": false,
          "rollover_expires_after_months": 0,
          "assess_charges_at_end_of_billing_period": false,
          "allow_user_to_purchase_capacity": false,
          "service_id": null
        },
        {
          "id": 2,
          "description": "Rollover 3 month expiration",
          "cap_in_gigabytes": 1,
          "rollover_enabled": true,
          "rollover_expiration_enabled": true,
          "rollover_expires_after_months": 3,
          "assess_charges_at_end_of_billing_period": false,
          "allow_user_to_purchase_capacity": true,
          "service_id": 15
        }
      ],
      "paginator": {
        "total_count": 3,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get an individual usage based billing free period (GET)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:usage_based_billing_policy_id/usage_based_billing_free_periods/:id`
- **Description**: Get an individual usage based billing free period
- **Parameters**:
    - `usage_based_billing_policy_id` (Number, required): The ID of the usage based billing policy the free period is attached to
    - `id` (Number, required): The ID of the usage based billing free period
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "day": 0,
        "start": "00:00:00",
        "end": "02:30:00"
      }
    }
    ```

## Get an individual usage based billing policy (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:id`
- **Description**: Get an individual usage based billing policy
- **Parameters**:
    - `id` (Number, required): The ID of the usage based billing policy
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "description": "Rollover 3 month expiration",
        "cap_in_gigabytes": 1,
        "rollover_enabled": true,
        "rollover_expiration_enabled": true,
        "rollover_expires_after_months": 3,
        "assess_charges_at_end_of_billing_period": false,
        "allow_user_to_purchase_capacity": true,
        "service_id": 15
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

## Update usage based billing free period (PATCH)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:usage_based_billing_policy_id/usage_based_billing_free_periods/:id`
- **Description**: Update an existing usage based billing free period.
- **Parameters**:
    - `usage_based_billing_policy_id` (Number, required): The ID of the usage based billing policy.
    - `id` (Number, required): The ID of the usage based billing free period
    - `day` (Number, optional): The day of the week of the free period, where 0 is Sunday and 6 is Saturday
    - `start` (Time, optional): The start of the free period in HH:MM:SS
    - `end` (Time, optional): The end of the free period in HH:MM:SS
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "day": 0,
        "start": "00:00:00",
        "end": "02:30:00"
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

## Update usage based billing policy (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/usage_based_billing_policies/:id`
- **Description**: Update an existing usage based billing policy.
- **Parameters**:
    - `id` (Number, required): The usage based billing policy ID
    - `description` (String, optional): A description of the policy.
    - `cap_in_gigabytes` (Number, optional): The cap on the policy, in gigabytes.
    - `rollover_enabled` (Boolean, optional): If rollover is enabled on this policy.
    - `rollover_expiration_enabled` (Boolean, optional): If rollover data expires
    - `rollover_expires_after_months` (Number, optional): If rollover_expiration_enabled is true, then any unused data rolled over expires after this many months. This is required if rollover_expiration_enabled is true!
    - `assess_charges_at_end_of_billing_period` (Boolean, optional): If this is true, then any data usage over cap_in_gigabytes will be charged at the rates defined in the overage service linked as service_id
    - `allow_user_to_purchase_capacity` (Boolean, optional): If this is true, then a user can purchase additional data mid-billing period (referred to as a 'top off' inside Sonar) at the rates defined in the overage service linked as service_id
    - `service_id` (Number, optional): If either assess_charges_at_end_of_billing_period or allow_user_to_purchase_capacity are true, then this is the ID of the overage service used to determine the rates for those functions. This is required if either of the aforementioned properties are true!
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 9,
        "description": "Test 123",
        "cap_in_gigabytes": 150,
        "rollover_enabled": false,
        "rollover_expiration_enabled": false,
        "rollover_expires_after_months": 0,
        "assess_charges_at_end_of_billing_period": false,
        "allow_user_to_purchase_capacity": false,
        "service_id": null
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
