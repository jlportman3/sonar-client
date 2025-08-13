# General Ledger Codes Endpoints

## Create a new general ledger code (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/general_ledger_codes`
- **Description**: Create a new general ledger code.
- **Parameters**:
    - `code` (String, required): A code for the general ledger code
    - `description` (String, required): A description for the general ledger code
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 4,
        "code": "12345",
        "description": "Internet Access"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "code": "The code must be unique."
         },
         "status_code": 422
       }
    }
    ```

## Delete a general ledger code (DELETE)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/general_ledger_codes/:id`
- **Description**: Delete a general ledger code
- **Parameters**:
    - `id` (Number, required): The ID of the general ledger code
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
            "message": "general ledger code does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all general ledger codes (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/general_ledger_codes`
- **Description**: Get all general ledger codes
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "code": "1000",
          "description": "test test"
        },
        {
          "id": 3,
          "code": "2010",
          "description": "test test test!"
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

## Get an individual general ledger code (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/general_ledger_codes/:id`
- **Description**: Get an individual general ledger code
- **Parameters**:
    - `id` (Number, required): The ID of the general ledger code
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 4,
        "code": "12345",
        "description": "Internet Access"
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

## Update general ledger code (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/general_ledger_codes/:id`
- **Description**: Update an existing general ledger code.
- **Parameters**:
    - `id` (Number, required): The general ledger code ID
    - `code` (String, optional): A code for the general ledger code
    - `description` (String, optional): A description for the general ledger code
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 4,
        "code": "123456",
        "description": "Internet Access"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "code": "The code has already been taken."
         },
         "status_code": 422
       }
    }
    ```
```
