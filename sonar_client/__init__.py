"""
Sonar Client - A Python client for the Sonar network management system

This package provides a drop-in replacement for the original Sonar.py module
with the same API for backward compatibility.

Usage:
    import sonar_client as Sonar
    
    Sonar.setup(username, password, protocol, host)
    customers = Sonar.load_tag("/accounts")
    account = Sonar.get_sonar_account(12345)
"""

__version__ = "1.0.0"
__author__ = "SonarAPI Team"
__email__ = "support@example.com"
__license__ = "MIT"

# Import all functions from core module to maintain backward compatibility
from .core import (
    # Core setup and configuration
    setup,
    version,
    
    # Global variables (for backward compatibility)
    username,
    password,
    protocol,
    host,
    VERSION,
    DEBUG_LEVEL,
    
    # Session management
    _session,
    _csrf_token,
    
    # Global data structures
    manufacturers,
    inventory_models,
    inventory_models_by_name,
    master_fields,
    
    # Core API functions
    load_array,
    load_tag,
    load_ref,
    load_item,
    load_hash,
    load_customers,
    load_inventory_tables,
    load_account_types,
    load_network_map,
    
    # Account operations
    get_sonar_account,
    get_addresses,
    patch_address,
    
    # Search operations
    search,
    
    # HTTP operations
    post,
    post_direct,
    patch,
    delete,
    get,
    
    # Direct access functions
    get_direct_json,
    get_dhcp_server_config,
    get_inline_device_config,
    
    # Authentication functions
    init_session,
    extract_csrf_token,
    
    # Utility functions
    trim,
    NOOP,
    batch_post,
    lookup_ip,
    get_inventory_models_by_name,
)

# Make all functions available at package level for backward compatibility
__all__ = [
    # Core setup and configuration
    'setup',
    'version',
    
    # Global variables
    'username',
    'password', 
    'protocol',
    'host',
    'VERSION',
    'DEBUG_LEVEL',
    
    # Session management
    '_session',
    '_csrf_token',
    
    # Global data structures
    'manufacturers',
    'inventory_models',
    'inventory_models_by_name',
    'master_fields',
    
    # Core API functions
    'load_array',
    'load_tag',
    'load_ref',
    'load_item',
    'load_hash',
    'load_customers',
    'load_inventory_tables',
    'load_account_types',
    'load_network_map',
    
    # Account operations
    'get_sonar_account',
    'get_addresses',
    'patch_address',
    
    # Search operations
    'search',
    
    # HTTP operations
    'post',
    'post_direct',
    'patch',
    'delete',
    'get',
    
    # Direct access functions
    'get_direct_json',
    'get_dhcp_server_config',
    'get_inline_device_config',
    
    # Authentication functions
    'init_session',
    'extract_csrf_token',
    
    # Utility functions
    'trim',
    'NOOP',
    'batch_post',
    'lookup_ip',
    'get_inventory_models_by_name',
]
