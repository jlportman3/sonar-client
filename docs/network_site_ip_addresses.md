# Network Site IP Addresses Endpoints

## Assign an IP to a network site (POST)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/ip_assignments`
- **Description**: This endpoint allows you to assign IPv4/IPv6 assignments to a network site or an inventory model field on an network site. Please see the documentation for more details about the different scenarios in which you would pick each entity.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `subnet` (String, required): The subnet to assign to this entity, with a CIDR prefix, either IPv4 or IPv6. E.g. 192.168.100.1/32 or 2001:DB8::/64. It must fit within an infrastructure/mixed subnet, or an IP pool. IP pool assignments can only be an IPv4 /32.
    - `assigned_entity` (String, required): The entity to assign this to - the network site directly or an inventory item on the network site. (`"network_sites"`, `"inventory_items"`)
    - `assigned_id` (Number, optional): The ID of the entity referenced in `assigned_entity`. If `assigned_entity` is 'network_sites'
    - `inventory_item_field_id` (Number, optional): If you are assigning this to an inventory item, supply the ID of the field that contains the MAC address (for DHCP assignment) or the IMSI (for LTE provisioning.) This is required if `assigned_entity` is "inventory_items"
    - `description` (String, optional): An optional description for the assignment
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
         "id": 53,
         "subnet_id": 4,
         "subnet": "192.168.0.153",
         "assigned_entity": "network_sites",
         "assigned_id": 1,
         "inventory_item_field_id": null,
         "ip_pool_id": 3,
         "network_site_id": 1,
         "description": "Loopback for Router ABC",
         "soft": false
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": "The requested subnet overlaps the existing assignment of 192.168.100.17",
            "status_code": 422
        }
    }
    ```

## Delete IP assignment (DELETE)
- **Version**: 0.4.1
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/ip_assignments/:ip_assignment_id`
- **Description**: Delete an IP assignment.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `ip_assignment_id` (Number, required): The ID of the IP assignment
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "success": true
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "message": "That IP assignment is not assigned to that network site."
            },
            "status_code": 422
        }
    }
    ```

## Get all IP assignments (GET)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/ip_assignments`
- **Description**: Retrieve a list of existing IP assignments on the account.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `id` (Number, required): The ID of the network site
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 52,
          "subnet_id": 4,
          "subnet": "192.168.0.2",
          "assigned_entity": "network_sites",
          "assigned_id": 1,
          "inventory_item_field_id": null,
          "ip_pool_id": null,
          "network_site_id": 1,
          "description": null,
          "soft": false
        },
        {
          "id": 53,
          "subnet_id": 4,
          "subnet": "192.168.0.153",
          "assigned_entity": "network_sites",
          "assigned_id": 1,
          "inventory_item_field_id": null,
          "ip_pool_id": 3,
          "network_site_id": 1,
          "description": null,
          "soft": false
        },
        {
          "id": 54,
          "subnet_id": 4,
          "subnet": "192.168.0.154",
          "assigned_entity": "inventory_items",
          "assigned_id": 3,
          "inventory_item_field_id": null,
          "ip_pool_id": 3,
          "network_site_id": 1,
          "description": "Some description",
          "soft": false
        }
      ],
      "paginator": {
        "total_count": 3,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get individual IP assignment (GET)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/ip_assignments/:ip_assignment_id`
- **Description**: Retrieve a specific IP assignment.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `ip_assignment_id` (Number, required): The ID of the IP assignment.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 52,
        "subnet_id": 4,
        "subnet": "192.168.0.2",
        "assigned_entity": "network_sites",
        "assigned_id": 1,
        "inventory_item_field_id": null,
        "ip_pool_id": null,
        "network_site_id": 1,
        "description": "Finn & Jake's favorite IP",
        "soft": false
      }
    }
    ```

## Update IP assignment (PATCH)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id/ip_assignments/:ip_assignment_id`
- **Description**: Update an existing IP assignment. If the assignment is on an network site, only the subnet can be changed. If it is on an inventory item, the assigned_id, the subnet and inventory_item_field_id can be changed. To change the entity on an assignment other than an inventory item, delete the existing assignment and create a new one.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `ip_assignment_id` (Number, required): The ID of the IP assignment
    - `subnet` (String, optional): The subnet to assign to this entity, with a CIDR prefix, either IPv4 or IPv6. E.g. 192.168.100.1/32 or 2001:DB8::/64. It must fit within a infrastructure/mixed subnet, or an IP pool. IP pool assignments can only be an IPv4 /32s.
    - `assigned_id` (Number, optional): Only valid if this is an inventory item - this will allow you to move the IP to another inventory item. If you supply this, you must also supply `inventory_item_field_id` or the query will be rejected. If the inventory item is not assigned to the same network site as the existing assignment, it will also be rejected.
    - `inventory_item_field_id` (Number, optional): If you want to change the field ID, supply the ID of the field that contains the MAC address (for DHCP assignment) or the IMSI (for LTE provisioning.).
    - `description` (String, optional): An optional description for the assignment
    - `make_permanent` (Boolean, optional): If this is set to true, and the soft property of this IP assignment is currently true, then this will be changed to a permanent assignment.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 52,
        "subnet_id": 4,
        "subnet": "192.168.0.156/32",
        "assigned_entity": "network_sites",
        "assigned_id": 1,
        "inventory_item_field_id": null,
        "ip_pool_id": 3,
        "network_site_id": 1,
        "description": null,
        "soft": false
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "subnet": "abcdefg is not a valid IP address."
            },
            "status_code": 422
        }
    }
    ```
```
