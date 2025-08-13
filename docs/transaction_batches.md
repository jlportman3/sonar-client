# Transaction Batches Endpoints

## Create a new transaction batch (POST)
- **Version**: 1.0.11
- **Endpoint**: `https://example.sonar.software/api/v1/financial/transaction_batches`
- **Description**: Create a new transaction batch. A transaction batch allows you to import multiple transactions in a single call. The transactions will be queued and entered in the background, and any failures will be sent to you as a notification.
- **Parameters**:
    - `name` (String, optional): A name for the transaction batch
    - `batch_id` (String, optional): A batch ID. This is not required, but recommended. If you submit a batch ID, then any further imports submitted with the same batch ID will be rejected. This is a safeguard to ensure external systems aren't submitting the same batches multiple times.
    - `transactions` (Array, required): An array of objects, the objects representing transactions to import. See the example below for a visual representation of the structure. The values below this line show the content of each object within this array.
        - `account_id` (Integer, required): An account ID to add a transaction to
        - `service_id` (Integer, required): The service ID to use when adding the transaction
        - `quantity` (Integer, optional): The quantity to use when running the transaction. This is only valid for recurring and one time services.
        - `description_override` (String, optional): If you want the transaction description to be overridden on the invoice, then enter an override string here
        - `amount` (Number, optional): An amount to use when adding the transaction. This can only be used when adding adjustment services, and is required if you are adding one. It should be ommitted for other types of services.
        - `override_taxation` (Boolean, optional): If this is true, then any taxes associated with the service referenced by service_id will not be applied. Instead, the tax amounts specified in the tax_transactions property will be used. If tax_transactions is missing or empty, instead, no tax will be applied.
        - `tax_transactions` (Array, optional): An array of objects, only used if override_taxation is true. Each object should have two properties, description and amount. These amounts will be applied to the service as taxes, with the tax name being the description property.
- **Example Request Body**:
    ```json
    {
         "name": "My first batch",
         "batch_id": "acme-12345",
         "transactions": [
             {
                 "account_id": 3,
                 "service_id": 89,
                 "quantity": 12,
                 "override_taxation": false
             },
             {
                 "account_id": 3,
                 "service_id": 55,
                 "description_override": "After Hours Support",
                 "override_taxation": true //Here, no taxes will be applied even if service_id 55 has taxes, because we are overriding taxes and supplying no transactions
             },
             {
                 "account_id": 55,
                 "service_id": 53,
                 "amount": 12.53,
                 "description_override": "Custom painting charge",
                 "override_taxation": true,
                 "tax_transactions": [
                     {
                         "amount": 12.43,
                         "description": "Some tax"
                     }
                 ]
             }
         ]
    }
    ```
- **Success Response (201 Created)**:
    ```json
    {
      "data": {
        "id": 3,
        "batch_id": "acme-12345",
        "name": "My first batch",
        "created_at": "2016-11-15 20:16:39"
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
       "error": {
         "message": {
           "batch_id": "The batch id must be unique."
         },
         "status_code": 422
       }
    }
    ```
```
