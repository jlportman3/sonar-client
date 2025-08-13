# Job Types Endpoints

## Create a new job type (POST)
- **Version**: 1.2.19
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/job_types`
- **Description**: Create a new job type.
- **Parameters**:
    - `name` (String, required): The name of the job type
    - `length_in_minutes` (Integer, required): The default length of time assigned for jobs of this type to be completed
    - `color` (String, required): The color of the job type on the schedule (`"blue"`, `"green"`, `"red"`, `"purple"`, `"yellow"`, `"orange"`, `"grey"`)
    - `icon` (String, required): The icon shown on jobs of this type on the schedule (`"smile"`, `"frown"`, `"graph"`, `"jellyfish"`, `"car"`, `"folder"`, `"cookie"`, `"book"`, `"dna"`, `"box"`)
    - `change_status_on_completion` (Boolean, optional): Set this to true if you want the status on an account to be changed when jobs of this type are completed
    - `account_status_id_completion` (Integer, optional): If `change_status_on_completion` is true, this is the account status ID that the account will be changed to when jobs of this type are completed
    - `change_status_on_failure` (Boolean, optional): Set this to true if you want the status on an account to be changed when jobs of this type are failed
    - `account_status_id_failure` (Integer, optional): If `change_status_on_failure` is true, this is the account status ID the account will be changed to when jobs of this type are failed
    - `create_completion_ticket` (Boolean, optional): If this is true, a ticket will be created when jobs of this type are completed
    - `completion_ticket_group_id` (Integer, optional): If `create_completion_ticket` is true, then tickets created on completion will be assigned to this ticket group ID
    - `create_failure_ticket` (Boolean, optional): If this is true, a ticket will be created when jobs of this type are failed
    - `failure_ticket_group_id` (Integer, optional): If `create_failure_ticket` is true, then tickets created on failure will be assigned to this ticket group ID
    - `allow_completion_with_uncompleted_tasks` (Boolean, optional): If this is false, jobs of this type cannot be completed while they have uncompleted tasks on them
    - `task_template_id` (Integer, optional): Setting a task template on a job type will automatically create all tasks defined in the template on jobs created of this type
    - `services` (Array, optional): An array of service IDs. If service IDs are set here, when jobs of this type are completed while assigned to an account, the account will have all services listed here added to it or charged to it. Only allows recurring, expiring, or one time services.
    - `contract_template_id` (Integer, optional): Setting a contract template ID on a job type will automatically add this contract to an account when a job of this type is scheduled.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 6,
        "name": "Donut Run",
        "length_in_minutes": 15,
        "color": "orange",
        "icon": "cookie",
        "change_status_on_completion": false,
        "account_status_id_completion": null,
        "change_status_on_failure": false,
        "account_status_id_failure": null,
        "create_completion_ticket": false,
        "completion_ticket_group_id": null,
        "create_failure_ticket": false,
        "failure_ticket_group_id": null,
        "allow_completion_with_uncompleted_tasks": true,
        "task_template_id": null,
        "services": [],
        "contract_template_id": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "account_status_id_completion": "The account status id completion field is required when change status on completion is 1."
         },
         "status_code": 422
       }
    }
    ```

## Delete a job type (DELETE)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/job_types/:id`
- **Description**: Delete a job type
- **Parameters**:
    - `id` (Integer, required): The ID of the job type
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
            "message": "job type does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all job types (GET)
- **Version**: 1.2.19
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/job_types`
- **Description**: Get all job types
- **Parameters**:
    - `limit` (Integer, optional): The number of entries to return
    - `page` (Integer, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "name": "Installation",
          "length_in_minutes": 90,
          "color": "blue",
          "icon": "smile",
          "change_status_on_completion": false,
          "account_status_id_completion": null,
          "change_status_on_failure": false,
          "account_status_id_failure": null,
          "create_completion_ticket": false,
          "completion_ticket_group_id": null,
          "create_failure_ticket": false,
          "failure_ticket_group_id": null,
          "allow_completion_with_uncompleted_tasks": false,
          "task_template_id": null,
          "services": [],
          "contract_template_id": 1
        },
        {
          "id": 2,
          "name": "Service Call",
          "length_in_minutes": 120,
          "color": "orange",
          "icon": "book",
          "change_status_on_completion": false,
          "account_status_id_completion": null,
          "change_status_on_failure": false,
          "account_status_id_failure": null,
          "create_completion_ticket": false,
          "completion_ticket_group_id": null,
          "create_failure_ticket": false,
          "failure_ticket_group_id": null,
          "allow_completion_with_uncompleted_tasks": false,
          "task_template_id": null,
          "services": [],
          "contract_template_id": null
        },
        {
          "id": 3,
          "name": "Job with services",
          "length_in_minutes": 15,
          "color": "purple",
          "icon": "folder",
          "change_status_on_completion": true,
          "account_status_id_completion": 4,
          "change_status_on_failure": true,
          "account_status_id_failure": 3,
          "create_completion_ticket": true,
          "completion_ticket_group_id": 1,
          "create_failure_ticket": true,
          "failure_ticket_group_id": 1,
          "allow_completion_with_uncompleted_tasks": false,
          "task_template_id": null,
          "services": [
            9,
            8
          ],
          "contract_template_id": null
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

## Get an individual job type (GET)
- **Version**: 1.2.19
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/job_types/:id`
- **Description**: Get an individual job type
- **Parameters**:
    - `id` (Integer, required): The ID of the job type
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 1,
        "name": "Installation",
        "length_in_minutes": 90,
        "color": "blue",
        "icon": "smile",
        "change_status_on_completion": false,
        "account_status_id_completion": null,
        "change_status_on_failure": false,
        "account_status_id_failure": null,
        "create_completion_ticket": false,
        "completion_ticket_group_id": null,
        "create_failure_ticket": false,
        "failure_ticket_group_id": null,
        "allow_completion_with_uncompleted_tasks": false,
        "task_template_id": null,
        "services": [],
        "contract_template_id": null
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

## Update job type (PATCH)
- **Version**: 1.2.19
- **Endpoint**: `https://example.sonar.software/api/v1/scheduling/job_types/:id`
- **Description**: Update an existing job type.
- **Parameters**:
    - `id` (Integer, required): The ID of the job type
    - `name` (String, optional): The name of the job type
    - `length_in_minutes` (Integer, optional): The default length of time assigned for jobs of this type to be completed
    - `color` (String, optional): The color of the job type on the schedule (`"blue"`, `"green"`, `"red"`, `"purple"`, `"yellow"`, `"orange"`, `"grey"`)
    - `icon` (String, optional): The icon shown on jobs of this type on the schedule (`"smile"`, `"frown"`, `"graph"`, `"jellyfish"`, `"car"`, `"folder"`, `"cookie"`, `"book"`, `"dna"`, `"box"`)
    - `change_status_on_completion` (Boolean, optional): Set this to true if you want the status on an account to be changed when jobs of this type are completed
    - `account_status_id_completion` (Integer, optional): If `change_status_on_completion` is true, this is the account status ID that the account will be changed to when jobs of this type are completed
    - `change_status_on_failure` (Boolean, optional): Set this to true if you want the status on an account to be changed when jobs of this type are failed
    - `account_status_id_failure` (Integer, optional): If `change_status_on_failure` is true, this is the account status ID the account will be changed to when jobs of this type are failed
    - `create_completion_ticket` (Boolean, optional): If this is true, a ticket will be created when jobs of this type are completed
    - `completion_ticket_group_id` (Integer, optional): If `create_completion_ticket` is true, then tickets created on completion will be assigned to this ticket group ID
    - `create_failure_ticket` (Boolean, optional): If this is true, a ticket will be created when jobs of this type are failed
    - `failure_ticket_group_id` (Integer, optional): If `create_failure_ticket` is true, then tickets created on failure will be assigned to this ticket group ID
    - `allow_completion_with_uncompleted_tasks` (Boolean, optional): If this is false, jobs of this type cannot be completed while they have uncompleted tasks on them
    - `task_template_id` (Integer, optional): Setting a task template on a job type will automatically create all tasks defined in the template on jobs created of this type
    - `services` (Array, optional): An array of service IDs. If service IDs are set here, when jobs of this type are completed while assigned to an account, the account will have all services listed here added to it or charged to it. Only allows recurring, expiring, or one time services.
    - `contract_template_id` (Integer, optional): Setting a contract template ID on a job type will automatically add this contract to an account when a job of this type is scheduled.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 6,
        "name": "Donut Walk",
        "length_in_minutes": 15,
        "color": "orange",
        "icon": "cookie",
        "change_status_on_completion": false,
        "account_status_id_completion": null,
        "change_status_on_failure": false,
        "account_status_id_failure": null,
        "create_completion_ticket": false,
        "completion_ticket_group_id": null,
        "create_failure_ticket": false,
        "failure_ticket_group_id": null,
        "allow_completion_with_uncompleted_tasks": true,
        "task_template_id": null,
        "services": [],
        "contract_template_id": null
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
