# Jobs Endpoints

## Check in to a job (POST)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/check_in`
- **Description**: Check a user in to a job. This is used when the user is on site and starting the job. Multiple users can check in to a job at the same time.
- **Parameters**:
    - `id` (Integer, required): The job ID
    - `user_id` (Integer, optional): The ID of the user to check in to the job. If not submitted, the user ID of the logged in user will be used.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "scheduled_datetime": "2016-01-01 01:02:03",
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "scheduled",
        "user_ids": [],
        "created_by_user_id": 1,
        "checked_in_users": [
             {
                  "user_id": 1,
                  "datetime": "2016-01-01 01:01:01"
             }
        ],
        "services": [
            1
        ],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
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

## Check out of a job (POST)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/check_out`
- **Description**: Check a user out of a job. This should only be used to remove a user from a checked in job prior to completion. Completing or failing a job will automatically remove all checked in users.
- **Parameters**:
    - `id` (Integer, required): The job ID
    - `user_id` (Integer, optional): The ID of the user to check out of the job. If not submitted, the user ID of the logged in user will be used.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "scheduled_datetime": "2016-01-01 01:02:03",
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "scheduled",
        "user_ids": [],
        "created_by_user_id": 1,
        "checked_in_users": [],
        "services": [],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
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

## Complete a job (POST)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/complete`
- **Description**: Completing a job will move the status to completed or failed, remove it from the schedule, remove all checked in users, add any services to the account that are associated with the job, and perform all events associated with the job type.
- **Parameters**:
    - `id` (Integer, required): The job ID
    - `completion_type` (String, optional): Whether or not the job was successfully completed (`"success"`, `"failure"`)
    - `reason` (String, optional): The reason for the job failure, or some notes on success. Required when failing a job.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "scheduled_datetime": null,
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "completed",
        "user_ids": [],
        "created_by_user_id": 1,
        "checked_in_users": [],
        "services": [],
        "completed_at": "2018-09-23 12:23:34",
        "completed_by_user_id": 1,
        "completed_successfully": true,
        "completion_reason": "foobar"
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

## Create a new desired job date/time (POST)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/desired_job_datetimes`
- **Description**: Create a new desired job date/time. This lets you specify when a customer would like to have the job performed as a date, a start time, and an end time, which denotes the range of time they will be available.
- **Parameters**:
    - `id` (Number, required): The ID of the job
    - `date` (Date, required): The date, in Y-m-d format
    - `start_time` (Time, required): The start time of the time range, in H:m:s format (24 hour)
    - `end_time` (Time, required): The end time of the time range, in H:m:s format (24 hour)
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "date": "2016-09-01",
        "start_time": "07:00:00",
        "end_time": "09:00:00"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "The start_time must be prior to the end_time.",
         "status_code": 422
       }
    }
    ```

## Create a new job (POST)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs`
- **Description**: Create a new job.
- **Parameters**:
    - `job_type_id` (Number, required): The ID of a job type
    - `assigned_type` (String, required): The entity you are assigning this job to (`"accounts"`, `"network_sites"`)
    - `assigned_id` (Number, required): The ID of the entity
    - `length_in_minutes` (Number, optional): The length of the job. Will be inherited from the job type if omitted. Must be divisible by 15.
    - `notes` (String, optional): Any notes for the job.
    - `scheduled_datetime` (DateTime, optional): If you want to schedule or reschedule this job, input a date/time to schedule it for. `user_ids` is required if this is submitted. The timezone should be the timezone of this Sonar instance.
    - `user_ids` (Array, optional): Input an array of user_ids to assign this job to. These are the parties that will be completing the job. They must all have available time in their schedules for the job. `scheduled_datetime` is required if this is submitted.
    - `services` (Array, optional): An array of service IDs that will be added to the account when the job is completed. The job can also have services added by the job type - query the job types endpoint to see those.
    - `ticket_id` (Integer, optional): ID of a ticket that this job is linked to. If null is sent, the job will not be linked to a ticket.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "scheduled_datetime": null,
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "queued",
        "user_ids": [],
        "created_by_user_id": 1,
        "checked_in_users": [],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "There is no availability for that day/time for user ID 1.",
         "status_code": 422
       }
    }
    ```

## Delete a desired job date/time (DELETE)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/desired_job_datetimes/:desired_job_datetime_id`
- **Description**: Delete a desired job date/time
- **Parameters**:
    - `id` (Number, required): The ID of the job
    - `desired_job_datetime_id` (Number, required): The ID of the desired job date/time
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
            "message": "desired job date/time does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a job (DELETE)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id`
- **Description**: Delete a job
- **Parameters**:
    - `id` (Number, required): The ID of the job
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
            "message": "job does not exist.",
            "status_code": 404
        }
    }
    ```

## Find any available space for a job (GET)
- **Version**: 1.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/find_any_available_space`
- **Description**: Return available blocks of time for a job. You can use this to quickly find available time blocks for a job of a specific length in a date range that you want to schedule for a specific user or group of users.
- **Parameters**:
    - `start_date` (DateTime, required): The start date for the date range in YYYY-MM-DD format.
    - `end_date` (DateTime, required): The end date for the date range in YYYY-MM-DD format.
    - `length_in_minutes` (Integer, required): The length of time required for the job, in minutes
    - `job_type_id` (Integer, required): A valid job type ID
    - `users` (Array, optional): An array of user IDs that you want to schedule this job for. If this is omitted, all users will be checked.
    - `entityType` (String, required): One of account or network_site. This is to limit results to entries that meet any defined geofences.
    - `entityId` (Integer, required): The ID of an account or network_site. This is to limit results to entries that meet any defined geofences.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "2016-09-16": {
          "1": [
            {
              "start": "04:00:00",
              "end": "10:00:00"
            },
            {
              "start": "15:00:00",
              "end": "15:47:00"
            },
            {
              "start": "16:02:00",
              "end": "17:20:00"
            },
            {
              "start": "18:20:00",
              "end": "21:00:00"
            }
          ],
          "2": [
            {
              "start": "04:00:00",
              "end": "10:00:00"
            },
            {
              "start": "15:00:00",
              "end": "16:56:00"
            },
            {
              "start": "17:26:00",
              "end": "21:00:00"
            }
          ]
        }
      }
    }
    ```

## Find compound available space for a job (GET)
- **Version**: 1.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/find_available_space`
- **Description**: Return available blocks of time for a job. You can use this to quickly find available time blocks for a job of a specific length in a date range that you want to schedule for a specific user or group of users. This data is compounded by all the users entered (e.g. if you submit 3 user IDs, it will only return time where all three of those users are available to perform a job of the type submitted.)
- **Parameters**:
    - `start_date` (DateTime, required): The start date for the date range in YYYY-MM-DD format.
    - `end_date` (DateTime, required): The end date for the date range in YYYY-MM-DD format.
    - `length_in_minutes` (Integer, required): The length of time required for the job, in minutes
    - `job_type_id` (Integer, required): A valid job type ID
    - `users` (Array, required): An array of user IDs that you want to schedule this job for. You can include a single ID if you want to schedule for a single user.
    - `entityType` (String, required): One of account or network_site. This is to limit results to entries that meet any defined geofences.
    - `entityId` (Integer, required): The ID of an account or network_site. This is to limit results to entries that meet any defined geofences.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "2016-09-16": [
          {
            "start": "04:00:00",
            "end": "10:00:00"
          },
          {
            "start": "15:19:00",
            "end": "16:56:00"
          },
          {
            "start": "18:20:00",
            "end": "21:00:00"
          }
        ],
        "2016-09-18": [
          {
            "start": "00:00:00",
            "end": "01:00:00"
          }
        ],
        "2016-09-19": [
          {
            "start": "00:00:00",
            "end": "21:00:00"
          }
        ]
      }
    }
    ```

## Get all desired job date/times (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/desired_job_datetimes`
- **Description**: Get all desired job date/times for a job
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
    - `id` (Number, required): The ID of the job
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "date": "2016-09-01",
          "start_time": "07:00:00",
          "end_time": "09:00:00"
        },
        {
          "id": 2,
          "date": "2016-10-01",
          "start_time": "09:00:00",
          "end_time": "11:30:00"
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

## Get all jobs (GET)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs`
- **Description**: Get all jobs
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
           "id": 8,
           "scheduled_datetime": null,
           "job_type_id": 1,
           "length_in_minutes": 60,
           "ticket_id": null,
           "assigned_type": "accounts",
           "assigned_id": 1,
           "notes": "Please replace the router.",
           "status": "queued",
           "user_ids": [],
           "created_by_user_id": 1,
           "checked_in_users": [],
           "services": [],
            "completed_at": null,
            "completed_by_user_id": null,
            "completed_successfully": null,
            "completion_reason": null
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

## Get an individual desired job date/time (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/desired_job_datetimes/:desired_job_datetime_id`
- **Description**: Get an individual desired job date/time
- **Parameters**:
    - `id` (Number, required): The ID of the job
    - `desired_job_datetime_id` (Number, required): The ID of the desired job date/time
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "date": "2016-09-01",
        "start_time": "07:00:00",
        "end_time": "09:00:00"
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

## Get an individual job (GET)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id`
- **Description**: Get an individual job
- **Parameters**:
    - `id` (Number, required): The ID of the job
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
         "id": 8,
         "scheduled_datetime": null,
         "job_type_id": 1,
         "length_in_minutes": 60,
         "ticket_id": null,
         "assigned_type": "accounts",
         "assigned_id": 1,
         "notes": "Please replace the router.",
         "status": "queued",
         "user_ids": [],
         "created_by_user_id": 1,
         "checked_in_users": [],
         "services": [],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
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

## Return a job to the queue (POST)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/queue`
- **Description**: Move a job back into the queue. This will take a scheduled or failed job, and put it back into the queue.
- **Parameters**:
    - `id` (Number, required): The job ID
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "scheduled_datetime": null,
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "queued",
        "user_ids": [],
        "created_by_user_id": 1,
        "checked_in_users": [],
        "services": [],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
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

## Update desired job date/time (PATCH)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id/desired_job_datetimes/:desired_job_datetime_id`
- **Description**: Update an existing desired job date/time.
- **Parameters**:
    - `id` (Number, required): The job ID
    - `desired_job_datetime_id` (Number, required): The ID of the desired job date/time
    - `date` (Date, optional): The date, in Y-m-d format
    - `start_time` (Time, optional): The start time of the time range, in H:m:s format (24 hour)
    - `end_time` (Time, optional): The end time of the time range, in H:m:s format (24 hour)
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "date": "2016-09-01",
        "start_time": "07:00:00",
        "end_time": "11:45:00"
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

## Update job (PATCH)
- **Version**: 1.7.12
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/jobs/:id`
- **Description**: Update an existing job. You can use this to reschedule an already scheduled job, or to schedule a queued job as well.
- **Parameters**:
    - `assigned_type` (String, optional): The entity you are assigning this job to. This is required if you input assigned_id. (`"accounts"`, `"network_sites"`)
    - `assigned_id` (Number, optional): The ID of the entity. This is required if you input assigned_type.
    - `length_in_minutes` (Number, optional): The length of the job. Will be inherited from the job type if omitted. Must be divisible by 15.
    - `notes` (String, optional): Any notes for the job.
    - `scheduled_datetime` (DateTime, optional): If you want to schedule this job now, input a date/time to schedule it for. `user_ids` is required if this is submitted. The timezone should be the timezone of this Sonar instance.
    - `user_ids` (Array, optional): Input an array of user_ids to assign this job to. These are the parties that will be completing the job. They must all have available time in their schedules for the job. This will be ignored if the job is not currently scheduled, or you do not submit a scheduled_datetime.
    - `services` (Array, optional): An array of service IDs that will be added to the account when the job is completed. The job can also have services added by the job type - query the job types endpoint to see those.
    - `ticket_id` (Integer, optional): ID of a ticket that this job is linked to. If null is sent, the job will not be linked to a ticket.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 22,
        "scheduled_datetime": "2016-08-29 11:00",
        "job_type_id": 1,
        "length_in_minutes": 60,
        "ticket_id": null,
        "assigned_type": "accounts",
        "assigned_id": 1,
        "notes": "Please replace the router.",
        "status": "scheduled",
        "user_ids": [
          1
        ],
        "created_by_user_id": 1,
        "checked_in_users": [],
        "services": [],
        "completed_at": null,
        "completed_by_user_id": null,
        "completed_successfully": null,
        "completion_reason": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "No item with that ID found.",
         "status_code": 422
       }
    }
    ```
```
