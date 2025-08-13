# Contracts Endpoints

## Create a new contract (POST)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts`

Description: Create a new contract from a contract template. A link to sign the contract will be emailed to the specified contact, as long as the contact has an email address.
#### Request Example
```json
{
  "account_id": 1,
  "contract_template_id": 1,
  "contact_id": 1,
  "custom_message": "example"
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The ID of the account to assign the contract to

contract_template_id	Integer
The ID of a contract template

contact_id	Integer
The ID of a contact on the account specified in account_id. This contact will receive an email with a link to sign the contract.

custom_messageoptional	String
If you'd like a customized message to be displayed on the contract signature page, then enter it here.

Success 200
Field	Type	Description
id	Integer
The ID of the contract.

contract_name	String
The name of the contract

contract_text	String
The body of the contract, may contain some HTML.

contact_id	Integer
The ID of the contact associated with the contract. Only valid while the contract is unsigned.

term_in_months	Integer
The contract term in months, if it has one.

acceptance_datetime	DateTime
The date and time the contract was signed, in UTC

expiration_date	Date
The date the contract with expire, if it had a term. This is in the system timezone.

custom_message	String
The custom message associated with the contract

signer_name	String
The name the signer entered when signing the contract, if it is signed

signer_ip	String
The IP address of the party that signed the contract, if it is signed

Success-Response:
 HTTP/1.1 201 OK
 {
  "data": {
    "id": 7,
    "contract_name": "Example Contract",
    "contract_text": "Here is an example contract. Very nice.",
    "contact_id": 1,
    "term_in_months": 12,
    "acceptance_datetime": null,
    "expiration_date": null,
    "custom_message": "Hello John! Please sign this contract so we can get the ball rolling on synergizing your ability to evaluate our ground breaking product!",
    "signer_name": null,
    "signer_ip": null
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
4xx

Error-Response:
HTTP/1.1 4xx
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
```

## Delete a contract (DELETE)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts/:id`

Description: Delete a contract. Only unsigned contracts can be deleted.
#### Request Example
```json
{
  "account_id": 1,
  "id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The ID of the account.

id	Integer
The ID of the contract

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
A reason as to why the contract could not be deleted

status_code	Integer
4x

Error-Response:
HTTP/1.1 404
 {
     "error": {
         "message": "Contract does not exist.",
         "status_code": 404
     }
 }
```

## Get all contracts (GET)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts`

Description: Get all contracts
#### Request Example
```json
{
  "account_id": 1,
  "limit": 1,
  "page": 1
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The ID of the account you wish to return the contract list for

limitoptional	Integer
The number of entries to return

pageoptional	Integer
The page of results to return

Success 200
Field	Type	Description
id	Integer
The ID of the contract.

contract_name	String
The name of the contract

contract_text	String
The body of the contract, may contain some HTML.

contact_id	Integer
The ID of the contact associated with the contract. Only valid while the contract is unsigned.

term_in_months	Integer
The contract term in months, if it has one.

acceptance_datetime	DateTime
The date and time the contract was signed, in UTC

expiration_date	Date
The date the contract with expire, if it had a term. This is in the system timezone.

custom_message	String
The custom message associated with the contract

signer_name	String
The name the signer entered when signing the contract, if it is signed

signer_ip	String
The IP address of the party that signed the contract, if it is signed

unique_link_key	String
The unique key used on the Sonar contract signature page

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
     "id": 7,
     "contract_name": "Example Contract",
     "contract_text": "Here is an example contract. Very nice!",
     "contact_id": 1,
     "term_in_months": 12,
     "acceptance_datetime": null,
     "expiration_date": null,
     "custom_message": "Hello John! Please sign this contract so we can get the ball rolling on synergizing your ability to evaluate our ground breaking product!",
     "signer_name": null,
     "signer_ip": null,
     "unique_link_key": "72ULw3Kn4mAeRnLAyrhC6XFowRdIWV7UEtyEFYQrfsILwvJv588660c0e2c12"
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

## Get an individual contract as base64 (GET)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts/:id/base64`

Description: Get an individual contract as base64. This allows you to reconstruct the PDF, so you can present it in an external system (e.g. the customer portal.)
#### Request Example
```json
{
  "account_id": 1,
  "id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The ID of the account

id	Integer
The ID of the contract

Success 200
Field	Type	Description
base64	String
The base64 encoded contract

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
     "base64": "Q29uZ3JhdHVsYXRpb25zLCB5b3UgaGF2ZSBtYW5hZ2VkIHRvIGRlY29kZSBteSBzZWNyZXQgYmFzZTY0IGRhdGEhIFBsZWFzZSBkb24ndCBzaGFyZSB0aGUgY29udGVudHMgb2YgdGhpcyB3aXRoIGFueW9uZSAtIGl0J3MgYSBzZWNyZXQh"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
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

## Get an individual contract (GET)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts/:id`

Description: Get an individual contract
#### Request Example
```json
{
  "account_id": 1,
  "id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The ID of the account

id	Integer
The ID of the contract

Success 200
Field	Type	Description
id	Integer
The ID of the contract.

contract_name	String
The name of the contract

contract_text	String
The body of the contract, may contain some HTML.

contact_id	Integer
The ID of the contact associated with the contract. Only valid while the contract is unsigned.

term_in_months	Integer
The contract term in months, if it has one.

acceptance_datetime	DateTime
The date and time the contract was signed, in UTC

expiration_date	Date
The date the contract with expire, if it had a term. This is in the system timezone.

custom_message	String
The custom message associated with the contract

signer_name	String
The name the signer entered when signing the contract, if it is signed

signer_ip	String
The IP address of the party that signed the contract, if it is signed

unique_link_key	String
The unique key used on the Sonar contract signature page

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
     "id": 7,
     "contract_name": "Example Contract",
     "contract_text": "Here is an example contract. Very nice!",
     "contact_id": 1,
     "term_in_months": 12,
     "acceptance_datetime": null,
     "expiration_date": null,
     "custom_message": "Hello John! Please sign this contract so we can get the ball rolling on synergizing your ability to evaluate our ground breaking product!",
     "signer_name": null,
     "signer_ip": null,
     "unique_link_key": "72ULw3Kn4mAeRnLAyrhC6XFowRdIWV7UEtyEFYQrfsILwvJv588660c0e2c12"
   }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
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

## Update contract (PATCH)
Version: 1.1.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/contracts/:id`

Description: Update an existing contract. The only thing that can be updated is the custom message - to make any other changes, delete and re-add.
#### Request Example
```json
{
  "account_id": 1,
  "id": 1,
  "custom_message": "example",
  "contact_id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Integer
The account ID

id	Integer
The contract ID

custom_message	String
The custom message to display when the contract is being signed.

contact_id	Integer
The ID of the contact the contract should be emailed to. If this is changed, the contract will be emailed to the new contact.

Success 200
Field	Type	Description
id	Integer
The ID of the contract.

contract_name	String
The name of the contract

contract_text	String
The body of the contract, may contain some HTML.

contact_id	Integer
The ID of the contact associated with the contract. Only valid while the contract is unsigned.

term_in_months	Integer
The contract term in months, if it has one.

acceptance_datetime	DateTime
The date and time the contract was signed, in UTC

expiration_date	Date
The date the contract with expire, if it had a term. This is in the system timezone.

custom_message	String
The custom message associated with the contract

signer_name	String
The name the signer entered when signing the contract, if it is signed

signer_ip	String
The IP address of the party that signed the contract, if it is signed

unique_link_key	String
The unique key used on the Sonar contract signature page

Success-Response:
 HTTP/1.1 201 OK
 {
  "data": {
    "id": 7,
    "contract_name": "Example Contract",
    "contract_text": "Here is an example contract. Very nice.",
    "contact_id": 1,
    "term_in_months": 12,
    "acceptance_datetime": null,
    "expiration_date": null,
    "custom_message": "Hello John! Please sign this contract so we can get the ball rolling on synergizing your ability to evaluate our ground breaking product!",
    "signer_name": null,
    "signer_ip": null,
    "unique_link_key": "72ULw3Kn4mAeRnLAyrhC6XFowRdIWV7UEtyEFYQrfsILwvJv588660c0e2c12"
  }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Integer
4xx

Error-Response:
HTTP/1.1 404
 {
   "error": {
     "message": "No item with that ID found.",
     "status_code": 404
   }
 }
Custom Fields
```
