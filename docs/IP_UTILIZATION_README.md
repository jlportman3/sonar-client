# Sonar IP Utilization Analysis Script

This script combines data from IP pools and allocated IP addresses to provide a comprehensive view of IP address utilization in Sonar.

## Prerequisites

- Python 3.6+
- Access to Sonar API
- Environment variables set up with Sonar credentials

## Environment Variables

The script requires the following environment variables to be set:

```
SONAR_USERNAME=your_username
SONAR_PASSWORD=your_password
SONAR_HOST=your_sonar_host
SONAR_PROTOCOL=https  # Optional, defaults to https
```

These can be set in a `.env` file in the same directory as the script.

## Usage

```bash
./get_ip_utilization.py
```

## Output

The script creates a `sonar_network_data` directory with the following files:

- `ip_utilization.json`: Complete data in JSON format, including allocation details
- `ip_utilization.csv`: Summary data in CSV format for easier analysis

## Data Structure

Each IP pool entry contains:

- `ip_pool_id`: The Sonar ID for this IP pool
- `ip_pool_name`: The name of the IP pool
- `start_address`: The starting IP address of the pool (may be called "start" in some Sonar versions)
- `end_address`: The ending IP address of the pool (may be called "end" in some Sonar versions)
- `total_ips`: The total number of IP addresses in the pool
- `allocated_ips`: The number of allocated IP addresses in the pool
- `utilization_percent`: The percentage of IP addresses that are allocated
- `subnet_id`: The ID of the subnet this pool belongs to
- `subnet_name`: The name of the subnet
- `subnet_network`: The network address of the subnet
- `supernet_id`: The ID of the supernet this pool belongs to
- `supernet_name`: The name of the supernet
- `supernet_network`: The network address of the supernet
- `allocations`: A list of all allocations within this pool (JSON only)

Each allocation contains:

- `ip_address` or `network`: The allocated IP address or network
- `account_id`: The Sonar account ID associated with this allocation
- `customer_name`: The name of the customer
- `ip_id`: The internal Sonar ID for this IP assignment
- `entity_type`: The type of entity this IP is assigned to
- `description`: Any description associated with this IP assignment

## Why This Matters

IP address utilization analysis is crucial for:

1. **Resource Planning**: Identify underutilized IP pools that could be reallocated
2. **Capacity Management**: Determine when new IP address blocks need to be acquired
3. **Network Optimization**: Find opportunities to consolidate or reorganize IP allocations
4. **Customer Auditing**: Verify that customers are using their allocated IP addresses

## API Endpoints Used

The script uses the following Sonar API endpoints:

- `/network/ipam/supernets` - Get all supernets
- `/network/ipam/supernets/:supernet_id/subnets` - Get all subnets for a specific supernet
- `/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools` - Get all IP pools for a specific subnet
- `/network/mapping` - Get all network mapping data (allocated IPs)
- `/accounts/:id` - Get account information for customer names

## Example Usage Scenarios

1. **IP Address Audit**: Identify which IP pools are over or under-utilized
2. **Resource Planning**: Find IP pools that can be reclaimed or consolidated
3. **Customer Documentation**: Generate reports of IP allocations by customer
4. **Network Planning**: Identify opportunities for optimizing IP address usage

## Troubleshooting

If you encounter issues:

1. Verify your Sonar credentials are correct in the `.env` file
2. Check that your Sonar instance is accessible
3. Ensure you have the necessary permissions to access the network mapping data
4. Check the logs for detailed error messages
