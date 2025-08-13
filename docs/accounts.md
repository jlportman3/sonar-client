# Accounts Endpoints

## Create account (POST)
Version: 0.3.2

Endpoint: `https://example.sonar.software/api/v1/accounts`

Description: Create a new account. There are items entered here such as the address and contact information that must be obtained from other endpoints. They are required here to meet the requirements with the Sonar application - a contact must have a physical address and primary contact when created.
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "account_type_id": 1,
  "account_status_id": 1,
  "account_groups": [],
  "sub_accounts": [],
  "next_bill_date": "example",
  "line1": "example",
  "line2": "example",
  "city": "example",
  "state": "example",
  "county": "example",
  "zip": "example",
  "country": "example",
  "latitude": 0.0,
  "longitude": 0.0,
  "contact_name": "example",
  "role": "example",
  "email_address": "example",
  "phone_numbers": "value",
  "email_message_categories": []
}
```

```
Parameter
Field	Type	Description
idoptional	Number
An ID for the account. The ID must be numeric and not currently in use. If you do not include an ID (which is the recommended method) then the next available ID will be automatically used. Once this is set, it cannot be changed.

name	String
A name for the new account

account_type_id	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_id	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groupsoptional	Array
An array of account group IDs, this can be referenced against /system/account_groups/:id

sub_accountsoptional	Array
An array of account IDs that you want to attach to this account as children

next_bill_dateoptional	String
A YYYY-MM-DD formatted date that dictates when the account should next bill. Generally speaking, you should allow Sonar to automatically calculate this. The only time you should set it is if this customer specifically needs to bill on a future date that would not be the calculated date - for example, if this is a customer that is billed once every 6 months and they billed 2 months ago, you would need to manually set this to 4 months in the future. Whatever day is set on your next_bill_date will also be set as the future recurring billing day. The day portion of next_bill_date cannot be higher than 28, as Sonar only allows 28 day billing

line1	String
The first line of the physical address

line2optional	String
The second line of the physical address, typically used for a suite number, apartment number, etc

city	String
The city

state	String
The state, province or other country subdivision. You can obtain a valid list from _data/subdivisions/:country

county	String
A valid county for the subdivision obtained from /_data/counties. This is only used for US states and should be blank for any other country. It is important to set this correctly as it will be used for calculating geo taxes

zip	String
The ZIP/postal code

country	String
A valid, two character country code. You can obtain a list of valid country codes from the /_data/countries API endpoint.

latitude	Float
The latitude of the address, in decimal.

longitude	Float
The longitude of the address, in decimal.

contact_name	String
The name of the primary account contact

role	String
The role of the primary account contact (e.g. CEO, Accountant)

email_addressoptional	String
The email address of the contact

phone_numbersoptional	Object
An object representing the phone numbers on the account, where the property is the type of phone number it is (one of work, home, mobile, fax) and the value of the property is an object containing two properties, number and extension. See the contact section of the API for an example

email_message_categories	Array
An array of IDs representing the email categories this contact should receive. You can get a descriptive string describing the category ID from /_data/email_categories.

Success 200
Field	Type	Description
id	Number
The internal ID of the account

name	String
The name of the account

account_type_id	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_id	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groups	Array
An array of account group IDs that this account belongs to, this can be referenced against /system/account_groups/:id

balance_due	Number
The sum of all remaining_due amounts on associated invoices

balance_total	Number
The sum of all remaining_due amounts on associated invoices, plus any uninvoiced debits

sub_accounts	Array
An array of account IDs that are children/sub accounts of this account

next_bill_date	String
The date on which this account will next bill. This will be null if the account has never been activated

delinquent	Boolean
Whether or not the account is currently delinquent

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
        "id": 1,
        "name": "Simon Westlake",
        "account_status_id": 1,
        "account_type_id": 1,
        "account_groups":  [],
        "balance_due": 0,
        "balance_total": 0,
        "sub_accounts": [],
        "next_bill_date": "2015-10-01",
        "delinquent": false
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
             "account_status_id": "The selected account status id is not valid.",
         },
         "status_code": 422
     }
 }
```

## Delete account (DELETE)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:id`

Description: Delete an account. Be careful when using this method! This will disable the accounts services and make all the data associated with this account inaccessible as soon as it is deleted.
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
The ID of the account

Success 200
Field	Type	Description
message	String
A message stating that the deletion was successful.

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "message": "Account deleted"
    }
}
Error 4xx
Name	Type	Description
message	String
A reason as to why the account could not be deleted

status_code	Number
4xx

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "That account does not exist",
         "status_code": 404
     }
 }
```

## Get all accounts (GET)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts`

Description: Get a list of the accounts in the system
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
The internal ID of the account

name	String
The name of the account

account_type_id	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_id	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groups	Array
An array of account group IDs that this account belongs to, this can be referenced against /system/account_groups/:id

balance_due	Number
The sum of all remaining_due amounts on associated invoices

balance_total	Number
The sum of all remaining_due amounts on associated invoices, plus any uninvoiced debits

sub_accounts	Array
An array of account IDs that are children/sub accounts of this account

next_bill_date	String
The date on which this account will next bill. This will be null if the account has never been activated

delinquent	Boolean
Whether or not the account is currently delinquent

Success-Response:
 HTTP/1.1 200 OK
 {
    "data": [
        {
            "id": 1,
            "name": "Jacob Kailing",
            "account_status_id": 1,
            "account_type_id": 1,
            "account_groups": [],
            "balance_due": 0,
            "balance_total": 0,
            "sub_accounts": [],
            "next_bill_date": "2015-10-01",
            "delinquent": false
        },
        {
            "id": 2,
            "name": "Horatio T Hornblower",
            "account_status_id": 1,
            "account_type_id": 1,
            "account_groups": [],
            "balance_due": 0,
            "balance_total": 0,
            "sub_accounts": [],
            "next_bill_date": "2015-11-03",
            "delinquent": true
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

## Get individual account (GET)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:id`

Description: Get an individual account.
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
The ID of the account

Success 200
Field	Type	Description
id	Number
The internal ID of the account

name	String
The name of the account

account_type_id	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_id	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groups	Array
An array of account group IDs that this account belongs to, this can be referenced against /system/account_groups/:id

balance_due	Number
The sum of all remaining_due amounts on associated invoices

balance_total	Number
The sum of all remaining_due amounts on associated invoices, plus any uninvoiced debits

sub_accounts	Array
An array of account IDs that are children/sub accounts of this account

next_bill_date	String
The date on which this account will next bill. This will be null if the account has never been activated

delinquent	Boolean
Whether or not the account is currently delinquent

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "id": 1,
        "name": "Simon Westlake",
        "account_status_id": 1,
        "account_type_id": 1,
        "account_groups":  [],
        "balance_due": 0,
        "balance_total": 0,
        "sub_accounts": [],
        "next_bill_date": "2018-03-04",
        "delinquent": false
    }
}
```

## Update account (PATCH)
Version: 0.2.10

Endpoint: `https://example.sonar.software/api/v1/accounts/:id`

Description: Update an account.
#### Request Example
```json
{
  "id": 1,
  "name": "example",
  "account_type_id": 1,
  "account_status_id": 1,
  "account_groups": [],
  "sub_accounts": [],
  "prorate": true,
  "next_bill_date": "2024-01-01"
}
```

```
Parameter
Field	Type	Description
id	Number
The ID of the account group to update

nameoptional	String
The name of the account

account_type_idoptional	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_idoptional	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groupsoptional	Array
An array of account group IDs, this can be referenced against /system/account_groups/:id

sub_accountsoptional	Array
An array of account IDs that you want to attach to this account as children. If you submit this parameter, you must submit all the IDs that should be children - if you omit existing children, they will be attached. An empty array will detach all children

prorate	Boolean
If you have account super user permissions, and you are changing the account status, set this to 'true' to prorate the change and 'false' to not prorate the change. If you do not have account superuser permissions, this value will be ignored and the system default prorating value will be used

Default value: false

next_bill_dateoptional	Date
If you would like to override the next bill date to a different date, it can be updated here in YYYY-MM-DD format. You should generally not do this, as you can cause serious billing issues - this is almost always only used when importing data from another system. The day portion of next_bill_date cannot be higher than 28, as Sonar only allows 28 day billing. This requires account superuser permissions

Success 200
Field	Type	Description
id	Number
The internal ID of the account

name	String
The name of the account

account_type_id	Number
An ID representing the type of account, this can be referenced against /system/account_types/:id

account_status_id	Number
An ID representing the status of the account, this can be referenced against /system/account_statuses/:id

account_groups	Array
An array of account group IDs that this account belongs to, this can be referenced against /system/account_groups/:id

balance_due	Number
The sum of all remaining_due amounts on associated invoices

balance_total	Number
The sum of all remaining_due amounts on associated invoices, plus any uninvoiced debits

sub_accounts	Array
An array of account IDs that are children/sub accounts of this account

next_bill_date	String
The date on which this account will next bill. This will be null if the account has never been activated

delinquent	Boolean
Whether or not the account is currently delinquent

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "id": 1,
        "name": "Simon Westlake",
        "account_status_id": 1,
        "account_type_id": 1,
        "account_groups":  [],
        "balance_due": 0,
        "balance_total": 0,
        "sub_accounts": [],
        "next_bill_date": "2015-10-01",
        "delinquent": false
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
             "account_status_id": "The selected account status id is not valid.",
         },
         "status_code": 422
     }
 }
Address Lists
```
