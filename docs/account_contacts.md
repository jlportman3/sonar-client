# Account Contacts Endpoints

## Create account contact (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/contacts`
- **Description**: Create a new account contact
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `name` (String, required): The name of the contact
    - `role` (String, optional): The role of the contact
    - `email_address` (String, optional): The email address of the contact
    - `phone_numbers` (Object, optional): An object representing the phone numbers on the account, where the property is the type of phone number it is (one of work, home, mobile, fax) and the value of the property is an object containing two properties, number and extension.
    - `email_message_categories` (Array, required): An array of IDs representing the email categories this contact should receive. You can get a descriptive string describing the category ID from `/_data/email_categories`.
    - `primary` (Boolean, required): Whether or not this the primary contact. Only one contact can be primary, setting a contact to primary will remove the attribute from all other contacts
    - `username` (String, optional): A username for the customer portal. Required if password is set.
    - `password` (String, optional): A password for the customer portal. Required if username is set.
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 46,
            "name": "Jacob Kailing",
            "role": "Chief Party Officer",
            "email_address": "jacob@sonar.software",
            "phone_numbers": {
               "work": {
                   "number": "1231231234",
                   "extension": 123
               },
               "mobile": {
                   "number": "1235550809",
                   "extension": null
               }
           },
           "email_message_categories": [
               2
           ],
           "primary": true,
           "username": "babymonkey"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name field is required."
            },
            "status_code": 422
        }
    }
    ```

## Delete account contact (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/contacts/:contact_id`
- **Description**: Delete an account contact
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `contact_id` (Number, required): The ID of the contact
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "Contact deleted"
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "That contact ID does not exist.",
            "status_code": 404
        }
    }
    ```

## Get all account contacts (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/contacts`
- **Description**: Get the contacts for an account
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Simon Westlake",
                "role": "CEO",
                "email_address": "simon@sonar.software",
                "phone_numbers": {
                    "work": {
                        "number": "1231231234",
                        "extension": 123
                    },
                    "mobile": {
                        "number": "4148675309",
                        "extension": null
                    }
                },
                "email_message_categories": [
                    2
                ],
                "primary": true,
                "username": "leethacker12345"
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

## Get individual account contact (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/contacts/:contact_id`
- **Description**: Get an individual account contact
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `contact_id` (Number, required): The ID of the contact
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 46,
            "name": "Jacob Kailing",
            "role": "Chief Party Officer",
            "email_address": "jacob@sonar.software",
            "phone_numbers": {
               "work": {
                   "number": "1231231234",
                   "extension": 123
               },
               "mobile": {
                   "number": "1235550809",
                   "extension": null
               }
           },
            "email_message_categories": [
               2
            ],
           "primary": true,
           "username": null
        }
    }
    ```

## Update account contact (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/contacts/:contact_id`
- **Description**: Update an account contact.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `contact_id` (Number, required): The ID of the contact
    - `name` (String, optional): The name of the contact
    - `role` (String, optional): The role of the contact
    - `email_address` (String, optional): The email address of the contact
    - `phone_numbers` (Object, optional): An object representing the phone numbers on the account, where the property is the type of phone number it is (one of work, home, mobile, fax) and the value of the property is an object containing two properties, number and extension.
    - `email_message_categories` (Array, optional): An array of IDs representing the email categories this contact should receive. You can get a descriptive string describing the category ID from `/_data/email_categories`.
    - `primary` (Boolean, optional): Whether or not this the primary contact. Only one contact can be primary, setting a contact to primary will remove the attribute from all other contacts
    - `username` (String, optional): A username for the customer portal.
    - `password` (String, optional): A password for the customer portal. Required if username is currently null, as you are creating a new account.
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 46,
            "name": "Jacob Kailing",
            "role": "Chief Party Officer",
            "email_address": "jacob@sonar.software",
            "phone_numbers": {
               "work": {
                   "number": "1231231234",
                   "extension": 123
               },
               "mobile": {
                   "number": "1235550809",
                   "extension": null
               }
           },
           "email_message_categories": [
               2
           ],
           "primary": false,
           "username": "ridingonapig"
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name field is required."
            },
            "status_code": 422
        }
    }
    ```
```
