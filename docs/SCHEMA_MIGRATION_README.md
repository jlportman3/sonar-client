# Sonar Schema Migration

This directory contains scripts and documentation for migrating Sonar-related tables from the public schema to a dedicated `sonar` schema in the PostgreSQL database.

## Migration Overview

The migration process:

1. Creates a new `sonar` schema
2. Copies all Sonar tables from the public schema to the new schema
3. Removes the "sonar_" prefix from table names in the new schema
4. Creates views in the public schema that point to the new schema tables
5. Preserves the original tables for backward compatibility

## Table Mapping

| Original Table (public schema) | New Table (sonar schema) |
|-------------------------------|--------------------------|
| sonar_customer_groups         | customer_groups          |
| sonar_customer_inventory      | customer_inventory       |
| sonar_customers               | customers                |
| sonar_customers_in_fiber      | customers_in_fiber       |
| sonar_groups                  | groups                   |
| sonar_inventory_items         | inventory_items          |
| sonar_metadata                | metadata                 |
| sonar_services                | services                 |

## View Mapping

To facilitate a gradual transition, views are created in the public schema:

| View Name (public schema)           | Points To (sonar schema)  |
|------------------------------------|--------------------------|
| sonar_schema_customer_groups       | customer_groups          |
| sonar_schema_customer_inventory    | customer_inventory       |
| sonar_schema_customers             | customers                |
| sonar_schema_customers_in_fiber    | customers_in_fiber       |
| sonar_schema_groups                | groups                   |
| sonar_schema_inventory_items       | inventory_items          |
| sonar_schema_metadata              | metadata                 |
| sonar_schema_services              | services                 |

## Migration Script

The migration is performed by the `migrate_sonar_tables_to_schema.sql` script. This script:

- Creates the sonar schema
- Copies data from the original tables to the new schema
- Preserves primary keys and indexes
- Creates views for backward compatibility
- Outputs statistics about the migrated tables

## Usage

To run the migration:

```bash
psql -U propagation -d propagation -f migrate_sonar_tables_to_schema.sql
```

## Post-Migration

After the migration is complete and all code has been updated to use the new schema:

1. Test thoroughly to ensure all functionality works with the new schema
2. Update application code to use the new schema-qualified names
3. When ready, the original tables can be dropped (script comments contain the necessary commands)

## Benefits of Schema Migration

1. **Better Organization**: Related tables are grouped together in a dedicated schema
2. **Cleaner Naming**: Removes redundant prefixes from table names
3. **Improved Security**: Permissions can be managed at the schema level
4. **Reduced Namespace Pollution**: Keeps the public schema cleaner
5. **Better Documentation**: Schema provides context about table relationships

## Code Update Guidelines

When updating application code to use the new schema:

1. Replace references to `sonar_customers` with `sonar.customers`
2. Replace references to `sonar_customer_inventory` with `sonar.customer_inventory`
3. And so on for all tables

For example:

```python
# Old code
query = "SELECT * FROM sonar_customers WHERE status = 'Active'"

# New code
query = "SELECT * FROM sonar.customers WHERE status = 'Active'"
```

During the transition period, you can use the views with the `sonar_schema_` prefix:

```python
# Transition code
query = "SELECT * FROM sonar_schema_customers WHERE status = 'Active'"
