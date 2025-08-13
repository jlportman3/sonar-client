# Tickets Endpoints

## Attach a child ticket to a parent ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/attach/:child_id`
- **Description**: Attach a child ticket to a parent ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the parent ticket
    - `child_id` (Number, required): The ID of the child ticket
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "subject": "The porridge was too hot",
        "type": "internal",
        "ticket_group_id": null,
        "user_id": 1,
        "assignee": "accounts",
        "assignee_id": 1,
        "due_date": null,
        "email_address": null,
        "priority": 3,
        "category_ids": [
           1,
           2,
           3
        ],
        "open": true,
        "parent_ticket_id": null,
        "child_ticket_ids": [
           594
        ]
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "user_id": "The ticket ID 10 has child tickets. You cannot make a ticket a child of another ticket if the child has children."
         },
         "status_code": 422
       }
    }
    ```

## Create a new ticket comment (POST)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_comments`
- **Description**: Create a new ticket comment. A comment is internal and will not be sent to any email address on the ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `text` (String, required): The text of the comment.
    - `files` (Array, optional): Uploading files to a reply will email them to the email_address on the ticket, if the reply is outgoing. The format of the files array is [ { "filename": "a_beautiful_picture.png", "base64": "base64_encoded_file_string" }, { "filename": "another_file.mp3", "base64": "base64_encoded_file_string" } ]
    - `add_to_children` (Boolean, optional): If you set this to true, and this ticket has child tickets, then this comment will also be appended to all child tickets.
- **Example Request Body**:
    ```json
    {
        "text": "Well, here's a story all about how my ticket got flipped turned upside down.",
        "files": [
            {
                "id": 234,
                "filename": "bmljZSB3b3Jr.txt",
                "base64": "SGVsbG8gbXkgbmFtZSBpcyBTaW1vbiwgeW91IGFyZSB2ZXJ5IGdvb2QgYXQgYmFzZTY0IGRlY29kaW5nIQ=="
            },
            {
                "id": 234,
                "filename": "kula_shaker.txt",
                "base64": "VGhlIHNvY2lldHkgd2hpY2ggc2Nvcm5zIGV4Y2VsbGVuY2UgaW4gcGx1bWJpbmcgYXMgYSBodW1ibGUgYWN0aXZpdHkgYW5kIHRvbGVyYXRlcyBzaG9kZGluZXNzIGluIHBoaWxvc29waHkgYmVjYXVzZSBpdCBpcyBhbiBleGFsdGVkIGFjdGl2aXR5IHdpbGwgaGF2ZSBuZWl0aGVyIGdvb2QgcGx1bWJpbmcgbm9yIGdvb2QgcGhpbG9zb3BoeTogbmVpdGhlciBpdHMgcGlwZXMgbm9yIGl0cyB0aGVvcmllcyB3aWxsIGhvbGQgd2F0ZXIuCg=="
            }
        ]
    }
    ```
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 4,
        "user_id": 1,
        "text": "Well, here's a story all about how my ticket got flipped turned upside down.",
        "created_at": "2016-04-24 15:25:03",
        "files": [
           {
               "id": 234,
               "filename": "bmljZSB3b3Jr.txt",
               "mime_type": "text/plain"
           },
           {
               "id": 234,
               "filename": "kula_shaker.txt",
               "mime_type": "text/plain"
           }
        ],
        "deleted_by": null,
        "deleted_at": null
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

## Create a new ticket reply (POST)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_replies`
- **Description**: Create a new ticket reply. A reply is public and will be sent to the email address set on the ticket. Replies can only be added to public tickets. Basic HTML can be used.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `text` (String, required): The text of the reply.
    - `incoming` (Boolean, optional): Whether or not the reply is incoming. If this is true, the reply will be treated as though it was received from a customer. If this is false, the reply will be treated as though posted by an employee, and will be emailed to the customer.
    - `author` (String, optional): Required if incoming is true. This is a name for the author of the reply.
    - `author_email` (String, optional): Required if incoming is true. This is the email address of the author of the reply.
    - `files` (Array, optional): Uploading files to a reply will email them to the email_address on the ticket. The format of the files array is [ { "filename": "a_beautiful_picture.png", "base64": "base64_encoded_file_string" }, { "filename": "another_file.mp3", "base64": "base64_encoded_file_string" } ]
    - `add_to_children` (Boolean, optional): If you set this to true, and this ticket has child tickets, then this reply will also be appended to all public child tickets. If the reply fails to apply to a child ticket for any reason (for example, the child ticket has an invalid inbound email account associated with it) then the child reply will be discarded silently for that specific child ticket. If you set this to true, you will be able to submit a reply on an internal ticket, as long as the ticket has children. In this case, the data response will be an array of successful replies.
- **Example Request Body**:
    ```json
    {
        "text": "I am a dancing master!",
        "files": [
            {
                "id": 234,
                "filename": "bmljZSB3b3Jr.txt",
                "base64": "SGVsbG8gbXkgbmFtZSBpcyBTaW1vbiwgeW91IGFyZSB2ZXJ5IGdvb2QgYXQgYmFzZTY0IGRlY29kaW5nIQ=="
            },
            {
                "id": 234,
                "filename": "kula_shaker.txt",
                "base64": "VGhlIHNvY2lldHkgd2hpY2ggc2Nvcm5zIGV4Y2VsbGVuY2UgaW4gcGx1bWJpbmcgYXMgYSBodW1ibGUgYWN0aXZpdHkgYW5kIHRvbGVyYXRlcyBzaG9kZGluZXNzIGluIHBoaWxvc29waHkgYmVjYXVzZSBpdCBpcyBhbiBleGFsdGVkIGFjdGl2aXR5IHdpbGwgaGF2ZSBuZWl0aGVyIGdvb2QgcGx1bWJpbmcgbm9yIGdvb2QgcGhpbG9zb3BoeTogbmVpdGhlciBpdHMgcGlwZXMgbm9yIGl0cyB0aGVvcmllcyB3aWxsIGhvbGQgd2F0ZXIuCg=="
            }
        ]
    }
    ```
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 5,
        "user_id": 1,
        "text": "I am a dancing master!",
        "author": "Hulk Hogan",
        "author_email": "hulkamania@example.org",
        "created_at": "2016-04-26 14:22:03",
        "files": [
           {
               "id": 234,
               "filename": "bmljZSB3b3Jr.txt",
               "mime_type": "text/plain"
           },
           {
               "id": 234,
               "filename": "kula_shaker.txt",
               "mime_type": "text/plain"
           }
        ],
        "incoming": false
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

## Create a new ticket (POST)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/tickets`
- **Description**: Create a new ticket.
- **Parameters**:
    - `subject` (String, required): A subject for the ticket
    - `type` (String, required): The type of ticket. Internal is for internal use only. Public will send emails to a customer if a reply is posted. (`"public"`, `"internal"`)
    - `inbound_email_account_id` (Number, optional): The inbound email account to use for this public ticket. This will control the 'From' address that email replies to customers are sent from. Required if the ticket is public, ignored if the ticket is internal.
    - `ticket_group_id` (Number, optional): A valid ID for a ticket group. A ticket must have at least a group or a responsible user.
    - `category_ids` (Array, optional): An array of ticket category IDs to assign to this ticket.
    - `user_id` (Number, optional): A valid responsible user ID. A ticket must have at least a group or a responsible user.
    - `assignee` (String, optional): The type of entity to assign the ticket to. Public tickets can only be assigned to accounts. (`"accounts"`)
    - `assignee_id` (Number, optional): The ID of the assignee to assign this ticket to. If this is set, assignee must be set and vice versa.
    - `due_date` (Date, optional): A date in Y-m-d format that dictates when the ticket must be completed by.
    - `email_address` (String, optional): An email address, required if this is a public ticket.
    - `priority` (Number, optional): A priority for the ticket. 4 is low, 3 is medium, 2 is high, 1 is critical. (`1`, `2`, `3`, `4`)
    - `comment` (String, optional): The first comment for the ticket. A comment is internal only and will not be sent to a customer. A ticket must have at least one comment or reply to open it.
    - `reply` (String, optional): The first reply for the ticket. A reply is public and will be sent to the email address on the ticket. A reply can only be saved if the ticket has an email address.
    - `comment_files` (Array, optional): An array of files to attach to the comment. The format of the files array is [ { "filename": "a_beautiful_picture.png", "base64": "base64_encoded_file_string" }, { "filename": "another_file.mp3", "base64": "base64_encoded_file_string" } ].
    - `reply_files` (Array, optional): Uploading files to a reply will email them to the email_address on the ticket. The format of the files array is [ { "filename": "a_beautiful_picture.png", "base64": "base64_encoded_file_string" }, { "filename": "another_file.mp3", "base64": "base64_encoded_file_string" } ].
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "subject": "The porridge was too hot",
        "type": "internal",
        "ticket_group_id": null,
        "user_id": 1,
        "assignee": "accounts",
        "assignee_id": 1,
        "due_date": null,
        "email_address": null,
        "priority": 3,
        "category_ids": [
           1,
           2,
           3
        ],
        "open": true,
        "parent_ticket_id": null,
        "child_ticket_ids": [],
        "inbound_email_account_id": null,
        "spam": false,
        "last_reply_incoming": false,
        "closed_at": null,
        "closed_by_user_id": null,
        "created_at": "2016-05-20 14:19:35"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "user_id": "The selected user is invalid."
         },
         "status_code": 422
       }
    }
    ```

## Delete a ticket (DELETE)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id`
- **Description**: Delete a ticket. This will remove all tasks, files, and other attached items as well.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `task_id` (Number, required): The ID of the task
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
            "message": "Ticket does not exist.",
            "status_code": 404
        }
    }
    ```

## Delete ticket comment (DELETE)
- **Version**: 0.5.2
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:ticket_id/ticket_comments/:comment_id`
- **Description**: Delete a ticket comment. You can only delete your own comments, unless you are a ticket super user. This will set deleted_at and deleted_by on the comment, and remove the comment text.
- **Parameters**:
    - `ticket_id` (Number, required): The ID of the ticket
    - `comment_id` (Number, required): The ID of the comment
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
            "message": "Comment does not exist.",
            "status_code": 404
        }
    }
    ```

## Detach a child ticket from a parent ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/detach/:child_id`
- **Description**: Detach a child ticket from a parent ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the parent ticket
    - `child_id` (Number, required): The ID of the child ticket
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "subject": "The porridge was too hot",
        "type": "internal",
        "ticket_group_id": null,
        "user_id": 1,
        "assignee": "accounts",
        "assignee_id": 1,
        "due_date": null,
        "email_address": null,
        "priority": 3,
        "category_ids": [
           1,
           2,
           3
        ],
        "open": true,
        "parent_ticket_id": null,
        "child_ticket_ids": []
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "user_id": "The ticket ID 12 is not a child of ticket ID 43."
         },
         "status_code": 422
       }
    }
    ```

## Get a list of subscribed tickets (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/subscribed`
- **Description**: Get a list of the ticket IDs you are currently subscribed to.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "ticket_ids": []
      }
    }
    ```

## Get all comments on a ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_comments`
- **Description**: Get a list of comments for a ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (201 Created)**:
    ```json
    {
      "data": [
        {
          "id": 1,
          "user_id": 1,
          "text": "There is a big problem here, the pedestal is full of snakes!",
          "created_at": "2016-04-21 22:00:55",
          "files": [],
          "deleted_by": null,
          "deleted_at": null
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

## Get all replies on a ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_replies`
- **Description**: Get a list of replies for a ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (201 Created)**:
    ```json
    {
      "data": [
        {
          "id": 66,
          "user_id": null,
          "text": "Some test reply",
          "author": "Simon Westlake",
          "author_email": "simon@sonar.software",
          "created_at": "2016-05-03 15:15:03",
          "files": [
            {
              "id": 19,
              "filename": "Invoice for March 2016.odt",
              "mime_type": "application/vnd.oasis.opendocument.text"
            },
            {
              "id": 18,
              "filename": "Invoice for July 2015.pdf",
              "mime_type": "application/pdf"
            }
          ]
        },
        "incoming": false
      ],
      "paginator": {
        "total_count": 1,
        "total_pages": 1,
        "current_page": 1,
        "limit": 100
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

## Get all tickets for an entity (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/:entity/:entity_id/tickets`
- **Description**: Get all tickets for a specific entity (e.g. an account
- **Parameters**:
    - `entity` (String, required): The entity to get tickets for (e.g. accounts)
    - `entity_id` (Number, required): The ID of the entity to get tickets for
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "subject": "The porridge was too hot",
          "type": "internal",
          "ticket_group_id": null,
          "user_id": 1,
          "assignee": "accounts",
          "assignee_id": 1,
          "due_date": null,
          "email_address": null,
          "priority": 3,
           "category_ids": [
               1,
               2,
               3
           ],
           "open": true,
           "parent_ticket_id": 1,
           "child_ticket_ids": [],
           "inbound_email_account_id": null,
           "spam": false
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

## Get all tickets (GET)
- **Version**: 0.5.10
- **Endpoint**: `https://example.sonar.software/api/v1/tickets`
- **Description**: Get all tickets
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "subject": "The porridge was too hot",
          "type": "internal",
          "ticket_group_id": null,
          "user_id": 1,
          "assignee": "accounts",
          "assignee_id": 1,
          "due_date": null,
          "email_address": null,
          "priority": 3,
           "category_ids": [
               1,
               2,
               3
           ],
           "open": true,
           "parent_ticket_id": 1,
           "child_ticket_ids": [],
           "inbound_email_account_id": null,
           "spam": false,
           "last_reply_incoming": false,
            "closed_at": null,
            "closed_by_user_id": null,
            "created_at": "2016-05-20 14:19:35"
        },
        {
          "id": 1,
          "subject": "The porridge was too cold",
          "type": "internal",
          "ticket_group_id": 1,
          "user_id": 1,
          "assignee": "accounts",
          "assignee_id": 1,
          "due_date": "2016-04-02",
          "email_address": "goldilocks@sonar.software",
          "priority": 3,
           "category_ids": [
               1,
               2,
               3
           ],
           "open": false,
           "parent_ticket_id": null,
           "child_ticket_ids": [],
           "inbound_email_account_id": null,
           "spam": false,
           "last_reply_incoming": false,
            "closed_at": null,
            "closed_by_user_id": null,
            "created_at": "2016-05-20 14:19:35"
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

## Get an individual ticket reply (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_replies/:reply_id`
- **Description**: Get a specific reply on a ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `reply_id` (Number, required): The ID of the reply
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 66,
        "user_id": null,
        "author": "Simon Westlake",
        "author_email": "simon@sonar.software",
        "text": "Writing ticket replies is so easy, a caveman could do it!",
        "created_at": "2016-05-03 15:15:03",
        "files": [
          {
            "id": 19,
            "filename": "Invoice for March 2016.odt",
            "mime_type": "application/vnd.oasis.opendocument.text"
          },
          {
            "id": 18,
            "filename": "Invoice for July 2015.pdf",
            "mime_type": "application/pdf"
          }
        ]
      },
      "incoming": false
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

## Get individual ticket comment (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_comments/:comment_id`
- **Description**: Get a a specific comment on a ticket.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
    - `comment_id` (Number, required): The ID of the comment
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 1,
        "user_id": 1,
        "text": "I just wanted to say how nice this ticket is.",
        "created_at": "2016-04-21 22:00:55",
        "files": [],
        "deleted_by": null,
        "deleted_at": null
      }
    }
    ```

## Get individual ticket (GET)
- **Version**: 0.5.10
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id`
- **Description**: Get an individual ticket
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 2,
        "subject": "The porridge was too hot",
        "type": "internal",
        "ticket_group_id": null,
        "user_id": 1,
        "assignee": "accounts",
        "assignee_id": 1,
        "due_date": null,
        "email_address": null,
        "priority": 3,
        "category_ids": [
           1,
           2,
           3
        ],
        "open": true,
        "parent_ticket_id": null,
        "child_ticket_ids": [
           5,
           7
        ],
        "inbound_email_account_id": null,
        "spam": false,
        "last_reply_incoming": false,
        "closed_at": null,
        "closed_by_user_id": null,
        "created_at": "2016-05-20 14:19:35"
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

## Merge two tickets (GET)
- **Version**: 0.6.1
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/merge`
- **Description**: Merge one ticket into another. The ticket referenced as :id will be kept, and the ticket merging into :id will be deleted. When merging one ticket into another, the ticket referenced as :id will gain all the replies and comments on the ticket referenced in child_ticket_id, and the child_ticket_id ticket will be deleted.
- **Parameters**:
    - `id` (Number, required): The ID of the master ticket
    - `child_ticket_id` (Number, required): The ID of the ticket to merge in.
    - `success` (Boolean, required): Will be true if the merge succeeds.
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
         "message": "You cannot merge a ticket into itself.",
         "status_code": 422
       }
    }
    ```

## Subscribe to a ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/subscribe`
- **Description**: Subscribe to a ticket. This will add it to your list of subscribed tickets.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
- **Success Response (201 Created)**:
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
         "message": "No item with that ID found.",
         "status_code": 404
       }
    }
    ```

## Unsubscribe from a ticket (GET)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/unsubscribe`
- **Description**: Unsubscribe from a ticket. This will remove it from your list of subscribed tickets.
- **Parameters**:
    - `id` (Number, required): The ID of the ticket
- **Success Response (201 Created)**:
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
         "message": "No item with that ID found.",
         "status_code": 404
       }
    }
    ```

## Update ticket comment (PATCH)
- **Version**: 0.5.0
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id/ticket_comments/:comment_id`
- **Description**: Update an existing ticket comment. You can only update your own comments, unless you are a ticket super user.
- **Parameters**:
    - `id` (Number, required): The ticket ID
    - `comment_id` (Number, required): The comment ID
    - `text` (String, required): The text of the comment
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 8,
        "user_id": 1,
        "text": "This is my updated comment.",
        "created_at": "2016-05-26 17:41:08",
        "files": [],
        "deleted_by": null,
        "deleted_at": null
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "text": "The text field is required."
         },
         "status_code": 422
       }
    }
    ```

## Update ticket (PATCH)
- **Version**: 1.2.15
- **Endpoint**: `https://example.sonar.software/api/v1/tickets/:id`
- **Description**: Update an existing ticket.
- **Parameters**:
    - `id` (Number, required): The ticket ID
    - `subject` (String, optional): A subject for the ticket
    - `type` (String, optional): If this is provided, and it differs from the existing type, it will move the ticket to this type. If you are switching a ticket from internal to public, you must also supply the inbound_email_account_id and email_address properties. (`"internal"`, `"public"`)
    - `ticket_group_id` (Number, optional): A valid ID for a ticket group. A ticket must have at least a group or a responsible user.
    - `category_ids` (Array, optional): An array of ticket category IDs to assign to this ticket.
    - `user_id` (Number, optional): A valid responsible user ID. A ticket must have at least a group or a responsible user.
    - `assignee` (String, optional): The type of entity to assign the ticket to. Public tickets can only be assigned to accounts. (`"accounts"`, `"network_sites"`)
    - `assignee_id` (Number, optional): The ID of the assignee to assign this ticket to. If this is set, assignee must be set and vice versa.
    - `due_date` (Date, optional): A date in Y-m-d format that dictates when the ticket must be completed by.
    - `email_address` (String, optional): An email address, required if this is a public ticket.
    - `priority` (Number, optional): A priority for the ticket. 4 is low, 3 is medium, 2 is high, 1 is critical. (`1`, `2`, `3`, `4`)
    - `open` (Boolean, optional): Whether the ticket is open or closed. Send false to close the ticket, true to open it.
    - `child_ticket_ids` (Array, optional): An array of child ticket IDs of this ticket
    - `inbound_email_account_id` (Number, optional): The inbound email account to use for this public ticket. This will control the 'From' address that email replies to customers are sent from. Can only be set on a public ticket.
    - `spam` (Boolean, optional): Whether or not the ticket is spam
    - `update_child_status` (Boolean, optional): If this ticket has child tickets, and you wish to update them all with whatever the status is of this ticket, set this to true. For example, if this ticket is closed, or you are closing it, and you want to update all child tickets to closed, set this value to true.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 2,
        "subject": "The porridge was too hot",
        "type": "internal",
        "ticket_group_id": null,
        "user_id": 1,
        "assignee": "accounts",
        "assignee_id": 1,
        "due_date": null,
        "email_address": null,
        "priority": 3,
        "category_ids": [
           1,
           2,
           3
        ],
        "open": true,
        "parent_ticket_id": 3,
        "child_ticket_ids": [],
        "inbound_email_account_id": null,
        "spam": true,
        "last_reply_incoming": false,
        "closed_at": null,
        "closed_by_user_id": null,
        "created_at": "2016-05-20 14:19:35"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "user_id": "The selected user is invalid."
         },
         "status_code": 422
       }
    }
    ```
```
