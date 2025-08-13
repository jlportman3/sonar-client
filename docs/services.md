# Services Endpoints

## Create service (POST)
Version: 1.7.16

Endpoint: `https://example.sonar.software/api/v1/system/services`

Description: Create a new service
#### Request Example
```json
{
  "id": 1,
  "active": true,
  "name": "example",
  "type": "example",
  "application": "example",
  "amount": 1,
  "billing_frequency_in_months": 1,
  "times_to_run": 1,
  "limit_adjustments": true,
  "period_days": 1,
  "max_amount_per_period": 1,
  "taxes": [],
  "roles": [],
  "data_service": true,
  "download_in_kilobits": 1,
  "upload_in_kilobits": 1,
  "technology_code": 1,
  "usage_based_billing_policy_id": 1,
  "unit_quantity_in_gigabytes": 1,
  "general_ledger_code_id": 1,
  "tax_exemption_amount": 1,
  "voice_service": true,
  "unlimited_local_minutes": true,
  "unlimited_long_distance_minutes": true,
  "local_minutes": 1,
  "local_minutes_amount": 1,
  "long_distance_minutes": 1,
  "long_distance_minutes_amount": 1,
  "first_interval_in_seconds": 1,
  "sub_interval_in_seconds": 1,
  "local_prefixes": [],
  "inbound_toll_free_rate": 1,
  "account_groups": []
}
```

```
Parameter
Field	Type	Description
idoptional	Integer
The internal ID assigned to the service. You should omit this unless you explicitly need a specific ID to facilitate an import.

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

type	String
One of one time, expiring, overage, or recurring, defines what type of service this is

Allowed values: "one time", "recurring", "expiring", "adjustment", "overage"

application	String
One of credit or debit, defines whether or not the service applies or charge or a discount

Allowed values: "credit", "debit"

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_runoptional	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustmentsoptional	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_daysoptional	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_periodoptional	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxesoptional	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

rolesoptional	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_serviceoptional	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobitsoptional	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second. Required if data_service is true.

upload_in_kilobitsoptional	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second. Required if data_service is true.

technology_codeoptional	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_idoptional	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true.

unit_quantity_in_gigabytesoptional	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount. Required if type is overage.

general_ledger_code_idoptional	Integer
The ID of the general ledger code you wish to assign to this service

tax_exemption_amountoptional	Number
The amount of the service to exempt from taxation. For example, if this service costs $50, but only $25 of it is taxable, set this to 25. Should be omitted in cases where the entirety of the service is taxable.

voice_serviceoptional	Boolean
Whether or not this is a voice service

unlimited_local_minutesoptional	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutesoptional	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutesoptional	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amountoptional	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutesoptional	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amountoptional	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_secondsoptional	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_secondsoptional	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixesoptional	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rateoptional	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groupsoptional	Array
An array of account group IDs

Success 200
Field	Type	Description
id	Number
The internal ID of the service

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

type	String
One of one time, adjustment, expiring, overage, or recurring

application	String
One of credit or debit

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_run	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustments	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_days	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_period	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxes	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

roles	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_service	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobits	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second.

upload_in_kilobits	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second.

technology_code	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_id	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true

unit_quantity_in_gigabytes	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount

general_ledger_code_id	Integer
The ID of the general ledger code assigned to this service

tax_exemption_amount	Number
The amount of the service cost to exempt from taxation

voice_service	Boolean
Whether or not this is a voice service

unlimited_local_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutes	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amount	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutes	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amount	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_seconds	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_seconds	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixes	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rate	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groups	Array
An array of account group IDs

Success-Response:
HTTP/1.1 201 OK
{
    "data": {
         "id": 3,
         "active": true,
         "name": "Schumm Ltd",
         "type": "recurring",
         "application": "debit",
         "amount": 63.62,
         "billing_frequency_in_months": 1,
         "times_to_run": 4,
         "limit_adjustments": false,
         "period_days": 0,
         "max_amount_per_period": "0.00",
         "taxes": [],
         "roles": [],
         "data_service": true,
         "upload_in_kilobits": 500,
         "download_in_kilobits": 1000,
         "technology_code": 70,
         "usage_based_billing_policy_id": 1,
         "unit_quantity_in_gigabytes": null,
         "general_ledger_code_id": 1,
         "tax_exemption_amount": 0,
         "voice_service": false,
         "unlimited_local_minutes": false,
         "unlimited_long_distance_minutes": false,
         "local_minutes": null,
         "local_minutes_amount": 0,
         "long_distance_minutes": null,
         "long_distance_minutes_amount": 0,
         "first_interval_in_seconds": null,
         "sub_interval_in_seconds": null,
         "local_prefixes": [],
         "inbound_toll_free_rate": null,
         "account_groups": []
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
             "type": "magic is not a valid service type"
         },
         "status_code": 422
     }
 }
```

## Delete service (DELETE)
Version: 0.2.0

Endpoint: `https://example.sonar.software/api/v1/system/services/:id`

Description: Delete a service. Be careful when using this method! Deletion will permanently disassociate the service from all accounts, packages and roles.
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
The ID of the service

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
         "message": "That service does not exist.",
         "status_code": 404
     }
 }
```

## Get all services (GET)
Version: 1.7.16

Endpoint: ``

Description: https://example.sonar.software/api/v1/system/services

```
Success 200
Field	Type	Description
id	Number
The internal ID of the service

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

type	String
One of one time, adjustment, expiring, overage, or recurring

application	String
One of credit or debit

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_run	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustments	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_days	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_period	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxes	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

roles	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_service	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobits	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second.

upload_in_kilobits	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second.

technology_code	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_id	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true

unit_quantity_in_gigabytes	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount

general_ledger_code_id	Integer
The ID of the general ledger code assigned to this service

tax_exemption_amount	Number
The amount of the service cost to exempt from taxation

voice_service	Boolean
Whether or not this is a voice service

unlimited_local_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutes	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amount	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutes	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amount	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_seconds	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_seconds	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixes	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rate	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groupsoptional	Array
An array of account group IDs

Success-Response:
HTTP/1.1 200 OK
{
     "data": [
         {
             "id": 3,
             "active": true,
             "name": "Schumm Ltd",
             "type": "recurring",
             "application": "debit",
             "amount": 63.62,
             "billing_frequency_in_months": 1,
             "times_to_run": 4,
             "limit_adjustments": false,
             "period_days": 0,
             "max_amount_per_period": "0.00",
             "taxes": [],
             "roles": [],
             "data_service": true,
             "upload_in_kilobits": 500,
             "download_in_kilobits": 1000,
             "technology_code": 70,
             "usage_based_billing_policy_id": 1,
             "unit_quantity_in_gigabytes": null,
             "general_ledger_code_id": 1,
             "tax_exemption_amount": 0,
             "voice_service": false,
             "unlimited_local_minutes": false,
             "unlimited_long_distance_minutes": false,
             "local_minutes": null,
             "local_minutes_amount": 0,
             "long_distance_minutes": null,
             "long_distance_minutes_amount": 0,
             "first_interval_in_seconds": null,
             "sub_interval_in_seconds": null,
             "local_prefixes": [],
             "inbound_toll_free_rate": null,
             "account_groups": []
         },
     ],
     "paginator": {
         "total_count": 30,
         "total_pages": 15,
         "current_page": 1,
         "limit": 2
     }
}
```

## Get individual service (GET)
Version: 1.7.16

Endpoint: `https://example.sonar.software/api/v1/system/services/:id`

Description: Get an individual service.
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
The ID of the account status

Success 200
Field	Type	Description
id	Number
The internal ID of the service

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

type	String
One of one time, adjustment, expiring, overage, or recurring

application	String
One of credit or debit

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_run	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustments	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_days	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_period	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxes	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

roles	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_service	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobits	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second.

upload_in_kilobits	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second.

technology_code	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_id	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true

unit_quantity_in_gigabytes	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount

general_ledger_code_id	Integer
The ID of the general ledger code assigned to this service

tax_exemption_amount	Number
The amount of the service cost to exempt from taxation

voice_service	Boolean
Whether or not this is a voice service

unlimited_local_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutes	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amount	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutes	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amount	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_seconds	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_seconds	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixes	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rate	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groupsoptional	Array
An array of account group IDs

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "id": 3,
             "active": true,
             "name": "Schumm Ltd",
             "type": "recurring",
             "application": "debit",
             "amount": 63.62,
             "billing_frequency_in_months": 1,
             "times_to_run": 4,
             "limit_adjustments": false,
             "period_days": 0,
             "max_amount_per_period": "0.00",
             "taxes": [],
             "roles": [],
             "data_service": true,
             "upload_in_kilobits": 500,
             "download_in_kilobits": 1000,
             "technology_code": 70,
             "usage_based_billing_policy_id": 1,
             "unit_quantity_in_gigabytes": null,
             "general_ledger_code_id": 1,
             "tax_exemption_amount": 0,
             "voice_service": false,
             "unlimited_local_minutes": false,
             "unlimited_long_distance_minutes": false,
             "local_minutes": null,
             "local_minutes_amount": 0,
             "long_distance_minutes": null,
             "long_distance_minutes_amount": 0,
             "first_interval_in_seconds": null,
             "sub_interval_in_seconds": null,
             "local_prefixes": [],
             "inbound_toll_free_rate": null,
             "account_groups": []
    }
}
```

## Update service (PATCH)
Version: 1.7.16

Endpoint: `https://example.sonar.software/api/v1/system/services/:id`

Description: Update a service. The type cannot be changed.
#### Request Example
```json
{
  "id": 1,
  "active": true,
  "name": "example",
  "application": "example",
  "amount": 1,
  "billing_frequency_in_months": 1,
  "times_to_run": 1,
  "limit_adjustments": true,
  "period_days": 1,
  "max_amount_per_period": 1,
  "taxes": [],
  "roles": [],
  "data_service": true,
  "download_in_kilobits": 1,
  "upload_in_kilobits": 1,
  "technology_code": 1,
  "usage_based_billing_policy_id": 1,
  "unit_quantity_in_gigabytes": 1,
  "general_ledger_code_id": 1,
  "tax_exemption_amount": 1,
  "voice_service": true,
  "unlimited_local_minutes": true,
  "unlimited_long_distance_minutes": true,
  "local_minutes": 1,
  "local_minutes_amount": 1,
  "long_distance_minutes": 1,
  "long_distance_minutes_amount": 1,
  "first_interval_in_seconds": 1,
  "sub_interval_in_seconds": 1,
  "local_prefixes": [],
  "inbound_toll_free_rate": 1,
  "account_groups": []
}
```

```
Parameter
Field	Type	Description
idoptional	Integer
The internal ID assigned to the service. You should omit this unless you explicitly need a specific ID to facilitate an import.

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

application	String
One of credit or debit, defines whether or not the service applies or charge or a discount

Allowed values: "credit", "debit"

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_runoptional	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustmentsoptional	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_daysoptional	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_periodoptional	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxesoptional	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

rolesoptional	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_serviceoptional	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobitsoptional	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second. Required if data_service is true.

upload_in_kilobitsoptional	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second. Required if data_service is true.

technology_codeoptional	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_idoptional	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true.

unit_quantity_in_gigabytesoptional	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount. Required if type is overage.

general_ledger_code_idoptional	Integer
The ID of the general ledger code you wish to assign to this service

tax_exemption_amountoptional	Number
The amount of the service to exempt from taxation. For example, if this service costs $50, but only $25 of it is taxable, set this to 25. Should be omitted in cases where the entirety of the service is taxable.

voice_serviceoptional	Boolean
Whether or not this is a voice service

unlimited_local_minutesoptional	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutesoptional	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutesoptional	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amountoptional	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutesoptional	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amountoptional	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_secondsoptional	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_secondsoptional	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixesoptional	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rateoptional	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groupsoptional	Array
An array of account group IDs

Success 200
Field	Type	Description
id	Number
The internal ID of the service

active	Boolean
Whether or not this service can still be added to accounts

name	String
A descriptive name for the service

type	String
One of one time, adjustment, expiring, overage, or recurring

application	String
One of credit or debit

amount	Number
The amount the service costs

billing_frequency_in_months	Integer
How often this service bills, 1 for monthly, 12 for annually, etc. Only valid for recurring services.

times_to_run	Number
This is only used for expiring services, it represents the number of times the service will run before being expired from the account. Setting this value on any other service does nothing

limit_adjustments	Boolean
This is only used for adjustment services. If it is true, then the period_days and max_amount_per_period values are applied. If false, they are ignored

Default value: false

period_days	Number
This is only used for adjustment services, it represents the number of days tracked for the max_amount_per_period value

max_amount_per_period	Number
This is only used for adjustment services. If it is greater than 0, a user can only apply this adjustment service until they have applied up to max_period_per_days amount, within a rolling window defined by period_days

taxes	Array
An array of tax IDs that are assessed on this service. Get details from the /taxes endpoint.

roles	Array
An array of role IDs. This is only valid for adjustment based services - it controls which roles can apply this adjustment

data_service	Boolean
Only valid for recurring services. If this is true, this is a data service (e.g. it provides data/Internet connectivity to an end user.)

download_in_kilobits	Integer
Only valid if data_service is true. The download speed of the service in kilobits per second.

upload_in_kilobits	Integer
Only valid if data_service is true. The upload speed of the service in kilobits per second.

technology_code	Integer
The technology code for the service. Only required if this is a data service. This is mostly used for generating the FCC Form 477 report, and the integers correspond to the following types. 0 = Other, 10 = Asymmetric xDSL, 20 = Symmetric xDSL, 30 = Copper Wireline, 40 = Cable Modem, 50 = Fiber, 60 = Satellite, 70 = Terrestrial Fixed Wireless, 90 = Electric Power Line.

Default value: 0

Allowed values: "0", "10", "20", "30", "40", "50", "60", "70", "90"

usage_based_billing_policy_id	Integer
The ID of the usage based billing policy applied to this service. Only valid if data_service is true

unit_quantity_in_gigabytes	Integer
If this is an overage service, this is the amount of gigabytes provided for the cost specified in amount

general_ledger_code_id	Integer
The ID of the general ledger code assigned to this service

tax_exemption_amount	Number
The amount of the service cost to exempt from taxation

voice_service	Boolean
Whether or not this is a voice service

unlimited_local_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited local minutes

unlimited_long_distance_minutes	Boolean
If this is a voice service, this describes whether the voice service offers unlimited long distance minutes

local_minutes	Integer
If unlimited_local_minutes is false, this is the number of free local minutes provided with the service

local_minutes_amount	Number
If unlimited_local_minutes is false, this is the cost per minute once the free minutes are used up.

long_distance_minutes	Integer
If unlimited_long_distance_minutes is false, this is the number of free long distance minutes provided with the service

long_distance_minutes_amount	Number
If unlimited_long_distance_minutes is false, this is the cost per minute once the free minutes are used up.

first_interval_in_seconds	Integer
If this is a voice service, this is the minimum amount of time for each call. For example, if this is 60, then a 2 second call will always be charged at a 60 second rate.

sub_interval_in_seconds	Integer
If this is a voice service, this is the minimum time per block after the first_interval_in_seconds. For example, if the first interval is 60, and the sub interval is 30, then a 61 second call will be charged at a 90 second rate.

local_prefixes	Array
If this is a voice service, this is an array of local prefixes (e.g. area codes). Any calls that start with a prefix in this array will be classified as local.

inbound_toll_free_rate	Number
If this is a voice service, this is the rate per minute charged for any inbound toll free calls

account_groupsoptional	Array
An array of account group IDs

Success-Response:
HTTP/1.1 200 OK
{
    "data": {
        "id": 3,
         "active": true,
         "name": "Schumm Ltd",
         "type": "recurring",
         "application": "debit",
         "amount": 63.62,
         "billing_frequency_in_months": 1,
         "times_to_run": 4,
         "limit_adjustments": false,
         "period_days": 0,
         "max_amount_per_period": "0.00",
         "taxes": [],
         "roles": [],
         "data_service": true,
         "upload_in_kilobits": 500,
         "download_in_kilobits": 1000,
         "technology_code": 70,
         "usage_based_billing_policy_id": 1,
         "unit_quantity_in_gigabytes": null,
         "general_ledger_code_id": 1,
         "tax_exemption_amount": 0,
         "voice_service": false,
         "unlimited_local_minutes": false,
         "unlimited_long_distance_minutes": false,
         "local_minutes": null,
         "local_minutes_amount": 0,
         "long_distance_minutes": null,
         "long_distance_minutes_amount": 0,
         "first_interval_in_seconds": null,
         "sub_interval_in_seconds": null,
         "local_prefixes": [],
         "inbound_toll_free_rate": null,
         "account_groups": [ 1 ]
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
        "type": "magic is not a valid service type"
    },
        "status_code": 422
    }
}
System
```
