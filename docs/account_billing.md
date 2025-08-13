# Account Billing Endpoints

## Get account billing details (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/billing_details`
- **Description**: Get some details about the accounts billing details. This is mainly used for the customer portal.
- **Parameters**:
    - `id` (Number, required): The internal ID of the account
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "balance_due": 586.5,
        "balance_total": 789.5,
        "next_recurring_charge_amount": 0,
        "next_bill_date": null,
        "available_funds": 123.45
      }
    }
    ```

## Get account billing parameters (GET)
- **Version**: 1.2.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/billing_parameters`
- **Description**: Get the account billing parameters
- **Parameters**:
    - `id` (Number, required): The internal ID of the account
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "bill_day": 18,
        "due_days": 10,
        "grace_days": 3,
        "grace_until": null,
        "months_to_bill": 1,
        "tax_exempt": false,
        "print_invoice": false,
        "separate_invoice_day_enabled": false,
        "invoice_day": 1,
        "auto_pay_days": 3,
        "bill_mode": "invoice",
        "auto_pay_day": "invoice",
        "due_days_day": "billing",
        "switch_status_after_delinquency": false,
        "days_of_delinquency_for_status_switch": 100,
        "delinquency_account_status_id": 3
      }
    }
    ```

## Update account billing parameters (PATCH)
- **Version**: 1.2.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/billing_parameters`
- **Description**: Update an accounts billing parameters. This requires account super user permission
- **Parameters**:
    - `id` (Number, required): The ID of the account to update
    - `bill_day` (Number, optional): The day of the month that the account bills
    - `due_days` (Number, optional): The number of days before the invoice becomes past due
    - `grace_days` (Number, optional): The number of days after the invoice is past due that penalties are applied
    - `grace_until` (Date, optional): A date that the account is graced until. This overrides grace_days until the date is passed, and then the account reverts to the grace_days parameter. This is null if unset
    - `months_to_bill` (Number, optional): The number of months that are invoiced at a time. For example, if this is 6, an invoice will be generated once every 6 months for 6 months worth of charges
    - `tax_exempt` (Boolean, optional): Whether or not the account is tax exempt
    - `prorate` (Boolean, optional): Whether or not to prorate the change, if you are updating the bill_day. If this is omitted, the system prorate default will be used. If this is included, it will override the default
    - `print_invoice` (Boolean, optional): Whether or not the account receives a printed invoice
    - `separate_invoice_day_enabled` (Boolean, optional): Whether or not invoices generated during automatic billing have a different invoice date/billing period than the day billing runs
    - `invoice_day` (Number, optional): If separate_invoice_day_enabled is true, this is the day of the following month that any automatic invoices will show as their date/billing period.
    - `auto_pay_days` (Number, optional): The number of days after automatic invoice generation that any auto-pay methods are charged
    - `bill_mode` (String, optional): Whether the user receives an invoice or a statement (`"invoice"`, `"statement"`)
    - `auto_pay_day` (String, optional): Whether the auto_pay_days value is counted from the billing date or the invoice date. Only applies if separate_invoice_day_enabled is true. (`"billing"`, `"invoice"`)
    - `due_days_day` (String, optional): Whether the due_days value is counted from the billing date or the invoice date. Only applies if separate_invoice_day_enabled is true. (`"billing"`, `"invoice"`)
    - `switch_status_after_delinquency` (Boolean, optional): Whether or not this account should be switched into a new inactive status after X days of delinquency.
    - `days_of_delinquency_for_status_switch` (Integer, optional): If switch_status_after_delinquency is true, this is the number of days of delinquency to allow before switching status
    - `delinquency_account_status_id` (Integer, optional): The account status ID to switch into after days_of_delinquency_for_status_switch is exceeded. Must be an inactive status.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "bill_day": 18,
        "due_days": 10,
        "grace_days": 3,
        "grace_until": null,
        "months_to_bill": 1,
        "tax_exempt": false,
        "print_invoice": false,
        "separate_invoice_day_enabled": false,
        "invoice_day": 1,
        "auto_pay_days": 3,
        "bill_mode": "invoice",
        "auto_pay_day": "invoice",
        "due_days_day": "billing",
        "switch_status_after_delinquency": false,
        "days_of_delinquency_for_status_switch": 100,
        "delinquency_account_status_id": 3
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "grace_until": "The grace until does not match the format Y-m-d."
            },
            "status_code": 422
        }
    }
    ```
```
