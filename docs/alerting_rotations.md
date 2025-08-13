# Alerting Rotations Endpoints

## Create a new alerting rotation day/time (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id/alerting_rotation_days`
- **Description**: Create a new alerting rotation day/time.
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
    - `day` (Integer, required): An integer representing the day of the week, where 0 is Sunday and 6 is Saturday (`0`, `1`, `2`, `3`, `4`, `5`, `6`)
    - `start_timestamp` (Time, required): A timestamp representing the start time of the rotation for this day, in the Sonar timezone. The format should be HH:mm where HH is a 24 hour hour, and mm is a two digit minute.
    - `end_timestamp` (Time, required): A timestamp representing the end time of the rotation for this day, in the Sonar timezone. The format should be HH:mm where HH is a 24 hour hour, and mm is a two digit minute.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "day": 5,
        "start_timestamp": "08:35",
        "end_timestamp": "17:00"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "data": {
         "id": 1,
         "day": 2,
         "start_timestamp": "8:0",
         "end_timestamp": "17:0"
       }
    }
    ```

## Create a new alerting rotation (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations`
- **Description**: Create a new alerting rotation.
- **Parameters**:
    - `enabled` (Boolean, required): Whether or not the rotation is enabled
    - `name` (String, required): A name for the alerting rotation
    - `start` (Date, required): A date when the rotation should begin
    - `repetitions` (Integer, required): The number of times the rotation should repeat
    - `weeks` (Integer, required): How frequently the rotation should repeat, in weeks. 1 means every week, 2 means every other week, 3 means on one week, off two weeks, on one week, etc.
    - `infinite_repetitions` (Boolean, required): Should this rotation repeat forever? If this is true, repetitions is ignored.
    - `warning_time_in_minutes_before_alerting` (Integer, required): How long devices that this alerting rotation covers can be in a warning state before an alert is sent
    - `down_time_in_minutes_before_alerting` (Integer, required): How long devices that this alerting rotation covers can be in a down state before an alert is sent
    - `user_ids` (Array, required): An array of users that are in this rotation
    - `all_accounts` (Boolean, required): If this is true, then the account_group_ids and account_type_ids values are ignored, and this rotation applies to all accounts
    - `all_network_sites` (Boolean, required): If this is true, then the network_site_ids value is ignored, and this rotation applies to all network sites
    - `all_inventory_models` (Boolean, required): If this is true, then the inventory_model_ids value is ignored, and this rotation applies to all inventory models
    - `network_site_ids` (Array, optional): An array of network site IDs that this rotation covers. You can use this to limit the network sites that will send alerts to the users in this rotation.
    - `inventory_model_ids` (Array, optional): An array of inventory model IDs that will push alerts into this rotation. You can use this to limit the types of devices that will send alerts to users in this rotation.
    - `account_group_ids` (Array, optional): An array of account groups that will push alerts into this rotation. You can use this to limit the accounts that will send alerts to users in this rotation.
    - `account_type_ids` (Array, optional): An array of account types that will push alerts into this rotation. You can use this to limit the accounts that will send alerts to users in this rotation.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "enabled": true,
        "name": "Rotation 1 Updated",
        "start": "2016-12-15",
        "repetitions": 5,
        "infinite_repetitions": true,
        "weeks": 1,
        "warning_time_in_minutes_before_alerting": 10,
        "down_time_in_minutes_before_alerting": 5,
        "user_ids": [
          1
        ],
        "all_accounts": true,
        "all_network_sites": true,
        "all_inventory_models": true,
        "network_site_ids": [],
        "inventory_model_ids": [
          1,
          2
        ],
        "account_group_ids": [],
        "account_type_ids": [
          2,
          1
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "start": "start must be a date in YYYY-MM-DD format."
         },
         "status_code": 422
       }
    }
    ```

## Delete a alerting rotation day/time (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id/alerting_rotation_days/:alerting_rotation_day_id`
- **Description**: Delete a alerting rotation day/time
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
    - `alerting_rotation_day_id` (Integer, required): The ID of the alerting rotation day/time
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
            "message": "alerting rotation day/time does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a alerting rotation (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id`
- **Description**: Delete a alerting rotation
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
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
            "message": "alerting rotation does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all alerting rotations (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations`
- **Description**: Get all alerting rotations
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "enabled": true,
          "name": "Rotation 1 Updated",
          "start": "2016-12-15",
          "repetitions": 5,
          "infinite_repetitions": true,
          "weeks": 1,
          "warning_time_in_minutes_before_alerting": 10,
          "down_time_in_minutes_before_alerting": 5,
          "user_ids": [
            1
          ],
          "all_accounts": true,
          "all_network_sites": true,
          "all_inventory_models": true,
          "network_site_ids": [],
          "inventory_model_ids": [
            1,
            2
          ],
          "account_group_ids": [],
          "account_type_ids": [
            2,
            1
          ]
        },
        {
          "id": 3,
          "enabled": true,
          "name": "Another Rotation",
          "start": "2016-12-15",
          "repetitions": 5,
          "infinite_repetitions": true,
          "weeks": 1,
          "warning_time_in_minutes_before_alerting": 10,
          "down_time_in_minutes_before_alerting": 5,
          "user_ids": [
            1
          ],
          "all_accounts": true,
          "all_network_sites": true,
          "all_inventory_models": true,
          "network_site_ids": [],
          "inventory_model_ids": [
            1,
            2
          ],
          "account_group_ids": [],
          "account_type_ids": [
            2,
            1
          ]
        }
      ],
      "paginator": {
        "total_count": 2,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get an individual alerting rotation day/time (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id/alerting_rotation_days/:alerting_rotation_day_id`
- **Description**: Get an individual alerting rotation day/time
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
    - `alerting_rotation_day_id` (Integer, required): The ID of the alerting rotation day
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "day": 2,
        "start_timestamp": "08:00",
        "end_timestamp": "17:00"
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

## Get an individual alerting rotation (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id`
- **Description**: Get an individual alerting rotation
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "enabled": true,
        "name": "Rotation 1 Updated",
        "start": "2016-12-15",
        "repetitions": 5,
        "infinite_repetitions": true,
        "weeks": 1,
        "warning_time_in_minutes_before_alerting": 10,
        "down_time_in_minutes_before_alerting": 5,
        "user_ids": [
          1
        ],
        "all_accounts": true,
        "all_network_sites": true,
        "all_inventory_models": true,
        "network_site_ids": [],
        "inventory_model_ids": [
          1,
          2
        ],
        "account_group_ids": [],
        "account_type_ids": [
          2,
          1
        ]
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

## Update alerting rotation day/time (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id/alerting_rotation_days/:alerting_rotation_day_id`
- **Description**: Update an existing alerting rotation day/time.
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
    - `alerting_rotation_day_id` (Integer, required): The ID of the alerting rotation day
    - `day` (Integer, required): An integer representing the day of the week, where 0 is Sunday and 6 is Saturday (`0`, `1`, `2`, `3`, `4`, `5`, `6`)
    - `start_timestamp` (Time, required): A timestamp representing the start time of the rotation for this day, in the Sonar timezone. The format should be HH:mm where HH is a 24 hour hour, and mm is a two digit minute.
    - `end_timestamp` (Time, required): A timestamp representing the end time of the rotation for this day, in the Sonar timezone. The format should be HH:mm where HH is a 24 hour hour, and mm is a two digit minute.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "day": 5,
        "start_timestamp": "08:35",
        "end_timestamp": "17:00"
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

## Update alerting rotation (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/alerting_rotations/:id`
- **Description**: Update an existing alerting rotation.
- **Parameters**:
    - `id` (Integer, required): The ID of the alerting rotation
    - `enabled` (Boolean, optional): Whether or not the rotation is enabled
    - `name` (String, optional): A name for the alerting rotation
    - `start` (Date, optional): A date when the rotation should begin
    - `repetitions` (Integer, optional): The number of times the rotation should repeat
    - `weeks` (Integer, optional): How frequently the rotation should repeat, in weeks. 1 means every week, 2 means every other week, 3 means on one week, off two weeks, on one week, etc.
    - `infinite_repetitions` (Boolean, optional): Should this rotation repeat forever? If this is true, repetitions is ignored.
    - `warning_time_in_minutes_before_alerting` (Integer, optional): How long devices that this alerting rotation covers can be in a warning state before an alert is sent
    - `down_time_in_minutes_before_alerting` (Integer, optional): How long devices that this alerting rotation covers can be in a down state before an alert is sent
    - `user_ids` (Array, optional): An array of users that are in this rotation
    - `all_accounts` (Boolean, optional): If this is true, then the account_group_ids and account_type_ids values are ignored, and this rotation applies to all accounts
    - `all_network_sites` (Boolean, optional): If this is true, then the network_site_ids value is ignored, and this rotation applies to all network sites
    - `all_inventory_models` (Boolean, optional): If this is true, then the inventory_model_ids value is ignored, and this rotation applies to all inventory models
    - `network_site_ids` (Array, optional): An array of network site IDs that this rotation covers. You can use this to limit the network sites that will send alerts to the users in this rotation.
    - `inventory_model_ids` (Array, optional): An array of inventory model IDs that will push alerts into this rotation. You can use this to limit the types of devices that will send alerts to users in this rotation.
    - `account_group_ids` (Array, optional): An array of account groups that will push alerts into this rotation. You can use this to limit the accounts that will send alerts to users in this rotation.
    - `account_type_ids` (Array, optional): An array of account types that will push alerts into this rotation. You can use this to limit the accounts that will send alerts to users in this rotation.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "enabled": true,
        "name": "Rotation 1 Updated",
        "start": "2016-12-15",
        "repetitions": 5,
        "infinite_repetitions": true,
        "weeks": 1,
        "warning_time_in_minutes_before_alerting": 10,
        "down_time_in_minutes_before_alerting": 5,
        "user_ids": [
          1
        ],
        "all_accounts": true,
        "all_network_sites": true,
        "all_inventory_models": true,
        "network_site_ids": [],
        "inventory_model_ids": [
          1,
          2
        ],
        "account_group_ids": [],
        "account_type_ids": [
          2,
          1
        ]
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

</final_file_content>

IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your SEARCH/REPLACE operations on this final version to ensure accuracy.<environment_details>
# VSCode Visible Files
docs/alerting_rotations.md

# VSCode Open Tabs
memory-bank/activeContext.md
memory-bank/progress.md
docs/account_billing.md
docs/account_call_logs.md
docs/account_call_records.md
docs/account_contacts.md
docs/account_dids.md
docs/account_data_usage.md
docs/account_ip_addresses.md
docs/account_inventory.md
docs/account_invoices.md
docs/account_payment_methods.md
docs/account_services.md
docs/account_tax_overrides.md
docs/account_transactions.md
docs/accounts.md
docs/address_lists.md
docs/alerting_rotations.md

# Current Time
6/28/2025, 12:35:36 PM (UTC, UTC+0:00)

# Context Window Usage
706,000 / 1,048.576K tokens used (67%)

# Current Mode
ACT MODE
```
