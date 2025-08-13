# Mapping Endpoints

## Get GeoJSON data (GET)
- **Version**: 0.7.0
- **Endpoint**: `https://example.sonar.software/api/v1/mapping/geojson/:type`
- **Description**: Get GeoJSON for specific data inside Sonar. This can be used to display your geographical data on an external map. This data is cached, and only updates once every minute.
- **Parameters**:
    - `type` (String, required): The type of data to get. (`"accounts"`, `"network_sites"`, `"inventory_locations"`, `"vehicles"`)
- **Success Response (200 OK)**:
    ```json
    {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                -80.33397,
                39.96938
              ]
            },
            "properties": {
              "id": 1,
              "name": "Some Test Account",
              "account_type": "Residential",
              "account_status": "Active",
              "status_color": "#3498db"
            }
          },
          {
            "type": "feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                -106.53,
                34.591
              ]
            },
            "properties": {
              "id": 2,
              "name": "Prof. Luna O'Hara V",
              "account_type": "Commercial",
              "account_status": "Lead",
              "status_color": "#9b59b6"
            }
          }
        ]
    }
    ```

## Get a mapping of network sites, inventory items, and subscriber IPs (GET)
- **Version**: 1.4.1
- **Endpoint**: `https://example.sonar.software/api/v1/network/mapping`
- **Description**: Retrieve a mapping of network data, pulled using the Sonar poller. This endpoint is explicitly in place to enable integration with external systems. The data is keyed by network site ID and inventory item ID respectively, to make integration with external systems easier.
- **Success Response (201 Created)**:
    ```json
    {
        "data": {
            "1": {
                "id": 1,
                "name": "A-002 DeBolt",
                "inventory_items": {
                    "2531": {
                        "id": 2531,
                        "category": "Access Points",
                        "model_name": "PMP 450 3.6 Ghz AP",
                        "ip_address": "172.20.1.10",
                        "ip_description": "A-002-36450AP-01",
                        "merged_description": "PMP 450 3.6 Ghz AP (172.20.1.10) - A-002-36450AP-01",
                        "subscriber_data": [],
                        "subscribers": {
                            "28": {
                                "name": "Tom & Alisa Burton",
                                "id": 28,
                                "ips": [
                                    "10.1.1.33/32"
                                ]
                            },
                            "35": {
                                "name": "Ellen Moore",
                                "id": 35,
                                "ips": [
                                    "10.1.1.89/32"
                                ]
                            },
                            "47": {
                                "name": "Jason Moody",
                                "id": 47,
                                "ips": [
                                    "10.1.1.57/32",
                                    "192.168.82.35/32"
                                ]
                            },
                            "49": {
                                "name": "828859 Alberta Ltd",
                                "id": 49,
                                "ips": [
                                    "10.1.1.50/32"
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
    ```
```
