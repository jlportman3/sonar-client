# Sonar Client

A Python client library for the Sonar network management system. This package provides a drop-in replacement for the original `Sonar.py` module with 100% backward compatibility.

## Features

- **Complete API Coverage**: Access to all Sonar API endpoints
- **Session Management**: Automatic authentication and session handling
- **Parallel Processing**: Efficient data loading with configurable parallelism
- **Retry Logic**: Built-in retry mechanisms with exponential backoff
- **Direct JSON Access**: Direct access to Sonar endpoints bypassing API limitations
- **Inventory Management**: Complete inventory system integration
- **Network Operations**: Full network management capabilities
- **100% Backward Compatible**: Drop-in replacement for existing Sonar.py scripts

## Installation

### From GitHub (SSH)
```bash
pip install git+ssh://git@github.com/jlportman3/SonarAPI.git#subdirectory=sonar_client
```

### Development Installation
```bash
git clone git@github.com:jlportman3/SonarAPI.git
cd SonarAPI/sonar_client
pip install -e .
```

## Quick Start

### Basic Usage

```python
import sonar_client as Sonar

# Setup connection
Sonar.setup(
    username="your_username",
    password="your_password", 
    protocol="https",
    host="your-sonar-instance.com"
)

# Load customer data
customers = Sonar.load_tag("/accounts")
print(f"Found {len(customers)} customers")

# Get specific customer
customer = Sonar.get_sonar_account(12345)
print(f"Customer: {customer['name']}")

# Search for customers
results = Sonar.search("accounts", "john@example.com")
```

### Migration from Sonar.py

If you're currently using the original `Sonar.py` module, migration is simple:

**Before:**
```python
import Sonar

Sonar.setup(username, password, protocol, host)
customers = Sonar.load_tag("/accounts")
```

**After:**
```python
import sonar_client as Sonar  # Only change needed!

Sonar.setup(username, password, protocol, host)
customers = Sonar.load_tag("/accounts")  # Everything else identical
```

## API Reference

### Core Functions

#### `setup(username, password, protocol, host)`
Initialize the Sonar API connection.

**Parameters:**
- `username` (str): Sonar username
- `password` (str): Sonar password  
- `protocol` (str): Protocol ("https" or "http")
- `host` (str): Sonar host (e.g., "sonar.example.com")

#### `load_tag(tag)`
Load data from a Sonar API endpoint.

**Parameters:**
- `tag` (str): API endpoint path (e.g., "/accounts", "/inventory/items")

**Returns:**
- List of data objects from the endpoint

#### `load_item(tag)`
Load a single item from a Sonar API endpoint.

**Parameters:**
- `tag` (str): API endpoint path (e.g., "/accounts/12345")

**Returns:**
- Single data object or None

#### `get_sonar_account(customer_id)`
Get detailed account information for a customer.

**Parameters:**
- `customer_id` (int): Customer ID

**Returns:**
- Customer account data dictionary

### Search Functions

#### `search(entity, query)`
Search for entities in Sonar.

**Parameters:**
- `entity` (str): Entity type ("accounts", "inventory", etc.)
- `query` (str): Search query

**Returns:**
- List of matching results

### HTTP Operations

#### `post(tag, data)`
POST data to a Sonar API endpoint.

#### `patch(tag, data)`
PATCH data to a Sonar API endpoint.

#### `delete(tag)`
DELETE request to a Sonar API endpoint.

#### `get_direct_json(endpoint)`
Get JSON data directly from Sonar (bypasses API limitations).

### Inventory Functions

#### `load_inventory_tables()`
Load all inventory-related data and build lookup tables.

#### `load_customers()`
Load all customer data indexed by ID.

#### `load_account_types()`
Load account types indexed by ID.

## Advanced Usage

### Parallel Processing

```python
# Load data with custom parallelism
data = Sonar.load_array(
    "https://sonar.example.com/api/v1/accounts",
    use_parallel=True,
    max_workers=10
)
```

### Direct JSON Access

```python
# Access endpoints directly (useful for reports)
report_data = Sonar.get_direct_json("reports/accounts/contact_information/json")
```

### Inventory Management

```python
# Load complete inventory system
inventory = Sonar.load_inventory_tables()

# Access inventory models by name
models = Sonar.get_inventory_models_by_name()
router_model = models.get("Cisco ISR 4331")
```

### Error Handling

```python
try:
    customer = Sonar.get_sonar_account(12345)
    if customer:
        print(f"Found customer: {customer['name']}")
    else:
        print("Customer not found")
except Exception as e:
    print(f"Error: {e}")
```

## Configuration

### Debug Levels

```python
# Set debug level for troubleshooting
Sonar.DEBUG_LEVEL = 1  # Basic debug info
Sonar.DEBUG_LEVEL = 2  # Verbose debug info
```

### Global Variables

The package maintains the same global variables as the original:

- `Sonar.username` - Current username
- `Sonar.password` - Current password  
- `Sonar.protocol` - Current protocol
- `Sonar.host` - Current host
- `Sonar.VERSION` - Package version

## Examples

### Customer Management

```python
import sonar_client as Sonar

# Setup
Sonar.setup("user", "pass", "https", "sonar.example.com")

# Get all customers
customers = Sonar.load_tag("/accounts")

# Process each customer
for customer in customers:
    print(f"Customer {customer['id']}: {customer['name']}")
    
    # Get detailed account info
    account = Sonar.get_sonar_account(customer['id'])
    
    # Get customer addresses
    addresses = Sonar.get_addresses(customer['id'])
    
    # Get customer services
    services = Sonar.load_tag(f"/accounts/{customer['id']}/services")
```

### Network Operations

```python
# Load network mapping
network_map = Sonar.load_network_map()

# Look up IP information
ip_info = Sonar.lookup_ip("192.168.1.1")

# Get DHCP server configuration
dhcp_config = Sonar.get_dhcp_server_config(server_id=1)
```

### Bulk Operations

```python
# Search for customers by email
email_results = Sonar.search("accounts", "gmail.com")

# Load all inventory items
inventory = Sonar.load_tag("/inventory/items")

# Process in batches
batch_size = 100
for i in range(0, len(inventory), batch_size):
    batch = inventory[i:i+batch_size]
    # Process batch...
```

## Requirements

- Python 3.8+
- requests >= 2.25.0
- beautifulsoup4 >= 4.9.0

## Development

### Running Tests

```bash
pip install -e .[dev]
pytest
```

### Code Formatting

```bash
black sonar_client/
flake8 sonar_client/
```

## License

MIT License - see LICENSE file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/jlportman3/SonarAPI/issues)
- **Documentation**: [GitHub Repository](https://github.com/jlportman3/SonarAPI/tree/main/sonar_client)

## Changelog

### v1.0.0
- Initial release
- Complete backward compatibility with original Sonar.py
- Professional packaging and distribution
- Comprehensive documentation
- Type hints and modern Python features
