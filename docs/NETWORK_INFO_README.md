# Sonar Network Information Scripts

These scripts retrieve network information from Sonar, including supernets, subnets, and IP pools.

## Prerequisites

- Python 3.6+
- Access to Sonar API
- Environment variables set up with Sonar credentials

## Environment Variables

The scripts require the following environment variables to be set:

```
SONAR_USERNAME=your_username
SONAR_PASSWORD=your_password
SONAR_HOST=your_sonar_host
SONAR_PROTOCOL=https  # Optional, defaults to https
```

These can be set in a `.env` file in the same directory as the scripts.

## Available Scripts

### 1. get_network_info.py

This script retrieves all supernets, subnets, and IP pools from Sonar and saves them to a single JSON file.

#### Usage

```bash
./get_network_info.py
```

#### Output

- `sonar_network_info.json`: A JSON file containing all network information

### 2. get_network_info_csv.py

This script retrieves the same information as `get_network_info.py` but saves it in both JSON and CSV formats for easier analysis.

#### Usage

```bash
./get_network_info_csv.py
```

#### Output

The script creates a `sonar_network_data` directory with the following files:

- `network_info.json`: Complete data in JSON format
- `supernets.csv`: Supernets in CSV format
- `subnets.csv`: Subnets with supernet information in CSV format
- `ip_pools.csv`: IP pools with subnet and supernet information in CSV format

## Data Structure

### Supernets

Each supernet contains the following information:
- `id`: Unique identifier
- `name`: Supernet name
- `network`: Network address (e.g., 192.168.0.0/16)
- `description`: Optional description
- `notes`: Optional notes
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Subnets

Each subnet contains:
- `id`: Unique identifier
- `name`: Subnet name
- `network`: Network address (e.g., 192.168.1.0/24)
- `description`: Optional description
- `notes`: Optional notes
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `supernet_id`: ID of the parent supernet (in CSV output)
- `supernet_name`: Name of the parent supernet (in CSV output)
- `supernet_network`: Network address of the parent supernet (in CSV output)

### IP Pools

Each IP pool contains:
- `id`: Unique identifier
- `name`: IP pool name
- `start_address`: Starting IP address
- `end_address`: Ending IP address
- `description`: Optional description
- `notes`: Optional notes
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `subnet_id`: ID of the parent subnet (in CSV output)
- `subnet_name`: Name of the parent subnet (in CSV output)
- `subnet_network`: Network address of the parent subnet (in CSV output)
- `supernet_id`: ID of the grandparent supernet (in CSV output)
- `supernet_name`: Name of the grandparent supernet (in CSV output)
- `supernet_network`: Network address of the grandparent supernet (in CSV output)

## API Endpoints Used

The scripts use the following Sonar API endpoints:

- `/network/ipam/supernets` - Get all supernets
- `/network/ipam/supernets/:supernet_id/subnets` - Get all subnets for a specific supernet
- `/network/ipam/supernets/:supernet_id/subnets/:subnet_id/ip_pools` - Get all IP pools for a specific subnet

## Example Usage Scenarios

1. **Network Inventory**: Generate a complete inventory of your network addressing scheme.
2. **IP Address Management**: Identify available IP ranges and usage patterns.
3. **Network Documentation**: Create documentation of your network structure.
4. **Network Planning**: Plan subnet allocations and IP pool assignments.
5. **Audit and Compliance**: Verify network configurations against documentation.

## Troubleshooting

If you encounter issues:

1. Verify your Sonar credentials are correct in the `.env` file
2. Check that your Sonar instance is accessible
3. Ensure you have the necessary permissions to access the IPAM endpoints
4. Check the logs for detailed error messages
