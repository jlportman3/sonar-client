# Customer Portal Endpoints

## Look up an email address (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/customer_portal/email_lookup`
- **Description**: Look up an email address to see if it is valid. This is designed to be used for account creation, or resetting forgotten passwords. This will return the first contact found with the email address provided, that is a primary contact, and has no username associated with it. This endpoint is not throttled - you must throttle your look up function or this presents a security risk!
- **Parameters**:
    - `email_address` (String, required): The email address to look up
    - `check_if_available` (Boolean, optional): If true, this checks if the contact is primary, and it does not have a username. If this is false, then it will check if the account is primary, and it does have a username.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "email_address": "someone@example.com",
        "account_id": 1,
        "contact_id": 1,
        "username": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "The email address was not found.",
         "status_code": 422
       }
    }
    ```

## Validate credentials (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/customer_portal/auth`
- **Description**: Validate a contact's username and password for customer portal access. This will validate if the username and password matches, and the contact is a primary contact. You should only use this endpoint if you are building your own customer portal, and you want to hook into the username/password storage on a Sonar contact. This endpoint is not throttled - you must throttle your authentication function or this presents a security risk!
- **Parameters**:
    - `username` (String, required): The case-insensitive username to use for authentication
    - `password` (Number, required): The case-sensitive password to use for authentication
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "contact_name": "John Doe",
        "email_address": "someone@example.com",
        "account_id": 1,
        "contact_id": 1,
        "username": "testtest123"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "Invalid username or password.",
         "status_code": 422
       }
    }
    ```
```
