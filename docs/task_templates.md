# Task Templates Endpoints

## Create a new task template (POST)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates`

Description: Create a new task template.
#### Request Example
```json
{
  "name": "example"
}
```

```
Parameter
Field	Type	Description
name	String
A name for the task template

Success 200
Field	Type	Description
id	Number
The ID of the task template.

name	String
The name of the task template

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "Some test name",
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
       "name": "The name must be unique."
     },
     "status_code": 422
   }
 }
```

## Create a new template task. (POST)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id/template_tasks`

Description: Create a new template task. A template task is a task contained within a task template.
#### Request Example
```json
{
  "name": "example"
}
```

```
Parameter
Field	Type	Description
name	String
A name for the template task

Success 200
Field	Type	Description
id	Number
The ID of the task template.

task	String
The name of the task

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "task": "Wash the dishes",
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
       "name": "The name must be unique."
     },
     "status_code": 422
   }
 }
```

## Delete a task template (DELETE)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id`

Description: Delete a task template
#### Request Example
```json
{
  "id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the task template

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
A reason as to why the task template could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "task template does not exist.",
         "status_code": 404
     }
 }
```

## Delete a template task. (DELETE)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id/template_tasks/:template_task_id`

Description: Delete a template task. A template task is a task contained within a task template.
#### Request Example
```json
{
  "id": 1,
  "template_task_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the task template

template_task_id	Number
The ID of the template task

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
A reason as to why the template task could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "template task does not exist.",
         "status_code": 404
     }
 }
```

## Get all task templates (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates`

Description: Get all task templates
#### Request Example
```json
{
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The ID of the task template.

name	String
The name of the task template

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 2,
      "name": "Installation tasks"
    },
    {
      "id": 1,
      "name": "Service call tasks"
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

## Get all template tasks. (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id/template_tasks`

Description: Get all template tasks. A template task is a task contained within a task template.
#### Request Example
```json
{
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The ID of the task template.

task	String
The name of the task

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 7,
      "task": "Do something"
    },
    {
      "id": 6,
      "task": "test"
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

## Get an individual task template (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id`

Description: Get an individual task template
#### Request Example
```json
{
  "id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the task template

Success 200
Field	Type	Description
id	Number
The ID of the task template.

name	String
The name of the task template

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "Some random tasks"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
404

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
```

## Get an individual template task. (GET)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id/template_tasks/:template_task_id`

Description: Get an individual template task. A template task is a task contained within a task template.
#### Request Example
```json
{
  "id": 1,
  "template_task_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the task template

template_task_id	Number
The ID of the template task

Success 200
Field	Type	Description
id	Number
The ID of the template task.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 7,
    "task": "Do something"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
404

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
```

## Update task template (PATCH)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id`

Description: Update an existing task template.
#### Request Example
```json
{
  "id": 1,
  "name": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The task template ID

nameoptional	String
The name of the task template

Success 200
Field	Type	Description
id	Number
The ID of the task template.

name	String
The name of the task template

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "A bunch of tasks"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
```

## Update template task. (PATCH)
Version: 0.7.0

Endpoint: `https://example.sonar.software/api/v1/system/misc/task_templates/:id/template_tasks/:task_template_id`

Description: Update an existing template task. A template task is a task contained within a task template.
#### Request Example
```json
{
  "id": 1,
  "template_task_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The task template ID

template_task_id	Number
The template task ID

Success 200
Field	Type	Description
id	Number
The ID of the template task.

task	String
The task

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "task": "Jump rope"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
Tasks
```
