# README for veracode-api_clients

## Overview

-   Simple project with bash and python scripts calling the Veracode XML and REST APIs
-   Python scripts use the [Veracode REST API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/TNCmFBcyE6F902_fr9Qz0g). The main one is [DynamicAnalysis.py](./restapi/DynamicAnalysis.py) that allows the use of new Veracode functionality that's not even covered by the Veracode Web UI (using crawl scripts) or the existing wrappers used for CI/CD -- AFAIK, the [Veracode API Wrappers](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/Ib32zUpRx3cEwdR3duvUdg) still don't support the (newer) REST API.
-   Bash scripts use the [Veracode XML API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/SdntedDhtLGc_zmxQ339OA). XML response parsing uses xsltproc.
-   The included Dockerfile helps ensure the proper execution environment (getting all OS and python dependencies, configuring the python3 virtual environment...).

### CSV File used by Dynamic Analysis

When using the DynamicAnalysis.py script in this format:

```bash
$ cd restapi
$ ./DynamicAnalysis.py --action create --name SCAN_NAME --csvfile CSV_FILENAME
```

The CSV file can include these values:

| FIELD                  | DESCRIPTION                                                |
| ---------------------- | ---------------------------------------------------------- |
| url (\*)               | URL to be scanned                                          |
| app_uuid (\*\*)        | UUID of Veracode App to link the scan to                   |
| base_path              | Base path for files (see next "\_file" fields)             |
| login_script_file      | File name for the login script (under base_path)           |
| logout_script_file     | File name for the logout script (under base_path)          |
| crawl_script_file      | File name for the crawl script (under base_path)           |
| allowed_hosts_file     | File name for additional allowed hosts/URLs (one per line) |
| blacklist_file         | File name for blacklisted hosts/URLs (one per line)        |
| ism_endpoint_id (\*\*) | ID for specific ISM endpoint/server to use                 |
| ism_gateway_id (\*\*)  | ID for ISM gateway                                         |

-   (\*) Mandatory field
-   (\*\*) To obtain those IDs, you can use `DynamicAnalysis.py --action export --name NAME`

See this [sample CSV file](sample_data/dynscan-dvna.csv) for an example.

## Example Usage

```bash

### Build Docker image
docker build -t veracode-api-clients .

### Run Docker image
docker run -it --rm --mount type=bind,source="$PWD",target=/app --name veracode-api-clients veracode-api-clients

### At first run:
$ ./setup.sh
$ cp .env.TEMPLATE .env
$ vi .env
$ . ./.env
$ mkdir $HOME/.veracode/
$ vi $HOME/.veracode/credentials
[default]
veracode_api_key_id = <YOUR_API_KEY_ID>
veracode_api_key_secret = <YOUR_API_KEY_SECRET>

### Run Dynamic Analysis Scan
$ vi data/dynscan.csv
url,app_uuid,base_path,login_script_file,logout_script_file,crawl_script_file,allowed_hosts_file,blacklist_file,ism_endpoint_id,ism_gateway_id
http://dvna:9090/learn/vulnerability/a1_injection,,../sample_data/,dvna-login.side,,dvna-A1-Injection.side,dvna-allowed-hosts-a1.txt,dvna-blacklist-a1.txt,,
http://dvna:9090/learn/vulnerability/a3_sensitive_data,,../sample_data/,dvna-login.side,,dvna-A3-SensitiveDataExposure.side,dvna-allowed-hosts-a3.txt,dvna-blacklist-a3.txt,,

$ cd restapi

$ ./DynamicAnalysis.py -h
usage: DynamicAnalysis.py [-h] [--action SCAN_ACTION] [--name NAME]
                          [--start START_DATE] [--team TEAMID]
                          [--csvfile CSV_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  --action SCAN_ACTION  Scan Action := [create, export]
  --name NAME           Scan Name.
  --start START_DATE    Start Date for scan.
  --team TEAMID         Team ID. Default: none.
  --csvfile CSV_FILENAME
                        CSV file name.

$ ./DynamicAnalysis.py --action create --name "App X Authenticated Scan" --csvfile ../data/dynscan.csv
[...]
2020/01/28-03:05:47 DEBUG: Successful response: <Response [201]>

$ ./DynamicAnalysis.py --name "App X Authenticated Scan" --action export
2020/01/28-03:09:41 INFO: Exporting scan spec data for scan named 'App X Authenticated Scan'
2020/01/28-03:09:42 INFO: Saved Veracode scan spec for 'App X Authenticated Scan' to /app/data/ScanSpec.json
2020/01/28-03:09:43 INFO: Saved Veracode scan details for 'App X Authenticated Scan' to /app/data/ScanDetails.json

### Get all app profile data
$ ./Applications.py
2020/01/27-05:54:02 INFO: Got page 1 of 6
2020/01/27-05:54:06 INFO: Got page 2 of 6
2020/01/27-05:54:09 INFO: Got page 3 of 6
2020/01/27-05:54:21 INFO: Got page 4 of 6
2020/01/27-05:54:26 INFO: Got page 5 of 6
2020/01/27-05:54:30 INFO: Got page 6 of 6
2020/01/27-05:54:30 INFO: Saved 568 Veracode App Profiles to /app/data/Apps.json
```
