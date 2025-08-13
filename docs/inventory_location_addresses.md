# Inventory Location Addresses Endpoints

## Create inventory location address (POST)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory_locations/:inventory_location_id/addresses`
- **Description**: Create a new inventory location address
- **Parameters**:
    - `inventory_location_id` (Number, required): The ID of the inventory location to add the address to
    - `line1` (String, required): The first line of the address
    - `line2` (String, optional): The second line of the address, typically used for a suite number, apartment number, etc
    - `city` (String, required): The city
    - `state` (String, required): The state, province or other country subdivision. You can obtain a valid list from `_data/subdivisions/:country`
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be blank for any other country.
    - `zip` (String, required): The ZIP/postal code
    - `country` (String, required): A valid, two character country code. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
    - `latitude` (Float, optional): The latitude of the address, in decimal. If no latitude is set, this will be null.
    - `longitude` (Float, optional): The longitude of the address, in decimal. If no longitude is set, this will be null.
    - `address_type_id` (Number, required): The type of address this is. You can obtain a list of address types from the `/system/address_types` API endpoint.
- **Success Response (201 Created)**:
    ```json
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
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "address_type_id": "The selected address type id is not valid."
            },
            "status_code": 422
        }
    }
    ```

## Delete inventory location address (DELETE)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory_locations/:inventory_location_id/addresses/:address_id`
- **Description**: Delete an inventory location address
- **Parameters**:
    - `inventory_location_id` (Number, required): The ID of the inventory location
    - `address_id` (Number, required): The ID of the address
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "Address deleted"
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

## Get all inventory location addresses (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory_location/:inventory_location_id/addresses`
- **Description**: Get a list of the addresses for inventory location ID :inventory_location_id
- **Parameters**:
    - `inventory_location_id` (Number, required): The ID of the inventory location
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`, null if not a US address
- **Success Response (200 OK)**:
    ```json
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

## Get individual inventory location address (GET)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory_locations/:inventory_location_id/addresses/:address_id`
- **Description**: Get an individual inventory location address.
- **Parameters**:
    - `inventory_location_id` (Number, required): The ID of the inventory location
    - `address_id` (Number, required): The ID of the address
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`, null if not a US address
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
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

## Update inventory location address (PATCH)
- **Version**: 0.3.0
- **Endpoint**: `https://example.sonar.software/api/v1/inventory_locations/:inventory_location_id/addresses/:address_id`
- **Description**: Update an inventory location address.
- **Parameters**:
    - `inventory_location_id` (Number, required): The ID of the inventory location to update the address on
    - `address_id` (Number, required): The ID of the address
    - `line1` (String, optional): The first line of the address
    - `line2` (String, optional): The second line of the address, typically used for a suite number, apartment number, etc
    - `city` (String, optional): The city
    - `state` (String, optional): The state, province or other country subdivision
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be blank for any other country.
    - `zip` (String, optional): The ZIP/postal code
    - `country` (String, optional): A valid, two character country code. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
    - `latitude` (Float, optional): The latitude of the address, in decimal. If no latitude is set, this will be null.
    - `longitude` (Float, optional): The longitude of the address, in decimal. If no longitude is set, this will be null.
    - `address_type_id` (Number, optional): The type of address this is. You can obtain a list of address types from the `/system/address_types` API endpoint.
- **Success Response (200 OK)**:
    ```json
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
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "address_type_id": "The selected address type id is not valid."
            },
            "status_code": 422
        }
    }
    ```
```
