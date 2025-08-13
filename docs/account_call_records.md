# Account Call Records Endpoints

## Get account call records (GET)
- **Version**: 0.6.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/call_records/:start_date/:end_date`
- **Description**: Get a list of call records on the account, between `:start_date` and `:end_date`, in YYYY-MM-DD format. The dates are checked in UTC (as call records are stored/entered with UTC.) For example, if you want to see all calls on 2016-08-01 UTC, you should enter 2016-08-01 as the start and 2016-08-02 as the end.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `start_date` (Date, required): The start date, in UTC. YYYY-MM-DD format.
    - `end_date` (Date, required): The end date, in UTC. YYYY-MM-DD format.
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 8,
          "origination": "14145132472",
          "destination": "18007776666",
          "call_start": "2016-08-26 16:09:46",
          "duration_in_seconds": 1999,
          "matched_prefix": "1800",
          "prefix_name": "TOLL FREE",
          "rate": "0.00000000000000000000",
          "local": false,
          "long_distance": false,
          "service_id": 5
        },
        {
          "id": 7,
          "origination": "14145132472",
          "destination": "011376312341231234",
          "call_start": "2016-08-26 16:09:46",
          "duration_in_seconds": 154,
          "matched_prefix": "3763",
          "prefix_name": "ANDORRA",
          "rate": "0.36400000000000000000",
          "local": false,
          "long_distance": false,
          "service_id": 5
        }
      ],
      "paginator": {
        "total_count": 8,
        "total_pages": 4,
        "current_page": 1,
        "limit": 2
      }
    }
    ```
```
