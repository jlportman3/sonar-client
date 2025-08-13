# DIDs Endpoints

## Delete a DID (DELETE)
Version: 0.6.11

Endpoint: `https://example.sonar.software/api/v1/system/voice/dids/:id`

Description: Delete a DID
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
The ID of the DID

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
A reason as to why the DID could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "DID does not exist.",
         "status_code": 404
     }
 }
```

## Get all DIDs (GET)
Version: 0.6.11

Endpoint: `https://example.sonar.software/api/v1/system/voice/dids`

Description: Get all DIDs
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
The ID of the DID.

did	String
The DID

account_id	Integer
The account ID the DID is assigned to

service_id	Integer
The ID of the voice service the DID is associated with

rate_center_id	Integer
The ID of the rate center the DID is assigned to

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
     "id": 7,
     "did": "1234567892",
     "account_id": null,
     "service_id": null,
     "rate_center_id": 1
   },
   {
     "id": 8,
     "did": "1234567893",
     "account_id": null,
     "service_id": null,
     "rate_center_id": 1
   },
   {
     "id": 9,
     "did": "1111112022",
     "account_id": null,
     "service_id": null,
     "rate_center_id": 1
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

## Get an individual DID (GET)
Version: 0.6.11

Endpoint: `https://example.sonar.software/api/v1/system/voice/dids/:id`

Description: Get an individual DID
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
The ID of the DID

Success 200
Field	Type	Description
id	Number
The ID of the DID.

did	String
The DID

account_id	Integer
The account ID the DID is assigned to

service_id	Integer
The ID of the voice service the DID is associated with

rate_center_id	Integer
The ID of the rate center the DID is assigned to

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 8,
    "did": "1234567893",
    "account_id": null,
    "service_id": null,
    "rate_center_id": 1
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

## Mass add DIDs (GET)
Version: 0.6.11

Endpoint: `https://example.sonar.software/api/v1/system/voice/dids`

Description: This endpoint allows you to import a large quantity of DIDs at once. This is used to add new, available DIDs to Sonar. When importing very large quantities of DIDs, split them into batches and import 5000 at a time. Sonar currently only supports 10 digit DIDs.
#### Request Example
```json
{
  "dids": [],
  "rate_center_id": 1
}
```

```
Example usage:

{
  "dids": [
      "1234567890",
      "0987654321"
  ],
  "rate_center_id": 1
}
Parameter
Field	Type	Description
dids	Array
An array of ten digit DIDs

rate_center_id	Integer
The ID of the rate center to add these DIDs to

Success 200
Field	Type	Description
success	Boolean
Will be true if the DIDs were successfully added.

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
        "success": true
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
     "message": "Your submission contains duplicate DIDs. All DIDs must be unique."
     "status_code": 422
   }
 }
Data
```
