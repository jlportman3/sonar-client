# Account Services Endpoints

## Add a package to an account (POST)
Version: 0.6.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/packages`

Description: Add a package to an account. A package is a group of recurring and/or expiring services. This will return a random, unique ID. This ID can be used to delete the package later. This unique ID is used to allow the account to have multiple instances of the same package, but still differentiate between them.
#### Request Example
```json
{
  "account_id": 1,
  "package_id": 1,
  "prorate": true
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account to add the package to

package_id	Number
The ID of the package you wish to add

prorate	Boolean
Whether or not you want to prorate this transaction, only valid for recurring services. If you don't have account super user permission, anything submitted here will be ignored and the system global prorate value will be used. If you do have account superuser, you must input a value here if you do not want the default of 'false'

Default value: false

Success 200
Field	Type	Description
unique_package_id	Boolean
This unique ID will be attached to all services on the account list that are part of this specific package. You need this ID to remove the package later.

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
        "unique_package_id": "5787b0cc6b25f"
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
         "message": "One of the services in the package is inactive.",
         "status_code": 422
     }
 }
```

## Add a service to an account (POST)
Version: 1.7.14

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/services`

Description: Add a service to an account. Adding a recurring or expiring service will add it to the account for future billing. Adding an adjustment or one time service will create a transaction for that service.
#### Request Example
```json
{
  "account_id": 1,
  "service_id": 1,
  "description": "example",
  "quantity": 1,
  "prorate": true,
  "amount": 1,
  "price_override": 1,
  "price_override_reason": "example",
  "name_override": "example",
  "next_bill_date": "2024-01-01",
  "service_metadata": []
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account to add the address to

service_id	Number
The ID of the service you wish to add

descriptionoptional	String
If you are entering a one time charge/adjustment, you can enter a description here to override the service name. This will show up on customer invoices!

quantityoptional	Number
If you are submitting a one time service, this is the quantity to add. If the one time service is $50, and this value is '3', a single transaction will be created for $150. If this is for a recurring service, the service will be added with this quantity for prorating, and future billing.

Default value: 1

prorateoptional	Boolean
Whether or not you want to prorate this transaction, only valid for recurring services. If you don't have account super user permission, anything submitted here will be ignored and the system global prorate value will be used.

amountoptional	Number
This is only valid for adjustment services, and is required if you are submitting one. This is the amount you wish to adjust the account by.

price_overrideoptional	Number
The amount to price override the service to. Only valid for recurring/expiring services.

price_override_reasonoptional	String
The reason for applying the price override. Only valid for recurring/expiring services.

name_overrideoptional	String
If this is set, then any transactions generated from this service when automatic billing runs will have this set as their description. See the debits/discounts endpoints for more details.

next_bill_dateoptional	Date
The next date this service will bill. Only valid for multi-month services. If unset, it will bill on the next account billing date.

service_metadataoptional	Array
An array of objects, each object should have an 'id' and 'value' property, where the 'id' is the ID of a service metadata field, and the 'value' is the value you wish to set the field to.

Success 200
Field	Type	Description
unique_service_relationship_id	Number
The unique ID representing the relationship of this specific service to this account. This is used in updates and deletes. If you are not adding a stored service (e.g. if you are performing a one time transaction/adjustment) this will instead return 'success': true on success.

One Time/Adjustment
Recurring Service
HTTP/1.1 201 OK
{
    "data": {
        "success": true
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
         "message": "You do not have permission to apply adjustment services.",
         "status_code": 422
     }
 }
```

## Delete a package from an account (DELETE)
Version: 0.6.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/packages/:unique_package_id`

Description: Delete a package from an account. A package is a group of recurring and/or expiring services
#### Request Example
```json
{
  "account_id": 1,
  "unique_package_id": 1,
  "prorate": true
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account to delete the package from

unique_package_id	Number
The unique ID returned when the package was added.

prorate	Boolean
Whether or not you want to prorate this transaction, only valid for recurring services. If you don't have account super user permission, anything submitted here will be ignored and the system global prorate value will be used. If you do have account superuser, you must input a value here if you do not want the default of 'false'

Default value: false

Success 200
Field	Type	Description
success	Boolean
If this is true, the process was completed successfully. If there are any errors, you will receive a non-2xx HTTP response code and an error object

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
        "success": true
    }
}
Error 4xx
Name	Type	Description
message	String
A list of validation errors

status_code	Number
4xx

Error-Response:
HTTP/1.1 422
 {
     "error": {
         "message": "One of the services in the package is inactive.",
         "status_code": 422
     }
 }
```

## Delete account service (DELETE)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/services/:unique_service_relationship_id`

Description: Delete a service from an account. Only valid for recurring/expiring services
#### Request Example
```json
{
  "account_id": 1,
  "unique_service_relationship_id": 1,
  "prorate": true
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

unique_service_relationship_id	Number
The unique relationship ID of the service

prorate	Boolean
Whether or not you want to prorate this transaction, only valid for recurring services. If you don't have account super user permission, anything submitted here will be ignored and the system global prorate value will be used. If you do have account superuser, you must input a value here if you do not want the default of 'false'

Default value: false

Success 200
Field	Type	Description
message	String
A message stating that the deletion was successful.

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
A reason as to why the service could not be deleted

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

## Get all account services (GET)
Version: 1.7.14

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/services`

Description: Get a list of the recurring and expiring services on the account.
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
account_id	Number
The ID of the account

limitoptional	Number
The number of entries to return

pageoptional	Number
The page of results to return

Success 200
Field	Type	Description
id	Number
The internal ID of the service. You can use this to retrieve service details from the /services endpoint

number_of_times_billed	Number
Only valid for expiring services, this is the number of times the service has been run

price_override	Number
If the service has a price override on it, it will be represented here. Otherwise, this will be null

price_override_reason	String
If the service has a price override, the optional reason will be displayed here

package_id	Number
If this service was added as part of a package, the ID of the package will be displayed here. Services added as part of a package cannot be removed, except by removing the package itself

unique_package_id	String
If this service is part of a package, this is a unique string that will identify all services added within the same package. The function of this string is to differentiate one package from another, if the same package is added to the account twice.

unique_service_relationship_id	Number
This is a unique ID that represents this specific service as it relates to this specific account. This ID is used when adding a price override for this service, or deleting this service from the account

name_override	String
If this is set, then any transactions generated from this service when automatic billing runs will have this set as their description. See the debits/discounts endpoints for more details.

quantity	Integer
The quantity of this particular service instance

next_bill_date	Date
The next date this service will bill. If null, it will bill on the next account billing date.

metadata	Object
An object where the property is the metadata ID, and the value is the metadata value.

Success-Response:
HTTP/1.1 200 OK
{
  "data": [
    {
      "id": 5,
      "number_of_times_billed": 0,
      "price_override": null,
      "price_override_reason": null,
      "package_id": null,
      "unique_package_id": null,
      "unique_service_relationship_id": 8,
      "name_override": null,
      "quantity": 1,
      "next_bill_date": "2018-11-06",
      "metadata": {}
    },
    {
      "id": 7,
      "number_of_times_billed": 0,
      "price_override": null,
      "price_override_reason": null,
      "package_id": null,
      "unique_package_id": null,
      "unique_service_relationship_id": 10,
      "name_override": "Hosting for www.example.com",
      "quantity": 12,
      "next_bill_date": "2018-11-06",
      "metadata": {
           "12": "test"
      }
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

## Get individual account service (GET)
Version: 1.7.14

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/services/:unique_service_relationship_id`

Description: Get details on an individual account service.
#### Request Example
```json
{
  "account_id": 1
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

Success 200
Field	Type	Description
unique_service_relationship_id	Number
This is a unique ID that represents this specific service as it relates to this specific account. This ID is used when adding a price override for this service, or deleting this service from the account

id	Number
The internal ID of the service. You can use this to retrieve service details from the /services endpoint

number_of_times_billed	Number
Only valid for expiring services, this is the number of times the service has been run

price_override	Number
If the service has a price override on it, it will be represented here. Otherwise, this will be null

price_override_reason	String
If the service has a price override, the optional reason will be displayed here

package_id	Number
If this service was added as part of a package, the ID of the package will be displayed here. Services added as part of a package cannot be removed, except by removing the package itself

unique_package_id	String
If this service is part of a package, this is a unique string that will identify all services added within the same package. The function of this string is to differentiate one package from another, if the same package is added to the account twice.

name_override	String
If this is set, then any transactions generated from this service when automatic billing runs will have this set as their description. See the debits/discounts endpoints for more details.

quantity	Integer
The quantity of this particular service instance

next_bill_date	Date
The next date this service will bill. If null, it will bill on the next account billing date.

metadata	Object
An object where the property is the metadata ID, and the value is the metadata value.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 5,
    "number_of_times_billed": 0,
    "price_override": null,
    "price_override_reason": null,
    "package_id": null,
    "unique_package_id": null,
    "unique_service_relationship_id": 10,
    "name_override": null,
    "quantity": 5,
    "next_bill_date": null,
    "metadata": {
         "12": "test"
    }
  }
}
```

## Get usage based billing policy details (GET)
Version: 0.6.0

Endpoint: `https://example.sonar.software/api/v1/accounts/:id/usage_based_billing_policy_details`

Description: Get details on any usage based billing policy that may be applied to the customer account, along with some other useful details.
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
The internal ID of the account

Success 200
Field	Type	Description
has_policy	Boolean
Does the account have a usage based billing policy being applied to it?

policy_cap_in_gigabytes	Number
The cap on the policy in gigabytes. This does not include any rollover or top offs.

rollover_enabled	Boolean
Is the rollover feature enabled on this policy?

rollover_expiration_enabled	Boolean
Does rollover data expire?

rollover_expires_after_months	Number
If rollover_expiration is true, this is the number of months after which rollover data expires.

assess_charges_at_end_of_billing_period	Boolean
If this is true, the customer will be charged for overages at the end of the billing period based on the values in overage_cost and overage_units_in_gigabytes.

allow_user_to_purchase_capacity	Boolean
If this is true, the customer can purchase additional capacity during his billing cycle based on the values in overage_cost and overage_units_in_gigabytes.

overage_cost	Number
The cost of overages on this policy.

overage_units_in_gigabytes	Number
This is the amount of data provided for the cost defined in overage_cost. E.g. if this is 5 and overage_cost is 10, then $10 provides 5 gigabytes.

rollover_available_in_bytes	Number
If rollover_enabled is true, then this is the amount of additional data available in the current billing period.

purchased_top_off_total_in_bytes	Number
If allow_user_to_purchase_capacity is true, then this is the amount of additional data purchased in the current billing period.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "has_policy": true,
    "policy_cap_in_gigabytes": 1,
    "rollover_enabled": true,
    "rollover_expiration_enabled": false,
    "rollover_expires_after_months": 0,
    "assess_charges_at_end_of_billing_period": false,
    "allow_user_to_purchase_capacity": false,
    "overage_cost": null,
    "overage_units_in_gigabytes": null,
    "rollover_available_in_bytes": 10000000000,
    "purchased_top_off_total_in_bytes": 0
  }
}
```

## Update account service (PATCH)
Version: 1.7.14

Endpoint: `https://example.sonar.software/api/v1/accounts/:account_id/services/:unique_service_relationship_id`

Description: Update an account service. The only values that can be changed are the price override, price override reason, and name override. To remove a price override or name override, set the price_override property to null.
#### Request Example
```json
{
  "account_id": 1,
  "unique_service_relationship_id": 1,
  "price_override": 1,
  "price_override_reason": "example",
  "name_override": "example",
  "quantity": 1,
  "prorate": true,
  "next_bill_date": "2024-01-01",
  "service_metadata": []
}
```

```
Parameter
Field	Type	Description
account_id	Number
The ID of the account

unique_service_relationship_id	Number
The unique relationship ID of the service that already exists on the account

price_overrideoptional	Number
The amount to price override the service by

price_override_reasonoptional	String
The reason for applying the price override

name_overrideoptional	String
If this is set, then any transactions generated from this service when automatic billing runs will have this set as their description. See the debits/discounts endpoints for more details.

quantityoptional	Integer
If this is set, the quantity of the service will be adjusted to this amount. Must be 1 or greater.

prorateoptional	Boolean
Whether or not you want to prorate this transaction, only valid if you are changing the quantity. If you don't have account super user permission, anything submitted here will be ignored and the system global prorate value will be used.

next_bill_dateoptional	Date
The next date this service will bill. Only valid for multi-month services. If unset, it will bill on the next account billing date.

service_metadataoptional	Array
An array of objects, each object should have an 'id' and 'value' property, where the 'id' is the ID of a service metadata field, and the 'value' is the value you wish to set the field to.

Success 200
Field	Type	Description
id	Number
The internal ID of the service. You can use this to retrieve service details from the /services endpoint

number_of_times_billed	Number
Only valid for expiring services, this is the number of times the service has been run

price_override	Number
If the service has a price override on it, it will be represented here. Otherwise, this will be null

price_override_reason	String
If the service has a price override, the optional reason will be displayed here

package_id	Number
If this service was added as part of a package, the ID of the package will be displayed here. Services added as part of a package cannot be removed, except by removing the package itself

unique_package_id	String
If this service is part of a package, this is a unique string that will identify all services added within the same package. The function of this string is to differentiate one package from another, if the same package is added to the account twice.

unique_service_relationship_id	Number
This is a unique ID that represents this specific service as it relates to this specific account. This ID is used when adding a price override for this service, or deleting this service from the account

name_override	String
If this is set, then any transactions generated from this service when automatic billing runs will have this set as their description. See the debits/discounts endpoints for more details.

next_bill_date	Date
The next date this service will bill. If null, it will bill on the next account billing date.

metadata	Object
An object where the property is the metadata ID, and the value is the metadata value.

Success-Response:
HTTP/1.1 200 OK
{
  "data": {
    "id": 10,
    "number_of_times_billed": 2,
    "price_override": "12.50",
    "price_override_reason": "Discounting service",
    "package_id": null,
    "unique_package_id": null,
    "unique_service_relationship_id": 10,
    "name_override": null,
    "next_bill_date": null,
    "metadata": {
       "1": "test!!!123!",
       "2": "another test",
       "3": null
    }
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
             "unique_service_relationship_id": "The selected unique_service_relationship_id is not valid.",
         },
         "status_code": 422
     }
 }
Account Tax Overrides
```
