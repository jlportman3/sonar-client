# Inbound Email Accounts Endpoints

## Create a new inbound email account (POST)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/inbound_email_accounts`

Description: Create a new inbound email account.
#### Request Example
```json
{
  "name": "example",
  "reply_address": "example",
  "reply_name": "example",
  "enabled": true,
  "user_id": 1,
  "ticket_group_id": 1,
  "priority": 1,
  "reply": "example",
  "signature": "example",
  "automatic_spam_filtering": true,
  "minimum_spam_score": 1,
  "days_before_spam_deletion": 1,
  "slack_enabled": true,
  "slack_webhook_url": "example"
}
```

```
Parameter
Field	Type	Description
name	String
A descriptive name for the inbound email account

reply_address	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_name	String
The name that emails sent using this account will be sent from.

enabledoptional	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

Default value: true

user_idoptional	Number
The ID of a user that will be the responsible user for tickets created using this inbound route. You must set either a user ID or a ticket group ID.

ticket_group_idoptional	Number
The ID of a ticket group that tickets created using this inbound route should be placed into. You must set either a user ID or a ticket group ID.

priorityoptional	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Default value: 4

Allowed values: 1, 2, 3, 4

replyoptional	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signatureoptional	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filteringoptional	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

Default value: false

minimum_spam_scoreoptional	Number
The minimum spam score for an inbound email to be considered spam.

Default value: 5

days_before_spam_deletionoptional	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

Default value: 30

slack_enabledoptional	Boolean
Enable Slack.com integration

Default value: false

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration, required if slack_enabled is true

Success 200
Field	Type	Description
id	Number
The ID of the inbound email account.

name	String
A descriptive name for the inbound email account

reply_address	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_name	String
The name that emails sent using this account will be sent from.

mailbox	String
The mailbox at sonarticketing.rocks that you should forward email to in order for it to be delivered to Sonar.

enabled	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

user_id	Number
The ID of a user that will be the responsible user for tickets created using this inbound route.

ticket_group_id	Number
The ID of a ticket group that tickets created using this inbound route should be placed into.

priority	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Allowed values: 1, 2, 3, 4

reply	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signature	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filtering	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

minimum_spam_score	Number
The minimum spam score for an inbound email to be considered spam.

days_before_spam_deletion	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

slack_enabledoptional	Boolean
Slack.com integration status

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 8,
    "name": "Technical Support Tier 3",
    "reply_address": "support@sonar.software",
    "reply_name": "Charles Darwin",
    "mailbox": "another_example_ok@sonarticketing.rocks",
    "enabled": true,
    "user_id": 1,
    "ticket_group_id": null,
    "priority": 4,
    "reply": null,
    "signature": null,
    "automatic_spam_filtering": false,
    "minimum_spam_score": 12,
    "days_before_spam_deletion": 60,
    "slack_enabled": false,
    "slack_webhook_url": null
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

## Delete an inbound email account (DELETE)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/inbound_email_accounts/:id`

Description: Delete a inbound email account
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
The ID of the inbound email account

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
A reason as to why the inbound email account could not be deleted

status_code	Number
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "Inbound email account does not exist.",
         "status_code": 404
     }
 }
```

## Get all inbound email accounts (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/inbound_email_accounts`

Description: Get all inbound email accounts
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
The ID of the inbound email account.

name	String
A descriptive name for the inbound email account

reply_address	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_name	String
The name that emails sent using this account will be sent from.

mailbox	String
The mailbox at sonarticketing.rocks that you should forward email to in order for it to be delivered to Sonar.

enabled	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

user_id	Number
The ID of a user that will be the responsible user for tickets created using this inbound route.

ticket_group_id	Number
The ID of a ticket group that tickets created using this inbound route should be placed into.

priority	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Allowed values: 1, 2, 3, 4

reply	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signature	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filtering	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

minimum_spam_score	Number
The minimum spam score for an inbound email to be considered spam.

days_before_spam_deletion	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

slack_enabledoptional	Boolean
Slack.com integration status

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 2,
      "name": "Sales",
      "reply_address": "sales@sonar.software",
      "reply_name": "Sonar",
      "mailbox": "example@sonarticketing.rocks",
      "enabled": true,
      "user_id": null,
      "ticket_group_id": null,
      "priority": 4,
      "reply": "
Thanks for emailing us, pal!

",
      "signature": null,
      "automatic_spam_filtering": false,
      "minimum_spam_score": 12,
      "days_before_spam_deletion": 60,
      "slack_enabled": false,
      "slack_webhook_url": null
    },
    {
      "id": 3,
      "name": "Test with reply",
      "reply_address": "simon-test@sonar.software",
      "reply_name": "Sir Chumley",
      "mailbox": "another_example@sonarticketing.rocks",
      "enabled": true,
      "user_id": null,
      "ticket_group_id": 4,
      "priority": 2,
      "reply": "This is my reply if you don't like it, you can always replace it!",
      "signature": "[PUBLIC_NAME]
Kings of the jungle.",
      "automatic_spam_filtering": false,
      "minimum_spam_score": 12,
      "days_before_spam_deletion": 60,
      "slack_enabled": false,
      "slack_webhook_url": null
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

## Get an individual inbound email account (GET)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/inbound_email_accounts/:id`

Description: Get an individual inbound email account
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
The ID of the inbound email account

Success 200
Field	Type	Description
id	Number
The ID of the inbound email account.

name	String
A descriptive name for the inbound email account

reply_address	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_name	String
The name that emails sent using this account will be sent from.

mailbox	String
The mailbox at sonarticketing.rocks that you should forward email to in order for it to be delivered to Sonar.

enabled	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

user_id	Number
The ID of a user that will be the responsible user for tickets created using this inbound route.

ticket_group_id	Number
The ID of a ticket group that tickets created using this inbound route should be placed into.

priority	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Allowed values: 1, 2, 3, 4

reply	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signature	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filtering	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

minimum_spam_score	Number
The minimum spam score for an inbound email to be considered spam.

days_before_spam_deletion	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

slack_enabledoptional	Boolean
Slack.com integration status

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 2,
    "name": "Sales",
    "reply_address": "sales@sonar.software",
    "reply_name": "Sonar",
    "mailbox": "example@sonarticketing.rocks",
    "enabled": true,
    "user_id": null,
    "ticket_group_id": null,
    "priority": 4,
    "reply": null,
    "signature": null,
    "automatic_spam_filtering": false,
    "minimum_spam_score": 12,
    "days_before_spam_deletion": 60,
    "slack_enabled": false,
    "slack_webhook_url": null
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

## Update inbound email account (PATCH)
Version: 0.5.0

Endpoint: `https://example.sonar.software/api/v1/system/tickets/inbound_email_accounts/:id`

Description: Update an existing inbound email account.
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "reply_address": "example",
  "reply_name": "example",
  "enabled": true,
  "user_id": 1,
  "ticket_group_id": 1,
  "priority": 1,
  "reply": "example",
  "signature": "example",
  "automatic_spam_filtering": true,
  "minimum_spam_score": 1,
  "days_before_spam_deletion": 1,
  "slack_enabled": true,
  "slack_webhook_url": "example"
}
```

```
Parameter
Field	Type	Description
id	Number
The inbound email account ID

nameoptional	String
A descriptive name for the inbound email account

reply_addressoptional	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_nameoptional	String
The name that emails sent using this account will be sent from.

enabledoptional	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

user_idoptional	Number
The ID of a user that will be the responsible user for tickets created using this inbound route. You must set either a user ID or a ticket group ID.

ticket_group_idoptional	Number
The ID of a ticket group that tickets created using this inbound route should be placed into. You must set either a user ID or a ticket group ID.

priorityoptional	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Allowed values: 1, 2, 3, 4

replyoptional	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signatureoptional	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filteringoptional	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

Default value: false

minimum_spam_scoreoptional	Number
The minimum spam score for an inbound email to be considered spam.

Default value: 5

days_before_spam_deletionoptional	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

Default value: 30

slack_enabledoptional	Boolean
Enable Slack.com integration

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration, required if slack_enabled is true

Success 200
Field	Type	Description
id	Number
The ID of the inbound email account.

name	String
A descriptive name for the inbound email account

reply_address	String
The email address that emails sent using this account will be sent from, and wil have as a reply to address.

reply_name	String
The name that emails sent using this account will be sent from.

mailbox	String
The mailbox at sonarticketing.rocks that you should forward email to in order for it to be delivered to Sonar.

enabled	Boolean
Whether the account is enabled. Disabled accounts will not accept inbound email.

user_id	Number
The ID of a user that will be the responsible user for tickets created using this inbound route.

ticket_group_id	Number
The ID of a ticket group that tickets created using this inbound route should be placed into.

priority	Number
The priority of tickets created using this inbound route. 1 = critical, 2 = high, 3 = medium, 4 = low

Allowed values: 1, 2, 3, 4

reply	String
The automatic reply to emails sent to this inbound route. Can use some basic HTML.

signature	String
The signature appended to emails sent using this account. One variable is allowed in the signature which is [PUBLIC_NAME], this variable will be replaced with the user's public name.

automatic_spam_filtering	Boolean
Whether or not to enable automatic spam filtering for this inbound account. Spam filtering uses SpamAssassin.

minimum_spam_score	Number
The minimum spam score for an inbound email to be considered spam.

days_before_spam_deletion	Number
The number of days for spam to remain in the spam folder before being automatically deleted.

slack_enabledoptional	Boolean
Slack.com integration status

slack_webhook_urloptional	String
The Slack webhook URL to use for Slack integration

Success-Response:
HTTP/1.1 201 OK
{
  "data": {
    "id": 2,
    "name": "Technical Support Tier 1000",
    "reply_address": "sales@sonar.software",
    "reply_name": "Sonar",
    "mailbox": "some_real_good_example@sonarticketing.rocks",
    "enabled": true,
    "user_id": 2,
    "ticket_group_id": null,
    "priority": 4,
    "reply": null,
    "signature": null,
    "automatic_spam_filtering": false,
    "minimum_spam_score": 12,
    "days_before_spam_deletion": 60,
    "slack_enabled": false,
    "slack_webhook_url": null
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
Inline Devices
```
