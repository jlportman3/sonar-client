# Files Endpoints

## Delete file (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:entity_id/files/:file_id`
- **Description**: Delete a file. Only entities that support files can be input to this endpoint. To get a valid entity name, use the portion of the route that corresponds to the entity in another API call - for example, the entity for an account is 'accounts', for ticket replies, it is 'ticket_replies'.
- **Parameters**:
    - `entity_id` (Number, required): The ID of the entity
    - `entity` (String, required): The type of entity (e.g. accounts, ticket_replies)
    - `file_id` (Number, required): The ID of the file
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
            "message": "File does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all files (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:id/files`
- **Description**: Get a list of files available on a specific entity. Only entities that support files can be input to this endpoint. To get a valid entity name, use the portion of the route that corresponds to the entity in another API call - for example, the entity for an account is 'accounts', for ticket replies, it is 'ticket_replies'.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `id` (Number, required): The ID of the entity
    - `entity` (String, required): The type of entity
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "filename": "HC04364756.pdf",
          "size_in_bytes": 76414,
          "description": "This is a contract!",
          "mime_type": "application/pdf",
          "uploader": "admin"
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

## Get individual file (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:entity_id/files/:file_id`
- **Description**: Get an individual file. This will return the file details and the base64 data which can be decoded to create the file itself. Only entities that support files can be input to this endpoint. To get a valid entity name, use the portion of the route that corresponds to the entity in another API call - for example, the entity for an account is 'accounts', for ticket replies, it is 'ticket_replies'.
- **Parameters**:
    - `entity_id` (Number, required): The ID of the entity
    - `entity` (String, required): The type of entity (e.g. accounts, ticket_replies)
    - `file_id` (Number, required): The ID of the file
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
          "id": 2,
          "filename": "my eighty ninth file upload.txt",
          "size_in_bytes": 19,
          "description": "This is a small file!",
          "mime_type": "text/plain",
          "uploader": "admin",
          "base64_data": "U29uYXIgaXMgdGhlIGJlc3QhCg=="
        }
    }
    ```

## Update file details (PATCH)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:entity_id/files/:file_id`
- **Description**: Update details on a file. You can only change the description or the filename. To change file contents, delete it and upload a new one.
- **Parameters**:
    - `entity_id` (Number, required): The ID of the entity
    - `entity` (String, required): The name of the entity (e.g. accounts, ticket_replies)
    - `file_id` (Number, required): The ID of the file
    - `description` (String, optional): A description for the file
    - `filename` (String, optional): A filename for the file (with extension) - e.g. myfile.pdf, myfile.png
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 1,
          "filename": "HC04364756.pdf",
          "size_in_bytes": 76414,
          "description": "This is a contract!",
          "mime_type": "application/pdf",
          "uploader": "admin"
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "file": "File ID not found."
            },
            "status_code": 422
        }
    }
    ```

## Upload a new file (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:id/files`
- **Description**: Upload a new file to the entity. Images uploaded will be automatically converted to JPEG format and resized to a max of 2048x2048.
- **Parameters**:
    - `entity` (String, required): The name of the entity (e.g. accounts, ticket_replies)
    - `id` (Number, required): The ID of the entity
    - `description` (String, optional): A description for the file
    - `base64_data` (String, required): The file, base64 encoded
    - `filename` (String, required): A filename for the file (with extension) - e.g. myfile.pdf, myfile.png
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
          "id": 2,
          "filename": "my first file upload.pdf",
          "size_in_bytes": 489384,
          "description": "This is a contract also!",
          "mime_type": "application/pdf",
          "uploader": "admin"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```
```
