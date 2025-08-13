# Voice Providers Endpoints

## Create a new voice provider (POST)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers`
- **Description**: Create a new voice provider.
- **Parameters**:
    - `name` (String, required): A name for the voice provider
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Flowroute"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "name": "The name must be unique."
         },
         "status_code": 422
       }
    }
    ```

## Delete a voice provider (DELETE)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers/:id`
- **Description**: Delete a voice provider
- **Parameters**:
    - `id` (Number, required): The ID of the voice provider
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
            "message": "Voice provider does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all voice providers (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers`
- **Description**: Get all voice providers
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "name": "Flowroute"
        },
        {
          "id": 1,
          "name": "Vitelity"
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

## Get an individual voice provider (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers/:id`
- **Description**: Get an individual voice provider
- **Parameters**:
    - `id` (Number, required): The ID of the voice provider
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Flowroute"
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

## Import a rate deck (POST)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers/:id/import_rates`
- **Description**: Import a rate deck for a voice provider. Please note that hitting this endpoint will delete all existing rates for this provider before beginning new import. In case of a failure, your rates may still be removed, so please ensure you successfully complete and verify a rate deck import when using this endpoint! It may also take some time for a large rate deck to be imported - importing 100,000 rates here can take upwards of 60 seconds. Please ensure you have a sufficiently large timeout set in your script/client when performing this import.
- **Parameters**:
    - `id` (Number, required): The ID of the voice provider
    - `rates` (Array, required): An array of names, prefixes, and rates. The array should contain multiple objects with a name property that explains the rate, a prefix property that contains the dialed number prefix, and a rate property that represents the rate to call that prefix, per minute, in cents (or whatever the smallest currency denomination you use is.) The rate can be represented as a fraction (float.) Example shown below.
    - `minimum_rate` (Number, required): The minimum rate for calls, per minute. You can use this to override the percentage increase in the case where you want a minimum rate that may be higher than the percentage increase for some rates.
    - `percentage_increase` (Number, required): A percentage increase, between 0 and 100. This will be used to increase the rate in the rates array by this percentage. If the percentage increase is less than minimum_rate, then the minimum rate will be used instead.
- **Example Request Body**:
    ```json
    {
          "minimum_rate": 0.01,
          "percentage_increase": 40,
          "rates": [
                 {
                        "name": "ANDORRA",
                        "prefix": "3763",
                        "rate": 0.30786
                 },
                 {
                        "name": "ANDORRA - MOBILE",
                        "prefix": "3764",
                        "rate": 0.307485
                 }
          ]
    }
    ```
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "success": true,
        "errors": [
          "Line 3 was skipped as it had a rate or prefix that was not numeric."
        ]
      }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "Voice provider does not exist.",
            "status_code": 404
        }
    }
    ```

## Update voice provider (PATCH)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/voice_providers/:id`
- **Description**: Update an existing voice provider.
- **Parameters**:
    - `id` (Number, required): The voice provider ID
    - `name` (String, optional): The name of the voice provider
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "Fowroute"
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
```
