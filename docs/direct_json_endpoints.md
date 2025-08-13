# Direct JSON Endpoints Documentation

## Overview

These endpoints access Sonar's internal web interface JSON responses, providing richer data than the official REST API. They require session-based authentication (CSRF + JWT tokens) and may change without notice since they are undocumented.

**Important Notes:**
- These endpoints are accessed via `Sonar.get_direct_json()` method
- They require an active session with proper authentication
- Response structures may change in future Sonar updates
- Use with caution in production environments

## Available Endpoints

### 1. Account Complete Data

**Endpoint**: `accounts/{id}/json`  
**Method**: GET (via get_direct_json)  
**Purpose**: Get comprehensive account information in a single call  
**Authentication**: Session-based (CSRF + JWT)

#### What You Get
This endpoint provides a complete account view that would normally require 10+ separate API calls:

- **Basic Account Info**: ID, name, status, type, creation/update dates
- **Financial Data**: Balance due, balance total, next recurring charge amount
- **Addresses**: Physical and mailing addresses with full geocoding data
- **Services**: Complete service details with pricing, technology codes, billing frequency
- **Contacts**: Primary contact with email categories, phone numbers, avatar URLs
- **Payment Methods**: All payment methods with formatting and editability flags
- **Data Usage History**: Detailed monthly usage records back to account creation
- **IP Assignments**: Network assignments with device details and parent relationships
- **Billing Parameters**: Complete billing configuration and custom fields
- **Dashboard Information**: Recent communications, invoice history, usage averages

#### Usage Example
```python
# Using Sonar.py directly
account_data = Sonar.get_direct_json("accounts/9263/json")

# Expected response structure
{
  "account": {
    "id": 9263,
    "name": "Customer Name",
    "account_status_id": 2,
    "account_type_id": 1,
    "addresses": [...],
    "services": [...],
    "contacts": [...],
    "payment_methods": [...],
    "data_usage_histories": [...],
    "ip_assignments": [...],
    "billing_parameters": {...},
    "dashboard_information": {...}
  }
}
```

#### Key Response Fields
- `account.id` - Account ID
- `account.name` - Account name
- `account.status` - Status object with ID, name, active flag
- `account.type` - Type object with ID, name, type classification
- `account.addresses[]` - Array of address objects (physical/mailing)
- `account.services[]` - Array of service objects with pricing details
- `account.contacts[]` - Array of contact objects with communication preferences
- `account.data_usage_histories[]` - Monthly usage records with in/out bytes
- `account.ip_assignments[]` - IP assignments with device and network details

### 2. Contact Information Report

**Endpoint**: `reports/accounts/contact_information/json`  
**Method**: GET (via get_direct_json)  
**Purpose**: Bulk export of contact information for all accounts  
**Authentication**: Session-based

#### What You Get
This endpoint returns tabular data (array of arrays) suitable for CSV export or bulk processing:

- One row per account with flattened contact information
- Physical and mailing addresses with geocoding
- Phone numbers (home, work, mobile, fax)
- Account status and group membership
- HTML-formatted account names with links

#### Usage Example
```python
# Using Sonar.py directly
contacts_data = Sonar.get_direct_json("reports/accounts/contact_information/json")

# Expected response structure
{
  "data": [
    [9263, "<a href='...'>Customer Name</a>", "Active", "Contact Name", "email@example.com", "phone1", "phone2", null, null, "Group", "addr1", "addr2", "city", "state", "zip", "lat", "lng", "mail1", "mail2", "mailcity", "mailstate", "mailzip"],
    // ... more rows
  ]
}
```

#### Field Structure (Array Indices)
- `[0]` - Account ID (integer)
- `[1]` - Account name with HTML link (string)
- `[2]` - Account status (string: "Active", "Inactive", "Closed", etc.)
- `[3]` - Primary contact name (string)
- `[4]` - Primary email address (string)
- `[5]` - Home phone number (string)
- `[6]` - Work phone number with extension (string)
- `[7]` - Mobile phone number (string or null)
- `[8]` - Fax number (string or null)
- `[9]` - Account groups (string)
- `[10]` - Physical address line 1 (string)
- `[11]` - Physical address line 2 (string)
- `[12]` - Physical address city (string)
- `[13]` - Physical address state (string)
- `[14]` - Physical address ZIP (string)
- `[15]` - Physical address latitude (string)
- `[16]` - Physical address longitude (string)
- `[17]` - Mailing address line 1 (string)
- `[18]` - Mailing address line 2 (string)
- `[19]` - Mailing address city (string)
- `[20]` - Mailing address state (string)
- `[21]` - Mailing address ZIP (string)

## Use Cases

### Account Complete Data
- **Customer Service Dashboard**: Get all customer info in one call
- **Billing Analysis**: Access complete billing and usage history
- **Network Troubleshooting**: View IP assignments and device relationships
- **Account Overview**: Display comprehensive account information

### Contact Information Report
- **Contact List Export**: Export all customer contacts for external systems
- **Marketing Campaigns**: Bulk contact data for communications
- **Emergency Notifications**: Quick access to all customer contact info
- **Address Verification**: Bulk address data with geocoding

## Error Handling

These endpoints may fail or return different structures if:
- Session authentication expires
- Sonar updates change internal structures
- Network connectivity issues
- Invalid account IDs (for account-specific endpoints)

Always implement proper error handling and fallback mechanisms when using these endpoints.

## Implementation Notes

1. **Session Management**: Ensure Sonar.py session is properly authenticated before calling
2. **Rate Limiting**: Be mindful of request frequency to avoid overwhelming the server
3. **Data Validation**: Validate response structure before processing
4. **Fallback Strategy**: Have fallback to official API endpoints when possible
5. **Monitoring**: Monitor for changes in response structure over time
