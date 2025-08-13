# get_direct_json Function

## Overview
The `get_direct_json` function in `Sonar.py` is designed to retrieve JSON data directly from the Sonar instance. Unlike standard API calls that might go through `/api/v1` endpoints, this function accesses specific `/json` endpoints, often requiring direct login authentication to fetch data not exposed via the public API. It manages its own session, including CSRF token handling and retry mechanisms for robustness.

## Function Signature
`get_direct_json(endpoint: str, retry_count=1)`

## Parameters
- `endpoint` (String, required): The specific URL path to the JSON endpoint on the Sonar instance (e.g., `reports/accounts/contact_information/json`, `accounts/{customer_id}/json`). This path should not include the protocol or host.
- `retry_count` (Integer, optional): The number of times the function should retry the request if it fails. Defaults to `1`.

## Functionality
1. **Session Initialization**: If no active session exists, it initializes a new `requests.Session`. This involves:
    - Fetching the home page to obtain initial cookies and a CSRF token.
    - Performing a login POST request with the provided `username`, `password`, and CSRF token.
    - Obtaining a new CSRF token and a JWT token after successful login to maintain the session.
2. **Direct JSON Fetch**: It constructs the full URL using the provided `endpoint` and the configured `host`. It then uses the established session to make a GET request to this URL.
3. **Response Handling**:
    - Checks if the response is successful (HTTP 200 OK).
    - Validates if the response content is not empty and appears to be JSON (checks `Content-Type` header or starts with `{`).
    - Attempts to parse the response as JSON.
    - If any of these checks fail, it prints an error message.
4. **Retry Mechanism**: If a request fails and `retry_count` is greater than 0, it closes the current session, clears the token, and recursively retries the request, decrementing `retry_count`.

## Error Handling
The function includes robust error handling for network issues, HTTP errors (e.g., 403, 404), empty responses, and JSON decoding errors. Failed requests are retried up to `retry_count` times after resetting the session.

## Usage Example
```python
from Sonar import setup, get_direct_json

# Setup Sonar connection details (replace with actual values)
setup("your_username", "your_password", "https", "your_sonar_host")

# Example 1: Get contact information report
contact_info = get_direct_json("reports/accounts/contact_information/json")
if contact_info:
    print("Contact Information Report:")
    # Process contact_info data
else:
    print("Failed to retrieve contact information.")

# Example 2: Get detailed customer data for a specific customer ID
customer_id = 12345
customer_data = get_direct_json(f"accounts/{customer_id}/json")
if customer_data:
    print(f"Customer Data for ID {customer_id}:")
    # Process customer_data
else:
    print(f"Failed to retrieve data for customer ID {customer_id}.")
