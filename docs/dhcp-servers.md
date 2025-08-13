# DHCP Servers Endpoint Documentation

## Overview
The `/dhcp_servers` endpoint provides comprehensive DHCP server information from the Sonar system, including detailed configuration scraped from the server edit pages. This endpoint combines data from the Sonar API with web scraping to provide port numbers, usernames, and other configuration details not available through the standard API.

## Endpoint Details
- **URL**: `GET /dhcp_servers`
- **Authentication**: X-API-Key header required
- **Content-Type**: application/json

## Query Parameters
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of results per page (default: 50)

## Request Example
```bash
curl -X GET "http://localhost:5050/dhcp_servers" \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json"
```

## Response Format
```json
{
  "status": "success",
  "dhcp_servers": [
    {
      "id": 4,
      "name": "SouthtonRack",
      "ip_address": "38.103.218.193",
      "type": "mikrotik",
      "enabled": false,
      "controls_all_pools": false,
      "failures": 0,
      "device_status": false,
      "status_message": "Disabled",
      "ip_pools": [22, 20],
      "port": "8729",
      "ssl_enabled": true,
      "username": "sonar"
    }
  ],
  "count": 17,
  "pagination": {
    "page": 1,
    "limit": 50,
    "total_count": 17,
    "total_pages": 1
  }
}
```

## Current DHCP Server Configuration

Based on live data retrieved from the Sonar system (as of January 2025):

### Active DHCP Servers

| Name | IP Address | Port | Username | Status | IP Pools | Failures |
|------|------------|------|----------|--------|----------|----------|
| Duke | 38.128.166.1 | 8729 | sonar | ✅ Enabled | [32, 98] | 0 |
| SSBC | 38.103.218.129 | 8729 | sonar | ✅ Enabled | [23, 25, 33, 95] | 0 |
| WW2 | 38.103.219.1 | 8729 | sonar | ✅ Enabled | [49, 82, 94, 50] | 1 |
| Sam54 | 38.128.145.65 | 8729 | sonar | ✅ Enabled | [11, 109, 65] | 0 |
| Texas Pride | 38.103.217.97 | 8729 | sonar | ✅ Enabled | [80, 45, 44, 46] | 0 |
| Hilltop | 38.128.162.1 | 8729 | sonar | ✅ Enabled | [38, 76] | 0 |
| Waterwood | 38.103.216.65 | 8729 | sonar | ✅ Enabled | [29, 28, 31, 81, 84] | 0 |
| Home | 38.103.219.65 | 8729 | sonar | ✅ Enabled | [27, 108] | 0 |
| Southton | 38.103.218.1 | 8729 | sonar | ✅ Enabled | [15, 17, 18, 16, 99] | 1 |
| WW5 | 38.128.144.1 | 8728 | sonar | ✅ Enabled | [26, 48, 47, 93] | 0 |
| Cook | 38.128.167.1 | 8729 | sonar | ✅ Enabled | [39, 73, 100] | 0 |
| FiberAggregator | 38.128.163.1 | 8729 | sonar | ✅ Enabled | [57, 111] | 0 |
| Nelson | 38.128.162.129 | 8728 | sonar | ✅ Enabled | [103, 43, 77, 92] | 0 |
| SVM | 38.128.160.1 | 8729 | sonar | ✅ Enabled | [103, 10, 36, 96] | 2 |

### Disabled DHCP Servers

| Name | IP Address | Port | Username | Status | Reason | IP Pools |
|------|------------|------|----------|--------|--------|----------|
| SouthtonRack | 38.103.218.193 | 8729 | sonar | ❌ Disabled | Disabled | [22, 20] |
| LTE-CCR | 38.128.163.1 | 8728 | sonar | ❌ Disabled | - | [] |
| SonarTest | 38.128.164.1 | 8728 | sonar | ❌ Disabled | Controls All Pools | [] |

## Response Fields

### DHCP Server Object
- **id**: Unique identifier for the DHCP server
- **name**: Human-readable name of the DHCP server
- **ip_address**: IP address of the DHCP server
- **type**: Type of DHCP server (currently all are "mikrotik")
- **enabled**: Boolean indicating if the server is enabled
- **controls_all_pools**: Boolean indicating if this server manages all IP pools
- **failures**: Number of recent failures encountered
- **device_status**: Boolean indicating if the device is responding properly
- **status_message**: Additional status information (if any)
- **ip_pools**: Array of IP pool IDs managed by this server
- **port**: DHCP server port (scraped from edit page)
- **ssl_enabled**: Boolean indicating if SSL is enabled for MikroTik API communication
- **username**: Username for DHCP server authentication (scraped from edit page)

## Technical Implementation

### Data Sources
1. **Sonar API**: Basic server information via `/network/provisioning/dhcp_servers`
2. **Web Scraping**: Detailed configuration via `https://sonar.alamobroadband.com/network/provisioning/dhcp_servers/{id}/edit`

### Enhanced Features
- **Port Discovery**: Automatically extracts port numbers from server edit pages
- **Username Extraction**: Retrieves authentication usernames from configuration forms
- **Session Management**: Maintains authenticated sessions for web scraping
- **Error Handling**: Graceful fallback when scraping fails

## Network Architecture Insights

### Port Configuration Analysis
- **Primary Port**: Most servers (12/17) use port **8729**
- **Secondary Port**: Some servers (5/17) use port **8728**
- **Standard Protocol**: All servers use MikroTik API protocol

### SSL Configuration Pattern
A clear pattern emerges between port numbers and SSL configuration:
- **Port 8729**: SSL enabled (API SSL) - 12 servers
- **Port 8728**: SSL disabled (API non-SSL) - 5 servers

This indicates a standardized configuration approach where:
- Secure connections use port 8729 with SSL encryption
- Non-secure connections use port 8728 without SSL encryption

### Authentication
- **Unified Username**: All servers use the username **"sonar"**
- **Consistent Configuration**: Standardized authentication across the network

### Operational Status
- **Total Servers**: 17 DHCP servers configured
- **Active Servers**: 14 servers currently enabled (82.4%)
- **Disabled Servers**: 3 servers currently disabled (17.6%)
- **Failure Rate**: Low failure rate with most servers at 0 failures

### IP Pool Distribution
- **Pool Management**: Servers manage between 0-5 IP pools each
- **Load Distribution**: Pools are distributed across multiple servers for redundancy
- **Specialized Servers**: Some servers (like SonarTest) are configured for testing

## Use Cases

This endpoint is valuable for:
- **Network Monitoring**: Real-time status of all DHCP servers
- **Configuration Management**: Port and authentication details for automation
- **Troubleshooting**: Identifying failed or misconfigured servers
- **Capacity Planning**: Understanding IP pool distribution
- **Security Auditing**: Reviewing authentication configurations
- **Infrastructure Documentation**: Complete DHCP server inventory

## API Limitations and Workarounds

### Standard API Limitations
- ❌ Port information not available via Sonar REST API
- ❌ Username/authentication details not exposed
- ❌ SSL configuration not accessible through API

### Web Scraping Solutions
- ✅ Port numbers extracted from edit pages
- ✅ Usernames retrieved from configuration forms
- ✅ SSL configuration successfully detected via radio button parsing
- ✅ Session-based authentication for page access

## Error Handling

The endpoint provides robust error handling:
- **200**: Success with complete data
- **401**: Unauthorized (invalid or missing API key)
- **500**: Internal server error
- **Graceful Degradation**: If scraping fails, basic API data is still returned

## Performance Considerations

- **Scraping Overhead**: Each server requires an additional HTTP request for detailed config
- **Session Reuse**: Authenticated sessions are maintained for efficiency
- **Caching**: Consider implementing caching for frequently accessed data
- **Rate Limiting**: Built-in retry logic with exponential backoff

## Security Notes

- **Authentication Required**: Both API key and Sonar session authentication
- **Sensitive Data**: Usernames are exposed (passwords are not retrieved)
- **Access Control**: Requires appropriate permissions in both systems
- **Audit Trail**: All access is logged for security monitoring

## Future Enhancements

Potential improvements:
1. **SSL Configuration**: Enhanced parsing for SSL settings
2. **Real-time Status**: Live device connectivity testing
3. **Configuration Validation**: Automated configuration compliance checking
4. **Performance Metrics**: Response time and throughput monitoring
5. **Bulk Operations**: Mass configuration updates via the API
