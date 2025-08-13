# Monitoring Templates Endpoints

## Create a new SNMP OID threshold (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:snmp_oid_id/snmp_oid_thresholds`
- **Description**: Create a new SNMP OID threshold. Defining thresholds allows you to move a device into a threshold violating status when it crosses a certain boundary. For example, you can define a threshold that CPU usage must remain below 50% by using the operator lt and the value 50 on an SNMP OID that pulls CPU usage.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `snmp_oid_id` (Integer, required): The ID of the SNMP OID
    - `operator` (String, required): The operator to use when evaluating the current result against the threshold defined. (`"gt"`, `"gte"`, `"lt"`, `"lte"`, `"eq"`, `"neq"`)
    - `value` (String, required): The value to use for the threshold. If the value is a string, then only eq or neq are allowed as operators.
    - `time_period_in_minutes` (Integer, required): The amount of time that the threshold must be violated before it is triggered
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "operator": "lt",
        "value": 5,
        "time_period_in_minutes": 1
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "That SNMP OID does not exist.",
         "status_code": 404
       }
    }
    ```

## Create a new SNMP OID (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids`
- **Description**: Create a new SNMP OID.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template to add this OID to.
    - `name` (String, required): A name for the SNMP OID
    - `oid` (String, required): A numeric OID
    - `color` (String, optional): A hex color code for the SNMP OID. This will define the color used when graphing this OID.
    - `unit_of_measurement` (String, optional): The unit of measurement for the SNMP OID (e.g. bytes, %, Fahrenheit.)
    - `monitoring_graph_id` (Integer, optional): If you want to attach this SNMP OID to a specific monitoring graph, enter the ID here. If this is null, then this OID will be graphed by itself.
    - `auto_scale` (Boolean, optional): Whether or not to automatically scale this OID in thousands.
    - `display_as_table` (Boolean, optional): If this is true, this OID will not be graphed, and will instead be displayed in a table. This is also the default display for text based OIDs.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "oid": "1.2.3.4",
        "name": "Test",
        "color": "#3498db",
        "unit_of_measurement": null,
        "monitoring_graph_id": null,
        "auto_scale": false,
        "display_as_table": true
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "oid": "The oid has already been taken."
         },
         "status_code": 422
       }
    }
    ```

## Create a new monitoring graph (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/monitoring/monitoring_templates/:monitoring_template_id/monitoring_graphs`
- **Description**: Create a new monitoring graph. This is a graph definition that can be associated with multiple SNMP OIDs, in order to graph multiple results on a single graph.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template this graph will be available for
    - `name` (String, required): A name for the monitoring graph
    - `type` (String, required): The type of graph (`"line"`, `"bar"`, `"area"`)
    - `stacked` (Boolean, optional): Whether or not values should be stacked on the graph, or drawn independently
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "Aggregate Graph",
        "type": "line",
        "stacked": false
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "type": "The selected type is invalid."
         },
         "status_code": 422
       }
    }
    ```

## Create a new monitoring template (POST)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates`
- **Description**: Create a new monitoring template. A monitoring template is a template that defines items to monitor on an inventory model.
- **Parameters**:
    - `name` (String, required): A name for the monitoring template
    - `snmp_version` (Integer, optional): Default SNMP queries made using this template to this SNMP version. 2 is version 2c. (`1`, `2`, `3`)
    - `snmp_community` (String, optional): Default SNMP queries made using this template to use this SNMP community. If your snmp_version is 3, then this will be used as the SNMPv3 securityName.
    - `snmp3_sec_level` (String, optional): If you are using SNMPv3, this is the default security level (`"noAuthNoPriv"`, `"authNoPriv"`, `"authPriv"`)
    - `snmp3_auth_protocol` (String, optional): If you are using SNMPv3, this is the default authentication protocol (`"MD5"`, `"SHA"`)
    - `snmp3_auth_passphrase` (String, optional): If you are using SNMPv3, this is the default authentication pass phrase
    - `snmp3_priv_protocol` (String, optional): If you are using SNMPv3, this is the default privacy protocol (`"DES"`, `"AES"`)
    - `snmp3_priv_passphrase` (String, optional): If you are using SNMPv3, this is the default privacy passphrase
    - `snmp3_context_name` (String, optional): If you are using SNMPv3, this is the default context name
    - `snmp3_context_engine_id` (String, optional): If you are using SNMPv3, this is the default context EngineID
    - `icmp` (Boolean, optional): Whether or not to perform ICMP monitoring
    - `icmp_latency_threshold` (Integer, optional): If this is set, then a median latency above this value will put a device into warning status
    - `icmp_loss_threshold` (Integer, optional): If this is set, then a packet loss percentage above this value will put the device into warning status
    - `collect_interface_statistics` (Boolean, optional): Whether or not to collect interface statistics
    - `inventory_model_ids` (Array, optional): An array of inventory model IDs that should have this monitoring template applied to them.
- **Example Request Body**:
    ```json
    {
         "name": "Standard CPE Template",
         "snmp_version": 2,
         "snmp_community": "public",
         "icmp": false,
         "collect_interface_statistics": true,
         "inventory_model_ids": [
              1,
              2,
              5
         ]
    }
    ```
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Standard CPE Template",
        "snmp_version": 2,
        "snmp_community": "public",
        "snmp3_sec_level": null,
        "snmp3_auth_protocol": null,
        "snmp3_auth_passphrase": null,
        "snmp3_priv_protocol": null,
        "snmp3_priv_passphrase": null,
        "snmp3_context_name": null,
        "snmp3_context_engine_id": null,
        "icmp": false,
        "collect_interface_statistics": true,
        "inventory_model_ids": [
             1,
             2,
             5
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "icmp": "icmp must be a boolean."
         },
         "status_code": 422
       }
    }
    ```

## Delete a SNMP OID threshold (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:snmp_oid_id/snmp_oid_thresholds/:id`
- **Description**: Delete a SNMP OID threshold
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `snmp_oid_id` (Integer, required): The ID of the SNMP oid
    - `id` (Integer, required): The ID of the SNMP OID threshold
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
            "message": "SNMP OID threshold does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a SNMP OID (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:id`
- **Description**: Delete a SNMP OID
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `id` (Integer, required): The ID of the SNMP OID
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
            "message": "SNMP OID does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a monitoring graph (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/monitoring/monitoring_templates/:monitoring_template_id/monitoring_graphs/:id`
- **Description**: Delete a monitoring graph
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `id` (Integer, required): The ID of the monitoring graph
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
            "message": "monitoring graph does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a monitoring template (DELETE)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:id`
- **Description**: Delete a monitoring template
- **Parameters**:
    - `id` (Number, required): The ID of the monitoring template
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
            "message": "monitoring template does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all SNMP OID thresholds (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:snmp_oid_id/snmp_oid_thresholds`
- **Description**: Get all SNMP OID thresholds.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `snmp_oid_id` (Integer, required): The ID of the SNMP oid
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "operator": "lt",
          "value": 5,
          "time_period_in_minutes": 15
        },
        {
          "id": 1,
          "operator": "gte",
          "value": 15,
          "time_period_in_minutes": 1
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

## Get all SNMP OIDs for a template (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids`
- **Description**: Get all SNMP OIDs associated with a particular monitoring template.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "oid": "1.2.3.4",
          "name": "Test",
          "color": "#3498db",
          "unit_of_measurement": null,
          "monitoring_graph_id": 2,
          "auto_scale": true,
          "display_as_table": false
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

## Get all monitoring graphs (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/monitoring/monitoring_templates/:monitoring_template_id/monitoring_graphs`
- **Description**: Get all monitoring graphs
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "Aggregate Graph",
          "type": "line",
          "stacked": false
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

## Get all monitoring templates (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates`
- **Description**: Get all monitoring templates
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 5,
          "name": "My Test Template",
          "snmp_version": 1,
          "snmp_community": "private",
          "snmp3_sec_level": null,
          "snmp3_auth_protocol": null,
          "snmp3_auth_passphrase": null,
          "snmp3_priv_protocol": null,
          "snmp3_priv_passphrase": null,
          "snmp3_context_name": null,
          "snmp3_context_engine_id": null,
          "icmp": false,
          "icmp_latency_threshold": null,
          "icmp_loss_threshold": null,
          "collect_interface_statistics": false,
          "inventory_model_ids": [
            3
          ]
        },
        {
          "id": 14,
          "name": "MikroTik Probe",
          "snmp_version": 2,
          "snmp_community": "public",
          "snmp3_sec_level": null,
          "snmp3_auth_protocol": null,
          "snmp3_auth_passphrase": null,
          "snmp3_priv_protocol": null,
          "snmp3_priv_passphrase": null,
          "snmp3_context_name": null,
          "snmp3_context_engine_id": null,
          "icmp": true,
          "icmp_latency_threshold": null,
          "icmp_loss_threshold": null,
          "collect_interface_statistics": false,
          "inventory_model_ids": [
               1
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

## Get an individual SNMP OID threshold (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:snmp_oid_id/snmp_oid_thresholds/:id`
- **Description**: Get an individual SNMP OID threshold.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `snmp_oid_id` (Integer, required): The ID of the SNMP oid
    - `id` (Integer, required): The ID of the SNMP OID threshold
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "operator": "lt",
        "value": 5,
        "time_period_in_minutes": 12
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

## Get an individual SNMP OID (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:id`
- **Description**: Get an individual SNMP OID
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `id` (Integer, required): The ID of the SNMP OID
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
          "id": 2,
          "oid": "1.2.3.4",
          "name": "Test",
          "color": "#3498db",
          "unit_of_measurement": null,
          "monitoring_graph_id": 2,
          "auto_scale": true,
          "display_as_table": false
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

## Get an individual monitoring graph (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/monitoring/monitoring_templates/:monitoring_template_id/monitoring_graphs/:id`
- **Description**: Get an individual monitoring graph
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `id` (Integer, required): The ID of the monitoring graph
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "Aggregate Graph",
        "type": "line",
        "stacked": false
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

## Get an individual monitoring template (GET)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:id`
- **Description**: Get an individual monitoring template
- **Parameters**:
    - `id` (Number, required): The ID of the monitoring template
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "MikroTik Probe",
        "snmp_version": 0,
        "snmp_community": null,
        "snmp3_sec_level": null,
        "snmp3_auth_protocol": null,
        "snmp3_auth_passphrase": null,
        "snmp3_priv_protocol": null,
        "snmp3_priv_passphrase": null,
        "snmp3_context_name": null,
        "snmp3_context_engine_id": null,
        "icmp": true,
        "icmp_latency_threshold": null,
        "icmp_loss_threshold": null,
        "collect_interface_statistics": false,
        "inventory_model_ids": []
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

## Update SNMP OID threshold (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:snmp_oid_id/snmp_oid_thresholds/:id`
- **Description**: Update an existing SNMP OID threshold.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `snmp_oid_id` (Integer, required): The ID of the SNMP oid
    - `id` (Integer, required): The ID of the SNMP OID threshold
    - `operator` (String, optional): The operator to use when evaluating the current result against the threshold defined. (`"gt"`, `"gte"`, `"lt"`, `"lte"`, `"eq"`, `"neq"`)
    - `value` (String, optional): The value to use for the threshold. If the value is a string, then only eq or neq are allowed as operators.
    - `time_period_in_minutes` (Integer, optional): The amount of time that the threshold must be violated before it is triggered
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "operator": "lt",
        "value": 5,
        "time_period_in_minutes": 15
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

## Update SNMP OID (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:monitoring_template_id/snmp_oids/:id`
- **Description**: Update an existing SNMP OID.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template to add this OID to.
    - `id` (Integer, required): The ID of the SNMP OID
    - `name` (String, optional): A name for the SNMP OID
    - `oid` (String, optional): A numeric OID
    - `color` (String, optional): A hex color code for the SNMP OID. This will define the color used when graphing this OID.
    - `unit_of_measurement` (String, optional): The unit of measurement for the SNMP OID (e.g. bytes, %, Fahrenheit.)
    - `monitoring_graph_id` (Integer, optional): If you want to attach this SNMP OID to a specific monitoring graph, enter the ID here. If this is null, then this OID will be graphed by itself.
    - `auto_scale` (Boolean, optional): Whether or not to automatically scale this OID in thousands.
    - `display_as_table` (Boolean, optional): If this is true, this OID will not be graphed, and will instead be displayed in a table. This is also the default display for text based OIDs.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "oid": "1.2.3.4",
        "name": "Test",
        "color": "#3498db",
        "unit_of_measurement": null,
        "monitoring_graph_id": null,
        "auto_scale": false,
        "display_as_table": true
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

## Update monitoring graph (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/monitoring/monitoring_templates/:monitoring_template_id/monitoring_graphs/:id`
- **Description**: Update an existing monitoring graph.
- **Parameters**:
    - `monitoring_template_id` (Integer, required): The ID of the monitoring template
    - `id` (Integer, required): The ID of the monitoring graph
    - `name` (String, optional): A name for the monitoring graph
    - `type` (String, optional): The type of graph (`"line"`, `"bar"`, `"area"`)
    - `stacked` (Boolean, optional): Whether or not values should be stacked on the graph, or drawn independently
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "Aggregate Graph",
        "type": "line",
        "stacked": false
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

## Update monitoring template (PATCH)
- **Version**: 1.0.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/monitoring/monitoring_templates/:id`
- **Description**: Update an existing monitoring template.
- **Parameters**:
    - `id` (Integer, required): The ID of the monitoring template
    - `name` (String, optional): A name for the monitoring template
    - `snmp_version` (Integer, optional): Default SNMP queries made using this template to this SNMP version. 2 is version 2c. (`1`, `2`, `3`)
    - `snmp_community` (String, optional): Default SNMP queries made using this template to use this SNMP community. If your snmp_version is 3, then this will be used as the SNMPv3 securityName.
    - `snmp3_sec_level` (String, optional): If you are using SNMPv3, this is the default security level (`"noAuthNoPriv"`, `"authNoPriv"`, `"authPriv"`)
    - `snmp3_auth_protocol` (String, optional): If you are using SNMPv3, this is the default authentication protocol (`"MD5"`, `"SHA"`)
    - `snmp3_auth_passphrase` (String, optional): If you are using SNMPv3, this is the default authentication pass phrase
    - `snmp3_priv_protocol` (String, optional): If you are using SNMPv3, this is the default privacy protocol (`"DES"`, `"AES"`)
    - `snmp3_priv_passphrase` (String, optional): If you are using SNMPv3, this is the default privacy passphrase
    - `snmp3_context_name` (String, optional): If you are using SNMPv3, this is the default context name
    - `snmp3_context_engine_id` (String, optional): If you are using SNMPv3, this is the default context EngineID
    - `icmp` (Boolean, optional): Whether or not to perform ICMP monitoring
    - `icmp_latency_threshold` (Integer, optional): If this is set, then a median latency above this value will put a device into warning status
    - `icmp_loss_threshold` (Integer, optional): If this is set, then a packet loss percentage above this value will put the device into warning status
    - `collect_interface_statistics` (Boolean, optional): Whether or not to collect interface statistics
    - `inventory_model_ids` (Array, optional): An array of inventory model IDs that should have this monitoring template applied to them.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "MikroTik Probe",
        "snmp_version": 2,
        "snmp_community": "somerandomcommunity",
        "snmp3_sec_level": null,
        "snmp3_auth_protocol": null,
        "snmp3_auth_passphrase": null,
        "snmp3_priv_protocol": null,
        "snmp3_priv_passphrase": null,
        "snmp3_context_name": null,
        "snmp3_context_engine_id": null,
        "icmp": true,
        "icmp_latency_threshold": null,
        "icmp_loss_threshold": null,
        "collect_interface_statistics": false,
        "inventory_model_ids": []
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
