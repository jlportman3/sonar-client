# Data Endpoints

## Email categories (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/email_categories`
- **Description**: Get a list of email categories. These are used when setting email category preferences on contacts. This returns an array of objects.
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        {
          "id": 2,
          "name": "Financial"
        },
        {
          "id": 3,
          "name": "General"
        },
        {
          "id": 4,
          "name": "Service Related"
        },
        {
          "id": 5,
          "name": "Outage Notifications"
        }
      ]
    }
    ```

## Get Sonar version (GET)
- **Version**: 0.3.2
- **Endpoint**: `https://example.sonar.software/api/v1/_data/version`
- **Description**: Get the version of this Sonar instance.
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "version": "1.2.38"
      }
    }
    ```

## Supported counties (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/counties/:subdivision`
- **Description**: Get a list of counties for a US state. These are mainly used when configuring geotaxes.
- **Parameters**:
    - `subdivision` (String, required): A US subdivision string obtained from `/_data/subdivisions/US`
- **Success Response (200 OK)**:
    ```json
    {
      "data": [
        "Adams Co.",
        "Ashland Co.",
        "Barron Co.",
        "Bayfield Co.",
        "Brown Co.",
        "Buffalo Co.",
        "Burnett Co.",
        "Calumet Co.",
        "Chippewa Co.",
        "Clark Co.",
        "Columbia Co.",
        "Crawford Co.",
        "Dane Co.",
        "Dodge Co.",
        "Door Co.",
        "Douglas Co.",
        "Dunn Co.",
        "Eau Claire Co.",
        "Florence Co.",
        "Fond du Lac Co.",
        "Forest Co.",
        "Grant Co.",
        "Green Co.",
        "Green Lake Co.",
        "Iowa Co.",
        "Iron Co.",
        "Jackson Co.",
        "Jefferson Co.",
        "Juneau Co.",
        "Kenosha Co.",
        "Kewaunee Co.",
        "La Crosse Co.",
        "Lafayette Co.",
        "Langlade Co.",
        "Lincoln Co.",
        "Manitowoc Co.",
        "Marathon Co.",
        "Marinette Co.",
        "Marquette Co.",
        "Menominee Co.",
        "Milwaukee Co.",
        "Monroe Co.",
        "Oconto Co.",
        "Oneida Co.",
        "Outagamie Co.",
        "Ozaukee Co.",
        "Pepin Co.",
        "Pierce Co.",
        "Polk Co.",
        "Portage Co.",
        "Price Co.",
        "Racine Co.",
        "Richland Co.",
        "Rock Co.",
        "Rusk Co.",
        "St. Croix Co.",
        "Sauk Co.",
        "Sawyer Co.",
        "Shawano Co.",
        "Sheboygan Co.",
        "Taylor Co.",
        "Trempealeau Co.",
        "Vernon Co.",
        "Vilas Co.",
        "Walworth Co.",
        "Washburn Co.",
        "Washington Co.",
        "Waukesha Co.",
        "Waupaca Co.",
        "Waushara Co.",
        "Winnebago Co.",
        "Wood Co."
      ]
    }
    ```

## Supported countries (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/countries`
- **Description**: Get a list of supported countries. The object property is the correct value to use when setting a country on an entity. The value is the name of the country.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "US": "United States",
           "CA": "Canada",
           "AF": "Afghanistan",
           "AL": "Albania",
           "DZ": "Algeria",
           "AS": "American Samoa"
           //etc etc
       }
    }
    ```

## Supported locales (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/locales`
- **Description**: Get a list of supported locales.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "en": "English (US)",
           "es": "Español",
           "fr": "Français"
           }
       }
    }
    ```

## Supported subdivisions (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/subdivisions/:country`
- **Description**: Get a list of supported subdivisions. A subdivision is a geographical area within a country - for example, subdivisions in the USA are states, in Canada they are provinces. The :country parameter should be a country code returned from `/_data/countries`.
- **Parameters**:
    - `country` (String, required): A two character country code obtained from `/_data/countries`
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "Alabama": "Alabama",
        "Alaska": "Alaska",
        "American Samoa": "American Samoa",
        "Arizona": "Arizona",
        "Arkansas": "Arkansas",
        "California": "California",
        "Colorado": "Colorado",
        "Connecticut": "Connecticut",
        "Delaware": "Delaware",
        "District of Columbia": "District of Columbia",
        "Florida": "Florida",
        "Georgia": "Georgia",
        "Guam": "Guam",
        "Hawaii": "Hawaii",
        "Idaho": "Idaho",
        "Illinois": "Illinois",
        "Indiana": "Indiana",
        "Iowa": "Iowa",
        "Kansas": "Kansas",
        "Kentucky": "Kentucky",
        "Louisiana": "Louisiana",
        "Maine": "Maine",
        "Maryland": "Maryland",
        "Massachusetts": "Massachusetts",
        "Michigan": "Michigan",
        "Minnesota": "Minnesota",
        "Mississippi": "Mississippi",
        "Missouri": "Missouri",
        "Montana": "Montana",
        "Nebraska": "Nebraska",
        "Nevada": "Nevada",
        "New Hampshire": "New Hampshire",
        "New Jersey": "New Jersey",
        "New Mexico": "New Mexico",
        "New York": "New York",
        "North Carolina": "North Carolina",
        "North Dakota": "North Dakota",
        "Northern Mariana Islands": "Northern Mariana Islands",
        "Ohio": "Ohio",
        "Oklahoma": "Oklahoma",
        "Oregon": "Oregon",
        "Pennsylvania": "Pennsylvania",
        "Puerto Rico": "Puerto Rico",
        "Rhode Island": "Rhode Island",
        "South Carolina": "South Carolina",
        "South Dakota": "South Dakota",
        "Tennessee": "Tennessee",
        "Texas": "Texas",
        "United States Minor Outlying Islands": "United States Minor Outlying Islands",
        "Utah": "Utah",
        "Vermont": "Vermont",
        "Virgin Islands, U.S.": "Virgin Islands, U.S.",
        "Virginia": "Virginia",
        "Washington": "Washington",
        "West Virginia": "West Virginia",
        "Wisconsin": "Wisconsin",
        "Wyoming": "Wyoming"
      }
    }
    ```

## Supported timezones (GET)
- **Version**: 0.2.0
- **Endpoint**: `https://example.sonar.software/api/v1/_data/timezones`
- **Description**: Get a list of supported timezones. The object property is the correct value to use when setting a timezone. The value is the translated string representing the timezone in the locale of the application.
- **Success Response (200 OK)**:
    ```json
    {
        "data": {
           "Africa/Abidjan": "Africa/Abidjan",
           "Africa/Accra": "Africa/Accra",
           "Africa/Addis_Ababa": "Africa/Addis_Ababa",
           "Africa/Algiers": "Africa/Algiers",
           "Africa/Asmara": "Africa/Asmara",
           "Africa/Bamako": "Africa/Bamako",
           "Africa/Bangui": "Africa/Bangui",
           "Africa/Banjul": "Africa/Banjul",
           "Africa/Bissau": "Africa/Bissau",
           "Africa/Blantyre": "Africa/Blantyre",
           "Africa/Brazzaville": "Africa/Brazzaville"
           //etc etc
       }
    }
    ```

## Validate an address (POST)
- **Version**: 0.2.11
- **Endpoint**: `https://example.sonar.software/api/v1/_data/validate_address`
- **Description**: Validate an address for proper entry into Sonar. All addresses that you plan to enter should be run through this function.
- **Parameters**:
    - `line1` (String, required): The first address line (e.g. 123 Main St)
    - `city` (String, required): The city (e.g. London)
    - `state` (String, required): The state/province/subdivision (e.g. Texas)
    - `country` (String, required): A 2 character ISO country code (e.g. US, GB, FR, DE)
- **Success Response (200 OK)**:
    ```json
    {
      "data": {
        "line1": "615 N 6th St",
        "city": "Sheboygan",
        "state": "WI",
        "county": "Sheboygan Co.",
        "country": "US",
        "zip": "53081",
        "latitude": 43.750915527344,
        "longitude": -87.708717346191
      }
    }
    ```
- **Error Response (422 Unprocessable Entity)**:
    ```json
    {
        "error": {
            "message": "The address could not be validated.",
            "status_code": 422
        }
    }
    ```
```
