# Sonar Network Information Scripts

This directory contains scripts for retrieving and analyzing network information from Sonar, specifically focusing on IP address allocation and utilization.

## Scripts Overview

### 1. get_network_info.py

Retrieves basic network information from Sonar in one efficient pass:
- All supernets
- All subnets per supernet
- All IP pools

**Features:**
- Filters out 10.* networks (private IP space)
- Calculates total IP addresses in each pool
- Saves data in a structured JSON format

**Usage:**
```bash
python get_network_info.py
```

**Output:**
- Creates `sonar_network_data/network_info.json` with all network information
- Displays a summary of the retrieved data

### 2. get_ip_utilization.py

Analyzes IP address utilization by combining data from IP pools and allocated IP addresses.

**Features:**
- Retrieves all IP pools and allocated addresses in one pass
- Uses efficient data structures for IP matching
- Includes private 10.* networks in the analysis
- Calculates utilization rates for each pool
- Identifies which customers are using which IP addresses
- Properly handles network allocations that span multiple pools

**Usage:**
```bash
python get_ip_utilization.py
```

**Output:**
- Creates `sonar_network_data/ip_utilization.json` with detailed utilization data
- Creates `sonar_network_data/ip_utilization.csv` with summary data (without allocations)
- Displays a summary of the overall utilization and top/bottom utilized pools

### 3. get_allocated_ips.py

Retrieves all allocated IP addresses from Sonar, focusing on networks larger than /30.

**Features:**
- Identifies networks larger than /30 (i.e., /29, /28, /27, etc.)
- Documents these networks with customer names
- Filters out 10.* networks (private IP space)

**Usage:**
```bash
python get_allocated_ips.py
```

**Output:**
- Creates `sonar_network_data/large_networks.json` with detailed allocation data
- Creates `sonar_network_data/large_networks.csv` with the same data in CSV format
- Displays a summary of the large network allocations

## Common Features

All scripts:
- Filter out 10.* networks (private IP space) except `get_ip_utilization.py`, which includes them for ARIN reporting
- Create a `sonar_network_data` directory for output files
- Use environment variables for Sonar API connection details
- Include detailed logging
- Handle different Sonar API versions (supporting both "start"/"end" and "start_address"/"end_address" field names)

## Requirements

- Python 3.6+
- `ipaddress` module
- `dotenv` module
- Access to Sonar API

## Environment Variables

The scripts require the following environment variables to be set:

```
SONAR_USERNAME=your_username
SONAR_PASSWORD=your_password
SONAR_HOST=your_sonar_host
SONAR_PROTOCOL=https  # Optional, defaults to https
```

These can be set in a `.env` file in the same directory as the scripts.
