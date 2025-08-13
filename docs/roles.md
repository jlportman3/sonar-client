# Roles Endpoints

## Get all roles (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/roles/`
- **Description**: Get a list of roles from within Sonar.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 2,
                "name": "Read Only"
            },
            {
                "id": 3,
                "name": "Network Support"
            },
            {
                "id": 1,
                "name": "Super Admin"
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

## Get individual role (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/roles/:id`
- **Description**: Get data on an Get individual role.
- **Parameters**:
    - `id` (Number, required): The id of the role
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Super Admin"
        }
    }
    ```
```
