"""
Core Sonar API functionality

This module contains all the original Sonar.py functions with minimal modifications
to maintain 100% backward compatibility.
"""

import json
import requests
import time
from typing import List, Tuple, Optional, Dict, Any, Union
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Global session and token
_session = None
_csrf_token = None

# Global configuration variables
username = None
password = None
protocol = "https"
host = None
VERSION = "1.31"
DEBUG_LEVEL = 0  # 0: no debug, 1: headers and tokens, 2: verbose

# Global data structures
manufacturers = {}
inventory_models = {}
inventory_models_by_name = {}  # Renamed from inventory_models_byname
master_fields = {}


def trim(s: str) -> str:
    """Trim whitespace and normalize line endings"""
    if s:
        s = s.strip()
        s = s.replace('\r', ' ')
        s = s.replace('\n', ' ')
        return s
    return None


def NOOP():
    """No operation function"""
    pass


def version():
    """Get the version string"""
    return VERSION


def setup(uname: str, pword: str, proto: str, hst: str) -> None:
    """Setup global connection parameters"""
    global username, password, protocol, host
    username = uname
    password = pword
    protocol = proto
    host = hst


def load_array(base: str, use_parallel: bool = True, max_workers: int = 5):
    """Load paginated data from API endpoint with optional parallel processing"""
    from concurrent.futures import ThreadPoolExecutor, as_completed
    
    limit = 200
    max_retries = 5
    retry_delay = 5
    
    def fetch_page(page_num: int):
        """Fetch a single page with retry logic"""
        url = f"{base}?limit={limit}&page={page_num}"
        retries = max_retries
        
        while retries > 0:
            try:
                response = requests.get(url, auth=(username, password), timeout=30)
                if response.status_code == 200:
                    json_obj = json.loads(response.content.decode())
                    # Some endpoints don't have pagination, handle gracefully
                    data = json_obj.get('data', [])
                    paginator = json_obj.get('paginator', None)
                    return page_num, data, paginator
                else:
                    print(f"Error {response.status_code} loading page {page_num}")
                    
            except requests.exceptions.RequestException as e:
                print(f"Network error loading page {page_num}: {str(e)}")
                if retries <= 1:
                    print(f"Failed to load page {page_num} after {max_retries} retries")
                    return page_num, [], None
                    
            retries -= 1
            if retries > 0:
                print(f"Retrying page {page_num} in {retry_delay} seconds... ({retries} attempts left)")
                time.sleep(retry_delay)
                
        return page_num, [], None
    
    # First, get the first page to determine total pages
    page_num, first_page_data, paginator = fetch_page(1)
    if not paginator:
        return first_page_data
    
    total_pages = paginator['total_pages']
    all_data = first_page_data.copy()
    
    # If only one page or parallel disabled, return first page data
    if total_pages <= 1 or not use_parallel:
        return all_data
    
    # Fetch remaining pages in parallel
    print(f"Fetching {total_pages - 1} additional pages in parallel (max {max_workers} workers)")
    
    with ThreadPoolExecutor(max_workers=min(max_workers, total_pages - 1)) as executor:
        # Submit tasks for pages 2 through total_pages
        future_to_page = {
            executor.submit(fetch_page, page): page 
            for page in range(2, total_pages + 1)
        }
        
        # Collect results as they complete
        page_results = {}
        for future in as_completed(future_to_page):
            page_num = future_to_page[future]
            try:
                result_page_num, page_data, _ = future.result()
                page_results[result_page_num] = page_data
            except Exception as e:
                print(f"Error fetching page {page_num}: {str(e)}")
                page_results[page_num] = []
    
    # Combine all pages in order
    for page in range(2, total_pages + 1):
        if page in page_results:
            all_data.extend(page_results[page])
    
    print(f"Successfully loaded {len(all_data)} records from {total_pages} pages")
    return all_data


def load_tag(tag: str):
    """Load data from API tag endpoint"""
    base = f"{protocol}://{host}/api/v1{tag}"
    return load_array(base)


def load_ref(tag: str):
    """Load reference data from API tag endpoint"""
    base = f"{protocol}://{host}/api/v1{tag}"
    data = load_array(base)
    return data


def batch_post(batcher_user: str, batcher_pass: str, batcher_url: str, mac: str, ip: str):
    """Post batch data to external endpoint"""
    data = {
        "leased_mac_address": mac,
        "ip_address": ip,
        "expired": False
    }
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    encoded_data = json.dumps(data)
    r = requests.post(batcher_url, auth=(batcher_user, batcher_pass), headers=headers, data=encoded_data)
    if not r.ok:
        print(r.status_line)
        print(r.content)
        print("\n")
    return r


def load_network_map():
    """Load network mapping data"""
    ep = "/network/mapping"
    base = f"{protocol}://{host}/api/v1{ep}"
    r = requests.get(base, auth=(username, password))
    if r.ok:
        data = r.json()
        return data
    else:
        return None


def load_inventory_tables():
    """Load all inventory-related tables and build lookup structures"""
    inventory_items = {}
    print("loading inventory tables")
    url = "/inventory/manufacturers"
    data = load_hash(url)
    if not data:
        print("Failed to load manufacturers")
        return None
        
    global manufacturers, inventory_models, inventory_models_by_name, master_fields
    manufacturers.clear()
    for i in data:
        item = data[i]
        manufacturers[item["id"]] = data[i]["name"]

    print("loading inventory models")
    url = "/inventory/models"
    data = load_hash(url)
    if not data:
        print("Failed to load inventory models")
        return None
    inventory_models.clear()
    inventory_models_by_name.clear()
    for i in data:
        item = data[i]
        inventory_models[item["id"]] = data[i]
        inventory_models_by_name[item["name"]] = data[i]

    print("loading inventory fields")
    master_fields.clear()  # Clear existing fields
    for k in sorted(inventory_models.keys()):
        url = "/inventory/models/{}/fields".format(k)
        data = load_tag(url)
        if data:
            inventory_models[k]["fields"] = data
            for i in range(len(data)):
                item = data[i]
                master_fields[item["id"]] = data[i]
        else:
            print(f"Failed to load fields for model {k}")

    print("loading inventory items")
    url = "/inventory/items"
    data = load_tag(url)
    if not data:
        print("Failed to load inventory items")
        return None
    print("{} items loaded".format(len(data)))

    print(f"Processing {len(data)} inventory items")
    # Use original item ID as key, but store MAC/IMSI in the item data
    for i in range(len(data)):
        try:
            item = data[i]
            item_id = item["id"]
            
            # Get model info from inventory_models using inventory_model_id
            model_id = item.get('inventory_model_id')
            if not model_id:
                print(f"No model ID for item {item_id}")
                continue
                
            model = inventory_models[model_id]
            if not model:
                print(f"Model {model_id} not found for item {item_id}")
                continue
                
            item['model'] = model
            
            # Get manufacturer info from the model
            if 'manufacturer_id' in model:
                manufacturer = manufacturers.get(model['manufacturer_id'])
                if manufacturer:
                    model['manufacturer'] = {'id': model['manufacturer_id'], 'name': manufacturer}
            
            # Extract MAC/IMSI from fields
            fp = item.get("fields", [])
            for field in fp:
                if field["field_id"] not in master_fields:
                    print(f"Field ID {field['field_id']} not found in master_fields")
                    continue
                    
                type = master_fields[field["field_id"]]["type"]
                if type == "mac" or type == "imsi":
                    item["mac_or_imsi"] = field["data"]
                    break
                    
            inventory_items[item_id] = item
            
        except Exception as e:
            print(f"Error processing item {i}: {str(e)}")
            continue

    return inventory_items


def get_inventory_models_by_name():
    """Get inventory models indexed by name"""
    return inventory_models_by_name


def load_item(tag):
    """Load a single item from API endpoint"""
    retval = {}

    url = f"{protocol}://{host}/api/v1{tag}"
    auth = (username, password)
    response = requests.get(url, auth=auth)
    if response.ok:
        json_obj = json.loads(response.content)
        retval = json_obj["data"]
        return retval
    return None


def get_sonar_account(custid):
    """Get account data for a specific customer ID"""
    return load_item("/accounts/" + str(custid))


def get_addresses(custid):
    """Get addresses for a specific customer ID"""
    return load_tag("/accounts/" + str(custid) + "/addresses")


def patch_address(account_id, address_id, address_data):
    """Patch/update an address for a specific account"""
    tag = f"/accounts/{account_id}/addresses/{address_id}"
    return patch(tag, address_data)


def search(entity, arg):
    """Search the API for entities"""
    retval = {}
    args = {}
    if arg:
        s = {"search": arg}
        args = {
            "size": 200,
            "page": 1,
            "search": arg
        }
    else:
        s = None
        args = {
            "size": 200,
            "page": 1   
        }
        
    url = "/search/" + entity
    response = post(url, args)
    return response


def post(tag, data):
    """POST data to API endpoint with pagination support"""
    page = 1
    limit = 200
    retval = []
    rdata = []
    empty = []
    hunk = {}
    url = f"{protocol}://{host}/api/v1{tag}?limit={limit}&page={page}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    encoded_data = json.dumps(data).encode('utf-8')
    while True:
        response = requests.post(url, headers=headers, data=encoded_data, auth=(username, password))

        if not response.ok:
            print(response.status_code)
            print(response.text)
            return []
        
        json_obj = json.loads(response.content.decode())
        hunk = json_obj.get('data', {}).get('results', {})
        for key in hunk.keys():
            if key == "aggregations":
                continue
            item = hunk[key]
            rdata.append(item)

        paginator = json_obj.get('data', {}).get('paginator')

        if paginator is None:
            return rdata

        if page >= paginator.get('total_pages', 1):
            return rdata
        page += 1
        
    return []


def post_direct(tag, data):
    """
    POST data to Sonar API and return the response directly without pagination logic.
    Used for endpoints that don't use pagination like /scheduling/jobs/find_any_available_space
    """
    url = f"{protocol}://{host}/api/v1{tag}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    encoded_data = json.dumps(data)
    
    try:
        response = requests.post(url, headers=headers, data=encoded_data, auth=(username, password))
        
        if not response.ok:
            print(f"POST_DIRECT error: {url} - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
        return response.json()
        
    except Exception as e:
        print(f"Error in POST_DIRECT request: {str(e)}")
        return None


def delete(tag):
    """DELETE request to API endpoint"""
    url = f"{protocol}://{host}/api/v1{tag}"
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    response = requests.delete(url, headers=headers, auth=(username, password))

    if not response.ok:
        print(f"account: {tag} {username} {response.content}")
        return None

    json_obj = json.loads(response.content)
    return json_obj


def patch(tag, data):
    """Patch data to Sonar API using basic authentication"""
    try:
        # Prepare the request
        url = f"{protocol}://{host}/api/v1{tag}"
        headers = {'Content-Type': 'application/json; charset=UTF-8'}
        encoded_data = json.dumps(data)
        
        # Make the request using basic authentication
        response = requests.patch(url, headers=headers, data=encoded_data, auth=(username, password))
        
        if not response.ok:
            print(f"PATCH error: {url} - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
        return response.json()
        
    except Exception as e:
        print(f"Error in PATCH request: {str(e)}")
        return None


def get(tag, data):
    """GET request to API endpoint with data"""
    url = f"{protocol}://{host}/api/v1{tag}"
    header = {'Content-Type': 'application/json; charset=UTF-8'}
    encoded_data = json.dumps(data).encode('utf-8')
    request = Request(url, method='GET', headers=header, data=encoded_data)
    request.add_header("Authorization", f"Basic {username}:{password}")
    response = urlopen(request)

    if response.status != 200:
        print(f"account: {tag} {username} {response.content}")
        return None
    json_obj = json.loads(response.read())
    return json_obj


def load_customers():
    """Load all customer data"""
    print("load customer tables")
    url = f"{protocol}://{host}/api/v1/accounts"
    while True:
        try:
            data = load_array(url)
            break
        except:
            time.sleep(1)
            
    customers = {}
    for i in range(len(data)):
        id = data[i]["id"]
        customers[id] = data[i]
    return customers


def load_hash(tag: str):
    """Load data from API and index by ID"""
    data = load_tag(tag)
    if not data:
        print(f"No data returned for {tag}")
        return {}
        
    items = {}
    for item in data:
        try:
            # Use native ID type (usually integer)
            item_id = item['id']
            items[item_id] = item
        except Exception as e:
            print(f"Error processing item in load_hash: {str(e)}")
            print(f"Item data: {item}")
    return items


def lookup_ip(search_ip: str):
    """Look up IP address information"""
    r = get(f"/network/ipam/ip_lookup?ip={search_ip}", {})
    return r


def load_account_types():
    """Load account types from /system/account_types and index by ID"""
    url = "/system/account_types"
    data = load_tag(url)
    if not data:
        print("Failed to load account types")
        return {}
        
    account_types = {}
    for item in data:
        try:
            account_types[item['id']] = item
        except Exception as e:
            print(f"Error processing account type: {str(e)}")
            print(f"Item data: {item}")
    return account_types


def extract_csrf_token(html_content):
    """Extract CSRF token from login page HTML"""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        # Look for meta tag with csrf-token
        csrf_meta = soup.find('meta', {'name': 'csrf-token'})
        if csrf_meta:
            return csrf_meta.get('content')
        # Look for input with _token
        csrf_input = soup.find('input', {'name': '_token'})
        if csrf_input:
            return csrf_input.get('value')
        return None
    except Exception as e:
        print(f"Error extracting CSRF token: {str(e)}")
        return None


def init_session():
    """Initialize session and get CSRF token"""
    global _session, _csrf_token
    
    try:
        if _session is not None:
            return True
            
        # Create new session
        _session = requests.Session()
        _session.headers.update({
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'
        })
        
        # First get the home page to get initial cookies
        home_url = f"https://{host}/"
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Attempting to access home page: {home_url}")
        home_response = _session.get(home_url)
        if not home_response.ok:
            print(f"ERROR: Error accessing home page: {home_response.status_code}")
            if DEBUG_LEVEL >= 2:
                print(f"DEBUG: Home page response content: {home_response.text[:500]}...")
            return False
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Home page response OK. Status: {home_response.status_code}")
            print(f"DEBUG: Home page response headers: {home_response.headers}")
            print(f"DEBUG: Home page response content preview: {home_response.text[:500]}...")
            
        # Get CSRF token from response headers
        _csrf_token = home_response.headers.get('x-meta-csrf-token')
        if not _csrf_token:
            _csrf_token = extract_csrf_token(home_response.text)
            if not _csrf_token:
                print("ERROR: Could not find CSRF token from meta tag or input field.")
                return False
        if DEBUG_LEVEL >= 1:
            print(f"DEBUG: CSRF Token: {_csrf_token}")
                
        # Login with CSRF token
        login_data = {
            'username': username,
            'password': password,
            '_token': _csrf_token
        }
        login_headers = {
            'X-CSRF-TOKEN': _csrf_token,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Attempting login to: {home_url}")
            print(f"DEBUG: Login data: {login_data}")
            print(f"DEBUG: Login headers: {login_headers}")
        login_response = _session.post(home_url, data=login_data, headers=login_headers)
        if not login_response.ok:
            print(f"ERROR: Login failed: {login_response.status_code}")
            if DEBUG_LEVEL >= 2:
                print(f"DEBUG: Login response content: {login_response.text[:500]}...")
            return False
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Login response OK. Status: {login_response.status_code}")
            print(f"DEBUG: Login response headers: {login_response.headers}")
            print(f"DEBUG: Login response content preview: {login_response.text[:500]}...")
            
        # Get new CSRF token after login (for subsequent requests)
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Attempting to get post-login CSRF token from: https://{host}/home")
        home_response = _session.get(f"https://{host}/home")
        if not home_response.ok:
            print(f"ERROR: Failed to get post-login CSRF token: {home_response.status_code}")
            if DEBUG_LEVEL >= 2:
                print(f"DEBUG: Post-login home page response content: {home_response.text[:500]}...")
            return False
            
        _csrf_token = home_response.headers.get('x-meta-csrf-token')
        if not _csrf_token:
            _csrf_token = extract_csrf_token(home_response.text)
            if not _csrf_token:
                print("ERROR: Could not find post-login CSRF token from meta tag or input field.")
                return False
        if DEBUG_LEVEL >= 1:
            print(f"DEBUG: Post-login CSRF Token: {_csrf_token}")
                
        # Get JWT token
        jwt_data = {
            'X-CSRF-TOKEN': _csrf_token,
            '_token': _csrf_token
        }
        jwt_headers = {
            'Referer': f"https://{host}/home",
            'X-CSRF-TOKEN': _csrf_token
        }
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: Attempting to get JWT token from: https://{host}/security/jwt")
            print(f"DEBUG: JWT data: {jwt_data}")
            print(f"DEBUG: JWT headers: {jwt_headers}")
        jwt_response = _session.post(
            f"https://{host}/security/jwt",
            data=jwt_data,
            headers=jwt_headers
        )
        
        if not jwt_response.ok:
            print(f"ERROR: Failed to get JWT token: {jwt_response.status_code}")
            if DEBUG_LEVEL >= 2:
                print(f"DEBUG: JWT response content: {jwt_response.text[:500]}...")
            return False
        if DEBUG_LEVEL >= 2:
            print(f"DEBUG: JWT response OK. Status: {jwt_response.status_code}")
            print(f"DEBUG: JWT response headers: {jwt_response.headers}")
            print(f"DEBUG: JWT response content preview: {jwt_response.text[:500]}...")
            
        return True
            
    except Exception as e:
        print(f"ERROR: Error initializing session: {str(e)}")
        return False


def get_direct_json(endpoint: str, retry_count=3, retry_delay=5):
    """Get JSON data directly from Sonar instance instead of through API"""
    global _session
    
    try:
        # Initialize session if needed
        if not init_session():
            return None
            
        # Access the endpoint using existing session
        url = f"https://{host}/{endpoint}"
        response = _session.get(url)
        
        if response.ok:
            # Check if response has content
            if not response.text.strip():
                print(f"Empty response from {url}")
                if retry_count > 0:
                    print(f"Server may be overloaded. Waiting {retry_delay} seconds before retry...")
                    time.sleep(retry_delay)
                    return get_direct_json(endpoint, retry_count - 1, retry_delay)
                return None
                
            # Check if response looks like JSON
            content_type = response.headers.get('content-type', '').lower()
            if 'json' not in content_type and not response.text.strip().startswith('{'):
                print(f"Non-JSON response from {url}: {content_type}")
                print(f"Response preview: {response.text[:200]}...")
                if retry_count > 0:
                    print(f"Server may be overloaded (non-JSON response). Waiting {retry_delay} seconds before retry...")
                    time.sleep(retry_delay)
                    # Close session and clear token for fresh retry
                    if _session:
                        _session.close()
                    _session = None
                    return get_direct_json(endpoint, retry_count - 1, retry_delay)
                return None
                
            try:
                return response.json()
            except json.JSONDecodeError as je:
                print(f"JSON decode error for {url}: {str(je)}")
                print(f"Response content: {response.text[:500]}...")
                if retry_count > 0:
                    print(f"Server may be overloaded (JSON decode error). Waiting {retry_delay} seconds before retry...")
                    time.sleep(retry_delay)
                    # Close session and clear token for fresh retry
                    if _session:
                        _session.close()
                    _session = None
                    return get_direct_json(endpoint, retry_count - 1, retry_delay)
                return None
        else:
            print(f"Error accessing {url}: {response.status_code}")
            print(f"Response: {response.text[:200]}...")
            if retry_count > 0:
                print(f"Server error {response.status_code}. Waiting {retry_delay} seconds before retry...")
                time.sleep(retry_delay)
                # Close session and clear token
                if _session:
                    _session.close()
                _session = None
                # Retry the request
                return get_direct_json(endpoint, retry_count - 1, retry_delay)
            return None
            
    except Exception as e:
        print(f"Error getting direct JSON from {endpoint}: {str(e)}")
        if retry_count > 0:
            print(f"Exception occurred. Waiting {retry_delay} seconds before retry...")
            time.sleep(retry_delay)
            # Close session and clear token
            if _session:
                _session.close()
            _session = None
            # Retry the request
            return get_direct_json(endpoint, retry_count - 1, retry_delay)
        return None


def get_dhcp_server_config(server_id: int, retry_count=1):
    """Scrape DHCP server edit page to get detailed configuration including port and SSL settings"""
    global _session
    
    try:
        # Initialize session if needed
        if not init_session():
            return None
            
        # Access the DHCP server edit page
        url = f"https://{host}/network/provisioning/dhcp_servers/{server_id}/edit"
        response = _session.get(url)
        
        if not response.ok:
            print(f"Error accessing DHCP server edit page {url}: {response.status_code}")
            if retry_count > 0:
                print("Closing session and retrying...")
                if _session:
                    _session.close()
                _session = None
                return get_dhcp_server_config(server_id, retry_count - 1)
            return None
            
        # Parse the HTML to extract configuration details
        soup = BeautifulSoup(response.text, 'html.parser')
        
        config = {
            'server_id': server_id,
            'name': None,
            'ip_address': None,
            'port': None,
            'ssl_enabled': None,
            'ssl_port': None,
            'username': None,
            'enabled': None,
            'type': None
        }
        
        # Extract form field values
        # Look for input fields by name attribute
        name_input = soup.find('input', {'name': 'name'})
        if name_input:
            config['name'] = name_input.get('value', '').strip()
            
        ip_input = soup.find('input', {'name': 'ip_address'})
        if ip_input:
            config['ip_address'] = ip_input.get('value', '').strip()
            
        port_input = soup.find('input', {'name': 'port'})
        if port_input:
            config['port'] = port_input.get('value', '').strip()
            
        ssl_port_input = soup.find('input', {'name': 'ssl_port'})
        if ssl_port_input:
            config['ssl_port'] = ssl_port_input.get('value', '').strip()
            
        username_input = soup.find('input', {'name': 'username'})
        if username_input:
            config['username'] = username_input.get('value', '').strip()
            
        # Check for SSL enabled via radio buttons (name="api")
        ssl_radio = soup.find('input', {'name': 'api', 'value': 'api-ssl'})
        if ssl_radio:
            config['ssl_enabled'] = ssl_radio.has_attr('checked')
        else:
            # Fallback: check if non-SSL radio is selected
            non_ssl_radio = soup.find('input', {'name': 'api', 'value': 'api'})
            if non_ssl_radio:
                config['ssl_enabled'] = not non_ssl_radio.has_attr('checked')
            
        # Check for enabled checkbox
        enabled_checkbox = soup.find('input', {'name': 'enabled'})
        if enabled_checkbox:
            config['enabled'] = enabled_checkbox.has_attr('checked')
            
        # Look for type select dropdown
        type_select = soup.find('select', {'name': 'type'})
        if type_select:
            selected_option = type_select.find('option', {'selected': True})
            if selected_option:
                config['type'] = selected_option.get('value', '').strip()
        
        # Also try to extract from any data attributes or JavaScript
        # Look for any script tags that might contain configuration data
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and 'dhcp' in script.string.lower():
                # Try to extract any JSON-like data from scripts
                script_content = script.string
                # This is a basic approach - might need refinement based on actual page structure
                if 'port' in script_content.lower():
                    # Could parse JavaScript variables here if needed
                    pass
        
        print(f"DEBUG: Extracted DHCP server config for ID {server_id}: {config}")
        return config
        
    except Exception as e:
        print(f"Error scraping DHCP server config for ID {server_id}: {str(e)}")
        if retry_count > 0:
            print("Closing session and retrying...")
            if _session:
                _session.close()
            _session = None
            return get_dhcp_server_config(server_id, retry_count - 1)
        return None


def get_inline_device_config(device_id: int, retry_count=1):
    """Scrape inline device edit page to get detailed configuration including port and SSL settings"""
    global _session
    
    try:
        # Initialize session if needed
        if not init_session():
            return None
            
        # Access the inline device edit page
        url = f"https://{host}/network/provisioning/inline_devices/{device_id}/edit"
        response = _session.get(url)
        
        if not response.ok:
            print(f"Error accessing inline device edit page {url}: {response.status_code}")
            if retry_count > 0:
                print("Closing session and retrying...")
                if _session:
                    _session.close()
                _session = None
                return get_inline_device_config(device_id, retry_count - 1)
            return None
            
        # Parse the HTML to extract configuration details
        soup = BeautifulSoup(response.text, 'html.parser')
        
        config = {
            'device_id': device_id,
            'name': None,
            'ip_address': None,
            'port': None,
            'ssl_enabled': None,
            'username': None,
            'enabled': None,
            'type': None
        }
        
        # Extract form field values
        # Look for input fields by name attribute
        name_input = soup.find('input', {'name': 'name'})
        if name_input:
            config['name'] = name_input.get('value', '').strip()
            
        ip_input = soup.find('input', {'name': 'ip_address'})
        if ip_input:
            config['ip_address'] = ip_input.get('value', '').strip()
            
        port_input = soup.find('input', {'name': 'port'})
        if port_input:
            config['port'] = port_input.get('value', '').strip()
            
        username_input = soup.find('input', {'name': 'username'})
        if username_input:
            config['username'] = username_input.get('value', '').strip()
            
        # Check for SSL enabled via radio buttons (name="api")
        ssl_radio = soup.find('input', {'name': 'api', 'value': 'api-ssl'})
        if ssl_radio:
            config['ssl_enabled'] = ssl_radio.has_attr('checked')
        else:
            # Fallback: check if non-SSL radio is selected
            non_ssl_radio = soup.find('input', {'name': 'api', 'value': 'api'})
            if non_ssl_radio:
                config['ssl_enabled'] = not non_ssl_radio.has_attr('checked')
            
        # Check for enabled checkbox
        enabled_checkbox = soup.find('input', {'name': 'enabled'})
        if enabled_checkbox:
            config['enabled'] = enabled_checkbox.has_attr('checked')
            
        # Look for type select dropdown
        type_select = soup.find('select', {'name': 'type'})
        if type_select:
            selected_option = type_select.find('option', {'selected': True})
            if selected_option:
                config['type'] = selected_option.get('value', '').strip()
        
        print(f"DEBUG: Extracted inline device config for ID {device_id}: {config}")
        return config
        
    except Exception as e:
        print(f"Error scraping inline device config for ID {device_id}: {str(e)}")
        if retry_count > 0:
            print("Closing session and retrying...")
            if _session:
                _session.close()
            _session = None
            return get_inline_device_config(device_id, retry_count - 1)
        return None
