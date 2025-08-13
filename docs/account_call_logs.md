# Account Call Logs Endpoints

## Create a new call log (POST)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/call_logs`
- **Description**: Create a new call log.
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `time_in_seconds` (Number, required): How long the call lasted, in seconds
    - `subject` (String, required): The subject of the call
    - `body` (String, required): A longer description of the call
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "account_id": 2,
        "time_in_seconds": 12,
        "subject": "Support issue",
        "body": "Blah blah blah blah blah",
        "user_id": 1,
        "created_at": "2016-05-20 14:14:33"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "time_in_seconds": "The time_in_seconds must be an integer."
         },
         "status_code": 422
       }
    }
    ```

## Delete a call log (DELETE)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/call_logs/:call_log_id`
- **Description**: Delete a call log. Requires account super user permissions.
- **Parameters**:
    - `id` (Number, required): The account ID
    - `call_log_id` (Number, required): The call log ID
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
            "message": "Call log does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all call logs (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/call_logs`
- **Description**: Get all call logs
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "account_id": 2,
          "time_in_seconds": 12,
          "subject": "Support issue",
          "body": "Blah blah blah blah blah",
          "user_id": 1,
          "created_at": "2016-05-20 14:14:33"
        },
        {
          "id": 2,
          "account_id": 2,
          "time_in_seconds": 12,
          "subject": "Support issue",
          "body": "Blah blah blah blah blah again!",
          "user_id": 1,
          "created_at": "2016-05-20 14:14:33"
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

## Get an individual call log (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/call_logs/:call_log_id`
- **Description**: Get an individual call log
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `call_log_id` (Number, required): The ID of the call log
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "account_id": 2,
        "time_in_seconds": 12,
        "subject": "Support issue",
        "body": "Blah blah blah blah blah",
        "user_id": 1,
        "created_at": "2016-05-20 14:14:33"
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

## Update call log (PATCH)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/call_logs/:call_log_id`
- **Description**: Update an existing call log. Requires account super user permissions.
- **Parameters**:
    - `id` (Number, required): The account ID
    - `call_log_id` (Number, required): The call log ID
    - `time_in_seconds` (Number, optional): How long the call lasted, in seconds
    - `subject` (String, optional): The subject of the call
    - `body` (String, optional): The body of the call
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "account_id": 2,
        "time_in_seconds": 12,
        "subject": "Support issue",
        "body": "Please don't write 'blah blah blah blah blah' in call logs.",
        "user_id": 1,
       "created_at": "2016-05-20 14:14:33"
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
