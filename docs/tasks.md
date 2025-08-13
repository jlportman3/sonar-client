# Tasks Endpoints

## Attach a task to an entity (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/:entity/:id/tasks`

Description: Attach a task to an entity.
#### Request Example
```json
{
  "id": 1,
  "entity": "example",
  "description": "example",
  "user_id": 1,
  "due_date": "2024-01-01"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the entity

entity	String
The entity to attach to.

Allowed values: "tickets", "accounts", "network_sites", "jobs"

description	String
A description of the task

user_idoptional	Number
The ID of a user you want to assign this task to

due_dateoptional	Date
The date the task is due

Success 200
Field	Type	Description
id	Number
The ID of the task

description	String
The description of the task

user_id	Number
The ID of the user assigned to the task

due_date	Date
The date the task is due

complete	Boolean
Whether or not the task has been completed

completed_by	String
The user ID of the person who completed the task, if it has been completed

completed_at	DateTime
The date and time in UTC that the task was completed, if it has been completed

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 4,
    "description": "Build a space elevator.",
    "user_id": 2,
    "due_date": "2016-01-02",
    "complete": false,
    "completed_by": null,
    "completed_at": null
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
       "id": "The ID must be an integer."
     },
     "status_code": 422
   }
 }
```

## Delete a task (DELETE)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/:entity/:id/tasks/:task_id`

Description: Delete a task from an entity.
#### Request Example
```json
{
  "id": 1,
  "entity": "example",
  "task_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the entity

entity	String
The entity

Allowed values: "tickets", "accounts", "network_sites", "jobs"

task_id	Number
The ID of the task

Success 200
Field	Type	Description
success	Boolean
Will be true if deletion succeeded.

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
A reason as to why the task could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "Task does not exist.",
         "status_code": 404
     }
 }
```

## Get all tasks on an entity (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/:entity/:id/tasks`

Description: Get all tasks on an entity.
#### Request Example
```json
{
  "limit": 1,
  "page": 1,
  "id": 1,
  "entity": "example"
}
```

```
Parameter
Field	Type	Description
limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

id	Number
The ID of the entity

entity	String
The entity

Allowed values: "tickets", "accounts", "network_sites", "jobs"

Success 200
Field	Type	Description
id	Number
The ID of the task

description	String
The description of the task

user_id	Number
The ID of the user assigned to the task

due_date	Date
The date the task is due

complete	Boolean
Whether or not the task has been completed

completed_by	String
The user ID of the person who completed the task, if it has been completed

completed_at	DateTime
The date and time in UTC that the task was completed, if it has been completed

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 5,
      "description": "Here's a description of what I want you to do.",
      "user_id": 1,
      "due_date": "2016-05-03",
      "complete": false,
      "completed_by": null,
      "completed_at": null
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

## Get an individual task (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/:entity/:id/tasks/:task_id`

Description: Get an individual task.
#### Request Example
```json
{
  "id": 1,
  "entity": "example",
  "task_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the entity

entity	String
The entity

Allowed values: "tickets", "accounts", "network_sites", "jobs"

task_id	Number
The ID of the task

Success 200
Field	Type	Description
id	Number
The ID of the task

description	String
The description of the task

user_id	Number
The ID of the user assigned to the task

due_date	Date
The date the task is due

complete	Boolean
Whether or not the task has been completed

completed_by	String
The user ID of the person who completed the task, if it has been completed

completed_at	DateTime
The date and time in UTC that the task was completed, if it has been completed

Success-Response:
 HTTP/1.1 200 OK
 {
  "data": {
    "id": 7,
    "description": "Here's a description of what I want you to do.",
    "user_id": 1,
    "due_date": "2016-05-03",
    "complete": false,
    "completed_by": null,
    "completed_at": null
  }
}
```

## Update a task (PATCH)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/:entity/:id/tasks/:task_id`

Description: Update an existing task.
#### Request Example
```json
{
  "id": 1,
  "entity": "example",
  "task_id": 1,
  "description": "example",
  "user_id": 1,
  "due_date": "2024-01-01",
  "complete": true
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the entity

entity	String
The entity

Allowed values: "tickets", "accounts", "network_sites", "jobs"

task_id	Number
The ID of the task

descriptionoptional	String
A description of the task

user_idoptional	Number
The ID of a user you want to assign this task to

due_dateoptional	Date
The date the task is due

completeoptional	Boolean
Set to true if the task is complete, or false if not.

Success 200
Field	Type	Description
id	Number
The ID of the task

description	String
The description of the task

user_id	Number
The ID of the user assigned to the task

due_date	Date
The date the task is due

complete	Boolean
Whether or not the task has been completed

completed_by	String
The user ID of the person who completed the task, if it has been completed

completed_at	DateTime
The date and time in UTC that the task was completed, if it has been completed

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 7,
    "description": "Here's a description of what I want you to do.",

    "user_id": 1,
    "due_date": "2016-05-03",
    "complete": true,
    "completed_by": 1,
    "completed_at": "2016-05-02 23:59:59"
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
       "id": "The ID must be an integer."
     },
     "status_code": 422
   }
 }
Ticket Categories
```
