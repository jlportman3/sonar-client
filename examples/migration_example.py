#!/usr/bin/env python3
"""
Migration example showing how to switch from original Sonar.py to sonar-client package

This example demonstrates that only the import statement needs to change.
All existing code remains identical.
"""

# OLD WAY (original Sonar.py):
# import Sonar

# NEW WAY (sonar-client package):
import sonar_client as Sonar

# Everything else remains exactly the same!

def example_existing_script():
    """
    This is an example of existing code that uses Sonar.py
    With sonar-client, only the import changes - everything else is identical
    """
    
    # Setup (identical to original)
    Sonar.setup("username", "password", "https", "sonar.example.com")
    
    # Load customers (identical to original)
    customers = Sonar.load_tag("/accounts")
    print(f"Loaded {len(customers)} customers")
    
    # Get specific account (identical to original)
    if customers:
        account = Sonar.get_sonar_account(customers[0]['id'])
        print(f"Account: {account.get('name', 'N/A')}")
    
    # Search functionality (identical to original)
    results = Sonar.search("accounts", "test@example.com")
    print(f"Search results: {len(results)}")
    
    # Load inventory (identical to original)
    inventory = Sonar.load_inventory_tables()
    if inventory:
        print(f"Loaded {len(inventory)} inventory items")
    
    # Access global variables (identical to original)
    print(f"Connected to: {Sonar.protocol}://{Sonar.host}")
    print(f"Version: {Sonar.version()}")
    
    # All other functions work exactly the same:
    # - Sonar.load_customers()
    # - Sonar.load_account_types()
    # - Sonar.get_direct_json()
    # - Sonar.post(), Sonar.patch(), Sonar.delete()
    # - etc.

def demonstrate_compatibility():
    """Show that all original functionality is preserved"""
    
    print("=== Sonar Client Migration Example ===")
    print()
    print("This script demonstrates 100% backward compatibility.")
    print("Only the import statement changes:")
    print()
    print("OLD: import Sonar")
    print("NEW: import sonar_client as Sonar")
    print()
    print("All existing code works without any modifications!")
    print()
    
    # Show that all the original functions are available
    functions = [
        'setup', 'version', 'load_tag', 'load_item', 'load_array',
        'get_sonar_account', 'search', 'post', 'patch', 'delete',
        'load_customers', 'load_inventory_tables', 'load_account_types',
        'get_direct_json', 'trim', 'NOOP'
    ]
    
    print("Available functions (same as original Sonar.py):")
    for func in functions:
        if hasattr(Sonar, func):
            print(f"  ✓ Sonar.{func}")
        else:
            print(f"  ✗ Sonar.{func} - MISSING!")
    
    print()
    print("Global variables (same as original Sonar.py):")
    variables = ['username', 'password', 'protocol', 'host', 'VERSION', 'DEBUG_LEVEL']
    for var in variables:
        if hasattr(Sonar, var):
            print(f"  ✓ Sonar.{var}")
        else:
            print(f"  ✗ Sonar.{var} - MISSING!")

if __name__ == "__main__":
    demonstrate_compatibility()
    
    # Uncomment to run the actual example (requires valid credentials)
    # example_existing_script()
