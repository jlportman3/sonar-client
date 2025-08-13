#!/usr/bin/env python3
"""
Compatibility tests for sonar-client package

These tests verify that the package maintains 100% backward compatibility
with the original Sonar.py module.
"""

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False

import sonar_client as Sonar


class TestCompatibility:
    """Test backward compatibility with original Sonar.py"""
    
    def test_module_imports(self):
        """Test that the module imports correctly"""
        assert Sonar is not None
        assert hasattr(Sonar, '__version__')
    
    def test_core_functions_exist(self):
        """Test that all core functions from original Sonar.py exist"""
        core_functions = [
            'setup', 'version', 'trim', 'NOOP',
            'load_array', 'load_tag', 'load_ref', 'load_item', 'load_hash',
            'get_sonar_account', 'get_addresses', 'patch_address',
            'search', 'post', 'post_direct', 'patch', 'delete', 'get',
            'load_customers', 'load_inventory_tables', 'load_account_types',
            'load_network_map', 'batch_post', 'lookup_ip',
            'get_inventory_models_by_name',
            'get_direct_json', 'get_dhcp_server_config', 'get_inline_device_config',
            'init_session', 'extract_csrf_token'
        ]
        
        for func_name in core_functions:
            assert hasattr(Sonar, func_name), f"Missing function: {func_name}"
            assert callable(getattr(Sonar, func_name)), f"Not callable: {func_name}"
    
    def test_global_variables_exist(self):
        """Test that all global variables from original Sonar.py exist"""
        global_vars = [
            'username', 'password', 'protocol', 'host', 
            'VERSION', 'DEBUG_LEVEL',
            '_session', '_csrf_token',
            'manufacturers', 'inventory_models', 'inventory_models_by_name', 'master_fields'
        ]
        
        for var_name in global_vars:
            assert hasattr(Sonar, var_name), f"Missing global variable: {var_name}"
    
    def test_version_function(self):
        """Test that version function works"""
        version = Sonar.version()
        assert isinstance(version, str)
        assert len(version) > 0
    
    def test_trim_function(self):
        """Test that trim function works as expected"""
        # Test with string
        result = Sonar.trim("  hello world  \n\r")
        assert result == "hello world"
        
        # Test with None
        result = Sonar.trim(None)
        assert result is None
        
        # Test with empty string
        result = Sonar.trim("")
        assert result == ""
    
    def test_noop_function(self):
        """Test that NOOP function works"""
        # Should not raise any exception
        result = Sonar.NOOP()
        assert result is None
    
    def test_setup_function_signature(self):
        """Test that setup function has correct signature"""
        import inspect
        sig = inspect.signature(Sonar.setup)
        params = list(sig.parameters.keys())
        
        expected_params = ['uname', 'pword', 'proto', 'hst']
        assert params == expected_params, f"Setup function signature mismatch. Expected {expected_params}, got {params}"
    
    def test_global_variable_defaults(self):
        """Test that global variables have expected default values"""
        assert Sonar.protocol == "https"
        assert Sonar.VERSION == "1.31"
        assert Sonar.DEBUG_LEVEL == 0
        assert Sonar.username is None
        assert Sonar.password is None
        assert Sonar.host is None
    
    def test_data_structures_are_dicts(self):
        """Test that global data structures are dictionaries"""
        assert isinstance(Sonar.manufacturers, dict)
        assert isinstance(Sonar.inventory_models, dict)
        assert isinstance(Sonar.inventory_models_by_name, dict)
        assert isinstance(Sonar.master_fields, dict)


class TestFunctionSignatures:
    """Test that function signatures match the original"""
    
    def test_load_array_signature(self):
        """Test load_array function signature"""
        import inspect
        sig = inspect.signature(Sonar.load_array)
        params = list(sig.parameters.keys())
        
        # Should have base, use_parallel, max_workers parameters
        assert 'base' in params
        assert 'use_parallel' in params
        assert 'max_workers' in params
    
    def test_search_signature(self):
        """Test search function signature"""
        import inspect
        sig = inspect.signature(Sonar.search)
        params = list(sig.parameters.keys())
        
        assert params == ['entity', 'arg']
    
    def test_post_signature(self):
        """Test post function signature"""
        import inspect
        sig = inspect.signature(Sonar.post)
        params = list(sig.parameters.keys())
        
        assert params == ['tag', 'data']


class TestModuleStructure:
    """Test the overall module structure"""
    
    def test_package_metadata(self):
        """Test that package has proper metadata"""
        assert hasattr(Sonar, '__version__')
        assert hasattr(Sonar, '__author__')
        assert hasattr(Sonar, '__license__')
        
        assert Sonar.__version__ == "1.0.0"
        assert Sonar.__license__ == "MIT"
    
    def test_all_exports(self):
        """Test that __all__ is properly defined"""
        assert hasattr(Sonar, '__all__')
        assert isinstance(Sonar.__all__, list)
        assert len(Sonar.__all__) > 0
        
        # Verify all exported items actually exist
        for item in Sonar.__all__:
            assert hasattr(Sonar, item), f"Exported item '{item}' not found in module"


if __name__ == "__main__":
    # Run a simple compatibility check
    print("Running basic compatibility tests...")
    
    # Test imports
    print("✓ Module imports successfully")
    
    # Test core functions exist
    core_functions = ['setup', 'version', 'load_tag', 'search', 'post']
    for func in core_functions:
        if hasattr(Sonar, func):
            print(f"✓ {func} function exists")
        else:
            print(f"✗ {func} function missing")
    
    # Test global variables
    global_vars = ['username', 'password', 'protocol', 'host', 'VERSION']
    for var in global_vars:
        if hasattr(Sonar, var):
            print(f"✓ {var} variable exists")
        else:
            print(f"✗ {var} variable missing")
    
    print("\nBasic compatibility check completed!")
    print("Run 'pytest' for full test suite.")
