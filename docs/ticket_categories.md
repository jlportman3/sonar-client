# Ticket Categories Endpoints

## Create a new ticket category (POST)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_categories`

Description: Create a new ticket category.
#### Request Example
```json
{
  "name": "example"
}
```

```
Parameter
Field	Type	Description
name	String
A name for the ticket category

Success 200
Field	Type	Description
id	Number
The ID of the ticket category.

name	String
The name of the ticket category.

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "The porridge was too hot"
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
       "name": "The name is already in use."
     },
     "status_code": 422
   }
 }
```

## Delete ticket category (DELETE)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_categories/:id`

Description: Delete a ticket category.
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
The ID of the ticket category

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
A reason as to why the ticket category could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "Ticket category does not exist.",
         "status_code": 404
     }
 }
```

## Get all ticket categories (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_categories`

Description: Get all ticket categories
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
The ID of the ticket category.

name	String
The name of the ticket category.

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
    "id": 2,
    "name": "The porridge was too hot"
   },
   {
    "id": 3,
    "name": "The porridge was too cold"
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

## Get an individual ticket category (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_categories/:id`

Description: Get an individual ticket category
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
The ID of the ticket category

Success 200
Field	Type	Description
id	Number
The ID of the ticket category.

name	String
The name of the ticket category.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "The porridge was too hot"
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

## Update ticket category (PATCH)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/ticket_categories/:id`

Description: Update an existing ticket category.
#### Request Example
```json
{
  "id": 1,
  "name": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the ticket category.

nameoptional	String
The name of the ticket category.

Success 200
Field	Type	Description
id	Number
The ID of the ticket category.

name	String
The name of the ticket category.

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "The porridge was too hot"
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
Ticket Groups
```
