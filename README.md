# README for veracode-api-clients

<!-- TOC -->

-   [README for veracode-api-clients](#readme-for-veracode-api-clients)
-   [Overview](#overview)
-   [Initial Setup](#initial-setup)
    -   [Using Docker](#using-docker)
    -   [Configuring Veracode credentials](#configuring-veracode-credentials)
-   [Python Scripts](#python-scripts)
    -   [Using DynamicAnalysis.py](#using-dynamicanalysispy)
        -   [General Usage](#general-usage)
        -   [Creating Dynamic Analysis scans with form login and crawl scripts](#creating-dynamic-analysis-scans-with-form-login-and-crawl-scripts)
            -   [CSV file format](#csv-file-format)
        -   [Exporting Scan Information](#exporting-scan-information)
        -   [Updating Crawl Scripts](#updating-crawl-scripts)
    -   [Using Applications.py](#using-applicationspy)
        -   [Exporting all app profile data](#exporting-all-app-profile-data)
-   [Bash Scripts](#bash-scripts)
    -   [Get App profiles with getApps.sh](#get-app-profiles-with-getappssh)
    -   [Other scripts](#other-scripts)

<!-- /TOC -->

# Overview

-   Simple project with bash and python scripts using the Veracode XML and REST APIs
-   Python scripts use the [Veracode REST API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/TNCmFBcyE6F902_fr9Qz0g). The main one is [DynamicAnalysis.py](./restapi/DynamicAnalysis.py) that allows the use of new Veracode functionality may not even be covered by the Veracode Web UI (e.g. CSV import of URLs with form-based auth) or the existing wrappers used for CI/CD -- AFAIK, the [Veracode API Wrappers](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/Ib32zUpRx3cEwdR3duvUdg) still don't support the (newer) REST API.
-   Bash scripts use the [Veracode XML API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/SdntedDhtLGc_zmxQ339OA). XML response parsing uses xsltproc.
-   The included Dockerfile helps ensure the proper execution environment (getting all OS and python dependencies, configuring the python3 virtual environment...).

# Initial Setup

## Using Docker

NOTE: Using Docker is optional but using it may prevent you from dealing with dependency issues.

```bash
### Build Docker image
$ cd veracode-api-clients
$ docker build -t veracode-api-clients .

### Run Docker image
$ docker run -it --rm --mount type=bind,source="$PWD",target=/app --name veracode-api-clients veracode-api-clients

### At first run:
$ ./setup.sh
```

## Configuring Veracode credentials

When using the REST API, you need to provide your Veracode API credentials:

```bash
$ mkdir $HOME/.veracode/
$ vi $HOME/.veracode/credentials
[default]
veracode_api_key_id = <YOUR_API_KEY_ID>
veracode_api_key_secret = <YOUR_API_KEY_SECRET>

```

# Python Scripts

## Using DynamicAnalysis.py

### General Usage

```bash
$ cd restapi

$ ./DynamicAnalysis.py -h

usage: DynamicAnalysis.py [-h] --action {create,export,update_crawl_script}
                          --name NAME [--start START_DATE] [--team TEAMID]
                          [--filename FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  --action {create,export,update_crawl_script}
                        Scan Action.
  --name NAME           Scan Name. Example: "Scan MyApp with form auth and crawl script".
  --start START_DATE    Start Date for scan. Applicable when --action=create.
                        Example: "2020-03-03T02:00+00:00". Default: (not scheduled).
  --team TEAMID         Team ID. Applicable when --action=create. If empty,
                        only Security Leads will have visibility.
  --filename FILENAME   Path to file. CSV file when --action=create. Path to
                        Selenium script when --action=update_crawl_script.
```

### Creating Dynamic Analysis scans with form login and crawl scripts

Example run to create a new Dynamic Analysis scan, as specified in a CSV file.

```bash
$ ./DynamicAnalysis.py --action=create \
    --name="Scan MyApp with login and crawl scripts" \
    --start="2020-03-03T02:00+00:00" \
    --team="132892" \
    --filename="../data/dynscan-dvna.csv"
```

#### CSV file format

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
-   (\*\*) To obtain those IDs, you can use `DynamicAnalysis.py --action=export --name=<EXISTING_SCAN_NAME>` and view the resulting JSON file content.

See this [sample CSV file](sample_data/dynscan-dvna.csv) for an example.

```bash
$ vi data/dynscan.csv
url,app_uuid,base_path,login_script_file,logout_script_file,crawl_script_file,allowed_hosts_file,blacklist_file,ism_endpoint_id,ism_gateway_id
http://dvna:9090/learn/vulnerability/a1_injection,,../data/,dvna-login.side,,dvna-A1-Injection.side,dvna-allowed-hosts-a1.txt,dvna-blacklist-a1.txt,,
http://dvna:9090/learn/vulnerability/a3_sensitive_data,,../data/,dvna-login.side,,dvna-A3-SensitiveDataExposure.side,dvna-allowed-hosts-a3.txt,dvna-blacklist-a3.txt,,
```

### Exporting Scan Information

Example run:

```bash
$ ./DynamicAnalysis.py --action=export  \
    --name="Scan MyApp with login and crawl scripts"
```

### Updating Crawl Scripts

Example run to update the crawl script for an existing scan:

```bash
$ ./DynamicAnalysis.py --action=update_crawl_script \
    --name="Scan MyApp with login and crawl scripts" \
    --filename="../data/dvna-crawl.side"
```

## Using Applications.py

### Exporting all app profile data

At this moment, this script only supports the export of all Applications to JSON.

```
$ ./Applications.py
2020/01/27-05:54:02 INFO: Got page 1 of 6
2020/01/27-05:54:06 INFO: Got page 2 of 6
2020/01/27-05:54:09 INFO: Got page 3 of 6
2020/01/27-05:54:21 INFO: Got page 4 of 6
2020/01/27-05:54:26 INFO: Got page 5 of 6
2020/01/27-05:54:30 INFO: Got page 6 of 6
2020/01/27-05:54:30 INFO: Saved 568 Veracode App Profiles to /app/data/Apps.json
```

# Bash Scripts

## Get App profiles with getApps.sh

Example run:

```bash
$ ./getApps.sh

-- Invoking Veracode API to get /app/data/Apps.xml

-- Converting XML file to /app/data/Apps.csv

-- Printing first few lines of /app/data/Apps.csv
AppName,AppId,BU,Owner,Product,LOB,DocUrl,CodeRepoUrl,ArtifactsRepoUrl,CodeReviewToolUrl,LastBuildVersion,LastBuildId,LastSubmitter,PolicyName,PolicyComplianceStatus,GracePeriodExpired
[...]
```

## Other scripts

| SCRIPT NAME              | PURPOSE                                                                       |
| ------------------------ | ----------------------------------------------------------------------------- |
| addVeracodeUser.sh       | Create a Veracode SSO user and enrich the profile with Active Directory data. |
| getAppBuilds.sh          | Get list of Veracode app builds                                               |
| getAppList.sh            | Get list of Veracode apps and save them to CSV file                           |
| getApps.sh               | Get list of Veracode apps and all their important metadata and stats          |
| getDetailedReports.sh    | Get detailed report data for all Veracode builds                              |
| getDetailedReportsPDF.sh | Get detailed report data for all Veracode builds in PDF                       |
| getSummaryReport.sh      | Get summary report data for all Veracode builds                               |
| getSummaryReportsPDF.sh  | Get PDF summary reports for all Veracode builds                               |
