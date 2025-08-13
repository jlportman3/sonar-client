# Custom Fields Endpoints

## Get custom fields for entity (GET)
- **Version**: 1.2.12
- **Endpoint**: `https://example.sonar.software/api/v1/entity_custom_fields/:entity/:entity_id`
- **Description**: Get a list of the custom fields assigned to this entity that have information set.
- **Parameters**:
    - `entity` (String, required): The type of entity to get custom fields for. (`"account"`, `"generic_inventory_assignee"`, `"network_site"`, `"jobs"`)
    - `entity_id` (Number, required): The ID of the entity
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "custom_field_id": 4,
          "data": false
        },
        {
          "custom_field_id": 3,
          "data": "Some text"
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

## Get individual custom field for entity (GET)
- **Version**: 1.2.12
- **Endpoint**: `https://example.sonar.software/api/v1/entity_custom_fields/:entity/:entity_id/:custom_field_id`
- **Description**: Get a specific custom field for a specific entity, by custom field ID.
- **Parameters**:
    - `entity` (String, required): The type of entity to get custom fields for. (`"account"`, `"generic_inventory_assignee"`, `"network_site"`, `"jobs"`)
    - `entity_id` (Number, required): The ID of the entity
    - `custom_field_id` (Number, required): The ID of the custom field (provided at `/system/custom_fields`)
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "custom_field_id": 4,
        "data": false
      }
    }
    ```

## Update a custom field for an entity (PATCH)
- **Version**: 1.2.12
- **Endpoint**: `https://example.sonar.software/api/v1/entity_custom_fields/:entity/:entity_id/:custom_field_id`
- **Description**: Update the data in a custom field for an entity.
- **Parameters**:
    - `entity` (String, required): The type of entity to get custom fields for. (`"account"`, `"generic_inventory_assignee"`, `"network_site"`, `"jobs"`)
    - `entity_id` (Number, required): The ID of the entity
    - `custom_field_id` (Number, required): The ID of the custom field (provided at `/system/custom_fields`)
    - `data` (String, required): The content of the custom field. If the custom field is a checkbox, this must be a boolean. If it is a select/dropdown, it must be one of the predefined fields allowed. If it is a date, it must be YYYY-MM-DD format.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "custom_field_id": 4,
        "data": false
      }
    }
    ```
```
