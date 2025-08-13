# RADIUS Groups Endpoints

## Create a new RADIUS group (POST)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups`

Description: Create a new RADIUS group. If there is an enabled RADIUS server in good status in Sonar, this group will immediately be created on it with appropriate accounts associated.
#### Request Example
```json
{
  "name": "example",
  "priority": 1,
  "delinquent": 1,
  "active": 1,
  "fall_through": true,
  "account_groups": [],
  "account_types": [],
  "services": [],
  "account_statuses": []
}
```

```
Parameter
Field	Type	Description
name	String
The name of the RADIUS group

priority	Number
The priority for this RADIUS group

delinquentoptional	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

Default value: 3

activeoptional	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

Default value: 3

fall_throughoptional	Boolean
Whether fall-through is enabled or not on this RADIUS group.

Default value: false

account_groupsoptional	Array
An array of account group IDs that are a relation to this RADIUS group.

account_typesoptional	Array
An array of account type IDs that are a relation to this RADIUS group.

servicesoptional	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statusesoptional	Array
An array of account status IDs that are a relation to this RADIUS group.

Success 200
Field	Type	Description
id	Number
The ID of the RADIUS group

name	String
The name of the RADIUS group

priority	Number
The priority for this RADIUS group

delinquent	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

active	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

fall_through	Boolean
Whether fall-through is enabled or not on this RADIUS group.

account_groups	Array
An array of account group IDs that are a relation to this RADIUS group.

account_types	Array
An array of account type IDs that are a relation to this RADIUS group.

services	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statuses	Array
An array of account status IDs that are a relation to this RADIUS group.

Success-Response:
 HTTP/1.1 201 OK
 {
  "data": {
    "id": 7,
    "name": "My Group Name?",
    "priority": 15,
    "active": 3,
    "delinquent": 2,
    "fall_through": true,
    "account_groups": [],
    "account_types": [
      1
    ],
    "services": [
      2,
      1
    ],
    "account_statuses": []
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
             "name": "The RADIUS group name has already been taken.",
         },
         "status_code": 422
     }
 }
```

## Create a new reply attribute (POST)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id/attributes`

Description: Create a new RADIUS group reply attribute. If there is an enabled RADIUS server in good status in Sonar, this attribute will immediately be created on it with appropriate groups associated.
#### Request Example
```json
{
  "attribute": "example",
  "operator": "example",
  "reply": "example"
}
```

```
Parameter
Field	Type	Description
attribute	String
The attribute name

operator	String
The operator for the attribute

Allowed values: "=", ":=", "+="

reply	String
The reply value for the attribute

Success 200
Field	Type	Description
id	Number
The ID of the attribute

attribute	String
The attribute name

operator	String
The operator for the attribute

reply	String
The reply value for the attribute

Success-Response:
 HTTP/1.1 201 OK
 {
  "data": {
    "id": 3,
    "attribute": "Some Other Attribute",
    "operator": "+=",
    "reply": "Some Other Value"
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
             "name": "Attribute test123 is duplicated. You may only include each attribute once.",
         },
         "status_code": 422
     }
 }
```

## Delete RADIUS group (DELETE)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id`

Description: Delete a RADIUS group. This will immediately remove the group from your RADIUS server, if it is enabled and in a good status.
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
The ID of the RADIUS group.

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
A reason as to why the RADIUS group could not be deleted

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": {
             "message": "RADIUS group does not exist."
         },
         "status_code": 404
     }
 }
```

## Delete reply attribute (DELETE)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id/attributes/:attribute_id`

Description: Delete a RADIUS group reply attribute.
#### Request Example
```json
{
  "id": 1,
  "attribute_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the RADIUS group

attribute_id	Number
The ID of the attribute

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
A reason as to why the RADIUS reply attribute could not be deleted

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": {
             "message": "RADIUS reply attribute does not exist."
         },
         "status_code": 404
     }
 }
```

## Get all RADIUS groups (GET)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups`

Description: Get a list of RADIUS groups.
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
The ID of the RADIUS group

name	String
The name of the RADIUS group

priority	Number
The priority for this RADIUS group

delinquent	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

active	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

fall_through	Boolean
Whether fall-through is enabled or not on this RADIUS group.

account_groups	Array
An array of account group IDs that are a relation to this RADIUS group.

account_types	Array
An array of account type IDs that are a relation to this RADIUS group.

services	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statuses	Array
An array of account status IDs that are a relation to this RADIUS group.

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 1,
      "name": "Delinquent",
      "priority": 1,
      "active": 3,
      "delinquent": 1,
      "fall_through": false,
      "account_groups": [],
      "account_types": [
        2,
        1
      ],
      "services": [],
      "account_statuses": []
    },
    {
      "id": 2,
      "name": "Commercial With Platinum Data Service",
      "priority": 2,
      "active": 3,
      "delinquent": 3,
      "fall_through": true,
      "account_groups": [],
      "account_types": [
        2
      ],
      "services": [
        1
      ],
      "account_statuses": []
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

## Get all reply attributes (GET)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id/attributes`

Description: Get a list of of attributes for a specific group.
#### Request Example
```json
{
  "id": 1,
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the RADIUS group

limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The ID of the attribute

attribute	String
The attribute name

operator	String
The operator for the attribute

reply	String
The reply value for the attribute

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 3,
      "attribute": "Some Other Attribute",
      "operator": "+=",
      "reply": "Some Other Value"
    },
    {
      "id": 2,
      "attribute": "Some Attribute",
      "operator": "=",
      "reply": "Some Value"
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

## Get individual RADIUS group (GET)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id`

Description: Get an individual RADIUS group.
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
The ID of the RADIUS group

Success 200
Field	Type	Description
id	Number
The ID of the RADIUS group

name	String
The name of the RADIUS group

priority	Number
The priority for this RADIUS group

delinquent	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

active	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

fall_through	Boolean
Whether fall-through is enabled or not on this RADIUS group.

account_groups	Array
An array of account group IDs that are a relation to this RADIUS group.

account_types	Array
An array of account type IDs that are a relation to this RADIUS group.

services	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statuses	Array
An array of account status IDs that are a relation to this RADIUS group.

Success-Response:
 HTTP/1.1 200 OK
 {
  "data": {
    "id": 7,
    "name": "My Group Name?",
    "priority": 15,
    "active": 3,
    "delinquent": 2,
    "fall_through": true,
    "account_groups": [],
    "account_types": [
      1
    ],
    "services": [
      2,
      1
    ],
    "account_statuses": []
  }
}
```

## Get individual reply attribute (GET)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id/attributes/:attribute_id`

Description: Get an individual RADIUS group.
#### Request Example
```json
{
  "id": 1,
  "attribute_id": 1
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the RADIUS group

attribute_id	Number
The ID of the attribute

Success 200
Field	Type	Description
id	Number
The ID of the attribute

attribute	String
The attribute name

operator	String
The operator for the attribute

reply	String
The reply value for the attribute

Success-Response:
 HTTP/1.1 200 OK
 {
  "data": {
    "id": 3,
    "attribute": "Some Other Attribute",
    "operator": "+=",
    "reply": "Some Other Value"
  }
}
```

## Update RADIUS group (PATCH)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id`

Description: Update a RADIUS group.
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "priority": 1,
  "delinquent": 1,
  "active": 1,
  "fall_through": true,
  "account_groups": [],
  "account_types": [],
  "services": [],
  "account_statuses": []
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the RADIUS group

nameoptional	String
The name of the RADIUS group

priorityoptional	Number
The priority for this RADIUS group

delinquentoptional	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

Default value: 3

activeoptional	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

Default value: 3

fall_throughoptional	Boolean
Whether fall-through is enabled or not on this RADIUS group.

Default value: false

account_groupsoptional	Array
An array of account group IDs that are a relation to this RADIUS group.

account_typesoptional	Array
An array of account type IDs that are a relation to this RADIUS group.

servicesoptional	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statusesoptional	Array
An array of account status IDs that are a relation to this RADIUS group.

Success 200
Field	Type	Description
id	Number
The ID of the RADIUS group

name	String
The name of the RADIUS group

priority	Number
The priority for this RADIUS group

delinquent	Number
If this is 1, the group is only applied to delinquent accounts. If this is 2, it is only applied to accounts that are not delinquent. If it is 3, delinquency is not checked.

active	Number
If this is 1, the group is only applied to accounts with an active status. If this is 2, it is only applied to accounts that have a non-active status. If it is 3, the active flag on the status is not checked.

fall_through	Boolean
Whether fall-through is enabled or not on this RADIUS group.

account_groups	Array
An array of account group IDs that are a relation to this RADIUS group.

account_types	Array
An array of account type IDs that are a relation to this RADIUS group.

services	Array
An array of data service IDs that are a relation to this RADIUS group.

account_statuses	Array
An array of account status IDs that are a relation to this RADIUS group.

Success-Response:
 HTTP/1.1 200 OK
 {
  "data": {
    "id": 7,
    "name": "My Group Name?",
    "priority": 15,
    "active": 3,
    "delinquent": 2,
    "fall_through": true,
    "account_groups": [],
    "account_types": [
      1
    ],
    "services": [
      2,
      1
    ],
    "account_statuses": []
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
             "name": "The name has already been taken."
         },
         "status_code": 422
     }
 }
```

## Update reply attribute (PATCH)
Version: 0.4.3

Endpoint: `https://example.sonar.software/api/v1/network/provisioning/radius_groups/:id/attributes/:attribute_id`

Description: Update a RADIUS group reply attribute.
#### Request Example
```json
{
  "id": 1,
  "attribute_id": 1,
  "attribute": "example",
  "operator": "example",
  "reply": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the RADIUS group

attribute_id	Number
The ID of the attribute

attributeoptional	String
The attribute name

operatoroptional	String
The operator for the attribute

Allowed values: "=", ":=", "+="

replyoptional	String
The reply value for the attribute

Success 200
Field	Type	Description
id	Number
The ID of the attribute

attribute	String
The attribute name

operator	String
The operator for the attribute

reply	String
The reply value for the attribute

Success-Response:
 HTTP/1.1 200 OK
 {
  "data": {
    "id": 3,
    "attribute": "Some Other Attribute",
    "operator": "+=",
    "reply": "Some Other Value"
  }
}
Rate Centers
```
