# Financial Endpoints

## Create geotax (POST)
- **Version**: 0.6.7
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id/geotaxes`
- **Description**: Create a new geographical tax. You must specify at least one geographical variable for automatic assignment to accounts based on address.
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `name` (String, required): A descriptive name for the geotax
    - `rate` (Number, required): The rate for the tax. This is either a percentage or a flat rate, depending on the configuration of the parent tax.
    - `subdivision` (String, optional): A valid subdivision obtained from `/_data/subdivisions`
    - `city` (String, optional): A valid city
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be blank for any other country.
    - `zip` (String, optional): A valid ZIP/postal code
    - `zip_partial_match` (Boolean, optional): Whether or not this geotax supports partial matching on a ZIP
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Sheboygan County",
        "rate": "0.4",
        "subdivision": "Wisconsin",
        "city": null,
        "county": "Sheboygan Co.",
        "zip": null,
        "zip_partial_match": false
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "Sheboygan Co. is not a valid county for the subdivision New York",
         "status_code": 422
       }
    }
    ```

## Create tax (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes`
- **Description**: Create a new tax.
- **Parameters**:
    - `name` (String, required): A descriptive name for the tax
    - `application` (String, required): Either flat or percentage (`"flat"`, `"percentage"`)
    - `type` (String, required): Either global or geo(graphical) (`"global"`, `"geo"`)
    - `rate` (Number, required): The tax rate, a currency amount for flat and a percentage for percentage based taxes.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "VAT",
        "application": "percentage",
        "type": "global",
        "rate": "20"
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

## Delete geotax (DELETE)
- **Version**: 0.6.7
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id/geotaxes/:geotaxid`
- **Description**: Delete a tax.
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `geotaxid` (Number, required): The ID of the geotax
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
            "message": "Geotax not found",
            "status_code": 404
        }
    }
    ```

## Get all geotaxes for a tax (GET)
- **Version**: 0.6.7
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id/geotaxes`
- **Description**: Get a list of all the geographic area taxes configured for a geographical tax.
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "Milwaukee County",
          "rate": "0.4",
          "subdivision": "Wisconsin",
          "city": "",
          "county": "Milwaukee Co.",
          "zip": "",
          "zip_partial_match": false
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

## Get all taxes (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes`
- **Description**: Get a list of all configured taxes.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "$9 Flat Tax",
          "application": "flat",
          "type": "global",
          "rate": "9"
        },
        {
          "id": 2,
          "name": "3% Tax Rate",
          "application": "percentage",
          "type": "global",
          "rate": "3"
        },
        {
          "id": 3,
          "name": "Some other tax",
          "application": "flat",
          "type": "global",
          "rate": "2"
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

## Get individual geo tax (GET)
- **Version**: 0.6.7
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id/geotaxes/:geotaxid`
- **Description**: Get an individual geotax from a parent tax
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `geotaxid` (Number, required): The ID of the geotax
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "Milwaukee County",
        "rate": "0.4",
        "subdivision": "Wisconsin",
        "city": "",
        "county": "Milwaukee Co.",
        "zip": "",
        "zip_partial_match": false
      }
    }
    ```

## Get individual tax (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id`
- **Description**: Get an individual tax
- **Parameters**:
    - `id` (Number, required): The ID of the tax
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "$9 Flat Tax",
        "application": "flat",
        "type": "global",
        "rate": "9"
      }
    }
    ```

## Update geotax (PATCH)
- **Version**: 0.6.7
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id/geotaxes/:geotaxid`
- **Description**: Update a geotax.
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `geotaxid` (Number, required): The ID of the geotax.
    - `name` (String, required): A descriptive name for the geotax
    - `rate` (Number, required): The rate for the tax. This is either a percentage or a flat rate, depending on the configuration of the parent tax.
    - `subdivision` (String, optional): A valid subdivision obtained from `/_data/subdivisions`
    - `city` (String, optional): A valid city
    - `county` (String, optional): A valid county for the subdivision obtained from `/_data/counties`. This is only used for US states and should be blank for any other country.
    - `zip` (String, optional): A valid ZIP/postal code
    - `zip_partial_match` (Boolean, optional): Whether or not this geotax supports partial matching on a ZIP
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Sheboygan County",
        "rate": "1.0",
        "subdivision": "Wisconsin",
        "city": null,
        "county": "Sheboygan Co.",
        "zip": "12345",
        "zip_partial_match": true
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "Sheboygan Co. is not a valid county for the subdivision New York",
         "status_code": 422
       }
    }
    ```

## Update tax (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/financial/taxes/:id`
- **Description**: Update a tax.
- **Parameters**:
    - `id` (Number, required): The ID of the tax
    - `name` (String, required): A descriptive name for the tax
    - `application` (String, required): Either flat or percentage (`"flat"`, `"percentage"`)
    - `type` (String, required): Either global or geo(graphical) (`"global"`, `"geo"`)
    - `rate` (Number, required): The tax rate, a currency amount for flat and a percentage for percentage based taxes.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 5,
        "name": "VAT",
        "application": "percentage",
        "type": "global",
        "rate": "21"
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
