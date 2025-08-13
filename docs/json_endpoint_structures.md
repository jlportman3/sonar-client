# JSON Endpoint Structures

This document provides example JSON structures for the `/json` endpoints accessed via `Sonar.get_direct_json`. These examples are based on actual data retrieved from a Sonar instance.

## 1. Customer Contact Information Report

- **Endpoint**: `reports/accounts/contact_information/json`
- **Description**: This endpoint returns a list of customer contact records. Each record is a list of values representing different attributes of the customer and their primary contact information.

- **Example JSON Structure (first record)**:
```json
[
  9263,
  "<a href='https://alamobb.sonar.software/accounts/9263'>Margie Vega</a>",
  "Active",
  "Margie Vega",
  "mgvega123@aol.com",
  "2103891279",
  "2102913779 x",
  null,
  null,
  "R.F.Wireless",
  "13670 old corpus christi rd",
  "#1",
  "Elmendorf",
  "TX",
  "78112",
  "29.2845",
  "-98.37306",
  "13670 old corpus christi rd",
  "#1",
  "Elmendorf",
  "TX",
  "78112"
]
```
- **Field Descriptions (based on observed data and common patterns)**:
    - Index 0: `customer_id` (Integer) - Unique identifier for the customer account.
    - Index 1: `customer_link_html` (String) - HTML string containing a link to the customer's account page.
    - Index 2: `account_status` (String) - Current status of the account (e.g., "Active", "Inactive").
    - Index 3: `customer_name` (String) - Name of the customer.
    - Index 4: `email_address` (String) - Primary email address of the customer.
    - Index 5: `phone_number_1` (String) - Primary phone number.
    - Index 6: `phone_number_2` (String) - Secondary phone number (may include extension).
    - Index 7-8: (Null) - Placeholder or unused fields.
    - Index 9: `account_group_name` (String) - Name of the account group the customer belongs to.
    - Index 10: `address_line_1` (String) - First line of the physical address.
    - Index 11: `address_line_2` (String) - Second line of the physical address (e.g., apartment/suite number).
    - Index 12: `city` (String) - City of the physical address.
    - Index 13: `state` (String) - State of the physical address.
    - Index 14: `zip_code` (String) - Zip/postal code of the physical address.
    - Index 15: `latitude` (String) - Latitude of the physical address.
    - Index 16: `longitude` (String) - Longitude of the physical address.
    - Index 17-21: (Repeated Address Fields) - These fields appear to be a repetition of address components, possibly for different address types or historical reasons.

## 2. Detailed Customer Data for a Specific ID

- **Endpoint**: `accounts/{customer_id}/json`
- **Description**: This endpoint provides a comprehensive JSON object containing detailed information about a single customer account, including nested objects for addresses, groups, services, and dashboard-related data.

- **Example JSON Structure (truncated for brevity)**:
```json
{
  "account": {
    "id": 9263,
    "name": "Margie Vega",
    "account_status_id": 2,
    "account_type_id": 1,
    "deleted_at": null,
    "created_at": "2018-03-24 05:27:30",
    "updated_at": "2025-06-01 05:05:11",
    "activation_date": "2018-03-24 00:27:30",
    "next_bill_date": "2025-07-01",
    "last_billed_invoice_id": 164548,
    "master_account_id": null,
    "delinquent": false,
    "delinquency_date": null,
    "usage_cap_exceeded": false,
    "geo_taxes": [],
    "addresses": [
      {
        "id": 2724,
        "line1": "13670 old corpus christi rd",
        "line2": "#1",
        "city": "Elmendorf",
        "state": "TX",
        "zip": "78112",
        "country": "US",
        "latitude": "29.2845",
        "longitude": "-98.37306",
        "fips": "480291418001025",
        "address_type_id": 1,
        "addressable_id": 9263,
        "addressable_type": "Sonar\\Account",
        "created_at": "2018-03-24 05:27:30",
        "updated_at": "2022-02-22 12:17:22",
        "county": "Bexar Co.",
        "failed_geocoding": false,
        "pcode": "3683100",
        "address_type": {
          "id": 1,
          "name": "physical",
          "is_internal": true,
          "created_at": "2018-03-23 22:47:26",
          "updated_at": "2018-03-23 22:47:26",
          "deleted_at": null
        }
      }
    ],
    "groups": [
      {
        "id": 1,
        "name": "R.F.Wireless",
        "created_at": "2018-03-24 00:56:41",
        "updated_at": "2018-04-05 12:10:27",
        "deleted_at": null,
        "pivot": {
          "account_id": 9263,
          "account_group_id": 1
        }
      }
    ],
    "sub_accounts": [],
    "contracts": [],
    "services": [
      {
        "id": 2424,
        "active": true,
        "name": "Optional Service Maintenance",
        "application": "debit",
        "amount": "7.00",
        "times_to_run": 0,
        "period_days": 0,
        "max_amount_per_period": 0,
        "deleted_at": null,
        "created_at": "2018-03-24 03:17:26",
        "updated_at": "2020-07-01 18:33:09",
        "tax_exemption_amount": 0,
        "limit_adjustments": false,
        "data_service": false,
        "download_in_kilobits": 0,
        "upload_in_kilobits": 0,
        "technology_code": 0,
        "usage_based_billing_policy_id": null,
        "unit_quantity_in_gigabytes": null,
        "type": "recurring",
        "general_ledger_code_id": 5,
        "lte_plan": null,
        "unlimited_local_minutes": false,
        "local_minutes": null,
        "unlimited_long_distance_minutes": false,
        "long_distance_minutes": null,
        "voice_service": false,
        "first_interval_in_seconds": null,
        "sub_interval_in_seconds": null,
        "local_prefixes": [],
        "inbound_toll_free_rate": 0,
        "billing_frequency_in_months": 1,
        "avalara_tax_type_id": 6,
        "pivot": {
          "account_id": 9263,
          "service_id": 2424,
          "number_of_times_billed": 0,
          "price_override": null,
          "price_override_reason": null,
          "created_at": "2018-04-02 01:27:50",
          "updated_at": "2018-04-02 01:27:50",
          "date_addition_prorate_applied": null,
          "package_id": null,
          "unique_service_relationship_id": 2841,
          "name_override": null,
          "unique_package_id": null,
          "quantity": 1,
          "next_bill_date": null,
          "package_name": null,
          "service_metadata": []
        },
        "usage_based_billing_policy": null
      }
    ],
    "master_account": null,
    "status": {
      "id": 2,
      "name": "Active",
      "is_internal": true,
      "active": true,
      "color": "#3498db",
      "created_at": "2018-03-23 22:47:10",
      "updated_at": "2018-03-23 22:47:10",
      "deleted_at": null,
      "account_super_user_only": false
    },
    "type": {
      "id": 1,
      "name": "Residential"
    },
    "dashboard_information": {
      "recent_communications": [
        {
          "id": 1809,
          "account_id": 9263,
          "subject": "Cancelling & Moving - Phone In 10.13.2021",
          "body": "Customer stated they would be cancelling soon and new tenants will be getting installed.",
          "time_in_seconds": 25,
          "user_id": 21,
          "created_at": "2021-11-12 19:36:58",
          "updated_at": "2021-11-12 19:36:58"
        }
      ],
      "communication_durations_and_counts": {
        "call_log_average_duration": 0,
        "ticket_average_duration": 0,
        "call_log_count": 0,
        "ticket_count": 0
      },
      "last_invoices": [
        {
          "invoice_id": 164548,
          "remaining_due": "0.00",
          "child_invoice_remaining_due": "0",
          "invoice_date": "2025-06-01",
          "delinquent": false,
          "invoice_debits_total": "46.95",
          "invoice_taxes_total": "0.48"
        }
      ],
      "average_data_usage": {
        "billable_in_bytes": 643914011553,
        "billable_out_bytes": 54498258942,
        "free_in_bytes": 0,
        "free_out_bytes": 0
      }
    }
  }
}
```
- **Key Fields and Nested Structures**:
    - `account` (Object): Contains core account details.
        - `id` (Integer): Account ID.
        - `name` (String): Account name.
        - `account_status_id` (Integer): ID of the account's status.
        - `account_type_id` (Integer): ID of the account's type.
        - `created_at` (DateTime): Timestamp of account creation.
        - `updated_at` (DateTime): Timestamp of last account update.
        - `addresses` (Array of Objects): List of addresses associated with the account.
            - `id` (Integer): Address ID.
            - `line1`, `line2`, `city`, `state`, `zip`, `country` (String): Address components.
            - `latitude`, `longitude` (String): Geographical coordinates.
            - `address_type` (Object): Details about the address type (e.g., "physical", "mailing").
        - `groups` (Array of Objects): List of groups the account belongs to.
            - `id` (Integer): Group ID.
            - `name` (String): Group name.
        - `services` (Array of Objects): List of services associated with the account.
            - `id` (Integer): Service ID.
            - `name` (String): Service name.
            - `type` (String): Type of service (e.g., "recurring", "one time").
            - `amount` (String): Cost of the service.
            - `data_service` (Boolean): Indicates if it's a data service.
            - `download_in_kilobits`, `upload_in_kilobits` (Integer): Speeds for data services.
            - `pivot` (Object): Relationship details between account and service.
        - `status` (Object): Detailed information about the account's status.
        - `type` (Object): Detailed information about the account's type.
        - `dashboard_information` (Object): Various statistics and recent activities related to the account.
            - `recent_communications` (Array of Objects): Recent call logs or tickets.
            - `communication_durations_and_counts` (Object): Aggregated communication metrics.
            - `last_invoices` (Array of Objects): Details of recent invoices.
            - `average_data_usage` (Object): Data usage statistics.
