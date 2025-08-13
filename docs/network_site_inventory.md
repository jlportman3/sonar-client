# Network Site Inventory Endpoints

## Get all inventory items (GET)
- **Version**: 0.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/inventory_items`
- **Description**: Get a list of inventory at a specific network site.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 3,
          "inventory_model_id": 1,
          "status": "functional",
          "purchase_price": 0,
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "00:00:00:00:00:0C"
            }
          ]
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

## Get individual inventory item (GET)
- **Version**: 0.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/inventory_items/:item_id`
- **Description**: Get a specific inventory item at a specific network site.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `item_id` (Number, required): The ID of the inventory item
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "inventory_model_id": 1,
        "status": "functional",
        "purchase_price": 0,
        "condition": "new",
        "consumed": false,
        "consumed_at": null,
        "fields": [
          {
            "field_id": 1,
            "data": "00:00:00:00:00:0C"
          }
        ]
      }
    }
    ```
```
