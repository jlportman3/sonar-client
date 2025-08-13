# Account Addresses Endpoints

## Create account address (POST)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/addresses`

Description: Create a new account address
#### Request Example
```json
{
  "account_id": 1,
  "line1": "example",
  "line2": "example",
  "city": "example",
  "state": "example",
  "county": "example",
  "zip": "example",
  "country": "example",
  "latitude": 0.0,
  "longitude": 0.0,
  "address_type_id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account to add the address to

line1	String
The first line of the address

line2optional	String
The second line of the address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision. You can obtain a valid list from _data/subdivisions/:country

county	String
A valid county for the subdivision obtained from /_data/counties. This is only used for US states and should be null for any other country.

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitude	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_id	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success 200
Field	Type	Description
id	Number
The internal ID of the address

line1	String
The first line of the address

line2	String
The second line of the address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision

county	String
The county, for US addresses

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitude	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_id	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
        "id": 3,
        "line1": "555 Packers Ln",
        "line2": "Suite 1337",
        "city": "Green Bay",
        "state": "Wisconsin",
        "county": "Green Bay Co.",
        "zip": "54332",
        "country": "US",
        "latitude": null,
        "longitude": null,
        "address_type_id": 2
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
             "address_type_id": "The selected address type id is not valid.",
         },
         "status_code": 422
     }
 }
```

## Delete account address (DELETE)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/addresses/:address_id`

Description: Delete an account address
#### Request Example
```json
{
  "account_id": 1,
  "address_id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

address_id	Number
The ID of the address

Success 200
Field	Type	Description
message	String
A message stating that the deletion was successful.

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
A reason as to why the address could not be deleted

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
```

## Get all account addresses (GET)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/addresses`

Description: Get a list of the addresses for account ID :account_id
#### Request Example
```json
{
  "account_id": 1,
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The internal ID of the address

line1	String
The first line of the address

line2	String
The second line of the address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision

county	String
A valid county for the subdivision obtained from /_data/counties, null if not a US address

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitude	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_id	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success-Response:
 HTTP/1.1 200 OK
 {
    "data": [
        {
            "line1": "12345 Some Ln",
            "line2": "",
            "city": "West Allis",
            "state": "Wisconsin",
            "county": "Milwaukee Co.",
            "zip": "53226",
            "country": "US",
            "latitude": null,
            "longitude": null,
            "address_type_id": 1
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

## Get individual account address (GET)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/addresses/:address_id`

Description: Get an individual account address.
#### Request Example
```json
{
  "account_id": 1,
  "address_id": 1,
  "county": "example"
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

address_id	Number
The ID of the address

county	String
A valid county for the subdivision obtained from /_data/counties, null if not a US address

Success 200
Field	Type	Description
id	Number
The internal ID of the address

line1	String
The first line of the address

line2	String
The second line of the address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitude	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_id	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success-Response:
HTTP/1.1 200 OK
{
    "data":
    {
       "line1": "12345 Some Ln",
       "line2": "",
       "city": "West Allis",
       "state": "Wisconsin",
       "county": "Milwaukee Co.",
       "zip": "53226",
       "country": "US",
       "latitude": null,
       "longitude": null,
       "address_type_id": 1
    }
}
```

## Update account address (PATCH)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/addresses/:address_id`

Description: Update an account address.
#### Request Example
```json
{
  "account_id": 1,
  "address_id": 1,
  "line1": "example",
  "line2": "example",
  "city": "example",
  "state": "example",
  "county": "example",
  "zip": "example",
  "country": "example",
  "latitude": 0.0,
  "longitude": 0.0,
  "address_type_id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account to update the address on

address_id	Number
The ID of the address

line1optional	String
The first line of the address

line2optional	String
The second line of the address, typically used for a suite number, apartment number, etc

cityoptional	String
The city

stateoptional	String
The state, province or other country subdivision

countyoptional	String
A valid county for the subdivision obtained from /_data/counties. This is only used for US states and should be null for any other country.

zipoptional	String
The ZIP/postal code

countryoptional	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitudeoptional	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitudeoptional	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_idoptional	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success 200
Field	Type	Description
id	Number
The internal ID of the address

line1	String
The first line of the address

line2	String
The second line of the address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal. If no latitude is set, this will be null.

longitude	Float
The longitude of the address, in decimal. If no longitude is set, this will be null.

address_type_id	Number
The type of address this is. You can obtain a list of address types from the /system/address_types API endpoint.

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "id": 3,
        "line1": "444 Packers Ln",
        "line2": "Suite 1337",
        "city": "Green Bay",
        "state": "Wisconsin",
        "county": "Green Bay Co.",
        "zip": "54332",
        "country": "US",
        "latitude": null,
        "longitude": null,
        "address_type_id": 2
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
             "address_type_id": "The selected address type id is not valid.",
         },
         "status_code": 422
     }
 }
Account Billing
```
