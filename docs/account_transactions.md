# Account Transactions Endpoints

## Apply an external PayPal payment (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/transactions/paypal_payments`
- **Description**: Store an externally made PayPal payment into Sonar. This should only be used to store PayPal payments made using the same PayPal API credentials as you have entered in Sonar. This endpoint is mostly designed to implement things like an external customer portal.
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `amount` (Number, required): The amount of the successful PayPal payment
    - `transaction_id` (String, required): The transaction ID of the PayPal payment. This is the sale ID provided in the returned transaction list from PayPal. It is important this is correct, or attempts to refund inside Sonar will fail.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 12.53,
        "payment_method_id": 0,
        "type": "paypal",
        "response_message": "APPROVED",
        "transaction_id": "ABC123",
        "success": true,
        "reversed": false,
        "reversed_at": null,
        "date": "2016-06-01 18:23:02"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "PayPal processing is not enabled.",
         "status_code": 422
       }
    }
    ```

## Create payment (POST)
- **Version**: 1.2.14
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments`
- **Description**: Create a payment. If you submit a payment method ID, this will use the payment processor for the payment method to run the payment in real time. If you do not, it will add a payment via whatever method you specify.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_method_id` (Number, optional): The ID of the payment method to use to make the payment. If this is omitted, payment_method must be specified
    - `payment_method` (String, optional): A string representing the type of payment this is. If payment_method_id is included, this is ignored (`"cash"`, `"check"`, `"wire"`)
    - `reference` (String, optional): If you're submitting a cash, check or wire payment, you can submit a string here that will be stored as a reference. If you're using a payment_method_id, this will be ignored, as the message stored will be the response from the payment processor.
    - `amount` (Number, required): The amount of the payment to post. This should be a decimal in the format xx.yy (e.g. 10.32 or 134.23)
    - `auto_apply` (Boolean, optional): Whether or not to automatically apply this payment to any outstanding invoices. If this is false, you will need to manually apply this payment to invoices to reduce their due balance
    - `date` (Date, optional): The date the payment should be applied for. Cannot be in the future, and is ignored for payments made via a payment method. If null, the current date will be used.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 55.39,
        "payment_method_id": 111,
        "type": "credit card",
        "response_message": "Successful.",
        "transaction_id": "12345ABC",
        "success": true,
        "reversed": false,
        "reversed_at": null,
        "date": "2015-09-23 16:55:12"
      }
    }
    ```

## Edit account payment (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments/:id`
- **Description**: Edit a payment. You can only change the reference on a wire, cash, check, or other payment.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `id` (Number, required): The ID of the payment
    - `response_message` (String, optional): The reference you want to store for this payment
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 7,
        "amount": 1,
        "payment_method_id": null,
        "type": "check",
        "response_message": "test",
        "transaction_id": null,
        "success": true,
        "reversed": false,
        "reversed_at": null,
        "date": "2016-07-10 18:43:28"
      }
    }
    ```

## Edit debit description (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/debits/:debit_id`
- **Description**: Edit the description on a debit
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `debit_id` (Number, required): The ID of the debit
    - `description` (String, optional): The description to overwrite the existing description with. Send null to remove it and revert to the service name.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 200,
        "amount": 186.48,
        "invoice_id": 241,
        "service_id": 6,
        "date": "2015-09-17 01:48:46",
        "reversed": true,
        "reversed_at": "2015-09-22",
        "discount_id": 265,
        "number_of_months": 3,
        "taxes": [
          {
            "description": "Sales Tax",
            "amount": 9
          },
          {
            "description": "Other Tax",
            "amount": 3
          }
        ],
        "description": "Fast Internet",
        "quantity": 1,
        "general_ledger_code": "1000",
        "general_ledger_code_description": "test test"
      }
    }
    ```

## Edit discount description (PATCH)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/discounts/:discount_id`
- **Description**: Edit the description on a discount
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `discount_id` (Number, required): The ID of the discount
    - `description` (String, optional): The description to overwrite the existing description with. Send null to revert back to the service name.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 265,
        "amount": 186.48,
        "amount_remaining": 198.48,
        "service_id": 6,
        "date": "2015-09-22 03:03:17",
        "reversed": false,
        "reversed_at": null,
        "taxes": [
          {
            "description": "Sales Tax",
            "amount": 9
          },
          {
            "description": "Other Tax",
            "amount": 3
          }
        ],
        "description": "Service name",
        "quantity": 1,
        "general_ledger_code": "1000",
        "general_ledger_code_description": "test test"
      }
    }
    ```

## Get all account debits (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/debits`
- **Description**: Get a list of the debits on the account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 200,
          "amount": 186.48,
          "invoice_id": 241,
          "service_id": 6,
          "date": "2015-09-17 01:48:46",
          "reversed": true,
          "reversed_at": "2015-09-22",
          "discount_id": 265,
          "number_of_months": 3,
          "taxes": [
            {
              "description": "Sales Tax",
              "amount": 9
            },
            {
              "description": "Some Other Tax",
              "amount": 3
            }
          ],
          "description": "Some Service",
          "quantity": 1
        },
        {
          "id": 201,
          "amount": 181.50,
          "invoice_id": 241,
          "service_id": 7,
          "date": "2015-09-17 01:48:46",
          "reversed": false,
          "reversed_at": null,
          "discount_id": null,
          "number_of_months": 3,
          "taxes": [],
          "description": "Look ma, no hands!",
          "quantity": 3,
          "general_ledger_code": "1000",
          "general_ledger_code_description": "test test"
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

## Get all account deposits (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/deposits`
- **Description**: Get a list of the deposits on the account. A deposit is created by a payment being applied to an account. The payment itself is tracked separately and is available at the /payments endpoint
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 3,
          "amount": 55.39,
          "amount_remaining": 0.00,
          "payment_id": 3,
          "void": false,
          "date": "2015-09-23 16:55:12"
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

## Get all account discounts (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/discounts`
- **Description**: Get a list of the discounts on the account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 265,
          "amount": 186.48,
          "amount_remaining": "198.48",
          "service_id": 6,
          "date": "2015-09-22 03:03:17",
          "reversed": false,
          "reversed_at": null,
          "taxes": [
            {
              "description": "Sales Tax",
              "amount": 9
            },
            {
              "description": "Other Tax",
              "amount": 3
            }
          ],
          "description": "Some description",
          "quantity": 1,
          "general_ledger_code": null,
          "general_ledger_code_description": null
        },
        {
          "id": 227,
          "amount": 214.53,
          "amount_remaining": 0.00,
          "service_id": 2,
          "date": "2015-09-17 01:48:46",
          "reversed": false,
          "reversed_at": null,
          "taxes": []
        },
        {
          "id": 228,
          "amount": 167.43,
          "amount_remaining": 1.98,
          "service_id": 10,
          "date": "2015-09-17 01:48:46",
          "reversed": false,
          "reversed_at": null,
          "taxes": [],
          "description": "Installation Credit",
          "quantity": 1,
          "general_ledger_code": null,
          "general_ledger_code_description": null
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

## Get all account payments (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments`
- **Description**: Get a list of the payments on the account. A payment creates a deposit
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 3,
          "amount": 55.39,
          "payment_method_id": 111,
          "type": "credit card",
          "response_message": "Successful.",
          "transaction_id": "12345ABC",
          "success": true,
          "reversed": false,
          "reversed_at": null,
          "date": "2015-09-23 16:55:12"
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

## Get individual account debit (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/debits/:debit_id`
- **Description**: Get an individual account debit by ID
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `debit_id` (Number, required): The ID of the debit
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 200,
        "amount": 186.48,
        "invoice_id": 241,
        "service_id": 6,
        "date": "2015-09-17 01:48:46",
        "reversed": true,
        "reversed_at": "2015-09-22",
        "discount_id": 265,
        "number_of_months": 3,
        "taxes": [
          {
            "description": "Sales Tax",
            "amount": 9
          },
          {
            "description": "Other Tax",
            "amount": 3
          }
        ],
        "description": "Some service name",
        "quantity": 1,
        "general_ledger_code": "1000",
        "general_ledger_code_description": "test test"
      }
    }
    ```

## Get individual account deposit (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/deposits/:deposit_id`
- **Description**: Get an individual account deposit by ID
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `deposit_id` (Number, required): The ID of the deposit
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 55.39,
        "amount_remaining": 0.00,
        "payment_id": 3,
        "void": false,
        "date": "2015-09-23 16:55:12"
      }
    }
    ```

## Get individual account discount (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/discounts/:discount_id`
- **Description**: Get an individual account discount by ID
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `discount_id` (Number, required): The ID of the discount
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 265,
        "amount": 186.48,
        "amount_remaining": 198.48,
        "service_id": 6,
        "date": "2015-09-22 03:03:17",
        "reversed": false,
        "reversed_at": null,
        "taxes": [
          {
            "description": "Sales Tax",
            "amount": 9
          },
          {
            "description": "Other Tax",
            "amount": 3
          }
        ],
        "description": "I wrote this",
        "quantity": 1,
        "general_ledger_code": "1000",
        "general_ledger_code_description": "test test"
      }
    }
    ```

## Get individual account payment (GET)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments/:payment_id`
- **Description**: Get an individual payment
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_id` (Number, required): The ID of the payment
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 55.39,
        "payment_method_id": 111,
        "type": "credit card",
        "response_message": "Successful.",
        "transaction_id": "12345ABC",
        "success": true,
        "reversed": false,
        "reversed_at": null,
        "date": "2015-09-23 16:55:12"
      }
    }
    ```

## Make a one time credit card payment (POST)
- **Version**: 1.7.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:id/transactions/one_time_credit_card_payment`
- **Description**: Make a one time credit card payment. This does not save the credit card to Sonar.
- **Parameters**:
    - `id` (Number, required): The ID of the account
    - `number` (Number, required): The credit card number
    - `cvc` (Number, optional): The CVC/CVV code on the credit card. Some providers require that this is sent - if so, this is not optional.
    - `expiration_month` (Number, required): The month as a digit (1-12)
    - `expiration_year` (Number, required): The 4 digit expiration year (e.g. 2018)
    - `amount` (Number, required): The amount to charge the card
    - `name_on_account` (String, required): The name on the credit card
    - `line1` (String, required): Line 1 of the card address (e.g. the street address.)
    - `city` (String, required): The city of the card address
    - `state` (String, required): The state, province or other country subdivision. You can obtain a valid list from `_data/subdivisions/:country`
    - `zip` (String, required): The ZIP/postal code of the card address
    - `country` (String, required): A valid, two character country code. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 4,
        "transaction_id": "100325923924",
        "message": "Declined Sale",
        "success": false
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": "That is not a valid credit card number. Please check and try again.",
         "status_code": 422
       }
    }
    ```

## Refund a payment (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments/:payment_id/refund`
- **Description**: Refund a payment. This will refund the payment transaction. You can only refund payments that are made with a payment processor, or via ACH batch. Cash, check or wire payments can only be reversed, as we have no way of refunding those payments.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_id` (Number, required): The ID of the payment
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 55.39,
        "payment_method_id": 111,
        "type": "credit card",
        "response_message": "Successful.",
        "transaction_id": "12345ABC",
        "success": true,
        "reversed": true,
        "reversed_at": "2015-09-30",
        "date": "2015-09-23 16:55:12"
      }
    }
    ```

## Reverse a payment (POST)
- **Version**: 0.6.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/transactions/payments/:payment_id/reverse`
- **Description**: Reverse a payment. This will reverse the payment transaction but will not issue a refund to the payment processor. Once a payment is reversed, it cannot be refunded, so ensure you use refund instead of reverse if you want the payment processor to issue a refund.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_id` (Number, required): The ID of the payment
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "id": 3,
        "amount": 55.39,
        "payment_method_id": 111,
        "type": "credit card",
        "response_message": "Successful.",
        "transaction_id": "12345ABC",
        "success": true,
        "reversed": true,
        "reversed_at": "2015-09-30",
        "date": "2015-09-23 16:55:12"
      }
    }
    ```
```
