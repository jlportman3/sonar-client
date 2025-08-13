# Invoice Messages Endpoints

## Create a new invoice message (POST)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/financial/invoices/invoice_messages`
- **Description**: Create a new invoice message.
- **Parameters**:
    - `name` (String, required): A name for the invoice message
    - `message` (String, required): The invoice message
    - `account_type_ids` (Array, optional): An array of account type IDs that this invoice message should be appended for
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 7,
        "name": "Commercial Message",
        "message": "Please remit payment through our business portal at www.example.biz",
        "account_type_ids": [
          2
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "account_type_ids": "You must input at least one account type ID."
         },
         "status_code": 422
       }
    }
    ```

## Delete a invoice message (DELETE)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/financial/invoices/invoice_messages/:id`
- **Description**: Delete a invoice message
- **Parameters**:
    - `id` (Integer, required): The ID of the invoice message
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
            "message": "invoice message does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all invoice messages (GET)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/financial/invoices/invoice_messages`
- **Description**: Get all invoice messages
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 6,
          "name": "Test message",
          "message": "This is a test message, I hope nobody sees it!",
          "account_type_ids": [
            1
          ]
        },
        {
          "id": 7,
          "name": "Commercial Message",
          "message": "Please remit payment through our business portal at www.example.biz",
          "account_type_ids": [
            2
          ]
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

## Get an individual invoice message (GET)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/financial/invoices/invoice_messages/:id`
- **Description**: Get an individual invoice message
- **Parameters**:
    - `id` (Integer, required): The ID of the invoice message
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "name": "Commercial Message",
        "message": "Please remit payment through our business portal at www.example.biz",
        "account_type_ids": [
          2
        ]
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

## Update invoice message (PATCH)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/financial/invoices/invoice_messages/:id`
- **Description**: Update an existing invoice message.
- **Parameters**:
    - `id` (Integer, required): The invoice message ID
    - `name` (String, optional): A name for the invoice message
    - `message` (String, optional): The invoice message
    - `account_type_ids` (Array, optional): An array of account type IDs that this invoice message should be appended for
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "name": "Commercial Message",
        "message": "Please remit payment through our business portal at www.example.software",
        "account_type_ids": [
          2
        ]
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
