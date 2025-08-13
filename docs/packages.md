# Packages Endpoints

## Create package (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/packages`
- **Description**: Create a new package
- **Parameters**:
    - `name` (String, required): A descriptive name of the package
    - `active` (Boolean, required): Whether or not this package can still be added to accounts
    - `services` (Array, required): An array of service IDs that make up this package
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "active": true,
        "name": "My Awesome Package",
        "services": [
          1,
          5,
          7
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "That service ID is not a valid service"
            },
            "status_code": 422
        }
    }
    ```

## Delete package (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/packages/:id`
- **Description**: Delete a package. This will not remove the services from accounts, it will just prevent the package being used in the future. Since packages have an 'active' flag, it generally makes more sense to set them inactive rather than deleting unless you want to permanently remove it from the interface.
- **Parameters**:
    - `id` (Number, required): The ID of the package
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "Package deleted"
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "Package not found",
            "status_code": 404
        }
    }
    ```

## Get all packages (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/packages`
- **Description**: Get a list of the service packages in the system
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "active": true,
          "name": "My Awesome Package",
          "services": [
            1,
            5,
            7
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

## Get individual package (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/packages/:id`
- **Description**: Get an individual service package.
- **Parameters**:
    - `id` (Number, required): The ID of the package
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "active": true,
        "name": "My Awesome Package",
        "services": [
          1,
          5,
          7
        ]
      }
    }
    ```

## Update package (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/packages/:id`
- **Description**: Update a service package.
- **Parameters**:
    - `id` (Number, required): The ID of the package
    - `name` (String, optional): A descriptive name of the package
    - `active` (Boolean, optional): Whether or not this package can still be added to accounts
    - `services` (Array, optional): An array of service IDs that make up this package
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "active": true,
        "name": "My Awesome Package",
        "services": [
          1,
          5,
          7
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "That service ID is not a valid service"
            },
            "status_code": 422
        }
    }
    ```
```
