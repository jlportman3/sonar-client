# Direct BDC Import to PostgreSQL

This script imports Sonar data directly into PostgreSQL/PostGIS for BDC (Broadband Data Collection) reporting, bypassing the SQLite cache step for improved performance and reliability.

## Overview

The `direct_bdc_import.py` script connects to the Sonar API, retrieves customer and inventory data, and imports it directly into PostgreSQL/PostGIS tables with proper spatial geometry support. This approach offers several advantages over the SQLite-based approach:

1. **Better Concurrency**: PostgreSQL handles concurrent operations better than SQLite
2. **Spatial Data Support**: Direct integration with PostGIS for spatial operations
3. **Eliminates Intermediate Step**: No need to maintain a separate SQLite database
4. **Improved Performance**: Optimized for large datasets with parallel processing

## Features

- **Parallel Processing**: Uses ThreadPoolExecutor to make concurrent API calls
- **Incremental Updates**: Only updates data older than a configurable threshold
- **Batch Operations**: Efficient batch inserts with proper transaction management
- **Spatial Data**: Automatically converts lat/lon to PostGIS geometry points
- **Progress Tracking**: Detailed progress bars and statistics
- **Error Handling**: Robust error recovery with transaction rollback

## Database Schema

The script creates the following tables in PostgreSQL (with configurable prefix):

1. `{prefix}customers` - Customer information with spatial geometry
2. `{prefix}inventory_items` - Equipment inventory data
3. `{prefix}customer_inventory` - Junction table linking customers to inventory items
4. `{prefix}groups` - Customer groups
5. `{prefix}customer_groups` - Junction table for customer group membership
6. `{prefix}services` - Service information for customers
7. `{prefix}metadata` - Metadata for tracking update times

## Usage

```bash
./direct_bdc_import.py [options]
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-w`, `--workers` | Number of worker threads (default: 10) |
| `-b`, `--batch-size` | Batch size for database operations (default: 100) |
| `-c`, `--commit-interval` | Commit interval for database operations (default: 1000) |
| `-f`, `--force` | Force update all data regardless of age |
| `-d`, `--days` | Only update data older than this many days (default: 7) |
| `-p`, `--prefix` | Table prefix for PostgreSQL tables (default: sonar.) |
| `-l`, `--limit` | Limit the number of customers to import (for testing) |
| `-v`, `--verbose` | Enable verbose output |
| `--inventory-only` | Only import inventory data |
| `--customers-only` | Only import customer data |
| `--max-retries` | Maximum number of retry attempts for API calls (default: 5) |
| `--initial-backoff` | Initial backoff delay in seconds (default: 1.0) |

### Examples

#### Basic Usage

```bash
./direct_bdc_import.py
```

#### Increase Worker Threads for Faster Processing

```bash
./direct_bdc_import.py -w 20
```

#### Force Update All Data

```bash
./direct_bdc_import.py -f
```

#### Update Only Inventory Data

```bash
./direct_bdc_import.py --inventory-only
```

#### Test with Limited Data

```bash
./direct_bdc_import.py -l 100
```

#### Use Custom Table Prefix

```bash
./direct_bdc_import.py -p bdc.
```

## Performance Tuning

You can adjust several parameters to optimize performance for your specific environment:

1. **Worker Threads (`-w`)**: Increase for faster processing, but be mindful of API rate limits and system resources. Start with the default (10) and adjust based on your system's capabilities.

2. **Batch Size (`-b`)**: Controls how many records are processed in a single batch before being inserted into the database. Larger batches can improve performance but use more memory.

3. **Commit Interval (`-c`)**: Controls how frequently the database commits changes. Higher values improve performance but increase the risk of data loss if the process is interrupted.

4. **Cache Days (`-d`)**: Controls how frequently data is refreshed. Increase this value to reduce unnecessary updates.

## Requirements

- Python 3.6+
- PostgreSQL with PostGIS extension
- Required Python packages:
  - psycopg2
  - tqdm
  - dotenv
  - concurrent.futures (standard library in Python 3.2+)

## Environment Variables

The script uses the following environment variables from your `.env` file:

- `POSTGRES_HOST`: PostgreSQL host (default: localhost)
- `POSTGRES_DB`: PostgreSQL database name (default: propagation)
- `POSTGRES_USER`: PostgreSQL user (default: propagation)
- `POSTGRES_PASSWORD`: PostgreSQL password
- `SONAR_USERNAME`: Sonar API username
- `SONAR_PASSWORD`: Sonar API password
- `SONAR_PROTOCOL`: Sonar API protocol (http or https)
- `SONAR_HOST`: Sonar API host

## Logging

The script logs detailed information to both the console and a log file (`bdc_import.log`). Use the `-v` flag to enable verbose logging for debugging.

## API Endpoint Reference

The importer relies on several Sonar API endpoints. Field names used in
`direct_bdc_import.py` match the responses documented under `sonar/docs/`:

- **`reports/accounts/contact_information/json`** – returns an array where each
  record includes the account ID, status, name and contact details. The importer
  uses indices `0`, `2`, `3`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`,
  `20` and `21` to pull the ID, status, name, address, city, state, ZIP, latitude,
  longitude, plus4, street2, country and source fields respectively.
- **`accounts/:id/json`** – provides a JSON object with an `account` key. This
  object contains `account_type_id`, `groups` and `services` arrays used to
  populate the related tables.
- **`accounts/:id/inventory_items`** – returns an array of inventory item objects
  containing at minimum `id` and `inventory_model_id` which are used when linking
  customers to inventory.
- **`inventory/models`** and **`inventory/manufacturers`** – supply model and
  manufacturer details. The script expects `id`, `name` and `manufacturer_id`
  fields in these responses.

These mappings ensure that the importer processes the JSON data correctly. If
Sonar modifies the API field names in the future, update the indices in
`direct_bdc_import.py` to match.
