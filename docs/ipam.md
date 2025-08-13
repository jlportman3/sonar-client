# IPAM Endpoints

## Lookup an individual IP address (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/ip_lookup?ip=:ip`
- **Description**: Lookup an individual IP address
- **Parameters**:
    - `ip` (String, required): The IP address to lookup. Can be an IPv4/IPv6 address or subnet.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "existing_assignment": {
          "subnet": "10.0.0.2",
          "account_id": 48,
          "soft": false,
          "subnet_name": "10.0.0.0/8",
          "ip_pool_name": "Test",
          "account_name": "West Allis Prep School"
        },
        "historical_assignments": [
          {
            "subnet": "10.0.0.2",
            "removed_datetime": "2017-02-04 15:57:22",
            "assigned_datetime": "2017-02-04 15:54:06",
            "soft": false,
            "name": "Jim Patient",
            "account_id": 1,
            "from": "Feb 4, 2017 09:54:06",
            "to": "Feb 4, 2017 09:57:22"
          }
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

## Create a new IP pool (POST)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools`
- **Description**: Create a new IP pool. IP pools can only be created in IPv4 subnets.
- **Parameters**:
    - `supernet_id` (Integer, required): The ID of the supernet
    - `subnet_id` (Integer, required): The ID of the subnet
    - `name` (String, required): A descriptive name for the IP pool
    - `start` (String, required): The starting IP for the IP pool
    - `end` (String, required): The ending IP for the IP pool
    - `dhcp_servers` (Array, optional): An array of DHCP server IDs. These are DHCP servers that are not set to control all pools and are specifically associated with this IP pool. Any IDs included here that have 'control_all_pools' set to true will cause the call to fail.
    - `dhcp_server_identifier_id` (Integer, optional): The ID of a DHCP server identifier to use for this pool. Set to null to use no identifier.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "My first IP pool",
        "start": "192.168.100.21",
        "end": "192.168.100.25",
        "dhcp_servers": [
               1,
               2
         ],
         "dhcp_server_identifier_id": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "The pool does not fit within the subnet.",
         "status_code": 422
       }
    }
    ```

## Create a new subnet (POST)
- **Version**: 1.0.5
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id/subnets`
- **Description**: Create a new subnet. A subnet is a subdivided piece of a supernet, and can be used to assign IPs to various entities within Sonar, or used to build pools.
- **Parameters**:
    - `name` (String, required): A descriptive name for the subnet.
    - `subnet` (String, required): The network address and CIDR prefix (e.g. 10.0.0.0/8)
    - `type` (String, required): The type of subnet this is. (`"customer"`, `"infrastructure"`, `"reserved"`, `"mixed"`)
    - `network_site_id` (Number, required): The ID of the network site that this subnet is deployed from.
    - `inline_devices` (Array, optional): An array of inline device IDs that should provide controls for this subnet. You can only submit IDs here for inline devices that do not have the 'Controls all subnets' value enabled.
    - `poller_id` (Number, optional): The ID of the poller responsible for this subnet
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "My first Subnet!",
        "subnet": "192.168.100.0/27",
        "type": "customer",
        "network_site_id": 1,
        "supernet_id": 4,
        "inline_devices": [
           1
        ],
        "poller_id": 1
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "Your submission overlaps subnet My first Subnet!.",
         "status_code": 422
       }
    }
    ```

## Create a new supernet (POST)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets`
- **Description**: Create a new supernet. A supernet is a top level subnet (all of your defined subnets are contained within a supernet.) For example, if you want to define the subnet 10.0.0.0/24 to use in your network, you would want to define a supernet at least as large as that in order to contain it.
- **Parameters**:
    - `name` (String, required): A descriptive name for the supernet
    - `subnet` (String, required): The network address and CIDR prefix (e.g. 10.0.0.0/8)
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 6,
        "name": "My second SUPERNET!",
        "subnet": "172.16.0.0/23"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "Your submission overlaps supernet My first SUPERNET!.",
         "status_code": 422
       }
    }
    ```

## Delete IP pool (DELETE)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools/:ip_pool_id`
- **Description**: Delete an IP pool.
- **Parameters**:
    - `supernet_id` (Integer, required): The ID of the supernet
    - `subnet_id` (Integer, required): The ID of the subnet
    - `ip_pool_id` (Integer, required): The ID of the IP pool
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
                "message": "You cannot delete a pool that contains IP assignments."
            },
            "status_code": 422
        }
    }
    ```

## Delete subnet (DELETE)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id/subnets/:subnet_id`
- **Description**: Delete a subnet. You cannot delete a subnet that has any IP pools or IP assignments associated with it, the relations must be deleted first.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
    - `subnet_id` (Number, required): The ID of the subnet
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
                "message": "This subnet cannot be deleted as it has IP pools associated with it."
            },
            "status_code": 422
        }
    }
    ```

## Delete supernet (DELETE)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id`
- **Description**: Delete a supernet. You cannot delete a supernet that has any subnets associated with it, the subnets must be deleted first.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
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
                "message": "Supernet cannot be deleted as it contains subnets."
            },
            "status_code": 422
        }
    }
    ```

## Get all IP pools (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools`
- **Description**: Get a list of IP pools contained within a subnet.
- **Parameters**:
    - `supernet_id` (Integer, required): The ID of the supernet
    - `subnet_id` (Integer, required): The ID of the subnet
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "My first IP Pool",
          "start": "192.168.100.10",
          "end": "192.168.100.200",
          "dhcp_servers": [
               1,
               2
          ],
          "dhcp_server_identifier_id": null
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

## Get all subnets (GET)
- **Version**: 1.0.5
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id/subnets`
- **Description**: Get a list of subnets contained within a supernet.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "My first Subnet!",
          "subnet": "192.168.100.0/27",
          "type": "customer",
          "network_site_id": 1,
          "supernet_id": 4,
          "inline_devices": [
               1
           ],
           "poller_id": null
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

## Get all supernets (GET)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets`
- **Description**: Get a list of supernets. A supernet is a top level subnet (all of your defined subnets are contained within a supernet.) For example, if you want to define the subnet 10.0.0.0/24 to use in your network, you would want to define a supernet at least as large as that in order to contain it.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 4,
          "name": "My first IPv6 Supernet!",
          "subnet": "2001::/48"
        },
        {
          "id": 5,
          "name": "My Second Supernet",
          "subnet": "10.0.0.0/8"
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

## Get individual IP pool (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools/:ip_pool_id`
- **Description**: Get an individual IP pool.
- **Parameters**:
    - `supernet_id` (Integer, required): The ID of the supernet
    - `subnet_id` (Integer, required): The ID of the subnet
    - `ip_pool_id` (Integer, required): The ID of the IP pool
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "My first IP pool",
        "start": "192.168.100.21",
        "end": "192.168.100.25",
        "dhcp_servers": [
           1,
           2
         ],
         "dhcp_server_identifier_id": 1
      }
    }
    ```

## Get individual subnet (GET)
- **Version**: 1.0.5
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id/subnets/:subnet_id`
- **Description**: Get an individual subnet.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
    - `subnet_id` (Number, required): The ID of the subnet
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "My first Subnet!",
        "subnet": "192.168.100.0/27",
        "type": "customer",
        "network_site_id": 1,
        "supernet_id": 4,
        "inline_devices": [],
        "poller_id": 12
      }
    }
    ```

## Get individual supernet (GET)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id`
- **Description**: Get an individual supernet.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "My Second Supernet",
        "subnet": "10.0.0.0/8"
      }
    }
    ```

## Update IP pool (PATCH)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools/:ip_pool_id`
- **Description**: Update an IP pool.
- **Parameters**:
    - `supernet_id` (Integer, required): The ID of the supernet
    - `subnet_id` (Integer, required): The ID of the subnet
    - `ip_pool_id` (Integer, required): The ID of the IP pool
    - `name` (String, required): A descriptive name for the IP pool
    - `start` (String, required): The starting IP for the IP pool
    - `end` (String, required): The ending IP for the IP pool
    - `dhcp_servers` (Array, optional): An array of DHCP server IDs. These are DHCP servers that are not set to control all pools and are specifically associated with this IP pool. Any IDs included here that have 'control_all_pools' set to true will cause the call to fail.
    - `dhcp_server_identifier_id` (Integer, optional): The ID of a DHCP server identifier to use for this pool. Set to null to use no identifier.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "My first IP pool",
        "start": "192.168.100.24",
        "end": "192.168.100.25",
        "dhcp_servers": [
               1,
               2
         ],
         "dhcp_server_identifier_id": 4
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "subnet": "Pool cannot be set to dynamic, as there are existing assignments in the space this pool is attempting to occupy."
            },
            "status_code": 422
        }
    }
    ```

## Update a dynamic IP assignment (POST)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/dynamic_ip_assignment`
- **Description**: This endpoint is deprecated and should not be used. Please visit https://github.com/sonarsoftware/dhcp_batcher for information on our new dynamic DHCP tool.
- **Parameters**:
    - `expired` (Boolean, optional): If this submission is notify that is a lease is expiring, set this to true.
    - `ip_address` (String, required): The IP address that is being assigned. You can also submit this as a subnet with a CIDR prefix if this is a larger assignment. While this will accept both IPv4 and IPv6, you would need some external method of figuring out a link between the IPv6 address and a MAC for association within Sonar, so this is likely to be difficult.
    - `mac_address` (String, required): The MAC address this IP is assigned to, in XX:XX:XX:XX:XX:XX format. The MAC submitted here should be the MAC you want Sonar to search for in order to find a match, so this does not necessarily need to be the 'real' MAC, but could instead be the MAC of the CPE or something similar.
    - `reference` (String, optional): If you would like to store additional information about this assignment for display in Sonar, submit it here as JSON. Sonar will parse the JSON to use for later display. For example, if you wanted to submit the hostname for the reservation, send something like `{ "Hostname": "Alex's Laptop" }`
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "account_id": 5,
        "ip_address": "192.168.100.12",
        "assigned_time": "2016-01-01 12:34:45",
        "expired_time": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "ip_address": "Invalid IP address."
            },
            "status_code": 422
        }
    }
    ```

## Update subnet (PATCH)
- **Version**: 1.0.5
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id/subnets/:subnet_id`
- **Description**: Update a subnet.
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
    - `subnet_id` (Number, required): The ID of the subnet
    - `name` (String, optional): A descriptive name for the subnet.
    - `subnet` (String, optional): The network address and CIDR prefix (e.g. 10.0.0.0/8)
    - `type` (String, optional): The type of subnet this is. (`"customer"`, `"infrastructure"`, `"reserved"`, `"mixed"`)
    - `network_site_id` (Number, optional): The ID of the network site that this subnet is deployed from.
    - `inline_devices` (Array, optional): An array of inline device IDs that should provide controls for this subnet. You can only submit IDs here for inline devices that do not have the 'Controls all subnets' value enabled.
    - `poller_id` (Number, optional): The ID of the poller responsible for this subnet
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "My first Subnet Redux",
        "subnet": "192.168.100.0/28",
        "type": "customer",
        "network_site_id": 1,
        "supernet_id": 4,
        "inline_devices": [],
        "poller_id": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "subnet": "Your new subnet is too small to contain all existing IP pools linked to this subnet."
            },
            "status_code": 422
        }
    }
    ```

## Update supernet (PATCH)
- **Version**: 0.4.0
- **Endpoint**: `https://example.sonar.software/api/v1/network/ipam/supernets/:id`
- **Description**: Update a supernet
- **Parameters**:
    - `id` (Number, required): The ID of the supernet
    - `name` (String, required): The name of the supernet
    - `subnet` (String, required): The supernet network address and CIDR prefix.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "My Second Supernet",
        "subnet": "10.0.0.0/8"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "subnet": "Your new subnet is too small to contain all existing subnets linked to this supernet."
            },
            "status_code": 422
        }
    }
    ```
```
