# Account IP Addresses Endpoints

## Assign an IP to an account (POST)
Version: 1.2.16

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/ip_assignments`

Description: This endpoint allows you to assign IPv4/IPv6 assignments to an account, a RADIUS account on an account, an uninventoried MAC address, or an inventory model field on an account. Please see the documentation for more details about the different scenarios in which you would pick each entity.
#### Request Example
```json
{
  "id": 1,
  "subnet": "example",
  "assigned_entity": "example",
  "assigned_id": 1,
  "inventory_item_field_id": 1,
  "non_inventoried_mac_address": "example",
  "description": "example",
  "service_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the account

subnet	String
The subnet to assign to this entity, with a CIDR prefix, either IPv4 or IPv6. E.g. 192.168.100.1/32 or 2001:DB8::/64. It must fit within a customer/mixed subnet, or an IP pool. IP pool assignments can only be an IPv4 /32. If this is in a pool, and is assigned to a RADIUS account, it will be written as a Framed-IP-Address. Otherwise, it will be written as a Framed-Route.

assigned_entity	String
The entity to assign this to - the account directly, a RADIUS account on the account, an inventory item on the account, or a non-inventoried MAC address. You should only use the non-inventoried MAC address option to add an assignment to a device you do not own (e.g. a customer router.)

Allowed values: "accounts", "inventory_items", "radius_accounts", "non_inventoried_mac_addresses"

assigned_idoptional	Number
The ID of the entity referenced in assigned_entity. If assigned_entity is 'accounts' or 'non_inventoried_mac_addresses', this can be omitted.

inventory_item_field_idoptional	Number
If you are assigning this to an inventory item, supply the ID of the field that contains the MAC address (for DHCP assignment) or the IMSI (for LTE provisioning.) This is required if assigned_entity is "inventory_items"

non_inventoried_mac_addressoptional	String
If the assigned_entity is non_inventoried_mac_addresses, then this should be the MAC address you wish to add, in AA:AA:AA:AA:AA:AA format.

descriptionoptional	String
Optional description for the assignment

service_idoptional	Number
If the account has multiple data services, you can decide which data service to associate this IP assignment to. This will affect the address list it is in, if you have address list that are assigned by service. If the account only has one service, you can omit this and it will be automatically assigned. If this IP is being associated with a RADIUS account, this value will be ignored, as the data service is inherited from the RADIUS account.

Success 200
Field	Type	Description
id	Number
The ID of the ip assignment

subnet_id	Number
The ID of the subnet

subnet	String
The IPv4/IPv6 subnet

assigned_entity	String
The type of entity this is assigned to

assigned_id	Number
The ID of the entity this is assigned to

inventory_item_field_id	Number
If this IP is assigned to an inventory item MAC/IMSI, this will be the ID of the inventory item field. Otherwise, it will be null.

ip_pool_id	Number
If this falls into an IP pool, the ID of the pool, otherwise, null

account_id	Number
The ID of the account the IP is assigned to

service_id	Number
The ID of the service that the IP is associated with

non_inventoried_mac_address	String
If this is a non-inventoried MAC, the MAC will be shown here, null otherwise.

description	String
An optional description for the assignment

soft	Boolean
If this is true, this IP was assigned by Sonar learning about it from an external source (e.g. DHCP server, RADIUS accounting data.)

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
       "id": 8,
       "subnet_id": 1,
       "subnet": "192.168.100.17/32",
       "assigned_entity": "accounts",
       "assigned_id": 1,
       "inventory_item_field_id": null,
       "ip_pool_id": null,
       "account_id": 1,
       "service_id": 4,
       "non_inventoried_mac_address": null,
       "description": null,
       "soft": false
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
        "message": "The requested subnet overlaps the existing assignment of 192.168.100.17",
        "status_code": 422
      }
 }
```

## Delete IP assignment (DELETE)
Version: 0.4.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/ip_assignments/:ip_assignment_id`

Description: Delete an IP assignment.
#### Request Example
```json
{
  "id": 1,
  "ip_assignment_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the account

ip_assignment_id	Number
The ID of the IP assignment

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
A reason as to why the IP assignment could not be deleted

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": {
             "message": "You cannot delete this subnet, as other subnets are using it as their next hop."
         },
         "status_code": 422
     }
 }
```

## Get all IP assignments (GET)
Version: 1.2.16

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/ip_assignments`

Description: Retrieve a list of existing IP assignments on the account.
#### Request Example
```json
{
  "limit": 1,
  "page": 1,
  "id": 1
}
```

```
Parameter
Field	Type	Description
limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

id	Number
The ID of the account

Success 200
Field	Type	Description
id	Number
The ID of the ip assignment

subnet_id	Number
The ID of the subnet

subnet	String
The IPv4/IPv6 subnet

assigned_entity	String
The type of entity this is assigned to

assigned_id	Number
The ID of the entity this is assigned to

inventory_item_field_id	Number
If this IP is assigned to an inventory item MAC/IMSI, this will be the ID of the inventory item field. Otherwise, it will be null.

ip_pool_id	Number
If this falls into an IP pool, the ID of the pool, otherwise, null

account_id	Number
The ID of the account the IP is assigned to

service_id	Number
The ID of the service the IP is associated with

non_inventoried_mac_address	String
If this is a non-inventoried MAC, the MAC will be shown here, null otherwise.

description	String
An optional description for the assignment

soft	Boolean
If this is true, this IP was assigned by Sonar learning about it from an external source (e.g. DHCP server, RADIUS accounting data.)

Success-Response:
HTTP/1.1 200 OK
{
    "data": [
       {
         "id": 1,
         "subnet_id": 1,
         "subnet": "192.168.100.5",
         "assigned_entity": "accounts",
         "assigned_id": 1,
         "inventory_item_field_id": null,
         "ip_pool_id": null,
         "account_id": 1,
         "service_id": 4,
         "non_inventoried_mac_address": null,
         "description": null,
         "soft": false
       },
       {
         "id": 2,
         "subnet_id": 1,
         "subnet": "192.168.100.6",
         "assigned_entity": "accounts",
         "assigned_id": 1,
         "inventory_item_field_id": null,
         "ip_pool_id": null,
          "account_id": 1,
          "service_id": 4,
          "non_inventoried_mac_address": null,
          "description": null,
          "soft": false
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

## Get individual IP assignment (GET)
Version: 1.2.16

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/ip_assignments/:ip_assignment_id`

Description: Retrieve a specific IP assignment.
#### Request Example
```json
{
  "id": 1,
  "ip_assignment_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the account

ip_assignment_id	Number
The ID of the IP assignment.

Success 200
Field	Type	Description
id	Number
The ID of the ip assignment

subnet_id	Number
The ID of the subnet

subnet	String
The IPv4/IPv6 subnet

assigned_entity	String
The type of entity this is assigned to

assigned_id	Number
The ID of the entity this is assigned to

inventory_item_field_id	Number
If this IP is assigned to an inventory item MAC/IMSI, this will be the ID of the inventory item field. Otherwise, it will be null.

ip_pool_id	Number
If this falls into an IP pool, the ID of the pool, otherwise, null

account_id	Number
The ID of the account the IP is assigned to

service_id	Number
The ID of the service the IP is associated with

non_inventoried_mac_address	String
If this is a non-inventoried MAC, the MAC will be shown here, null otherwise.

description	String
An optional description for the assignment

soft	Boolean
If this is true, this IP was assigned by Sonar learning about it from an external source (e.g. DHCP server, RADIUS accounting data.)

Success-Response:
HTTP/1.1 200 OK
{
   {
     "id": 1,
     "subnet_id": 1,
     "subnet": "192.168.100.5",
     "assigned_entity": "accounts",
     "assigned_id": 1,
     "inventory_item_field_id": null,
     "ip_pool_id": null,
     "account_id": 1,
     "service_id": 3,
     "non_inventoried_mac_address": null,
     "description": null,
     "soft": false
   }
}
```

## Update IP assignment (PATCH)
Version: 1.2.16

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/ip_assignments/:ip_assignment_id`

Description: Update an existing IP assignment. If the assignment is on an account, only the subnet can be changed. If it is on a RADIUS account, only the subnet can be changed. If it is on an inventory item, the assigned_id, the subnet and inventory_item_field_id can be changed. To change the entity on an assignment other than an inventory item, delete the existing assignment and create a new one.
#### Request Example
```json
{
  "id": 1,
  "ip_assignment_id": 1,
  "subnet": "example",
  "assigned_id": 1,
  "inventory_item_field_id": 1,
  "non_inventoried_mac_address": "example",
  "description": "example",
  "service_id": 1,
  "make_permanent": true
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the account

ip_assignment_id	Number
The ID of the IP assignment

subnetoptional	String
The subnet to assign to this entity, with a CIDR prefix, either IPv4 or IPv6. E.g. 192.168.100.1/32 or 2001:DB8::/64. It must fit within a customer/mixed subnet, or an IP pool. IP pool assignments can only be an IPv4 /32s.

assigned_idoptional	Number
Only valid if this is an inventory item - this will allow you to move the IP to another inventory item. If the inventory item is not assigned to the same account as the existing assignment, it will be rejected. If the IP is currently assigned to an inventory_item_field_id and you supply this value and not inventory_item_field_id, the IP will be moved from the field level to the item level.

inventory_item_field_idoptional	Number
If you want to change the field ID, supply the ID of the field that contains the MAC address (for DHCP assignment) or the IMSI (for LTE provisioning.).

non_inventoried_mac_addressoptional	String
If the assigned_entity is non_inventoried_mac_addresses, then this should be the MAC address you wish to add, in AA:AA:AA:AA:AA:AA format. If this is omitted, an dthe IP is currently associated with an inventory item field, then the IP will be moved from an existing field down to the inventory item level.

descriptionoptional	String
An optional description for the assignment

service_idoptional	Number
If the account has multiple data services, you can decide which data service to associate this IP assignment to. This will affect the address list it is in, if you have address list that are assigned by service. If the account only has one service, you can omit this and it will be automatically assigned. If this IP is being associated with a RADIUS account, this value will be ignored, as the data service is inherited from the RADIUS account.

make_permanent	Boolean
If this is set to true, and the soft property of this IP assignment is currently true, then this will be changed to a permanent assignment.

Success 200
Field	Type	Description
id	Number
The ID of the ip assignment

subnet_id	Number
The ID of the subnet

subnet	String
The IPv4/IPv6 subnet

assigned_entity	String
The type of entity this is assigned to

assigned_id	Number
The ID of the entity this is assigned to

inventory_item_field_id	Number
If this IP is assigned to an inventory item MAC/IMSI, this will be the ID of the inventory item field. Otherwise, it will be null.

ip_pool_id	Number
If this falls into an IP pool, the ID of the pool, otherwise, null

account_id	Number
The ID of the account the IP is assigned to

service_id	Number
The ID of the service the IP is associated with

non_inventoried_mac_address	String
If this is a non-inventoried MAC, the MAC will be shown here, null otherwise.

description	String
An optional description for the assignment

soft	Boolean
If this is true, this IP was assigned by Sonar learning about it from an external source (e.g. DHCP server, RADIUS accounting data.)

Success-Response:
HTTP/1.1 200 OK
{
   {
     "id": 1,
     "subnet_id": 1,
     "subnet": "192.168.100.5",
     "assigned_entity": "accounts",
     "assigned_id": 1,
     "inventory_item_field_id": null,
     "ip_pool_id": null,
     "account_id": 1,
     "service_id": 4,
     "non_inventoried_mac_address": null,
     "description": null,
     "soft": false
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": {
             "subnet": "abcdefg is not a valid IP address."
         },
         "status_code": 422
     }
 }
Account Inventory
```
