# Account Tax Overrides Endpoints

## Create a new account tax override (POST)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/account_tax_overrides`
- **Description**: Create a new account tax override. This requires account super user permission.
- **Parameters**:
    - `account_id` (Integer, required): The account ID
    - `tax_id` (Integer, required): The ID of the tax to override
    - `rate` (Number, required): The rate at which to override. If this is a flat tax, this is a monetary amount. If this is a percentage based tax, this will be the percentage to override to.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 5,
        "tax_id": 3,
        "account_id": 12,
        "rate": 15.43234
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "tax_id": "The tax ID is invalid."
         },
         "status_code": 422
       }
    }
    ```

## Delete an account tax override (DELETE)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/account_tax_overrides/:id`
- **Description**: Delete an account tax override. This requires account super user permission.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `id` (Integer, required): The ID of the account tax override
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
            "message": "account tax override does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all account tax overrides (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/account_tax_overrides`
- **Description**: Get all account tax overrides. This requires account super user permission.
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
    - `account_id` (Integer, required): The ID of the account
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 5,
          "tax_id": 3,
          "account_id": 12,
          "rate": 15.43234
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

## Get an individual account tax override (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/account_tax_overrides/:id`
- **Description**: Get an individual account tax override. This requires account super user permission.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `id` (Integer, required): The ID of the account tax override
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "tax_id": 3,
        "account_id": 12,
        "rate": 15.43234
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

## Update account tax override (PATCH)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/account_tax_overrides/:id`
- **Description**: Update an existing account tax override. This requires account super user permission.
- **Parameters**:
    - `id` (Integer, required): The ID of the tax override
    - `account_id` (Integer, required): The account ID
    - `tax_id` (Integer, required): The ID of the tax to override
    - `rate` (Number, required): The rate at which to override. If this is a flat tax, this is a monetary amount. If this is a percentage based tax, this will be the percentage to override to.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "tax_id": 3,
        "account_id": 12,
        "rate": 15.43234
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
