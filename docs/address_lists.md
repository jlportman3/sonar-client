# Address Lists Endpoints

## Create a new address list (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/provisioning/address_lists`
- **Description**: Create a new address list. If there are enabled, available inline devices in Sonar, this address list will be immediately created on them.
- **Parameters**:
    - `name` (String, required): The name of the address list
    - `delinquent` (Number, optional): If this is 1, the list is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked. (`1`, `2`, `3`)
    - `active` (Number, optional): If this is 1, the list is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked. (`1`, `2`, `3`)
    - `account_groups` (Array, optional): An array of account group IDs that are a relation to this address list.
    - `account_types` (Array, optional): An array of account type IDs that are a relation to this address list.
    - `services` (Array, optional): An array of data service IDs that are a relation to this address list.
    - `account_statuses` (Array, optional): An array of account status IDs that are a relation to this address list.
    - `usage_based_billing_policies` (Array, optional): An array of usage based billing policy IDs that are checked for caps being exceeded
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "test",
        "delinquent": 3,
        "active": 3,
        "account_groups": [],
        "account_types": [],
        "services": [
          14,
          12
        ],
        "account_statuses": [],
        "usage_based_billing_policies": [
          6,
          5
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The address list name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Delete address list (DELETE)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/provisioning/address_lists/:id`
- **Description**: Delete an address list. This will immediately remove the address list from all enabled inline devices in a good status.
- **Parameters**:
    - `id` (Number, required): The ID of the address list.
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
            "message": {
                "message": "Address list does not exist."
            },
            "status_code": 404
        }
    }
    ```

## Get all address lists (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/provisioning/address_lists`
- **Description**: Get a list of address lists.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "test",
          "delinquent": 3,
          "active": 3,
          "account_groups": [],
          "account_types": [],
          "services": [
            14,
            12
          ],
          "account_statuses": [],
          "usage_based_billing_policies": [
            6,
            5
          ]
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

## Get individual address list (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/provisioning/address_lists/:id`
- **Description**: Get an individual address list.
- **Parameters**:
    - `id` (Number, required): The ID of the address list
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "test",
        "delinquent": 3,
        "active": 3,
        "account_groups": [],
        "account_types": [],
        "services": [
          14,
          12
        ],
        "account_statuses": [],
        "usage_based_billing_policies": [
          6,
          5
        ]
      }
    }
    ```

## Update address list (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/provisioning/address_lists/:id`
- **Description**: Update an address list
- **Parameters**:
    - `id` (Number, required): The ID of the address list
    - `name` (String, optional): The name of the address list
    - `delinquent` (Number, optional): If this is 1, the list is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked. (`1`, `2`, `3`)
    - `active` (Number, optional): If this is 1, the list is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked. (`1`, `2`, `3`)
    - `account_groups` (Array, optional): An array of account group IDs that are a relation to this address list.
    - `account_types` (Array, optional): An array of account type IDs that are a relation to this address list.
    - `services` (Array, optional): An array of data service IDs that are a relation to this address list.
    - `account_statuses` (Array, optional): An array of account status IDs that are a relation to this address list.
    - `usage_based_billing_policies` (Array, optional): An array of usage based billing policy IDs that are checked for caps being exceeded
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 23,
        "name": "Active",
        "delinquent": 3,
        "active": 1,
        "account_groups": [],
        "account_types": [],
        "services": [],
        "account_statuses": [],
        "usage_based_billing_policies": []
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```
```
