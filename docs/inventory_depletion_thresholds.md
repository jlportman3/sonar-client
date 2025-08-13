# Inventory Depletion Thresholds Endpoints

## Create a new depletion threshold (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/depletion_thresholds`
- **Description**: Create a new depletion threshold.
- **Parameters**:
    - `enabled` (Boolean, required): Whether or not the threshold is enabled. Disabled thresholds will not send alerts
    - `threshold` (Number, required): The quantity of items below which the threshold is triggered
    - `type` (String, required): The type of threshold. An aggregate threshold is applied to all assignees, constrained by the boolean values described below. A single threshold is applied individually to each assignee defined within the assignee arrays defined below. (`"aggregate"`, `"single"`)
    - `include_inventory_locations` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all inventory locations
    - `include_vehicles` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all vehicles
    - `include_generic_inventory_assignees` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all generic inventory assignees
    - `notified_user_ids` (Array, optional): An array of user IDs that are notified when this threshold is violated
    - `included_inventory_location_ids` (Array, optional): If type is single, the array of IDs in here correspond to inventory locations that this threshold is applied to
    - `included_vehicle_ids` (Array, optional): If type is single, the array of IDs in here correspond to vehicles that this threshold is applied to
    - `included_generic_inventory_assignee_ids` (Array, optional): If type is single, the array of IDs in here correspond to generic inventory assignees that this threshold is applied to
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "enabled": true,
        "threshold": 100,
        "type": "aggregate",
        "include_inventory_locations": true,
        "include_vehicles": false,
        "include_generic_inventory_assignees": false,
        "notified_user_ids": [],
        "included_inventory_location_ids": [],
        "included_vehicle_ids": [],
        "included_generic_inventory_assignee_ids": []
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "notified_user_ids": "At least one user ID is not a valid user ID."
            },
            "status_code": 422
        }
    }
    ```

## Delete depletion threshold (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/depletion_thresholds/:depletion_threshold_id`
- **Description**: Delete a manufacturer
- **Parameters**:
    - `id` (Number, required): The ID of the depletion threshold
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
            "message": "No item with that ID could be found.",
            "status_code": 404
        }
    }
    ```

## Get all depletion thresholds (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/depletion_thresholds`
- **Description**: Get a list of depletion thresholds for this model ID. A depletion threshold allows you to define criteria by which a group of users are notified when the quantity of items for a specific model falls below a certain threshold. This can also be constrained by specific assignees - for example, you can be notified when there are less than 50 widgets in your 'Main Warehouse' and less than 100 widgets across all inventory locations.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `model_id` (Number, required): The internal ID of the inventory model
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "enabled": true,
          "threshold": 100,
          "type": "aggregate",
          "include_inventory_locations": true,
          "include_vehicles": false,
          "include_generic_inventory_assignees": false,
          "notified_user_ids": [],
          "included_inventory_location_ids": [],
          "included_vehicle_ids": [],
          "included_generic_inventory_assignee_ids": []
        },
        {
          "id": 2,
          "enabled": true,
          "threshold": 100,
          "type": "aggregate",
          "include_inventory_locations": true,
          "include_vehicles": false,
          "include_generic_inventory_assignees": false,
          "notified_user_ids": [],
          "included_inventory_location_ids": [],
          "included_vehicle_ids": [],
          "included_generic_inventory_assignee_ids": []
        },
        {
          "id": 3,
          "enabled": true,
          "threshold": 100,
          "type": "aggregate",
          "include_inventory_locations": true,
          "include_vehicles": false,
          "include_generic_inventory_assignees": false,
          "notified_user_ids": [
            1
          ],
          "included_inventory_location_ids": [],
          "included_vehicle_ids": [],
          "included_generic_inventory_assignee_ids": []
        },
        {
          "id": 4,
          "enabled": true,
          "threshold": 100,
          "type": "aggregate",
          "include_inventory_locations": true,
          "include_vehicles": false,
          "include_generic_inventory_assignees": false,
          "notified_user_ids": [
            1
          ],
          "included_inventory_location_ids": [
            1
          ],
          "included_vehicle_ids": [],
          "included_generic_inventory_assignee_ids": []
        },
        {
          "id": 5,
          "enabled": true,
          "threshold": 100,
          "type": "single",
          "include_inventory_locations": true,
          "include_vehicles": false,
          "include_generic_inventory_assignees": false,
          "notified_user_ids": [
            1
          ],
          "included_inventory_location_ids": [
            1
          ],
          "included_vehicle_ids": [],
          "included_generic_inventory_assignee_ids": []
        }
      ],
      "paginator": {
        "total_count": 5,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get an individual depletion threshold (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/depletion_thresholds/:depletion_threshold_id`
- **Description**: Get an individual depletion threshold from a single model.
- **Parameters**:
    - `model_id` (Number, required): The ID of an inventory model
    - `depletion_threshold_id` (Number, required): The ID of a depletion threshold
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "enabled": true,
        "threshold": 100,
        "type": "aggregate",
        "include_inventory_locations": true,
        "include_vehicles": false,
        "include_generic_inventory_assignees": false,
        "notified_user_ids": [],
        "included_inventory_location_ids": [],
        "included_vehicle_ids": [],
        "included_generic_inventory_assignee_ids": []
      }
    }
    ```

## Update depletion threshold (PATCH)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/depletion_thresholds/:depletion_threshold_id`
- **Description**: Update a depletion threshold.
- **Parameters**:
    - `model_id` (Number, required): The ID of the inventory model
    - `depletion_threshold_id` (Number, required): The ID of the depletion threshold
    - `enabled` (Boolean, required): Whether or not the threshold is enabled. Disabled thresholds will not send alerts
    - `threshold` (Number, required): The quantity of items below which the threshold is triggered
    - `type` (String, required): The type of threshold. An aggregate threshold is applied to all assignees, constrained by the boolean values described below. A single threshold is applied individually to each assignee defined within the assignee arrays defined below. (`"aggregate"`, `"single"`)
    - `include_inventory_locations` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all inventory locations
    - `include_vehicles` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all vehicles
    - `include_generic_inventory_assignees` (Boolean, required): If this is true and type is aggregate, then this threshold will be applied to all models of this ID across all generic inventory assignees
    - `notified_user_ids` (Array, optional): An array of user IDs that are notified when this threshold is violated
    - `included_inventory_location_ids` (Array, optional): If type is single, the array of IDs in here correspond to inventory locations that this threshold is applied to
    - `included_vehicle_ids` (Array, optional): If type is single, the array of IDs in here correspond to vehicles that this threshold is applied to
    - `included_generic_inventory_assignee_ids` (Array, optional): If type is single, the array of IDs in here correspond to generic inventory assignees that this threshold is applied to
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "enabled": true,
        "threshold": 50,
        "type": "single",
        "include_inventory_locations": true,
        "include_vehicles": false,
        "include_generic_inventory_assignees": false,
        "notified_user_ids": [
          1
        ],
        "included_inventory_location_ids": [
          1
        ],
        "included_vehicle_ids": [],
        "included_generic_inventory_assignee_ids": []
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "notified_user_ids": "One of the IDs in notified_user_ids is invalid."
            },
            "status_code": 422
        }
    }
    ```
```
