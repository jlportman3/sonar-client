# CDRs Endpoints

## Submit a standardized CDR for rating (POST)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/system/voice/cdr_rating`
- **Description**: Submit call records to be rated by Sonar. The records must be in a standardized format. When submitting records to this endpoint, batch them into sets of 5,000 records at a time. At this time, only 10 digit calls are supported for national calls (NANP.) Anything longer than 10 digits will be treated as international.
- **Example Request Body**:
    ```json
    {
       "voice_provider_id": 1,
       "records": [
           {
               "origination": "1234567890",
               "destination": "0111234657364",
               "call_start": "2016-08-11 09:43:21",
               "duration": 123
           },
           {
               "origination": "1234567891",
               "destination": "18006667777",
               "call_start": "2016-08-11 09:47:21",
               "duration": 38
           }
       ]
    }
    ```
- **Parameters**:
    - `voice_provider_id` (Integer, required): The ID of the voice provider which these CDRs are for. This is how you specify which rate deck to use for these calls.
    - `records` (Array, required): An array of records, each with the following properties:
        - `origination` (String, required): The originating DID (10 digits, or 11 with a leading 1.)
        - `destination` (String, required): The destination DID (Minimum of 10 digits)
        - `call_start` (DateTime, required): The date and time the call was placed, in UTC in YYYY-MM-DD HH:mm:ss format. Hours should be in 24 hour format.
        - `duration` (Integer, required): The duration of the call, in seconds
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "success": true
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": "A list of validation errors",
            "status_code": 422
        }
    }
    ```
```
