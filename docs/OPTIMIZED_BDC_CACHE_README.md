# Optimized BDC Cache Manager

This is an optimized version of the BDC (Broadband Data Collection) Cache Manager that significantly improves performance when downloading and caching Sonar data in SQLite.

## Performance Improvements

The optimized version addresses several performance bottlenecks in the original script:

1. **Parallel Processing**
   - Uses ThreadPoolExecutor to make concurrent API calls
   - Processes multiple customers simultaneously
   - Configurable number of worker threads

2. **Optimized SQLite Operations**
   - Uses WAL (Write-Ahead Logging) mode for better concurrency
   - Implements bulk inserts with executemany()
   - Optimized transaction management with proper batching
   - Configurable commit intervals
   - Increased cache size and other SQLite performance settings

3. **Incremental Updates**
   - Only updates data older than a configurable threshold
   - Tracks last update times in a metadata table
   - Skips customers that don't need updating

4. **Improved Error Handling**
   - Robust error recovery
   - Detailed logging with configurable verbosity
   - Progress tracking with statistics

## Usage

```bash
./optimized_bdc_cache.py [options]
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `-db`, `--database` | SQLite database path (default: bdc_cache.db) |
| `-w`, `--workers` | Number of worker threads (default: 10) |
| `-b`, `--batch-size` | Batch size for database operations (default: 100) |
| `-c`, `--commit-interval` | Commit interval for database operations (default: 1000) |
| `-f`, `--force` | Force update all data regardless of age |
| `-d`, `--days` | Only update data older than this many days (default: 7) |
| `-l`, `--limit` | Limit the number of customers to cache (for testing) |
| `-v`, `--verbose` | Enable verbose output |
| `--inventory-only` | Only update inventory data |
| `--customers-only` | Only update customer data |

### Examples

#### Basic Usage

```bash
./optimized_bdc_cache.py
```

#### Increase Worker Threads for Faster Processing

```bash
./optimized_bdc_cache.py -w 20
```

#### Force Update All Data

```bash
./optimized_bdc_cache.py -f
```

#### Update Only Inventory Data

```bash
./optimized_bdc_cache.py --inventory-only
```

#### Test with Limited Data

```bash
./optimized_bdc_cache.py -l 100
```

## Performance Tuning

You can adjust several parameters to optimize performance for your specific environment:

1. **Worker Threads (`-w`)**: Increase for faster processing, but be mindful of API rate limits and system resources. Start with the default (10) and adjust based on your system's capabilities.

2. **Batch Size (`-b`)**: Controls how many records are processed in a single batch before being inserted into the database. Larger batches can improve performance but use more memory.

3. **Commit Interval (`-c`)**: Controls how frequently the database commits changes. Higher values improve performance but increase the risk of data loss if the process is interrupted.

4. **Cache Days (`-d`)**: Controls how frequently data is refreshed. Increase this value to reduce unnecessary updates.

## Database Schema

The database schema remains compatible with the original script, so existing tools that use the BDC cache database will continue to work without modification.

## Requirements

- Python 3.6+
- Required packages:
  - tqdm
  - dotenv
  - concurrent.futures (standard library in Python 3.2+)

## Comparison with Original Script

| Feature | Original Script | Optimized Script |
|---------|----------------|------------------|
| API Calls | Sequential | Parallel |
| Database Operations | Individual inserts | Bulk operations |
| Transaction Management | Infrequent commits | Configurable batching |
| Update Strategy | Full refresh | Incremental updates |
| Error Handling | Basic | Robust with recovery |
| Progress Reporting | Basic | Detailed statistics |
| SQLite Optimizations | None | WAL mode, cache settings |
| Configurability | Limited | Highly configurable |

## Logging

The script logs detailed information to both the console and a log file (`bdc_cache.log`). Use the `-v` flag to enable verbose logging for debugging.
