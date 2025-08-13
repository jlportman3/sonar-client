# Users Endpoints

## Create user (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/users`
- **Description**: Create a new user.
- **Parameters**:
    - `username` (String, required): A unique username for the user
    - `password` (String, required): A plain text password
    - `name` (String, required): The name of the user
    - `public_name` (String, required): The public name of the user
    - `role_id` (Number, required): The ID of the role for this user. These can be loaded from the roles endpoint.
    - `email_address` (String, required): The email address for the user
    - `mobile_number` (Number, optional): The mobile telephone number for the user
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 15,
            "username": "Hansolo",
            "name": "Han Solo",
            "public_name": "Han S.",
            "locale": "en",
            "role_id": 3,
            "email_address": "test@example.com",
            "mobile_number": null
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "username": "The username has already been taken.",
                "email_address": "The email address has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Delete user (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/users/:id`
- **Description**: Delete a user
- **Parameters**:
    - `id` (Number, required): The ID of the user
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "User deleted"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": "You cannot delete the last user with super admin privileges.",
            "status_code": 422
        }
    }
    ```

## Get all users (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/users/`
- **Description**: Get a list of users from within Sonar.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 15,
                "username": "Hansolo",
                "name": "Han Solo",
                "public_name": "Han S.",
                "locale": "en",
                "role_id": 3,
                "email_address": "test@example.com",
                "mobile_number": "4148675309"
            },
            {
                "id": 11,
                "username": "admin",
                "name": "John Doe the Third",
                "public_name": "Johnny D",
                "locale": "en",
                "role_id": 1,
                "email_address": "simon@sonar.software",
                "mobile_number": null
            }
        ]
    }
    ```

## Get individual user (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/users/:id`
- **Description**: Get data on an Get individual user.
- **Parameters**:
    - `id` (Number, required): The id of the user
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 15,
                "username": "Hansolo",
                "name": "Han Solo",
                "public_name": "Han S.",
                "locale": "en",
                "role_id": 3,
                "email_address": "test@example.com",
                "mobile_number": null
            }
       ]
    }
    ```

## Update user (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/users/:id`
- **Description**: Update a user
- **Parameters**:
    - `id` (Number, required): The ID of the user
    - `username` (String, optional): The username of the user
    - `password` (String, optional): A plain text password for the user
    - `name` (String, optional): The name of the user
    - `public_name` (String, optional): The public name of the user
    - `role_id` (Number, optional): The ID of the role for this user. These can be loaded from the roles endpoint.
    - `email_address` (String, optional): The email address for the user
    - `mobile_number` (Number, optional): The mobile telephone number for the user
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 35,
            "username": "JohnDoe",
            "name": "Jonathan Doe",
            "public_name": "John D",
            "role_id": 1,
            "email_address": "Johnathan_Doe@example.com",
            "mobile_number": null
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "username": "The username has already been taken.",
                "email_address": "The email address has already been taken."
            },
            "status_code": 422
        }
    }
    ```
```
