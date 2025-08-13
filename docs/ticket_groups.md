# Ticket Groups Endpoints

## Create a new ticket group (POST)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_groups`

Description: Create a new ticket group.
#### Request Example
```json
{
  "name": "example",
  "private": true,
  "enabled": true,
  "users": []
}
```

```
Parameter
Field	Type	Description
name	String
A name for the ticket group

privateoptional	Boolean
Whether the group is private

Default value: false

enabledoptional	Boolean
Whether the group is enabled

Default value: true

usersoptional	Array
An array of user IDs that are associated with the group

Success 200
Field	Type	Description
id	Number
The ID of the ticket group.

name	String
The name of the ticket group

private	Boolean
Whether the group is private

enabled	Boolean
Whether the group is enabled

users	Array
An array of user IDs that are associated with the group

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "Some test name",
    "private": false,
    "enabled": true,
    "users": [
       1,
       2
    ]
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
       "name": "The name is already taken."
     },
     "status_code": 422
   }
 }
```

## Delete ticket group (DELETE)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_groups/:id`

Description: Delete a ticket group.
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
The ID of the ticket group

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
A reason as to why the ticket group could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "Ticket group does not exist.",
         "status_code": 404
     }
 }
```

## Get all ticket groups (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_groups`

Description: Get all tickets
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
The ID of the ticket group.

name	String
The name of the ticket group

private	Boolean
Whether the group is private

enabled	Boolean
Whether the group is enabled

users	Array
An array of user IDs that are associated with the group

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
     "id": 1,
     "name": "Test",
     "private": false,
     "enabled": true,
     "users": []
   },
   {
     "id": 4,
     "name": "Test yet again",
     "private": false,
     "enabled": true,
     "users": [
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

## Get an individual ticket group (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_groups/:id`

Description: Get an individual ticket group
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
The ID of the ticket group

Success 200
Field	Type	Description
id	Number
The ID of the ticket group.

name	String
The name of the ticket group

private	Boolean
Whether the group is private

enabled	Boolean
Whether the group is enabled

users	Array
An array of user IDs that are associated with the group

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
     "id": 1,
     "name": "Test",
     "private": false,
     "enabled": true,
     "users": []
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
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

## Update ticket group (PATCH)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_groups/:id`

Description: Update an existing ticket group.
#### Request Example
```json
{
  "name": "example",
  "private": true,
  "enabled": true,
  "users": []
}
```

```
Parameter
Field	Type	Description
nameoptional	String
A name for the ticket group

privateoptional	Boolean
Whether the group is private

Default value: false

enabledoptional	Boolean
Whether the group is enabled

Default value: true

usersoptional	Array
An array of user IDs that are associated with the group

Success 200
Field	Type	Description
id	Number
The ID of the ticket group.

name	String
The name of the ticket group

private	Boolean
Whether the group is private

enabled	Boolean
Whether the group is enabled

users	Array
An array of user IDs that are associated with the group

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
     "id": 1,
     "name": "Test",
     "private": false,
     "enabled": true,
     "users": []
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
Tickets
```
