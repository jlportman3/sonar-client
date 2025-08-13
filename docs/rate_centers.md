# Rate Centers Endpoints

## Create a new rate center (POST)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/rate_centers`
- **Description**: Create a new rate center. A rate center is used to store DIDs for voice services.
- **Parameters**:
    - `name` (String, required): A name for the rate center
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "My rate center"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "name": "The name must be unique."
         },
         "status_code": 422
       }
    }
    ```

## Delete a rate center (DELETE)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/rate_centers/:id`
- **Description**: Delete a rate center
- **Parameters**:
    - `id` (Number, required): The ID of the rate center
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
            "message": "Rate center does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all rate centers (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/rate_centers`
- **Description**: Get all rate centers
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "name": "My rate center"
        },
        {
          "id": 1,
          "name": "Another rate center"
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

## Get an individual rate center (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/rate_centers/:id`
- **Description**: Get an individual rate center
- **Parameters**:
    - `id` (Number, required): The ID of the rate center
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "ABC123"
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

## Update rate center (PATCH)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/rate_centers/:id`
- **Description**: Update an existing rate center.
- **Parameters**:
    - `id` (Number, required): The rate center ID
    - `name` (String, optional): The name of the rate center
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "My updated name"
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
