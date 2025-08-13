# Sonar Allocated IP Addresses Script

This script retrieves information about allocated IP addresses from Sonar, with a focus on identifying networks larger than /30 and documenting them with customer names.

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
./get_allocated_ips.py
```

## Output

The script creates a `sonar_network_data` directory with the following files:

- `large_networks.json`: Complete data in JSON format
- `large_networks.csv`: Data in CSV format for easier analysis

## Data Structure

Each network entry contains:

- `network`: The CIDR notation of the network (e.g., 192.168.0.0/24)
- `account_id`: The Sonar account ID associated with this network
- `customer_name`: The name of the customer associated with this network
- `ip_id`: The internal Sonar ID for this IP assignment
- `entity_type`: The type of entity this network is assigned to (e.g., account, network_site)
- `description`: Any description associated with this network assignment

## Why Focus on Networks Larger than /30?

Networks larger than /30 (i.e., /29, /28, /27, etc.) are of particular interest because:

1. They contain more IP addresses (a /30 has only 4 addresses with 2 usable)
2. They are typically assigned to customers with specific needs or for special purposes
3. They represent a more significant allocation of IP address space

## API Endpoints Used

The script uses the following Sonar API endpoints:

- `/network/mapping` - Get all network mapping data
- `/accounts/:id` - Get account information for customer names

## Example Usage Scenarios

1. **IP Address Audit**: Identify which customers have been allocated larger blocks of IP addresses
2. **Resource Planning**: Understand how IP address space is currently allocated
3. **Customer Documentation**: Generate reports of IP allocations by customer
4. **Network Planning**: Identify opportunities for reclaiming or reallocating IP space

## Troubleshooting

If you encounter issues:

1. Verify your Sonar credentials are correct in the `.env` file
2. Check that your Sonar instance is accessible
3. Ensure you have the necessary permissions to access the network mapping data
4. Check the logs for detailed error messages
