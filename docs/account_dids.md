# Account DIDs Endpoints

## Assign a DID to an account (POST)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/dids`
- **Description**: Assign a currently unassigned DID to an account.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `did` (String, required): The DID to assign. This DID must already have been inventoried in Sonar.
    - `service_id` (Integer, required): The ID of a voice service to associate the DID with. This voice service must already be on the account.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "did": "1234567892",
        "account_id": 1,
        "service_id": 30,
        "rate_center_id": 1
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
      "error": {
        "message": "DID is already assigned to account 1.",
        "status_code": 422
      }
    }
    ```

## Get all DIDs assigned to account (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/dids`
- **Description**: Get all DIDs assigned to the account.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 7,
          "did": "1234567892",
          "account_id": 1,
          "service_id": 30,
          "rate_center_id": 1
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

## Get an individual DID assigned to an account (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/dids/:did_id`
- **Description**: Get an individual DID associated with an account.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `did_id` (Integer, required): The ID of the DID
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "did": "1234567892",
        "account_id": 1,
        "service_id": 30,
        "rate_center_id": 1
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

## Move a DID to another voice service (PATCH)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/dids/:did_id`
- **Description**: Update an existing DID assignment to change the assigned service
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `did_id` (Integer, required): The ID of the DID
    - `service_id` (Integer, required): The ID of a voice service on the account
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 7,
        "did": "1234567892",
        "account_id": 1,
        "service_id": 31,
        "rate_center_id": 1
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

## Unassign a DID from an account (DELETE)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/dids/:did_id`
- **Description**: Unassociate a DID from an account.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `did_id` (Integer, required): The ID of the DID
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "did": "1234567892",
        "account_id": null,
        "service_id": null,
        "rate_center_id": 1
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
