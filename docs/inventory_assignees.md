# Inventory Assignees Endpoints

## Create a new generic inventory assignee (POST)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/generic_inventory_assignees`

Description: Create a new generic inventory assignee.
#### Request Example
```json
{
  "name": "example",
  "notes": "example"
}
```

```
Parameter
Field	Type	Description
name	String
A unique name for the assignee

notesoptional	String
Some notes to describe the assignee

Success 200
Field	Type	Description
id	Number
The internal id of the manufacturer

name	String
The name of the manufacturer

notes	String
Some notes to describe the assignee

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "Mike's House of Installs",
    "notes": "If you give routers to Mike, put them here!"
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
             "name": "The name has already been taken.",
         },
         "status_code": 422
     }
 }
```

## Create a new location (POST)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/inventory_locations`

Description: Create a new physical inventory location.
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
A unique name for the location

Success 200
Field	Type	Description
id	Number
The internal id of the location

name	String
The name of the location

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
        "id": 35,
        "name": "Warehouse 4A-B6-234"
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
             "name": "The name has already been taken.",
         },
         "status_code": 422
     }
 }
```

## Create a new vehicle (POST)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/vehicles`

Description: Create a new vehicle. Vehicles are a type of location inventory can be stored in.
#### Request Example
```json
{
  "name": "example",
  "manufacturer": "example",
  "model": "example",
  "year": 1,
  "license_plate": "example",
  "vin": "example"
}
```

```
Parameter
Field	Type	Description
name	String
The unique name of the vehicle

manufactureroptional	String
The vehicle manufacturer

modeloptional	String
The vehicle model

yearoptional	Number
The year the vehicle was constructed

license_plateoptional	String
The license plate/number plate of the vehicle

vinoptional	String
The VIN (vehicle identification number) of the vehicle

Success 200
Field	Type	Description
id	Number
The internal id of the vehicle

name	String
The name of the vehicle

manufacturer	String
The vehicle manufacturer

model	String
The vehicle model

year	Number
The year the vehicle was constructed

license_plate	String
The license plate/number plate of the vehicle

vin	String
The VIN (vehicle identification number) of the vehicle

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
          "id": 1,
          "name": "Bob's Work Van",
          "manufacturer": "Fjord",
          "model": "G150",
          "year": 2014,
          "license_plate": "ABC123",
          "vin": "1231231234"
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
             "name": "The name has already been taken.",
         },
         "status_code": 422
     }
 }
```

## Delete generic inventory assignee (DELETE)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/generic_inventory_assignees/:id`

Description: Delete a generic inventory assignee
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
The ID of the generic inventory assignee

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
A reason as to why the generic inventory assignee could not be deleted

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": "Assignee cannot be deleted as inventory items are stored in it.",
         "status_code": 422
     }
 }
```

## Delete location (DELETE)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/inventory_locations/:id`

Description: Delete an inventory location
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
The ID of the location

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
A reason as to why the location could not be deleted

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": "Location cannot be deleted as inventory items are stored in it.",
         "status_code": 422
     }
 }
```

## Delete vehicle (DELETE)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/vehicles/:id`

Description: Delete a vehicle
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
The ID of the vehicle

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
A reason as to why the vehicle could not be deleted

status_code	Number
422

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": "Vehicle cannot be deleted as inventory items are stored in it.",
         "status_code": 422
     }
 }
```

## Get all generic inventory assignees (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/generic_inventory_assignees`

Description: Get a list of generic inventory assignees. A generic inventory assignee is used when nothing else matches - for example, you may use this to assign inventory to contractors.
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
The internal id of the manufacturer

name	String
The name of the manufacturer

notes	String
Some notes to describe the assignee

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 1,
      "name": "Jim's Sloppy Contracting Service",
      "notes": "This is the place to assign inventory that we give to this contractor!"
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

## Get all locations (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/inventory_locations`

Description: Get a list of physical locations that inventory items can be stored at.
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
The internal id of the location

name	String
The name of the location

Success-Response:
HTTP/1.1 200 OK
{
    "data": [
       {
            "id": 35,
            "name": "Benjamin's Big Red Barn"
       },
       {
           "id": 36,
           "name": "Main Warehouse"
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

## Get all vehicles (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/vehicles`

Description: Get a list of vehicles. Vehicles are a type of location inventory can be stored in.
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
The internal id of the vehicle

name	String
The name of the vehicle

manufacturer	String
The vehicle manufacturer

model	String
The vehicle model

year	Number
The year the vehicle was constructed

license_plate	String
The license plate/number plate of the vehicle

vin	String
The VIN (vehicle identification number) of the vehicle

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 1,
      "name": "Bob's Work Van",
      "manufacturer": "Fjord",
      "model": "G150",
      "year": 2014,
      "license_plate": "ABC123",
      "vin": "1231231234"
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

## Get individual generic inventory assignee (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/generic_inventory_assignees/:id`

Description: Get an individual generic assignee.
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
The ID of the assignee

Success 200
Field	Type	Description
id	Number
The internal id of the manufacturer

name	String
The name of the manufacturer

notes	String
Some notes to describe the assignee

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "Mike's House of Installs",
    "notes": "If you give routers to Mike, put them here!"
  }
}
```

## Get individual location (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/inventory_locations/:id`

Description: Get an individual physical inventory location.
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
The ID of the location

Success 200
Field	Type	Description
id	Number
The internal id of the location

name	String
The name of the location

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
       "id": 1,
       "name": "Warehouse"
   }
}
```

## Get individual vehicle (GET)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/vehicles/:id`

Description: Get an individual vehicle.
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
The ID of the vehicle

Success 200
Field	Type	Description
id	Number
The internal id of the vehicle

name	String
The name of the vehicle

manufacturer	String
The vehicle manufacturer

model	String
The vehicle model

year	Number
The year the vehicle was constructed

license_plate	String
The license plate/number plate of the vehicle

vin	String
The VIN (vehicle identification number) of the vehicle

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
        "id": 1,
        "name": "Bob's Work Van",
        "manufacturer": "Fjord",
        "model": "G150",
        "year": 2014,
        "license_plate": "ABC123",
        "vin": "1231231234"
  }
}
```

## Update generic inventory assignee (PATCH)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/generic_inventory_assignees/:id`

Description: Update a generic inventory assignee.
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "notes": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the assignee

nameoptional	String
A unique name for the assignee

notesoptional	String
Some notes to describe the assignee

Success 200
Field	Type	Description
id	Number
The internal id of the manufacturer

name	String
The name of the manufacturer

notes	String
Some notes to describe the assignee

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "Michael's House of Installs",
    "notes": "If you give routers to Mike, put them here! Don't call him Mike."
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
             "name": "The name has already been taken."
         },
         "status_code": 422
     }
 }
```

## Update location (PATCH)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/inventory_locations/:id`

Description: Update a physical inventory location
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
The ID of the location

name	String
The name of the location

Success 200
Field	Type	Description
id	Number
The internal id of the location

name	String
The name of the location

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
       "id": 1,
       "name": "Not the Warehouse"
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
             "name": "The name has already been taken."
         },
         "status_code": 422
     }
 }
```

## Update vehicle (PATCH)
Version: 0.3.0

Endpoint: `https://example.sonar.software/api/v1/inventory/vehicles/:id`

Description: Update a vehicle
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "manufacturer": "example",
  "model": "example",
  "year": 1,
  "license_plate": "example",
  "vin": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the vehicle

nameoptional	String
The unique name of the vehicle

manufactureroptional	String
The vehicle manufacturer

modeloptional	String
The vehicle model

yearoptional	Number
The year the vehicle was constructed

license_plateoptional	String
The license plate/number plate of the vehicle

vinoptional	String
The VIN (vehicle identification number) of the vehicle

Success 200
Field	Type	Description
id	Number
The internal id of the vehicle

name	String
The name of the vehicle

manufacturer	String
The vehicle manufacturer

model	String
The vehicle model

year	Number
The year the vehicle was constructed

license_plate	String
The license plate/number plate of the vehicle

vin	String
The VIN (vehicle identification number) of the vehicle

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 1,
    "name": "Bill's Work Van",
    "manufacturer": "Dadge",
    "model": "Rum",
    "year": "2014",
    "license_plate": "ABC123",
    "vin": "1231231234"
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
             "name": "The name has already been taken."
         },
         "status_code": 422
     }
 }
Inventory Depletion Thresholds
```
