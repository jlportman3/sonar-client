# Sonar V2 GraphQL API Interface Documentation

## Overview
This document outlines the key information for accessing and utilizing the Sonar V2 GraphQL API, specifically focusing on retrieving addresses associated with a customer ID.

## GraphQL Endpoint
The base URL for the Sonar V2 GraphQL API is:
`https://api.sonar.software/graphql`

## Querying Addresses by Customer ID

To retrieve a list of addresses for a specific customer, you can use the `addresses` query. This query allows filtering by `addressable_id` (the customer's ID) and `addressable_type` (which should be "Account" for customers).

### Query Details

*   **Query Name**: `addresses`
*   **Arguments**:
    *   `addressable_id`: The unique identifier of the customer (type `Int64Bit`).
    *   `addressable_type`: The type of entity the address is associated with. For customers, this should be `"Account"` (type `AddressableType`).
*   **Return Type**: A connection type (`AddressConnection`) that contains a list of `Address` objects.

### Address Object Structure

The `Address` object contains the following relevant fields:

*   `id`: Unique identifier for the address (type `Int64Bit`).
*   `sonar_unique_id`: A system-wide unique identifier (type `ID`).
*   `created_at`: Timestamp of when the address was created (type `Datetime`).
*   `updated_at`: Timestamp of when the address was last modified (type `Datetime`).
*   `_version`: Version string of the entity (type `String`).
*   `address_status_id`: ID of the address status (type `Int64Bit`).
*   `addressable_id`: The ID of the entity that owns this address (type `Int64Bit`).
*   `addressable_type`: The type of entity that owns this address (type `AddressableType`).
*   `anchor_address_id`: The address ID for the Anchor address (type `Int64Bit`).
*   `attainable_download_speed`: Download speed in kilobits per second (type `Int`).
*   `attainable_upload_speed`: Upload speed in kilobits per second (type `Int`).
*   `avalara_pcode`: Avalara PCode (type `String`).
*   `billing_default_id`: ID of a BillingDefault (type `Int64Bit`).
*   `census_year`: Year used for FIPS and census tract information (type `Int`).
*   `city`: City name (type `String`).
*   `country`: Two-character country code (type `Country`).
*   `county`: US county (type `UsCounty`).
*   `fips`: Census tract information for US addresses (type `String`).
*   `fips_source`: Source of the FIPS code (type `FipsSource`).
*   `is_anchor`: Boolean indicating if this is an anchor address (type `Boolean`).
*   `latitude`: Decimal latitude (type `Latitude`).
*   `line1`: Address line 1 (type `String`).
*   `line2`: Address line 2 (type `String`).
*   `longitude`: Decimal longitude (type `Longitude`).
*   `serviceable`: Boolean indicating if the address is serviceable (type `Boolean`).
*   `subdivision`: State, province, or other country subdivision (type `Subdivision`).
*   `timezone`: Timezone for display (type `Timezone`).
*   `type`: Type of address (type `AddressType`).
*   `zip`: ZIP or postal code (type `String`).

### Example GraphQL Query

```graphql
query GetAddressesByCustomerId($customerId: Int64Bit!) {
  addresses(addressable_id: $customerId, addressable_type: "Account") {
    edges {
      node {
        id
        line1
        line2
        city
        subdivision
        zip
        country
        # Add any other fields you need here
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
```

### Variables for the Example Query

```json
{
  "customerId": 12345 // Replace with an actual customer ID
}
```

## Authentication
The documentation implies that authentication is handled via an API key, similar to the REST API. Further details on how to pass this API key with GraphQL requests (e.g., as a header) would typically be found in a general authentication section of the API documentation, which was not explicitly provided in the initial `api.sonar.software` page. It is generally expected to be passed as an `Authorization` header with a `Bearer` token or a custom `X-API-Key` header.

## Next Steps
This documentation provides the foundation for integrating with the Sonar V2 GraphQL API to retrieve customer addresses. The next step would be to implement the client-side logic to construct and execute these GraphQL queries.
