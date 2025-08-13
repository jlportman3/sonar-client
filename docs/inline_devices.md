# Inline Devices Endpoint Documentation

## Overview
The `/inline_devices` endpoint provides comprehensive inline device information from the Sonar system, including detailed configuration scraped from the device edit pages. This endpoint combines data from the Sonar API with web scraping to provide port numbers, usernames, and SSL configuration details not available through the standard API.

## Endpoint Details
- **URL**: `GET /inline_devices`
- **Authentication**: X-API-Key header required
- **Content-Type**: application/json

## Query Parameters
- `page` (optional): Page number for pagination (default: 1)
- `limit` (optional): Number of results per page (default: 50)

## Request Example
```bash
curl -X GET "http://localhost:5050/inline_devices" \
  -H "X-API-Key: your-api-key-here" \
  -H "Content-Type: application/json"
```

## Response Format
```json
{
  "status": "success",
  "inline_devices": [
    {
      "id": 14,
      "name": "SVM",
      "ip_address": "38.128.160.1",
      "type": "mikrotik",
      "enabled": true,
      "failures": 0,
      "device_status": true,
      "status_message": false,
      "port": "8729",
      "ssl_enabled": true,
      "username": "sonar"
    }
  ],
  "count": 20,
  "pagination": {
    "page": 1,
    "limit": 50,
    "total_count": 20,
    "total_pages": 1
  }
}
```

## Current Inline Device Configuration

Based on live data retrieved from the Sonar system (as of January 2025):

### Active Inline Devices

| Name | IP Address | Port | SSL | Username | Status | Failures |
|------|------------|------|-----|----------|--------|----------|
| SVM | 38.128.160.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Hilltop | 38.128.162.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Weston10G | 38.103.216.5 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| master2 | 38.103.216.8 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Texas Pride | 38.103.217.97 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| SSBC | 38.103.218.129 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Waterwood | 38.103.216.65 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Cook | 38.128.167.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Nelson2 | 38.128.162.129 | 8728 | ❌ | sonar | ✅ Enabled | 2 |
| WW5 | 38.128.144.1 | 8728 | ❌ | sonar | ✅ Enabled | 0 |
| Fiber2 | 38.128.163.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Duke | 38.128.166.1 | 8728 | ❌ | sonar | ✅ Enabled | 0 |
| Sam54 | 38.128.145.65 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Home | 38.103.219.65 | 8728 | ❌ | sonar | ✅ Enabled | 0 |
| WatewoodFiber | 38.128.163.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Southton | 38.103.218.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |
| Master | 38.103.216.7 | 8728 | ❌ | sonar | ✅ Enabled | 0 |
| WW2 | 38.103.219.1 | 8729 | ✅ | sonar | ✅ Enabled | 0 |

### Disabled Inline Devices

| Name | IP Address | Port | SSL | Username | Status | Reason |
|------|------------|------|-----|----------|--------|--------|
| SouthtonRack | 38.103.218.193 | 8729 | ✅ | sonar | ❌ Disabled | Device Offline |
| master1 | 38.103.216.10 | 8729 | ✅ | sonar | ❌ Disabled | Device Offline |

## Response Fields

### Inline Device Object
- **id**: Unique identifier for the inline device
- **name**: Human-readable name of the inline device
- **ip_address**: IP address of the inline device
- **type**: Type of inline device (currently all are "mikrotik")
- **enabled**: Boolean indicating if the device is enabled
- **failures**: Number of recent failures encountered
- **device_status**: Boolean indicating if the device is responding properly
- **status_message**: Additional status information (boolean in current implementation)
- **port**: Device API port (scraped from edit page)
- **ssl_enabled**: Boolean indicating if SSL is enabled for MikroTik API communication
- **username**: Username for device authentication (scraped from edit page)

## Technical Implementation

### Data Sources
1. **Sonar API**: Basic device information via `/network/provisioning/inline_devices`
2. **Web Scraping**: Detailed configuration via `https://sonar.alamobroadband.com/network/provisioning/inline_devices/{id}/edit`

### Enhanced Features
- **Port Discovery**: Automatically extracts port numbers from device edit pages
- **SSL Detection**: Determines SSL configuration via radio button parsing
- **Username Extraction**: Retrieves authentication usernames from configuration forms
- **Session Management**: Maintains authenticated sessions for web scraping
- **Error Handling**: Graceful fallback when scraping fails

## Network Architecture Insights

### Port Configuration Analysis
- **Primary Port**: Most devices (15/20) use port **8729**
- **Secondary Port**: Some devices (5/20) use port **8728**
- **Standard Protocol**: All devices use MikroTik API protocol

### SSL Configuration Pattern
Consistent with DHCP servers, inline devices show the same SSL/port relationship:
- **Port 8729**: SSL enabled (API SSL) - 15 devices
- **Port 8728**: SSL disabled (API non-SSL) - 5 devices

This confirms a standardized configuration approach across the entire network infrastructure where:
- Secure connections use port 8729 with SSL encryption
- Non-secure connections use port 8728 without SSL encryption

### Authentication
- **Unified Username**: All devices use the username **"sonar"**
- **Consistent Configuration**: Standardized authentication across all inline devices

### Operational Status
- **Total Devices**: 20 inline devices configured
- **Active Devices**: 18 devices currently enabled (90%)
- **Disabled Devices**: 2 devices currently disabled (10%)
- **Failure Rate**: Very low failure rate with most devices at 0 failures

### Device Types and Roles
- **Core Infrastructure**: Devices like "master1", "master2", "Master" suggest hierarchical network design
- **Location-Based**: Many devices named after locations (Hilltop, Waterwood, Texas Pride, etc.)
- **Technology Mix**: Both traditional and fiber infrastructure (WatewoodFiber, Fiber2)
- **Specialized Functions**: Devices like "Weston10G" indicate high-bandwidth capabilities

## Use Cases

This endpoint is valuable for:
- **Network Monitoring**: Real-time status of all inline devices
- **Configuration Management**: Port and authentication details for automation
- **Troubleshooting**: Identifying failed or misconfigured devices
- **Security Auditing**: Reviewing authentication and SSL configurations
- **Infrastructure Documentation**: Complete inline device inventory
- **Performance Analysis**: Monitoring device failures and status
- **Network Planning**: Understanding device distribution and capabilities

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

- **Scraping Overhead**: Each device requires an additional HTTP request for detailed config
- **Session Reuse**: Authenticated sessions are maintained for efficiency
- **Caching**: Consider implementing caching for frequently accessed data
- **Rate Limiting**: Built-in retry logic with exponential backoff

## Security Notes

- **Authentication Required**: Both API key and Sonar session authentication
- **Sensitive Data**: Usernames are exposed (passwords are not retrieved)
- **Access Control**: Requires appropriate permissions in both systems
- **Audit Trail**: All access is logged for security monitoring

## Comparison with DHCP Servers

Inline devices show remarkable consistency with DHCP server configurations:

| Aspect | DHCP Servers | Inline Devices | Consistency |
|--------|--------------|----------------|-------------|
| SSL/Port Pattern | 8729=SSL, 8728=non-SSL | 8729=SSL, 8728=non-SSL | ✅ Identical |
| Username | "sonar" | "sonar" | ✅ Identical |
| Device Types | All MikroTik | All MikroTik | ✅ Identical |
| Configuration Method | Web scraping required | Web scraping required | ✅ Identical |

This consistency suggests a well-standardized network infrastructure with unified configuration management practices.

## Future Enhancements

Potential improvements:
1. **Real-time Monitoring**: Live device connectivity testing
2. **Configuration Validation**: Automated configuration compliance checking
3. **Performance Metrics**: Response time and throughput monitoring
4. **Bulk Operations**: Mass configuration updates via the API
5. **Historical Data**: Tracking device performance over time
6. **Integration**: Cross-referencing with DHCP server data for complete network view
