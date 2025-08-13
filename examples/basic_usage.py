#!/usr/bin/env python3
"""
Basic usage example for sonar-client package

This example shows how to use the sonar-client package for common operations.
"""

import os
import sonar_client as Sonar

def main():
    """Main example function"""
    
    # Setup connection (you can also use environment variables)
    username = os.getenv('SONAR_USERNAME', 'your_username')
    password = os.getenv('SONAR_PASSWORD', 'your_password')
    protocol = os.getenv('SONAR_PROTOCOL', 'https')
    host = os.getenv('SONAR_HOST', 'your-sonar-instance.com')
    
    print("Setting up Sonar API connection...")
    Sonar.setup(username, password, protocol, host)
    
    # Example 1: Load all customers
    print("\n1. Loading customers...")
    customers = Sonar.load_tag("/accounts")
    print(f"Found {len(customers)} customers")
    
    # Show first few customers
    for i, customer in enumerate(customers[:3]):
        print(f"  Customer {customer['id']}: {customer.get('name', 'N/A')}")
    
    # Example 2: Get specific customer details
    if customers:
        customer_id = customers[0]['id']
        print(f"\n2. Getting details for customer {customer_id}...")
        
        account = Sonar.get_sonar_account(customer_id)
        if account:
            print(f"  Account name: {account.get('name', 'N/A')}")
            print(f"  Account type: {account.get('account_type_id', 'N/A')}")
        
        # Get customer addresses
        addresses = Sonar.get_addresses(customer_id)
        print(f"  Found {len(addresses)} addresses")
    
    # Example 3: Search functionality
    print("\n3. Searching for accounts...")
    search_results = Sonar.search("accounts", "test")
    print(f"Found {len(search_results)} accounts matching 'test'")
    
    # Example 4: Load inventory data
    print("\n4. Loading inventory...")
    inventory_items = Sonar.load_tag("/inventory/items")
    print(f"Found {len(inventory_items)} inventory items")
    
    # Example 5: Load account types
    print("\n5. Loading account types...")
    account_types = Sonar.load_account_types()
    print(f"Found {len(account_types)} account types")
    
    for type_id, account_type in list(account_types.items())[:3]:
        print(f"  Type {type_id}: {account_type.get('name', 'N/A')}")
    
    print("\nExample completed successfully!")

if __name__ == "__main__":
    main()
