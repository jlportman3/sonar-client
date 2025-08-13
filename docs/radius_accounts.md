# RADIUS Accounts Endpoints

## Create a new RADIUS account (POST)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/radius_accounts`
- **Description**: Create a new RADIUS account. For this to work, there must be an enabled RADIUS server defined in Sonar.
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `username` (String, required): The username for the account
    - `password` (String, required): The password for the account
    - `create_on_server` (Boolean, optional): Whether or not this account should be created on the RADIUS server. This should generally always be set to true unless you are performing an import and you just need to get Sonar to match what currently exists on the server.
    - `service_id` (Number, optional): If the account has multiple data services, you can decide which data service to associate this RADIUS account with. This will affect the groups it is in, if you have groups that are assigned by service. If the account only has one service, you can omit this and it will be automatically assigned.
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
           "id": 2,
           "username": "s_westlake",
           "password": "goldeneagle",
           "service_id": 2
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "username": "The username has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Delete RADIUS account (DELETE)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/radius_accounts/:radius_account_id`
- **Description**: Delete a RADIUS account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `radius_account_id` (Number, required): The ID of the RADIUS account
    - `delete_from_server` (Boolean, optional): Whether or not to delete the account from the remote RADIUS server, or just from Sonar. You should only set this to false if you don't want to manipulate the remote RADIUS server for some reason.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "success": true
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "message": "RADIUS account does not exist."
            },
            "status_code": 422
        }
    }
    ```

## Get all RADIUS accounts (GET)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/radius_accounts`
- **Description**: Get a list of RADIUS accounts.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `id` (Number, required): The ID of the account
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
           {
               "id": 1,
               "username": "p_luckey",
               "password": "oculus"
           },
           {
               "id": 2,
               "username": "s_westlake",
               "password": "eaglerare"
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

## Get individual RADIUS account (GET)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/radius_accounts/:radius_account_id`
- **Description**: Get an individual RADIUS account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `radius_account_id` (Number, required): The ID of the RADIUS account
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 2,
           "username": "s_westlake",
           "password": "goldeneagle",
           "service_id": 2
       }
    }
    ```

## Update RADIUS account (PATCH)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/radius_accounts/:radius_account_id`
- **Description**: Update a RADIUS account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `radius_account_id` (Number, required): The ID of the RADIUS account
    - `username` (String, optional): The username for RADIUS account
    - `password` (String, optional): The password for the RADIUS account
    - `update_on_server` (Boolean, optional): Whether or not this account should be updated on the remote RADIUS server, or only in Sonar. The only time you should set this to false is if you are trying to reconcile Sonar with your RADIUS server
    - `service_id` (Number, optional): If the account has multiple data services, you can decide which data service to associate this RADIUS account with. This will affect the groups it is in, if you have groups that are assigned by service. If the account only has one service, you can omit this and it will be automatically assigned.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 2,
           "username": "s_westlake",
           "password": "regulareagle",
           "service_id": 2
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "username": "The username has already been taken."
            },
            "status_code": 422
        }
    }
    ```
```
