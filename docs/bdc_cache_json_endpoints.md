# BDC Cache JSON Endpoints

This document details the specific `/json` endpoints accessed by the `bdc_cache.py` script using the `Sonar.get_direct_json` function. These endpoints are crucial for populating the local SQLite cache with customer and contact information for BDC reporting.

## Endpoints Used

### 1. Contact Information Report
- **Endpoint**: `reports/accounts/contact_information/json`
- **Description**: This endpoint is used to retrieve a comprehensive list of customer contact information. The `bdc_cache.py` script fetches this data to identify unique customer records and extract basic customer details such as name, status, address, and geographical coordinates.
- **Usage in `bdc_cache.py`**:
    ```python
    data = Sonar.get_direct_json("reports/accounts/contact_information/json")
    if not data or "data" not in data:
        print("Failed to get customer list")
        return
    all_records = data["data"]
    # ... further processing to filter unique records
    ```
- **Purpose**: Provides a high-level overview of all customer accounts, serving as the initial dataset for caching.

### 2. Detailed Customer Data
- **Endpoint**: `accounts/{customer_id}/json`
- **Description**: For each unique customer identified from the contact information report, this endpoint is queried to retrieve more detailed information about the individual customer account. This includes account-specific details like account type, associated inventory items, groups, and services.
- **Usage in `bdc_cache.py`**:
    ```python
    customer_data = Sonar.get_direct_json(f"accounts/{customer_id}/json")
    if not customer_data or "account" not in customer_data:
        continue
    account = customer_data["account"]
    # ... further processing to cache inventory, groups, and services
    ```
- **Purpose**: Enriches the cached customer data with granular details necessary for comprehensive BDC reporting.

## Importance of `get_direct_json`
The use of `get_direct_json` for these endpoints highlights that the required data might not be readily available through the standard Sonar API endpoints (e.g., `/api/v1/accounts`). This function's ability to handle direct login authentication and session management is critical for accessing these specific `/json` views, which often provide data tailored for internal reporting or specific application needs.
