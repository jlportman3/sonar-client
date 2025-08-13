# Network Sites Endpoints

## Create network site address (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/network_sites/:network_site_id/addresses`
- **Description**: Create a new network site address
- **Parameters**:
    - `network_site_id` (Number, required): The ID of the network site to add the address to
    - `line1` (String, required): The first line of the address
    - `line2` (String, optional): The second line of the address, typically used for a suite number, apartment number, etc
    - `city` (String, required): The city
    - `state` (String, required): The state, province or other country subdivision
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be null for any other country.
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

## Create network site (POST)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites`
- **Description**: Create a new network site.
- **Parameters**:
    - `name` (String, required): A unique name for the network site
    - `line1` (String, optional): Line1 of the physical address of the site
    - `line2` (String, optional): Line2 of the physical address of the site
    - `city` (String, optional): The city of the site
    - `state` (String, optional): The state/province of the site
    - `zip` (String, optional): The zip/postal code of the site
    - `country` (String, required): The country of the site, as a two digit string
    - `latitude` (String, required): The latitude of the site in decimal
    - `longitude` (String, required): The longitude of the site in decimal
    - `height_in_meters` (Number, required): The height of the network site, in meters. This is only really used if you're utilizing the path profiling tools in Sonar, or anything related to calculating wireless signals.
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
          "id": 1,
          "name": "My House",
          "height_in_meters": 15
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Delete network site address (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/network_sites/:network_site_id/addresses/:address_id`
- **Description**: Delete a network site address.
- **Parameters**:
    - `network_site_id` (Number, required): The ID of the network site
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

## Delete network site (DELETE)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id`
- **Description**: Delete a network site.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "success": true
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "Network site not found.",
            "status_code": 404
        }
    }
    ```

## Get all network site addresses (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/network_sites/:network_site_id/addresses`
- **Description**: Get a list of the addresses for network site ID :network_site_id
- **Parameters**:
    - `network_site_id` (Number, required): The ID of the network site
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states.
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

## Get all network sites (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites`
- **Description**: Get a list of network sites.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "My House",
          "height_in_meters": 100.4
        },
        {
          "id": 2,
          "name": "Jimbob's House of Data",
          "height_in_meters": 50
        },
        {
          "id": 3,
          "name": "Equinix",
          "height_in_meters": 501
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

## Get individual network site address (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/network_sites/:network_site_id/addresses/:address_id`
- **Description**: Get an individual network site address.
- **Parameters**:
    - `network_site_id` (Number, required): The ID of the network site
    - `address_id` (Number, required): The ID of the address
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states.
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

## Get individual network site (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id`
- **Description**: Get an individual network site.
- **Parameters**:
    - `id` (Number, required): The ID of the account type
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
          "id": 1,
          "name": "My House",
          "height_in_meters": 43
        }
    }
    ```

## Update network site address (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/network_sites/:network_site_id/addresses/:address_id`
- **Description**: Update a network site address.
- **Parameters**:
    - `network_site_id` (Number, required): The ID of the network site to update the address on
    - `address_id` (Number, required): The ID of the address
    - `line1` (String, optional): The first line of the address
    - `line2` (String, optional): The second line of the address, typically used for a suite number, apartment number, etc
    - `city` (String, optional): The city
    - `state` (String, optional): The state, province or other country subdivision
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be null for any other country.
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

## Update network site (PATCH)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/network/network_sites/:id`
- **Description**: Update a network site.
- **Parameters**:
    - `id` (Number, required): The ID of the network site
    - `name` (String, optional): A unique name for the network site
    - `height_in_meters` (Number, optional): The height of the network site, in meters. This is only really used if you're utilizing the path profiling tools in Sonar, or anything related to calculating wireless signals.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
          "id": 1,
          "name": "My Data Center",
          "height_in_meters": 12
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```
```
