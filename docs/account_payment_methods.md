# Account Payment Methods Endpoints

## Create account payment method from an existing token (POST)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/tokenized_payment_method`
- **Description**: Create a new account payment method from an existing token. This should generally only be used when importing from another billing platform with existing tokens. You should ensure your Sonar system is already configured with the correct payment processor information before using this method. It is not possible for us to validate that the tokenized information is correct, so make sure you have done so on your side before submission.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account this payment method should exist on
    - `payment_processor_customer_profile_id` (String, optional): If the payment processor being used stores a customer ID for their tokenization service, submit it here. This is optional, but must be included if the processor requires it
    - `token` (String, required): The existing token for the payment method
    - `name_on_account` (String, required): The name on the credit card, or the name on the bank account.
    - `type` (String, required): The type of payment method (`"credit card"`, `"echeck"`)
    - `identifier` (String, required): This is generally the last few digits of the credit card or bank account. This should be a maximum of 4 characters
    - `expiration_year` (Number, required): Only required for credit cards, a 4 digit expiration year
    - `expiration_month` (Number, required): Only required for credit cards, a 2 digit expiration month
    - `auto` (Boolean, required): Whether or not this payment method should be set to auto pay
    - `card_type` (String, optional): If this is a credit card, the type of card this is (`"visaelectron"`, `"maestro"`, `"forbrugsforeningen"`, `"dankort"`, `"visa"`, `"mastercard"`, `"amex"`, `"dinersclub"`, `"discover"`, `"unionpay"`, `"jcb"`)
    - `line1` (String, required): The address line of the credit card billing address. Only required if type is credit card.
    - `city` (String, required): City of the credit card billing address. Only required if type is credit card.
    - `state` (String, required): The state/province of the credit card billing address. Only required if type is credit card. You can obtain a valid list from `_data/subdivisions/:country`
    - `zip` (String, required): ZIP/postal code of the credit card billing address. Only required if type is credit card.
    - `country` (String, required): Two character ISO code of the country of the credit card billing address. Only required if type is credit card. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
         "id": 1195,
         "name_on_account": "Steve Martin",
         "type": "credit card",
         "identifier": "1111",
         "expiration_month": "09",
         "expiration_year": 2018,
         "auto": false,
         "line1": "4546 N Avenue",
         "city": "Somewhere",
         "state": "WI",
         "zip": "51234",
         "country": "US"
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "The selected type is not valid."
            },
            "status_code": 422
        }
    }
    ```

## Create account payment method (POST)
- **Version**: 1.7.11
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods`
- **Description**: Create a new account payment method. Be cautious when using this method as you will be transmitting raw credit card or bank account data. You must ensure you take all necessary precautions to secure this data and that you understand the impact this may have on your PCI compliance.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account to add the payment method to
    - `type` (String, required): The type of payment method being added (`"credit card"`, `"bank account"`)
    - `expiration_month` (Number, optional): An integer representing the expiration month, if this is a credit card. 1 for January, 12 for December. Don't submit for bank accounts
    - `expiration_year` (Number, optional): A four digit integer representing the expiration year, if this is a credit card. Don't submit for bank account
    - `account_number` (Number, required): For credit cards, this is the account number on the card, typically 16 digits but can be a different length. For bank accounts, this is the bank account number
    - `cvc` (Number, optional): The CVC/CVV code from the credit card. Optional but recommended for credit cards, should be excluded otherwise. Some providers require this - in this case, it is not optional.
    - `routing_number` (Number, optional): If this is a bank account, the routing number for the bank. Don't submit for credit cards
    - `name_on_account` (String, required): The name that is on the credit card, or the name that is on the bank account
    - `account_type` (String, optional): If this is a bank account, submit one of 'checking' or 'savings'. Don't submit for credit cards (`"checking"`, `"savings"`)
    - `auto` (Boolean, required): Whether or not this payment method should be set to auto pay
    - `line1` (String, required): The address line of the credit card billing address. Only required if type is credit card.
    - `city` (String, required): City of the credit card billing address. Only required if type is credit card.
    - `state` (String, required): The state/province of the credit card billing address. Only required if type is credit card. You can obtain a valid list from `_data/subdivisions/:country`
    - `zip` (String, required): ZIP/postal code of the credit card billing address. Only required if type is credit card.
    - `country` (String, required): Two character ISO code of the country of the credit card billing address. Only required if type is credit card. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 111,
        "type": "credit card",
        "identifier": "2333",
        "expiration_month": 8,
        "expiration_year": 2020,
        "auto": true
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "type": "The selected type is not valid."
            },
            "status_code": 422
        }
    }
    ```

## Delete account payment method (DELETE)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods/:payment_method_id`
- **Description**: Delete an account payment method
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_method_id` (Number, required): The ID of the payment method
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
            "message": "No item with that ID found.",
            "status_code": 404
        }
    }
    ```

## Get all account payment methods (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods`
- **Description**: Get a list of the payment methods for account
- **Parameters**:
    - `limit` (Number, optional): The number of entries to return
    - `page` (Number, optional): The page of results to return
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
         "id": 1195,
         "name_on_account": "Steve Martin",
         "type": "credit card",
         "identifier": "1111",
         "expiration_month": "09",
         "expiration_year": 2018,
         "auto": false,
         "line1": "4546 N Avenue",
         "city": "Somewhere",
         "state": "WI",
         "zip": "51234",
         "country": "US"
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

## Get individual account payment method (GET)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods/:payment_method_id`
- **Description**: Get an individual account payment method.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account
    - `payment_method_id` (Number, required): The ID of the payment method
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
         "id": 1195,
         "name_on_account": "Steve Martin",
         "type": "credit card",
         "identifier": "1111",
         "expiration_month": "09",
         "expiration_year": 2018,
         "auto": false,
         "line1": "4546 N Avenue",
         "city": "Somewhere",
         "state": "WI",
         "zip": "51234",
         "country": "US"
       }
    }
    ```

## Toggle the auto payment setting (POST)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods/:id/toggle_auto`
- **Description**: Toggle the automatic payment flag on a payment method. Only one payment method can be auto at a time - enabling auto on a method will disable auto on all other methods.
- **Parameters**:
    - `account_id` (Integer, required): The ID of the account
    - `id` (Integer, required): The ID of the payment method
    - `auto` (Boolean, required): The automatic payment state of the payment method
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
         "id": 1195,
         "name_on_account": "Steve Martin",
         "type": "credit card",
         "identifier": "1111",
         "expiration_month": "09",
         "expiration_year": 2018,
         "auto": false,
         "line1": "4546 N Avenue",
         "city": "Somewhere",
         "state": "WI",
         "zip": "51234",
         "country": "US"
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "auto": "auto must be a boolean."
            },
            "status_code": 422
        }
    }
    ```

## Update stored credit card (PATCH)
- **Version**: 1.1.7
- **Endpoint**: `https://example.sonar.software/api/v1/accounts/:account_id/payment_methods/:payment_method_id`
- **Description**: Update a stored credit card on an account.
- **Parameters**:
    - `account_id` (Number, required): The ID of the account to update the address on
    - `payment_method_id` (Number, required): The ID of the payment method
    - `name_on_account` (String, required): The name on the credit card.
    - `expiration_month` (Number, required): A representation of the expiration month for credit cards as an integer, where 1 is January and 12 is December.
    - `expiration_year` (Number, required): A 4 digit integer representing the expiration year for credit cards.
    - `auto` (Boolean, required): Whether or not this should be an automatic payment method. Setting auto to true on a payment method will unset auto on any other payment methods on the account
    - `line1` (String, required): The address line of the credit card billing address.
    - `city` (String, required): City of the credit card billing address.
    - `state` (String, required): The state/province of the credit card billing address.. You can obtain a valid list from `_data/subdivisions/:country`
    - `zip` (String, required): ZIP/postal code of the credit card billing address..
    - `country` (String, required): Two character ISO code of the country of the credit card billing address.. You can obtain a list of valid country codes from the `/_data/countries` API endpoint.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
         "id": 1195,
         "name_on_account": "Steve Martin",
         "type": "credit card",
         "identifier": "1111",
         "expiration_month": "09",
         "expiration_year": 2018,
         "auto": false,
         "line1": "4546 N Avenue",
         "city": "Somewhere",
         "state": "WI",
         "zip": "51234",
         "country": "US"
       }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": {
                "auto": "The selected value is not valid."
            },
            "status_code": 422
        }
    }
    ```
```
