# Search Endpoints

## Search for specific entities (GET)
Version: 1.0.4

Endpoint: ``

Description: The search endpoint supports a number of complex operations, and can be used to search for data within your Sonar instance. The format of data returned from this endpoint for each entity is not fully documented here, and may be subject to change - do not rely on the data format of this endpoint being consistent across versions! All data from this endpoint is paginated and limited by size.
#### Request Example
```json
{
  "entity": "example",
  "size": 1,
  "page": 1,
  "group_by": [],
  "return_all_ids": true,
  "search": "value",
  "fields": "value",
  "parse_nulls_fields": [],
  "quantity_based_match": [],
  "quantity_based_exists": "value",
  "not_fields": [],
  "date_limits": []
}
```

```
Generally speaking, if you want to implement this data into an external system, you should use this endpoint to search for the particular ID you need, and then perform a GET to the appropriate endpoint to get the consistently formatted data. However, the data format returned here can be useful if you're building some kind of search display page.

There are a number of parameters that can be passed in here to search for data in very specific ways. Each parameter can be used in tandem with other parameters to return very precise results.

Every result will contain a datetime property, which is the date and time in system timezone that the entity was created. All fields that contain a date and time will be returned in the system timezone, formatted into the selected datetime format. However, there will always be an unformatted field in the _$FIELDNAME_unformatted property (e.g. _datetime_unformatted) as an ISO8601 string.

Please see the examples below for more details.

https://example.sonar.software/api/v1/search/:entity/
Simple search
Search by field
Complex search with multiple parameters
{
	"size": 100,
	"page": 1,
	"search": {
		"search": "Activ" //Find anything matching the partial string 'Activ'
	}
}
Parameter
Field	Type	Description
entity	String
A valid entity to search for. See the other API endpoints to determine the proper naming convention here. For example, to search accounts, enter accounts. To search invoices, enter invoices. To search network sites, enter network_sites.

size	Number
The number of entries to return

page	Number
The page of results to return

group_byoptional	Array
An array of field names to group by. This will return a count of all results, grouped by that field name, in addition to the normal results.

return_all_idsoptional	Boolean
If this is set to true, then the search results will return all entity IDs that match your parameters, ignoring all pagination. For example, if there are 10,000 results, and your size parameter is 100, the results would only contain 100 entries at a time, but the results will also contain a all_ids property that contains a list of all 10,000 matching entity IDs. Use this parameter with caution!

Default value: false

searchoptional	Object
An object containing a list of search parameters. All parameters below this line must be contained within the search object.. This object may also contain a search property, which is a simple string to search all indexed fields for. This can match on partial strings.

fieldsoptional	Object
An object where the value is the data you wish to search for, and the property is the name of the field. The value must be a string. This will work on exact matches on full words only - e.g. 'Simon' will match 'Simon Westlake' but not 'Simonis'. If you want to search for partial matches, use the search property within the master search object (see example for details.)

parse_nulls_fieldsoptional	Array
An array containing a list of field names. In the fields parameter above, any value entered as null or an empty string is silently discarded. If you explicitly name a field in this parameter, then searching for an empty string or null in the fields parameter will explicitly return results where that field is null or an empty string.

quantity_based_matchoptional	Array
An array of objects, each of which has a fields parameter, which is formatted in the same manner as the fields parameter described above. This object should also contain a minimum_should_match property, which is an integer. This defines how many of the search terms you have described in this property must match. Each object will be independently evaluated.

quantity_based_existsoptional	Object
An object where the fields property is an array of fields that must exist in the result (e.g. are not null or an empty string.) This object should also contain a minimum_should_exist property, which is an integer. This defines how many of the search terms you have described in this property must exist.

not_fieldsoptional	Array
An array formatted identically to the fields parameter described above. This contains a list of fields and values that must not match in the result.

date_limitsoptional	Array
You can use this to limit results to items within a certain date range. This can only be used on fields that are represented as a date field. Do not reference fields here with the format _fieldname_unformatted, where _fieldname is a fieldname. Submit an object with three parameters - 'field', which is the field name to filter on, 'from', which is the start date/time, and 'to', which is the end date/time. These dates/times should be in the system timezone. At least one of 'from' and 'to' must be present for this filter to be applied. Bear in mind that most date fields that do not have the _unformatted suffix are represented in the system timezone.

Success-Response:
{
    "data": {
        "results": {
            "0": {
                "name": "Activation Testing",
                "account_status_id": 2,
                "account_type_id": 1,
                "tax_exempt": null,
                "activation_date": "Dec 12, 2016 08:09:47",
                "next_bill_date": "Jan 12, 2017",
                "last_billed_invoice_id": null,
                "master_account_id": null,
                "delinquent": false,
                "delinquency_date": null,
                "datetime": "Dec 12, 2016 14:09:00",
                "id": 2,
                "addresses": [
                    {
                        "zip": "27000",
                        "country": "TR",
                        "address_type": "physical",
                        "city": "Test",
                        "latitude": 37.26306,
                        "county": null,
                        "address_type_id": 1,
                        "datetime": "2016-12-12T20:09:00+0000",
                        "state": "Gaziantep",
                        "id": 4,
                        "line2": "",
                        "line1": "Unnamed Road",
                        "longitude": 37.26306
                    }
                ],
                "_activation_date_unformatted": "2016-12-12T14:09:47+0000",
                "_next_bill_date_unformatted": "2017-01-12",
                "_datetime_unformatted": "2016-12-12T20:09:00+0000",
                "_uid": "accounts_2"
            },
            "aggregations": []
        },
        "paginator": {
            "current_page": 1,
            "limit": 100,
            "total_pages": 1,
            "total_count": 1
        }
    }
}
Services
```
