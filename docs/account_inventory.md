# Account Inventory Endpoints

## Get all inventory items (GET)
- **Version**: 0.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/inventory_items`
- **Description**: Get a list of inventory on a specific account.
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
          "inventory_model_id": 1,
          "status": "lost",
          "purchase_price": 0,
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "00:00:00:00:00:DD"
            },
            {
              "field_id": 2,
              "data": ""
            }
          ]
        },
        {
          "id": 2,
          "inventory_model_id": 1,
          "status": "functional",
          "purchase_price": 0,
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "00:00:00:00:00:0B"
            }
          ]
        },
        {
          "id": 29,
          "inventory_model_id": 1,
          "status": "functional",
          "purchase_price": 0,
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "00:DD:11:AA:BB:CC"
            },
            {
              "field_id": 2,
              "data": "1"
            }
          ]
        },
        {
          "id": 30,
          "inventory_model_id": 1,
          "status": "functional",
          "purchase_price": 0,
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "00:00:00:0A:BC:12"
            },
            {
              "field_id": 2,
              "data": "12345"
            }
          ]
        }
      ],
      "paginator": {
        "total_count": 4,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get individual inventory item (GET)
- **Version**: 0.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/inventory_items/:item_id`
- **Description**: Get a specific inventory item on an account.
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `item_id` (Number, required): The ID of the inventory item
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "inventory_model_id": 1,
        "status": "lost",
        "purchase_price": 0,
        "condition": "new",
        "consumed": false,
        "consumed_at": null,
        "fields": [
          {
            "field_id": 1,
            "data": "00:00:00:00:00:DD"
          },
          {
            "field_id": 2,
            "data": ""
          }
        ]
      }
    }
    ```
```
