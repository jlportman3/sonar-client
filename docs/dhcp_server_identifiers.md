# DHCP Server Identifiers Endpoints

## Create a new DHCP server identifier (POST)
Version: 1.1.7

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_server_identifiers`

Description: Create a new DHCP server identifier.
#### Request Example
```json
{
  "name": "example",
  "ip_pool_ids": []
}
```

```
Parameter
Field	Type	Description
name	String
A name for the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success 200
Field	Type	Description
id	Integer
The ID of the DHCP server identifier.

name	String
The name of the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "Papaya",
    "ip_pool_ids": [
       1,
       3
    ]
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
422

Error-Response:
HTTP/1.1 422
 {
   "error": {
     "message": {
       "name": "The name must be unique."
     },
     "status_code": 422
   }
 }
```

## Delete a DHCP server identifier (DELETE)
Version: 1.1.7

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_server_identifiers/:id`

Description: Delete a DHCP server identifier
#### Request Example
```json
{
  "id": 1
}
```

```
Parameter
Field	Type	Description
id	Integer
The ID of the DHCP server identifier

Success 200
Field	Type	Description
success	Boolean
Will be true if deletion succeeded.

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "success": true
    }
}
Error 4xx
Name	Type	Description
message	String
A reason as to why the DHCP server identifier could not be deleted

status_code	Integer
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "DHCP server identifier does not exist.",
         "status_code": 404
     }
 }
```

## Get all DHCP server identifiers (GET)
Version: 1.1.7

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_server_identifiers`

Description: Get all DHCP server identifiers
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
limitoptional	Integer
The number of entries to return

pageoptional	Integer
The page of results to return

Success 200
Field	Type	Description
id	Integer
The ID of the DHCP server identifier.

name	String
The name of the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
      {
      "id": 2,
      "name": "Papaya",
      "ip_pool_ids": [
         1,
         3
      ]
    },
    {
      "id": 3,
      "name": "SteelBlue",
      "ip_pool_ids": [
         4,
         6,
         12
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

## Get an individual DHCP server identifier (GET)
Version: 1.1.7

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_server_identifiers/:id`

Description: Get an individual DHCP server identifier
#### Request Example
```json
{
  "id": 1
}
```

```
Parameter
Field	Type	Description
id	Integer
The ID of the DHCP server identifier

Success 200
Field	Type	Description
id	Integer
The ID of the DHCP server identifier.

name	String
The name of the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
     "id": 3,
     "name": "SteelBlue",
     "ip_pool_ids": [
        4,
        6,
        12
     ]
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
404

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
```

## Update DHCP server identifier (PATCH)
Version: 1.1.7

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/dhcp_server_identifiers/:id`

Description: Update an existing DHCP server identifier.
#### Request Example
```json
{
  "name": "example",
  "ip_pool_ids": []
}
```

```
Parameter
Field	Type	Description
name	String
A name for the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success 200
Field	Type	Description
id	Integer
The ID of the DHCP server identifier.

name	String
The name of the DHCP server identifier

ip_pool_ids	Array
An array of IP pool IDs that should be associated with this identifier

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
4xx

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
DHCP Servers
```
