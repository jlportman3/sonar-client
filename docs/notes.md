# Notes Endpoints

## Create note (POST)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/notes/:entity_type/:entity_id`
- **Description**: Create a new note
- **Parameters**:
    - `entity_type` (String, required): The type of entity. An entity can be anything stored in the system - use the URL for the entity API functions to determine the name. E.g. to store an account note, use 'accounts'. To store a network site note, use 'network_sites'.
    - `entity_id` (Integer, required): The ID of the entity
    - `category` (String, required): A non-localized string representing the category of the note (`"inquiry"`, `"billing"`, `"support"`, `"sales"`, `"other"`)
    - `message` (String, required): The content of the note. This may contain HTML
    - `priority` (Integer, optional): The priority of the note. 0 means a regular note. 1 is a sticky note. 2 is an alert note. (`0`, `1`, `2`)
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "category": "billing",
        "message": "I just found out I can type ANYTHING I want in here!",
        "username": "ermintrude",
        "priority": 0
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "That is not a valid entity type for a note."
            },
            "status_code": 422
        }
    }
    ```

## Delete a note (DELETE)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/notes/:entity_type/:entity_id/:note_id`
- **Description**: Delete a note.
- **Parameters**:
    - `entity_type` (String, required): The type of entity. An entity can be anything stored in the system - use the URL for the entity API functions to determine the name. E.g. to store an account note, use 'accounts'. To store a network site note, use 'network_sites'.
    - `entity_id` (Integer, required): The ID of the entity
    - `note_id` (Integer, required): The ID of the note
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
            "message": "alerting rotation day/time does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all notes for an entity (GET)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/notes/:entity_type/:entity_id`
- **Description**: Get a list of the notes for an entity, such as an account.
- **Parameters**:
    - `entity_type` (String, required): The type of entity. An entity can be anything stored in the system - use the URL for the entity API functions to determine the name. E.g. to store an account note, use 'accounts'. To store a network site note, use 'network_sites'.
    - `entity_id` (Integer, required): The ID of the entity
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
    - `priority` (Integer, optional): The priority of the note. 0 means a regular note. 1 is a sticky note. 2 is an alert note. (`0`, `1`, `2`)
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "category": "billing",
          "message": "Took a call from Adelaide, she said it was time we got paid. She busted out her VISA because she said the invoice pleased her.",
          "username": "reginald",
          "priority": 0
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

## Get individual note for an entity (GET)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/notes/:entity_type/:entity_id/:note_id`
- **Description**: Get a list of the notes for an entity, such as an account.
- **Parameters**:
    - `entity_type` (String, required): The type of entity. An entity can be anything stored in the system - use the URL for the entity API functions to determine the name. E.g. to store an account note, use 'accounts'. To store a network site note, use 'network_sites'.
    - `entity_id` (Integer, required): The ID of the entity
    - `note_id` (Integer, required): The ID of the note
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "category": "billing",
        "message": "I just found out I can type ANYTHING I want in here!",
        "username": "ermintrude",
        "priority": 1
      }
    }
    ```

## Update a note (PATCH)
- **Version**: 1.0.15
- **Endpoint**: `https://example.sonar.software/api/v1/notes/:entity_type/:entity_id/:note_id`
- **Description**: Update a note.
- **Parameters**:
    - `entity_type` (String, required): The type of entity. An entity can be anything stored in the system - use the URL for the entity API functions to determine the name. E.g. to store an account note, use 'accounts'. To store a network site note, use 'network_sites'.
    - `entity_id` (Integer, required): The ID of the entity
    - `note_id` (Integer, required): The ID of the note
    - `category` (String, optional): The category of the note (`"inquiry"`, `"billing"`, `"support"`, `"sales"`, `"other"`)
    - `message` (String, optional): The note content
    - `priority` (Integer, optional): The priority of the note. 0 means a regular note. 1 is a sticky note. 2 is an alert note. (`0`, `1`, `2`)
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 4,
        "category": "inquiry",
        "message": "test",
        "username": "admin",
        "priority": 0
      }
    }
    ```
```
