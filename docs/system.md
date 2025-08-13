# System Endpoints

## Create account group (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_groups`
- **Description**: Create a new account group.
- **Parameters**:
    - `name` (String, required): A unique name for the account group
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 6,
            "name": "People That I Like"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Create account status (POST)
- **Version**: 1.2.17
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_statuses`
- **Description**: Create a new account status.
- **Parameters**:
    - `name` (String, required): A unique name for the account status
    - `active` (Boolean, required): Whether or not the status should activate customer services
    - `color` (String, required): A 6 digit hex code, prefixed with #, that represents the color for the status in the application
    - `account_super_user_only` (Boolean, required): If this is true, only users in a role with the 'Account Super User' permission can set this status on an account
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
             "id": 5,
             "name": "Sent to Collections",
             "active": false,
             "color": "#00ffff",
             "account_super_user_only": true
         }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Create account type (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_types`
- **Description**: Create a new account type.
- **Parameters**:
    - `name` (String, required): A unique name for the account type
    - `type` (String, required): The type of account type this is (`"residential"`, `"commercial"`)
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
             "id": 12,
             "name": "My Custom Type",
             "type": "commercial"
         }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Create address type (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/address_types`
- **Description**: Create a new address type.
- **Parameters**:
    - `name` (String, required): A unique name for the address type
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Physical"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Create custom field (POST)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/custom_fields`
- **Description**: Create a new custom field.
- **Parameters**:
    - `name` (String, required): The name of the custom field
    - `type` (String, required): The type of field (`"text"`, `"checkbox"`, `"select"`, `"date"`)
    - `unique` (Boolean, optional): Whether input to this custom field must be unique. Only applies to text fields and should not be submitted for other types
    - `active` (Boolean, required): If the field is not active, it won't show up on any entities that don't already have a value set
    - `entity_type` (String, required): The type of entity this custom field is displayed on (`"account"`)
    - `select_options` (Array, optional): If the type of this field is 'select', this will contain an array of options to display in the select field, formatted as JSON - see example for details. This field should not be submitted for other types
- **Success Response (201 Created)**:
    ```json
    {
      "id": 8,
      "name": "Height of Antenna",
      "type": "text",
      "unique": true,
      "active": true,
      "entity_type": "account",
      "select_options": []
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "The value entered for type is invalid."
            },
            "status_code": 422
        }
    }
    ```

## Delete account group (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_groups/:id`
- **Description**: Delete an account group.
- **Parameters**:
    - `id` (Number, required): The ID of the account group
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "Account group deleted"
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "Account group not found",
            "status_code": 404
        }
    }
    ```

## Delete account status (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_statuses/:id`
- **Description**: Delete an account status.
- **Parameters**:
    - `id` (Number, required): The ID of the account status
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "message": "Account status deleted"
        }
    }
    ```
- **Error Response (404 Not Found)**:
    ```json
    {
        "error": {
            "message": "Account status not found",
            "status_code": 404
        }
    }
    ```

## Delete account type (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_types/:id`
- **Description**: Delete an account types.
- **Parameters**:
    - `id` (Number, required): The ID of the account type
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
            "message": "Account type not found",
            "status_code": 404
        }
    }
    ```

## Delete address type (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/address_types/:id`
- **Description**: Delete an account type.
- **Parameters**:
    - `id` (Number, required): The ID of the address type
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
            "message": "Address type not found",
            "status_code": 404
        }
    }
    ```

## Delete custom field (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/custom_fields/:id`
- **Description**: Delete a custom field. This will remove all data stored in this custom field from all entities also. If you just want to disable further use of the field, set the 'active' property to 'false'.
- **Parameters**:
    - `id` (Number, required): The ID of the custom field
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
            "message": "Custom field does not exist.",
            "status_code": 404
        }
    }
    ```

## Get KPIs and statistics (GET)
- **Version**: 1.5.7
- **Endpoint**: `https://example.sonar.software/api/v1/_data/kpi`
- **Description**: Get various key performance indicators and statistics. This data is collected in real time, so should be queried daily and stored if you want to track it over time.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "active_accounts": 1,
            "delinquent_accounts": 0,
            "all_accounts": 1,
            "invoiced_this_month": null,
            "total_due_balances": null,
            "undeposited_payments": 0,
            "invoices_to_print": 0,
            "open_public_tickets": 0,
            "open_internal_tickets": 0,
            "tickets_by_group": [],
            "ticket_group_names": [],
            "count_of_accounts_status_changed_in_last_30_days": 0,
            "today": {
                "tickets": 0,
                "tickets_closed": 0,
                "payments": "150.00",
                "payments_failed": 2,
                "accounts": 0,
                "debits": null,
                "discounts": null,
                "customers_billed": 0,
                "jobs": {
                    "scheduled": 0,
                    "completed": 0,
                    "failed": 0
                },
                "accounts_activated": 0,
                "bounced_emails": 0,
                "contracts_expiring": 0,
                "towercoverage_submissions_good": 0,
                "towercoverage_submissions_bad": 0
            },
            "accounts_by_status_id": {
               "2": 1234,
               "5": 5678,
               "12": 2
            },
            "arpu": 12.34
        }
    }
    ```

## Get all account groups (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_groups`
- **Description**: Get a list of available account groups.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Habitual Late Payers"
            },
            {
                "id": 2,
                "name": "JC Kenney Employees"
            },
            {
                "id": 3,
                "name": "Free Accounts"
            },
            {
                "id": 4,
                "name": "Employees"
            },
            {
                "id": 5,
                "name": "Friends & Family"
            }
        ],
        "paginator": {
            "total_count": 5,
            "total_pages": 1,
            "current_page": 1,
            "limit": 100
        }
    }
    ```

## Get all account statuses (GET)
- **Version**: 1.2.17
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_statuses`
- **Description**: Get a list of available account statuses.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Lead",
                "active": false,
                "color": "#9b59b6",
                "account_super_user_only": false
            },
            {
                "id": 2,
                "name": "Active",
                "active": true,
                "color": "#123123",
                "account_super_user_only": false
            },
            {
                "id": 3,
                "name": "Inactive",
                "active": false,
                "color": "#fff000",
                "account_super_user_only": false
            },
            {
                "id": 5,
                "name": "My Custom Status Active",
                "active": true,
                "color": "#00ff00",
                "account_super_user_only": true
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

## Get all account types (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_types`
- **Description**: Get a list of available account types.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Residential",
                "type": "residential"
            },
            {
                "id": 2,
                "name": "Commercial",
                "type": "commercial"
            },
            {
                "id": 3,
                "name": "Service Trade",
                "type": "commercial"
            }
        ],
        "paginator": {
            "total_count": 6,
            "total_pages": 1,
            "current_page": 1,
            "limit": 100
        }
    }
    ```

## Get all address types (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/address_types`
- **Description**: Get a list of available address types.
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
        "data": [
            {
                "id": 1,
                "name": "Physical"
            },
            {
                "id": 2,
                "name": "Billing"
            },
            {
                "id": 3,
                "name": "Billing"
            },
            {
                "id": 4,
                "name": "Some Other Type"
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

## Get all custom fields (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/custom_fields`
- **Description**: Get a list of custom fields
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 8,
          "name": "Serial Number for Anti-Virus",
          "type": "text",
          "unique": true,
          "active": true,
          "entity_type": "account",
          "select_options": []
        },
        {
          "id": 7,
          "name": "My First Dropdown",
          "type": "select",
          "unique": false,
          "active": false,
          "entity_type": "account",
          "select_options": [
            {
              "text": "Option Number One"
            },
            {
              "text": "Option Number Two"
            }
          ]
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

## Get application configuration (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/application`
- **Description**: Get the current application configuration.
- **Success Response (200 OK)**:
    ```json
    {
    "data": {
    "locale": "en",
    "timezone": "America/Chicago",
    "country": "US",
    "thousands_separator": ",",
    "decimal_separator": ".",
    "date_format": "m/d/Y",
    "currency_symbol": "$",
    "time_format": "g:i:s",
    "units": "metric"
    }
    }
    ```

## Get individual account group (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_groups/:id`
- **Description**: Get an individual account status.
- **Parameters**:
    - `id` (Number, required): The ID of the account status
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Habitual Late Payers"
        }
    }
    ```

## Get individual account status (GET)
- **Version**: 1.2.17
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_statuses/:id`
- **Description**: Get an individual account status.
- **Parameters**:
    - `id` (Number, required): The ID of the account status
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Lead",
            "active": false,
            "color": "#00ff00",
            "account_super_user_only": false
        }
    }
    ```

## Get individual account type (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_types/:id`
- **Description**: Get an individual account type.
- **Parameters**:
    - `id` (Number, required): The ID of the account type
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Residential",
            "type": "residential"
        }
    }
    ```

## Get individual address type (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://sonar.software/api/v1/system/address_types/:id`
- **Description**: Get an individual account address.
- **Parameters**:
    - `id` (Number, required): The ID of the address type
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Physical"
        }
    }
    ```

## Get individual custom field (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/custom_fields/:id`
- **Description**: Get an individual custom field
- **Parameters**:
    - `id` (Number, required): The id of the custom field
- **Success Response (200 OK)**:
    ```json
    {
      "id": 8,
      "name": "Height of Antenna",
      "type": "text",
      "unique": true,
      "active": true,
      "entity_type": "account",
      "select_options": []
    }
    ```

## Update account group (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_groups/:id`
- **Description**: Update an account group.
- **Parameters**:
    - `id` (Number, required): The ID of the account group to update
    - `name` (String, required): A unique name for the account group
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 6,
            "name": "People That I No Longer Like"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Update account status (PATCH)
- **Version**: 1.2.17
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_statuses/:id`
- **Description**: Update an account status.
- **Parameters**:
    - `id` (Number, required): The ID of the account status to update
    - `name` (String, required): A unique name for the account status
    - `active` (Boolean, required): Whether or not this status activates customer services
    - `color` (String, required): A 6 digit hex code, prefixed with #, that represents the color for the status in the application
    - `account_super_user_only` (Boolean, required): If this is true, only users in a role with the 'Account Super User' permission can set this status on an account
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
            "id": 5,
            "name": "Pending",
            "active": false,
            "color": "#00ff00",
            "account_super_user_only": true
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Update account type (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/account_types/:id`
- **Description**: Update an account type.
- **Parameters**:
    - `id` (Number, required): The ID of the account type to update
    - `name` (String, required): A unique name for the account type
    - `type` (String, required): The type of account type this is (`"residential"`, `"commercial"`)
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
             "id": 12,
             "name": "My Custom Type Updated",
             "type": "commercial"
         }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Update address type (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/address_types/:id`
- **Description**: Update an address type.
- **Parameters**:
    - `id` (Number, required): The ID of the address type to update
    - `name` (String, required): A unique name for the address type
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "id": 1,
            "name": "Physical"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "name": "The name has already been taken."
            },
            "status_code": 422
        }
    }
    ```

## Update application (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/application`
- **Description**: Update application
- **Parameters**:
    - `locale` (String, optional): The application locale. You can retrieve a list of valid locales from `/_data/locales`
    - `timezone` (String, optional): The application timezone. You can retrieve a list of valid timezones from `/_data/timezones`
    - `country` (String, optional): An ISO 3166-1 alpha-2 character code representing the country the application is configured for. You can retrieve a list of these from `/_data/countries`
    - `thousands_separator` (String, optional): The character to use to separate thousands (e.g. 1,000 has a comma (,) separator). Typical options are a space, a comma or a period, although the application allows any characters.
    - `decimal_separator` (String, optional): The character to use to separate decimals (e.g. 100.34 has a period (.) separator). Typical options are a comma or a period, although the application allows any characters.
    - `date_format` (String, optional): The format for dates in the application. One of Y-m-d, d/m/Y or m/d/Y. These will format to 2015-01-30, 30/01/2015 and 01/30/2015 respectively.
    - `currency_symbol` (String, optional): The symbol used for currency in the application. Any characters are allowed.
    - `time_format` (String, optional): The format used for time in the application, one of g:i:s and H:i:s. These will format to 1:30:34 PM and 13:30:34 respectively. (`"g:i:s"`, `"H:i:s"`)
    - `units` (String, optional): The units used for measurement (`"metric"`, `"imperial"`)
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "locale": "en",
            "timezone": "America/Chicago",
            "country": "US",
            "thousands_separator": ",",
            "decimal_separator": ".",
            "date_format": "m/d/Y",
            "currency_symbol": "$",
            "time_format": "g:i:s",
            "units": "metric"
        }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "locale": "The selected language is invalid."
            },
            "status_code": 422
        }
    }
    ```

## Update custom field (PATCH)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/system/custom_fields/:id`
- **Description**: Update a custom field. The type and entity_type cannot be changed once created
- **Parameters**:
    - `id` (Number, required): The ID of the custom field
    - `name` (String, optional): The name of the custom field
    - `unique` (Boolean, optional): Whether input to this custom field must be unique. Only applies to text fields and should not be submitted for other types
    - `active` (Boolean, optional): If the field is not active, it won't show up on any entities that don't already have a value set
    - `select_options` (Array, optional): If the type of this field is 'select', this will contain an array of options to display in the select field, formatted as JSON - see example for details. This field should not be submitted for other types
- **Success Response (200 OK)**:
    ```json
    {
      "id": 8,
      "name": "Height of Antenna",
      "type": "text",
      "unique": true,
      "active": true,
      "entity_type": "account",
      "select_options": []
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "unique": "Unique must be a boolean."
            },
            "status_code": 422
        }
    }
    ```
```
