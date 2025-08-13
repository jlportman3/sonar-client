# Schedules Endpoints

## Create a new schedule blocker (POST)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers`
- **Description**: Create a new schedule blocker.
- **Parameters**:
    - `name` (String, required): A name for the schedule blocker
    - `sunday` (Boolean, required): true if this schedule blocks on Sunday, false if not
    - `monday` (Boolean, required): true if this schedule blocks on Monday, false if not
    - `tuesday` (Boolean, required): true if this schedule blocks on Tuesday, false if not
    - `wednesday` (Boolean, required): true if this schedule blocks on Wednesday, false if not
    - `thursday` (Boolean, required): true if this schedule blocks on Thursday, false if not
    - `friday` (Boolean, required): true if this schedule blocks on Friday, false if not
    - `saturday` (Boolean, required): true if this schedule blocks on Saturday, false if not
    - `start_timestamp` (Time, required): The start of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `end_timestamp` (Time, required): The end of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `user_ids` (Array, required): An array of user IDs that this blocker should apply to
    - `start` (Date, required): The start date for this blocker
    - `weeks` (Integer, required): The frequency of repetition for this blocker. If this is 1, it repeats weekly. If this is 2, it repeats every other week.
    - `repetitions` (Integer, required): How many times this blocker repeats. Ignored if infinite_repetitions is true
    - `infinite_repetitions` (Boolean, required): If this is true, this blocker repeats forever
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
         "id": 2,
         "name": "brunch",
         "sunday": false,
         "monday": true,
         "tuesday": false,
         "wednesday": false,
         "thursday": false,
         "friday": false,
         "saturday": false,
         "start_timestamp": "13:55",
         "end_timestamp": "14:30",
         "user_ids": [
           1
         ],
         "start": "2017-01-01",
         "weeks": 1,
         "repetitions": 1,
         "infinite_repetitions": true
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "infinite_repetitions": "Infinite repetitions must be a boolean."
         },
         "status_code": 422
       }
    }
    ```

## Create a new schedule day/time (POST)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:schedule_id/schedule_days`
- **Description**: Create a new schedule day/time. A schedule day and time is contained within a schedule, so you must create a schedule first.
- **Parameters**:
    - `schedule_id` (Number, required): The ID of the schedule that contains this day/time
    - `day` (Number, required): The day of the week for this scheduled day/time, where 0 is Sunday and 6 is Saturday. (`0`, `1`, `2`, `3`, `4`, `5`, `6`)
    - `start_timestamp` (Time, required): The starting time for this particular period, in Hour:Minute format, where minute must be in 15 minute increments. This is in the Sonar timezone, not UTC.
    - `end_timestamp` (Time, required): The ending time for this particular period, in Hour:Minute format, where minute must be in 15 minute increments. This is in the Sonar timezone, not UTC.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "day": 1,
        "start_timestamp": "13:45:00",
        "end_timestamp": "17:00:00"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "day": "The day must be between 0 and 6."
         },
         "status_code": 422
       }
    }
    ```

## Create a new schedule (POST)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules`
- **Description**: Create a new schedule. A schedule is a container for availability, or lack thereof. You must add days to the schedule for it to have any purpose.
- **Parameters**:
    - `name` (String, required): A name for the schedule
    - `user_ids` (Array, required): An array of user IDs that this schedule is applied to
    - `job_type_ids` (Array, required): An array of job type IDs that this time is for. Only jobs with this job type will be allowed to be scheduled in this container.
    - `start` (Date, required): The date that the schedule should start to be applied, in the local system timezone. YYYY-MM-DD format.
    - `available` (Boolean, required): Whether this schedule defines availability, or lack of availability. A schedule with available set to false will always override another schedule with available set to true.
    - `infinite_repetitions` (Boolean, required): Set this to true if you want this schedule to run indefinitely
    - `repetitions` (Number, required): How many times this schedule should repeat. 0 to never repeat.
    - `weeks` (Number, required): How often the repetition should occur, in weeks. If this is 1, it repeats weekly. If this is 2, the schedule runs for one week, then breaks for one week, then runs for one week, then breaks for two weeks, etc. If this is 3, the schedule runs for one week, then breaks for two weeks, then runs for one week, then breaks for two weeks, etc. This interacts with repetitions by repeating repetitions times for the number of active weeks. For example, if weeks is 2, and repetitions is 1, this schedule would run for a week, skip a week, run for a week, and then stop.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 6,
        "user_ids": [ 1 ],
        "job_type_ids": [ 1 ],
        "name": "Test",
        "start": "2016-08-05",
        "available": true,
        "infinite_repetitions": false,
        "repetitions": 1,
        "weeks": 3
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "user_id": "That user does not exist."
         },
         "status_code": 422
       }
    }
    ```

## Create a new scheduled time off (POST)
- **Version**: 0.7.2
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/scheduled_time_offs`
- **Description**: Create a new scheduled time off. This is typically used to block out a span of time when an employee is unavailable, for example, during vacation.
- **Parameters**:
    - `user_id` (Integer, required): The ID of the user that has time off scheduled
    - `start_time` (DateTime, required): The day and time that the user has scheduled off, in the system timezone.
    - `end_time` (DateTime, required): The day and time that the user has scheduled off, in the system timezone.
    - `name` (String, required): A description/reason for the time off.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 10,
        "user_id": 1,
        "start_time": "2016-11-01 01:00:00",
        "end_time": "2016-11-01 01:30:00",
        "name": "test"
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

## Delete a schedule blocker (DELETE)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers/:id`
- **Description**: Delete a schedule blocker
- **Parameters**:
    - `id` (Integer, required): The ID of the schedule blocker
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
            "message": "schedule blocker does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a schedule day/time (DELETE)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:schedule_id/schedule_days/:id`
- **Description**: Delete a schedule day/time
- **Parameters**:
    - `schedule_id` (Number, required): The ID of the schedule that contains this day/time
    - `id` (Number, required): The ID of the schedule day/time
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
            "message": "schedule day/time does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a schedule (DELETE)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:id`
- **Description**: Delete a schedule
- **Parameters**:
    - `id` (Number, required): The ID of the schedule
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
            "message": "Schedule does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete a scheduled time off (DELETE)
- **Version**: 0.7.2
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/scheduled_time_offs/:id`
- **Description**: Delete a scheduled time off
- **Parameters**:
    - `id` (Number, required): The ID of the scheduled time off
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
            "message": "scheduled time off does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all schedule blockers (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers`
- **Description**: Get all schedule blockers
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "name": "Brunch",
          "sunday": false,
          "monday": true,
          "tuesday": false,
          "wednesday": false,
          "thursday": false,
          "friday": false,
          "saturday": false,
          "start_timestamp": "13:55",
          "end_timestamp": "14:30",
          "user_ids": [
            1
          ],
          "start": "2017-01-01",
          "weeks": 1,
          "repetitions": 1,
          "infinite_repetitions": true
        },
        {
          "id": 7,
          "name": "Lunch",
          "sunday": false,
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": false,
          "friday": false,
          "saturday": false,
          "start_timestamp": "00:00",
          "end_timestamp": "00:45",
          "user_ids": [
            1
          ],
          "start": "2017-02-02",
          "weeks": 1,
          "repetitions": 1,
          "infinite_repetitions": true
        },
        {
          "id": 8,
          "name": "Dinner",
          "sunday": false,
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": false,
          "friday": false,
          "saturday": false,
          "start_timestamp": "00:00",
          "end_timestamp": "00:30",
          "user_ids": [
            1
          ],
          "start": "2017-02-01",
          "weeks": 1,
          "repetitions": 1,
          "infinite_repetitions": true
        },
        {
          "id": 9,
          "name": "Breakfast",
          "sunday": true,
          "monday": true,
          "tuesday": true,
          "wednesday": true,
          "thursday": true,
          "friday": true,
          "saturday": true,
          "start_timestamp": "00:30",
          "end_timestamp": "11:00",
          "user_ids": [],
          "start": "2017-02-01",
          "weeks": 1,
          "repetitions": 1,
          "infinite_repetitions": true
        }
      ],
      "paginator": {
        "total_count": 4,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
      }
    }
    ```

## Get all scheduled time offs (GET)
- **Version**: 0.7.2
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/scheduled_time_offs`
- **Description**: Get all scheduled time offs
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 5,
          "user_id": 9,
          "start_time": "2016-10-18 21:00:00",
          "end_time": "2016-10-18 22:00:00",
          "name": "Matt's Vacation"
        },
        {
          "id": 3,
          "user_id": 9,
          "start_time": "2016-10-18 01:00:00",
          "end_time": "2016-10-20 19:45:00",
          "name": "Really long dentist appointment"
        },
        {
          "id": 6,
          "user_id": 1,
          "start_time": "2016-10-19 00:00:00",
          "end_time": "2016-10-19 23:45:00",
          "name": "Just a block of time off for user ID 1"
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

## Get all schedules (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules`
- **Description**: Get all schedules
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 3,
          "user_ids": [ 1 ],
          "job_type_ids": [ 1 ],
          "name": "Commercial Installs",
          "start": "2016-08-05",
          "available": true,
          "infinite_repetitions": false,
          "repetitions": 90,
          "weeks": 1
        },
        {
          "id": 4,
          "user_ids": [ 2, 3 ],
          "name": "Residential Installs",
          "start": "2016-08-05",
          "available": true,
          "infinite_repetitions": true,
          "repetitions": 1,
          "weeks": 3
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

## Get an individual schedule blocker (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers/:id`
- **Description**: Get an individual schedule blocker
- **Parameters**:
    - `id` (Integer, required): The ID of the schedule blocker
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "name": "brunch",
        "sunday": false,
        "monday": true,
        "tuesday": false,
        "wednesday": false,
        "thursday": false,
        "friday": false,
        "saturday": false,
        "start_timestamp": "13:55",
        "end_timestamp": "14:30",
        "user_ids": [
          1
        ],
        "start": "2017-01-01",
        "weeks": 1,
        "repetitions": 1,
        "infinite_repetitions": true
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

## Get an individual schedule day/time (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:schedule_id/schedule_days/:id`
- **Description**: Get an individual schedule day/time
- **Parameters**:
    - `schedule_id` (Number, required): The ID of the schedule that contains this day/time
    - `id` (Number, required): The ID of the schedule day/time
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
         "id": 9,
         "day": 1,
         "start_timestamp": "00:00",
         "end_timestamp": "23:00"
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

## Get an individual schedule (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:id`
- **Description**: Get an individual schedule
- **Parameters**:
    - `id` (Number, required): The ID of the schedule
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "user_ids": [ 1 ],
        "job_type_ids": [ 1, 2 ],
        "name": "Test",
        "start": "2016-08-05",
        "available": true,
        "infinite_repetitions": false,
        "repetitions": 1,
        "weeks": 3
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

## Get an individual scheduled time off (GET)
- **Version**: 0.7.2
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/scheduled_time_offs/:id`
- **Description**: Get an individual scheduled time off
- **Parameters**:
    - `id` (Integer, required): The ID of the scheduled time off
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 10,
        "user_id": 1,
        "start_time": "2016-11-01 01:00:00",
        "end_time": "2016-11-01 01:30:00",
        "name": "test"
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

## Get the calculated schedule for a date range (GET)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/calculated_schedule/:start_date/:end_date`
- **Description**: This function will calculate out the availability for all scheduled users, between :start_date and :end_date. It will also include all jobs scheduled within those times. This is a fairly complex data structure that is designed to be used to allow easier integration into external display/scheduling systems.
- **Parameters**:
    - `start_date` (Date, required): The start date for this query, in the system timezone.
    - `end_date` (Date, required): The end date for this query, in the system timezone.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "2017-02-06": {
          "1": {
            "schedule": {
              "1": [
                {
                  "start": "00:00",
                  "end": "23:59"
                }
              ]
            },
            "jobs": [
              {
                "id": 2,
                "scheduled_datetime": "2017-02-06 12:53",
                "job_type_id": 1,
                "length_in_minutes": 60,
                "ticket_id": null,
                "assigned_type": "accounts",
                "assigned_id": 1,
                "notes": "",
                "status": "scheduled",
                "user_ids": [
                  1
                ],
                "created_by_user_id": 1,
                "checked_in_users": [],
                "services": []
              },
              {
                "id": 5,
                "scheduled_datetime": "2017-02-06 17:43",
                "job_type_id": 1,
                "length_in_minutes": 60,
                "ticket_id": null,
                "assigned_type": "accounts",
                "assigned_id": 35,
                "notes": "",
                "status": "scheduled",
                "user_ids": [
                  1
                ],
                "created_by_user_id": 1,
                "checked_in_users": [],
                "services": []
              },
              {
                "id": 4,
                "scheduled_datetime": "2017-02-06 08:00",
                "job_type_id": 1,
                "length_in_minutes": 60,
                "ticket_id": null,
                "assigned_type": "accounts",
                "assigned_id": 35,
                "notes": "",
                "status": "scheduled",
                "user_ids": [
                  1
                ],
                "created_by_user_id": 1,
                "checked_in_users": [],
                "services": []
              }
            ],
            "schedule_blockers": [
              {
                "start": "10:30",
                "end": "11:30",
                "name": "Brunch",
                "id": 2,
                "overridden": true,
                "uniqueid": "2_1"
              },
              {
                "start": "00:00",
                "end": "00:45",
                "name": "Break",
                "id": 7,
                "overridden": false,
                "uniqueid": "7_1"
              },
              {
                "start": "00:00",
                "end": "00:30",
                "name": "Lunch",
                "id": 8,
                "overridden": false,
                "uniqueid": "8_1"
              }
            ]
          }
        },
        "2017-02-07": {
          "1": {
            "schedule": {
              "1": [
                {
                  "start": "00:00",
                  "end": "23:59"
                }
              ]
            },
            "jobs": [],
            "schedule_blockers": [
              {
                "start": "00:00",
                "end": "00:45",
                "name": "Break",
                "id": 7,
                "overridden": false,
                "uniqueid": "7_1"
              },
              {
                "start": "00:00",
                "end": "00:30",
                "name": "Lunch",
                "id": 8,
                "overridden": false,
                "uniqueid": "8_1"
              }
            ]
          }
        }
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": "schedule day/time does not exist.",
            "status_code": 404
        }
    }
    ```

## Override a schedule blocker (POST)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers/:id/schedule_blocker_overrides`
- **Description**: Override a schedule blocker for a single user
- **Parameters**:
    - `id` (Integer, required): The ID of the blocker
    - `date` (Date, required): The date you wish to override the blocker for
    - `start_timestamp` (Time, required): The start of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `end_timestamp` (Time, required): The end of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `user_id` (Integer, required): The ID of the user you wish to override the blocker time for
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "date": "2017-02-06",
        "start_timestamp": "10:30",
        "end_timestamp": "11:30",
        "user_id": "1",
        "schedule_blocker_id": 2
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

## Update schedule blocker (PATCH)
- **Version**: 1.1.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedule_blockers/:id`
- **Description**: Update an existing schedule blocker.
- **Parameters**:
    - `id` (Integer, required): The ID of the blocker
    - `name` (String, optional): A name for the schedule blocker
    - `sunday` (Boolean, optional): true if this schedule blocks on Sunday, false if not
    - `monday` (Boolean, optional): true if this schedule blocks on Monday, false if not
    - `tuesday` (Boolean, optional): true if this schedule blocks on Tuesday, false if not
    - `wednesday` (Boolean, optional): true if this schedule blocks on Wednesday, false if not
    - `thursday` (Boolean, optional): true if this schedule blocks on Thursday, false if not
    - `friday` (Boolean, optional): true if this schedule blocks on Friday, false if not
    - `saturday` (Boolean, optional): true if this schedule blocks on Saturday, false if not
    - `start_timestamp` (Time, optional): The start of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `end_timestamp` (Time, optional): The end of the blocker, expressed as H:m where H is in 24 hour time, and m is minutes (e.g. 13:40)
    - `user_ids` (Array, optional): An array of user IDs that this blocker should apply to
    - `start` (Date, optional): The start date for this blocker
    - `weeks` (Integer, optional): The frequency of repetition for this blocker. If this is 1, it repeats weekly. If this is 2, it repeats every other week.
    - `repetitions` (Integer, optional): How many times this blocker repeats. Ignored if infinite_repetitions is true
    - `infinite_repetitions` (Boolean, optional): If this is true, this blocker repeats forever
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2
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

## Update schedule day/time (PATCH)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:schedule_id/schedule_days/:id`
- **Description**: Update an existing schedule day/time.
- **Parameters**:
    - `schedule_id` (Number, required): The ID of the schedule that contains this day/time
    - `id` (Number, required): The schedule day/time ID
    - `day` (Number, optional): The day of the week for this scheduled day/time, where 0 is Sunday and 6 is Saturday. (`0`, `1`, `2`, `3`, `4`, `5`, `6`)
    - `start_timestamp` (Time, optional): The starting time for this particular period, in Hour:Minute format, where minute must be in 15 minute increments. This is in the Sonar timezone, not UTC.
    - `end_timestamp` (Time, optional): The ending time for this particular period, in Hour:Minute format, where minute must be in 15 minute increments. This is in the Sonar timezone, not UTC.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
         "id": 9,
         "day": 1,
         "start_timestamp": "00:00",
         "end_timestamp": "23:00"
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

## Update schedule (PATCH)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/schedules/:id`
- **Description**: Update an existing schedule.
- **Parameters**:
    - `name` (String, optional): A name for the schedule
    - `user_ids` (Array, optional): An array of user IDs that this schedule is applied to
    - `job_type_ids` (Array, optional): An array of job type IDs that this time is for. Only jobs with this job type will be allowed to be scheduled in this container
    - `start` (Date, optional): The date that the schedule should start to be applied, in the local system timezone. YYYY-MM-DD format.
    - `available` (Boolean, optional): Whether this schedule defines availability, or lack of availability. A schedule with available set to false will always override another schedule with available set to true.
    - `infinite_repetitions` (Boolean, optional): Set this to true if you want this schedule to run indefinitely
    - `repetitions` (Number, optional): How many times this schedule should repeat. 0 to never repeat. You can set this to a high number to repeat indefinitely (e.g. 2147483647)
    - `weeks` (Number, optional): How often the repetition should occur, in weeks. If this is 1, it repeats weekly. If this is 2, the schedule runs for one week, then breaks for one week, then runs for one week, then breaks for two weeks, etc. If this is 3, the schedule runs for one week, then breaks for two weeks, then runs for one week, then breaks for two weeks, etc. This interacts with repetitions by repeating repetitions times for the number of active weeks. For example, if weeks is 2, and repetitions is 1, this schedule would run for a week, skip a week, run for a week, and then stop.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 6,
        "user_ids": [ 1 ],
        "job_type_ids": [ 1, 2, 3 ],
        "name": "Test",
        "start": "2016-08-05",
        "available": true,
        "infinite_repetitions": true,
        "repetitions": 1,
        "weeks": 3
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

## Update scheduled time off (PATCH)
- **Version**: 0.7.2
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/scheduled_time_offs/:id`
- **Description**: Update an existing scheduled time off.
- **Parameters**:
    - `user_id` (Integer, optional): The ID of the user that has time off scheduled
    - `start_time` (DateTime, optional): The day and time that the user has scheduled off, in the system timezone.
    - `end_time` (DateTime, optional): The day and time that the user has scheduled off, in the system timezone.
    - `name` (String, optional): A description/reason for the time off.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 10,
        "user_id": 1,
        "start_time": "2016-11-01 01:00:00",
        "end_time": "2016-11-01 02:00:00",
        "name": "Update me"
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

</final_file_content>

IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your SEARCH/REPLACE operations on this final version to ensure accuracy.<environment_details>
# VSCode Visible Files
docs/schedules.md

# VSCode Open Tabs
memory-bank/activeContext.md
memory-bank/progress.md
docs/account_billing.md
docs/account_call_logs.md
docs/account_call_records.md
docs/account_contacts.md
docs/account_dids.md
docs/account_data_usage.md
docs/account_ip_addresses.md
docs/account_inventory.md
docs/account_invoices.md
docs/account_payment_methods.md
docs/account_services.md
docs/account_tax_overrides.md
docs/account_transactions.md
docs/accounts.md
docs/address_lists.md
docs/alerting_rotations.md
docs/cdrs.md
docs/contracts.md
docs/custom_fields.md
docs/customer_portal.md
docs/data.md
docs/files.md
docs/financial.md
docs/general_ledger_codes.md
docs/ipam.md
docs/inbound_email_accounts.md
docs/inline_devices.md
docs/inventory_assignees.md
docs/inventory_depletion_thresholds.md
docs/inventory_items.md
docs/inventory_location_addresses.md
docs/invoice_messages.md
docs/job_types.md
docs/jobs.md
docs/mapping.md
docs/monitoring_data.md
docs/monitoring_templates.md
docs/network_site_ip_addresses.md
docs/network_site_inventory.md
docs/network_sites.md
docs/notes.md
docs/packages.md
docs/radius_accounts.md
docs/radius_groups.md
docs/rate_centers.md
docs/roles.md
docs/scheduled_events.md
docs/schedules.md

# Current Time
6/28/2025, 1:26:40 PM (UTC, UTC+0:00)

# Context Window Usage
869,010 / 1,048.576K tokens used (83%)

# Current Mode
ACT MODE
```
