# DHCP Servers Endpoints

## Get all DHCP servers (GET)
Version: 0.4.0

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_servers`

Description: Get a list of DHCP servers.
#### Request Example
```json
{
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The ID of the DHCP server

ip_address	String
The IP address of the DHCP server

name	String
The name provided for the DHCP server

type	String
The type of DHCP server that this is

Allowed values: "mikrotik"

controls_all_pools	Boolean
If this DHCP server stores leases for all pools defined in Sonar or not

failures	Number
The number of failures writing leases that have been encountered since last rewrite/reset

device_status	Boolean
Whether or not the device is in a good status. Devices with a status of 'false' will not have leases written.

status_message	String
A message describing why the device is in a bad status, if device_status is false.

ip_pools	Array
If controls_all_pools is false, this will be an array of IP pool IDs that the server controls.

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 1,
      "ip_address": "192.168.1.51",
      "name": "MikroTik",
      "enabled": true,
      "type": "mikrotik",
      "controls_all_pools": true,
      "failures": 0,
      "device_status": true,
      "status_message": null,
      "ip_pools": []
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

## Get individual DHCP server (GET)
Version: 0.4.0

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_servers/:id`

Description: Get a single DHCP server
#### Request Example
```json
{
  "id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the DHCP server

Success 200
Field	Type	Description
id	Number
The ID of the DHCP server

ip_address	String
The IP address of the DHCP server

name	String
The name provided for the DHCP server

type	String
The type of DHCP server that this is

Allowed values: "mikrotik"

controls_all_pools	Boolean
If this DHCP server stores leases for all pools defined in Sonar or not

failures	Number
The number of failures writing leases that have been encountered since last rewrite/reset

device_status	Boolean
Whether or not the device is in a good status. Devices with a status of 'false' will not have leases written.

status_message	String
A message describing why the device is in a bad status, if device_status is false.

ip_pools	Array
If controls_all_pools is false, this will be an array of IP pool IDs that the server controls.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 1,
    "ip_address": "192.168.1.51",
    "name": "MikroTik",
    "enabled": true,
    "type": "mikrotik",
    "controls_all_pools": true,
    "failures": 0,
    "device_status": true,
    "status_message": null,
    "ip_pools": []
  }
}
DIDs
```
