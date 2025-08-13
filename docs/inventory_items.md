# Inventory Items Endpoints

## Create a new inventory model deployment type (POST)
- **Version**: 1.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:inventory_model_id/inventory_model_deployment_types`
- **Description**: Create a new inventory model deployment type.
- **Parameters**:
    - `inventory_model_id` (Integer, required): The ID of the inventory model to create the type for
    - `deployment_type` (String, required): A descriptive name for the inventory model deployment type
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Some test name"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "name": "The name must be unique."
         },
         "status_code": 422
       }
    }
    ```

## Create a new manufacturer (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/manufacturers`
- **Description**: Create a new manufacturer.
- **Parameters**:
    - `name` (String, required): A unique name for the manufacturer
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 35,
            "name": "Cambium"
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

## Create a new model field (POST)
- **Version**: 0.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id/fields`
- **Description**: Create a new model field.
- **Parameters**:
    - `id` (Number, required): The ID of the model
    - `name` (String, required): The name of the field
    - `type` (String, required): The type of field this is. Can be a string (any data), an integer (a number such as 1,2,3) a decimal (a number such as 1.0 or 4.55), a MAC address in XX:YY:ZZ:11:22:33 format, an IMSI number, an OP/OPc value, an LTE auth key, or a regular expression. Regular expressions are entered in PCRE format. (`"string"`, `"integer"`, `"decimal"`, `"mac"`, `"imsi"`, `"regexp"`, `"op_opc"`, `"lte_auth_key"`)
    - `is_required` (Boolean, optional): Whether or not the field is required to be completed when entering a new inventory item. If you do not add any fields, the item will be treated as generic, and can be added and reassigned by quantity. If an item has fields, is is unique and must always be referenced directly when adding and reassigning
    - `unique` (Boolean, optional): Whether or not the contents of this field must be unique. This is only within the context of the model itself - e.g. if you create a field named 'Serial Number' for a model with ID 1 and mark it as unique, all items added that correspond to model ID 1 must have unique data in the 'Serial Number' field, but another field named 'Serial Number' on model ID 2 would not conflict.
    - `regexp` (String, optional): If type is set to regexp, this is the regular expression to run against data input into this field, in PCRE format. For example, you could validate a MAC address with "/^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$/". You can use https://regex101.com/ as a third party site to test/validate your regular expressions.
- **Success Response (201 Created)**:
    ```json
    {
       "id": 9,
       "name": "MAC Address",
       "type": "mac",
       "is_required": true,
       "unique": true,
       "regexp": null
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name is required."
            },
            "status_code": 422
        }
    }
    ```

## Create a new model (POST)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models`
- **Description**: Create a new model.
- **Parameters**:
    - `manufacturer_id` (Number, required): The internal id of the manufacturer
    - `name` (String, required): The name of the model
    - `inventory_model_category_id` (Number, required): The category ID that this model is part of
    - `https` (Boolean, optional): Whether or not links to IPs associated with this inventory model should use HTTPS or HTTP
    - `port` (Integer, optional): The TCP port to use for clickable links to IPs associated with this model
- **Success Response (201 Created)**:
    ```json
    {
       "id": 1,
       "name": "PMP450 5GHz AP",
       "manufacturer_id": 2,
       "inventory_model_category_id": 1,
       "https": true,
       "port": 443
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

## Create category (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/categories`
- **Description**: Create an inventory model category. This describes a group of inventory models and should be descriptive enough to be utilized in provisioning, monitoring, etc. For example, 'CPE Routers', 'CPE Radios' or 'GPON ONTs' is typically sufficiently descriptive but 'CPE' would not be.
- **Parameters**:
    - `name` (String, required): The name of the category
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "CPE Radios"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name must be unique."
            },
            "status_code": 422
        }
    }
    ```

## Create inventory items (POST)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items`
- **Description**: Create inventory items. This endpoint is slightly different than other endpoints as you must submit data in an array. This allows you to save multiple items at a time. It is recommended that you do validation on the input fields before submitting them here, as if you are submitting a large amount of items, a single invalid field will abort the entire insertion. If you are inserting very large quantities of items (1000) then make sure you set an adequate timeout on your connection, as it may take some additional time to process the data. You can also batch the insertions into groups in order to speed up processing.
- **Parameters**:
    - `model_id` (Number, required): The ID of an inventory model
    - `assignee_type` (String, required): The type of assignee to assign this item to (`"accounts"`, `"network_sites"`, `"inventory_locations"`, `"vehicles"`, `"generic_inventory_assignees"`, `"users"`)
    - `assignee_id` (Number, required): The ID of the assignee (e.g. the ID of the vehicle, account, etc)
    - `condition` (String, optional): The condition of the items (`"new"`, `"used"`)
    - `individualList` (Array, optional): An array of field objects, if items being added have fields. The format of the field object is a 'fields' property, which is an object with multiple properties representing field IDs, and values representing field data. See example below. If there are no fields defined and you are entering multiple generic items, use the 'quantity' option show below.
    - `quantity` (Number, optional): Only valid if the item being added has no fields defined. You must either define quantity or individualList.
    - `purchase_price` (Number, optional): Set the purchase price for the items, in your local currency. This is used for reporting purposes.
- **Example Request Body (Individual List)**:
    ```json
    {
        "assignee_type": "generic_inventory_assignees",
        "assignee_id": 23,
        "model_id": 1305,
        "condition": "new",
        "individualList": [
            {
                "fields": {
                    "1228": "This is the data for field ID 1228",
                    "1229": "This is the data for field ID 1229"
                }
            },
            {
                "fields": {
                    "1228": "This is the data for a second item being inserted for field ID 1228",
                    "1229": "This is the data for a second item being inserted for field ID 1229"
                }
            }
        ]
    }
    ```
- **Example Request Body (Quantity)**:
    ```json
    {
        "assignee_type": "generic_inventory_assignees",
        "assignee_id": 23,
        "model_id": 1305,
        "condition": "new",
        "quantity": 5
    }
    ```
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "ids": [
           1,
           2,
           3,
           4
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "data": "The MAC Address field must be formatted as a MAC address in xx:xx:xx:xx:xx:xx format."
            },
            "status_code": 422
        }
    }
    ```

## Delete a inventory model deployment type (DELETE)
- **Version**: 1.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:inventory_model_id/inventory_model_deployment_types/:id`
- **Description**: Delete a inventory model deployment type
- **Parameters**:
    - `inventory_model_id` (Integer, required): The ID of the inventory model to delete the type from
    - `id` (Integer, required): The ID of the inventory model deployment type
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
            "message": "inventory model deployment type does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete category (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/categories/:id`
- **Description**: Delete an inventory model category
- **Parameters**:
    - `id` (Number, required): The ID of the category
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
            "message": "Category cannot be deleted as inventory models are utilizing it.",
            "status_code": 422
        }
    }
    ```

## Delete item (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items/:id`
- **Description**: Delete an item. Generally, you don't want to do this unless you've made a mistake. If a unit is failed or sold, you should use the appropriate properties to denote that. Deleting items from inventory will destroy history.
- **Parameters**:
    - `id` (Number, required): The ID of the item
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
            "message": "Item cannot be deleted as it has been sold.",
            "status_code": 422
        }
    }
    ```

## Delete manufacturer (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/manufacturers/:id`
- **Description**: Delete a manufacturer
- **Parameters**:
    - `id` (Number, required): The ID of the manufacturer
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
            "message": "Manufacturer cannot be deleted as inventory models are utilizing it.",
            "status_code": 422
        }
    }
    ```

## Delete model field (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/fields/:field_id`
- **Description**: Delete a model field. Deleting a field will also remove any data present in these fields on existing items.
- **Parameters**:
    - `model_id` (Number, required): The ID of the model
    - `field_id` (Number, required): The ID of the field
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
            "message": "Model field cannot be deleted as IP addresses are associated with this field on existing items.",
            "status_code": 422
        }
    }
    ```

## Delete model (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id`
- **Description**: Delete a model
- **Parameters**:
    - `id` (Number, required): The ID of the model
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
            "message": "Model cannot be deleted as inventory items are utilizing it.",
            "status_code": 422
        }
    }
    ```

## Get all categories (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/categories`
- **Description**: Get a list of categories.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "CPE Radios"
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

## Get all inventory items (GET)
- **Version**: 1.7.14
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items/`
- **Description**: Get all inventory items
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "inventory_model_id": 2,
          "assignee_id": 1,
          "assignee_type": "users",
          "status": "functional",
          "condition": "new",
          "consumed": false,
          "consumed_at": null,
          "fields": [
            {
              "field_id": 1,
              "data": "Some data"
            },
            {
              "field_id": 2,
              "data": "00:AA:BB:CC:11:DD"
            }
          ],
          "inventory_model_deployment_type_id": null
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

## Get all inventory model deployment types (GET)
- **Version**: 1.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:inventory_model_id/inventory_model_deployment_types`
- **Description**: Get all inventory model deployment types
- **Parameters**:
    - `inventory_model_id` (Integer, required): The ID of the inventory model to get the type for
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "deployment_type": "Backhaul"
        },
        {
          "id": 1,
          "deployment_type": "Access Point"
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

## Get all manufacturers (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/manufacturers`
- **Description**: Get a list of manufacturers.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
           {
                "id": 35,
                "name": "Cambium"
           },
           {
               "id": 36,
               "name": "Cisco"
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

## Get all model fields (GET)
- **Version**: 0.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id/fields`
- **Description**: Get a list of model fields. This is not the data in the fields themselves - this is the definition of the fields on the model. When adding an inventory item, these fields will be present for each item.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `id` (Number, required): The ID of the model
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
           {
               "id": 9,
               "name": "MAC Address",
               "type": "mac",
               "is_required": true,
               "unique": true,
               "regexp": null
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

## Get all models (GET)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models`
- **Description**: Get a list of models. A model is the descriptor for an item - e.g. a Cisco 2940 switch would have a model of '2940' and a manufacturer of 'Cisco'
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
           {
               "id": 1,
               "name": "PMP450 5GHz AP",
               "manufacturer_id": 2,
               "inventory_model_category_id": 1,
               "https": false,
               "port": 80
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

## Get an individual inventory model deployment type (GET)
- **Version**: 1.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:inventory_model_id/inventory_model_deployment_types/:id`
- **Description**: Get an individual inventory model deployment type
- **Parameters**:
    - `inventory_model_id` (Integer, required): The ID of the inventory model to get the type for
    - `id` (Integer, required): The ID of the inventory model deployment type
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "CPE"
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

## Get individual category (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/categories/:id`
- **Description**: Get an individual inventory model category.
- **Parameters**:
    - `id` (Number, required): The ID of the category
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "CPE Radios"
      }
    }
    ```

## Get individual inventory item (GET)
- **Version**: 1.7.14
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items/:id`
- **Description**: Get an individual item.
- **Parameters**:
    - `id` (Number, required): The ID of the item
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "inventory_model_id": 2,
        "assignee_id": 1,
        "assignee_type": "users",
        "status": "functional",
        "condition": "new",
        "consumed": false,
        "consumed_at": null,
        "fields": [
          {
            "field_id": 1,
            "data": "Some data"
          },
          {
            "field_id": 2,
            "data": "00:AA:BB:CC:11:DD"
          }
        ],
        "inventory_model_deployment_type_id": null
      }
    }
    ```

## Get individual manufacturer (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/manufacturers/:id`
- **Description**: Get an individual manufacturer.
- **Parameters**:
    - `id` (Number, required): The ID of the manufacturer
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 1,
           "name": "Cambium"
       }
    }
    ```

## Get individual model field (GET)
- **Version**: 0.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:model_id/fields/:field_id`
- **Description**: Get an individual model field.
- **Parameters**:
    - `model_id` (Number, required): The ID of the model
    - `field_id` (Number, required): The ID of the field
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 9,
           "name": "MAC Address",
           "type": "mac",
           "is_required": true,
           "unique": true,
           "regexp": null
       }
    }
    ```

## Get individual model (GET)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id`
- **Description**: Get an individual model.
- **Parameters**:
    - `id` (Number, required): The ID of the model
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 1,
           "name": "PMP450 5GHz AP",
           "manufacturer_id": 2,
           "inventory_model_category_id": 1,
           "https": false,
           "port": 12345
       }
    }
    ```

## Mass delete items (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items`
- **Description**: Mass delete inventory items. Be very careful using this endpoint, you cannot restore deleted items!
- **Parameters**:
    - `inventory_item_ids` (Array, required): An array of inventory item IDs to be deleted.
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
            "message": "Item cannot be deleted as the list of IDs is not valid.",
            "status_code": 422
        }
    }
    ```

## Mass update inventory items (POST)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items`
- **Description**: Mass update inventory items. This is frequently used in order to assign a large quantity of items to a new assignee, or to update the status of a group of items. You cannot update item fields using this endpoint - only the items themselves.
- **Parameters**:
    - `assignee_type` (String, optional): The type of assignee to assign these items to. You can only move items to other entities that treat the items as undeployed. If you want to assign to an account, use the single update endpoint. (`"inventory_locations"`, `"vehicles"`, `"generic_inventory_assignees"`, `"users"`)
    - `assignee_id` (Number, optional): The ID of the assignee (e.g. the ID of the vehicle, account, etc)
    - `item_ids` (Array, required): An array that contains the IDs of all the items that should be updated.
    - `status` (String, optional): The status of the items. (`"functional"`, `"failed"`, `"lost"`)
    - `condition` (String, optional): The condition of the items. (`"new"`, `"used"`)
    - `consumed` (Boolean, optional): Whether or not the item has been consumed.
    - `purchase_price` (Number, optional): The purchase price of the items.
- **Example Request Body**:
    ```json
    {
        "assignee_type": "users",
        "assignee_id": 1,
        "status": "failed",
        "item_ids": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            10,
            53,
            4938
        ]
    }
    ```
- **Success Response (201 Created)**:
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
                "data": "The MAC Address field must be formatted as a MAC address in xx:xx:xx:xx:xx:xx format."
            },
            "status_code": 422
        }
    }
    ```

## Update SNMP override (PATCH)
- **Version**: 1.0.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items/:id/snmp_override`
- **Description**: Override the SNMP authentication information for an item. This will override any defaults set on a monitoring template.
- **Parameters**:
    - `id` (Number, required): The ID of the item
    - `enabled` (Boolean, optional): Whether or not to enable the override
    - `snmp_version` (Number, optional): The SNMP version to use (`1`, `2`, `3`)
    - `snmp_community` (String, optional): The SNMP community/security name to use
    - `snmp3_sec_level` (String, optional): If you are using SNMPv3, this is the security level (`"noAuthNoPriv"`, `"authNoPriv"`, `"authPriv"`)
    - `snmp3_auth_protocol` (String, optional): If you are using SNMPv3, this is the authentication protocol (`"MD5"`, `"SHA"`)
    - `snmp3_auth_passphrase` (String, optional): If you are using SNMPv3, this is the authentication pass phrase
    - `snmp3_priv_protocol` (String, optional): If you are using SNMPv3, this is the privacy protocol (`"DES"`, `"AES"`)
    - `snmp3_priv_passphrase` (String, optional): If you are using SNMPv3, This is the privacy passphrase
    - `snmp3_context_name` (String, optional): If you are using SNMPv3, this is the context name
    - `snmp3_context_engine_id` (String, optional): If you are using SNMPv3, this is the default context EngineID
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "inventory_model_id": 2,
        "assignee_id": 1,
        "assignee_type": "accounts",
        "status": "functional",
        "purchase_price": 0,
        "condition": "new",
        "consumed": false,
        "consumed_at": null,
        "fields": [
          {
            "field_id": 1,
            "data": "AA:BB:CC:DD:EE:FF"
          }
        ],
        "snmp_override": {
          "enabled": true,
          "snmp_version": 2,
          "snmp_community": "public",
          "snmp3_sec_level": null,
          "snmp3_auth_protocol": null,
          "snmp3_auth_passphrase": null,
          "snmp3_priv_protocol": null,
          "snmp3_priv_passphrase": null,
          "snmp3_context_name": null,
          "snmp3_context_engine_id": null
        }
      }
    }
    ```

## Update category (PATCH)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/categories/:id`
- **Description**: Update an individual inventory model category
- **Parameters**:
    - `id` (Number, required): The ID of the inventory model category
    - `name` (String, required): The name for the inventory model category
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "CPE Radios"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name must be unique."
            },
            "status_code": 422
        }
    }
    ```

## Update inventory item (PATCH)
- **Version**: 1.7.14
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/items/:id`
- **Description**: Update an individual inventory item
- **Parameters**:
    - `id` (Number, required): The ID of the inventory item
    - `assignee_type` (String, optional): The type of assignee to assign this item to (`"accounts"`, `"network_sites"`, `"inventory_locations"`, `"vehicles"`, `"generic_inventory_assignees"`, `"users"`)
    - `assignee_id` (Number, optional): The ID of the assignee (e.g. the ID of the vehicle, account, etc)
    - `status` (String, optional): The status of the device (`"functional"`, `"failed"`, `"lost"`)
    - `condition` (String, optional): The condition of the device (`"new"`, `"used"`)
    - `purchase_price` (Number, optional): The purchase price of the item, in local currency. This is used for reporting.
    - `consumed` (Boolean, optional): If this is a consumable item (e.g. a spool of Ethernet cable) and the spool is consumed, set this to true.
    - `fields` (Array, optional): An array of fields for this item. The structure is detailed below
    - `inventory_model_deployment_type_id` (Number, optional): The ID of a valid inventory model deployment type for this item.
- **Example Request Body**:
    ```json
    {
        "assignee_type": "vehicles",
        "assignee_id": 3,
        "status": "functional",
        "purchase_price": 10.53,
        "condition": "new",
        "fields": [
            {
                "field_id": 6,
                "data": "00:AA:BB:CC:DD:EF"
            },
            {
                "field_id": 7,
                "data": "Some data I want to store"
            }
        ],
        "inventory_model_deployment_type_id": 2
    }
    ```
- **Success Response (200 OK)**:
    ```json
    {
       "id": 68,
       "inventory_model_id": 1,
       "assignee_type": "vehicles",
       "assignee_id": 3,
       "status": "functional",
       "consumed": false,
       "consumed_at": null,
       "fields": [
           {
               "field_id": 6,
               "data": "00:AA:BB:CC:DD:EF"
           },
           {
               "field_id": 7,
               "data": "Some data I want to store"
           }
       ],
       "inventory_model_deployment_type_id": 2
   }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "data": "The MAC Address field must be formatted as a MAC address in xx:xx:xx:xx:xx:xx format."
            },
            "status_code": 422
        }
    }
    ```

## Update inventory model deployment type (PATCH)
- **Version**: 1.4.3
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:inventory_model_id/inventory_model_deployment_types/:id`
- **Description**: Update an existing inventory model deployment type.
- **Parameters**:
    - `inventory_model_id` (Integer, required): The ID of the inventory model to update the type for
    - `id` (Integer, required): The inventory model deployment type ID
    - `deployment_type` (String, required): The name of the deployment type
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "deployment_type": "Backhaul"
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

## Update manufacturer (PATCH)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/manufacturers/:id`
- **Description**: Update a manufacturer
- **Parameters**:
    - `id` (Number, required): The ID of the manufacturer
    - `name` (String, required): The name of the manufacturer
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "id": 1,
           "name": "Cambium"
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

## Update model field (PATCH)
- **Version**: 0.6.5
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id/fields/:field_id`
- **Description**: Update a model field. When modifying existing fields, all existing data must adhere to the new type. For example, if you change a field from "string" to "mac", all existing data must match the requirements of the "mac" format.
- **Parameters**:
    - `id` (Number, required): The ID of the model
    - `field_id` (Number, required): The ID of the field
    - `name` (String, required): The name of the field
    - `type` (String, required): The type of field this is. Can be a string (any data), an integer (a number such as 1,2,3) a decimal (a number such as 1.0 or 4.55), a MAC address in XX:YY:ZZ:11:22:33 format, an IMSI number, an OP/OPc value, an LTE auth key, or a regular expression. Regular expressions are entered in PCRE format. (`"string"`, `"integer"`, `"decimal"`, `"mac"`, `"imsi"`, `"regexp"`, `"op_opc"`, `"lte_auth_key"`)
    - `is_required` (Boolean, required): Whether or not the field is required to be completed when entering a new inventory item
    - `unique` (Boolean, required): Whether or not the contents of this field must be unique. This is only within the context of the model itself - e.g. if you create a field named 'Serial Number' for a model with ID 1 and mark it as unique, all items added that correspond to model ID 1 must have unique data in the 'Serial Number' field, but another field named 'Serial Number' on model ID 2 would not conflict.
    - `regexp` (String, optional): If type is set to regexp, this is the regular expression to run against data input into this field, in PCRE format. For example, you could validate a MAC address with "/^([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}$/". You can use https://regex101.com/ as a third party site to test/validate your regular expressions.
- **Success Response (201 Created)**:
    ```json
    {
       "id": 9,
       "name": "MAC Address",
       "type": "mac",
       "is_required": true,
       "unique": true,
       "regexp": null
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "You cannot enable the unique attribute on field MAC Address because there is duplicated data on existing items.",
         "status_code": 422
       }
    }
    ```

## Update model (PATCH)
- **Version**: 1.2.16
- **Endpoint**: `https://example.sonar.software/api/v1/inventory/models/:id`
- **Description**: Update a model
- **Parameters**:
    - `id` (Number, required): The ID of the model
    - `manufacturer_id` (Number, required): The internal id of the manufacturer
    - `name` (String, required): The name of the model
    - `inventory_model_category_id` (Number, required): The category that this model is part of
    - `https` (Boolean, optional): Whether or not links to IPs associated with this inventory model should use HTTPS or HTTP
    - `port` (Integer, optional): The TCP port to use for clickable links to IPs associated with this model
- **Success Response (200 OK)**:
    ```json
    {
       "id": 1,
       "name": "PMP450 5GHz AP",
       "manufacturer_id": 2,
       "inventory_model_category_id": 1,
       "https": false,
       "port": 432
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
