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
            -   [Using exports as part of Pipeline/CI/CD jobs](#using-exports-as-part-of-pipelinecicd-jobs)
        -   [Creating a simple Crawl Script from a path list](#creating-a-simple-crawl-script-from-a-path-list)
        -   [Updating Crawl Scripts](#updating-crawl-scripts)
    -   [Triggering the immediate execution for an existing scan](#triggering-the-immediate-execution-for-an-existing-scan)
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

When using the REST API, you need to provide your Veracode API credentials by modifying the API KEY ID and secret....

```bash
$ mkdir $HOME/.veracode/
$ vi $HOME/.veracode/credentials
[default]
veracode_api_key_id = <YOUR_API_KEY_ID>
veracode_api_key_secret = <YOUR_API_KEY_SECRET>

$ chmod 600 $HOME/.veracode/credentials

$ cp .env.TEMPLATE .env

$ chmod 600 .env

$ vi .env
# Parameters that are normally static
export OUTPUT_DIR="$HOME/data"
export LOGDIR="$HOME/log"

# Active Directory Parameters
BASEDN="DC=example,DC=com"
LDAP_DN="CN=Smith\, John,OU=Employees,OU=Users,DC=example,DC=com"
export AD_HOST=addc01.example.com
export HOST="$AD_HOST"

# Veracode Parameters
export VERACODE_API_KEY_ID=<YOUR_VERACODE_KEY_ID>
export VERACODE_API_KEY_SECRET=<YOUR_VERACODE_KEY_SECRET>
```

# Python Scripts

## Using DynamicAnalysis.py

### General Usage

```bash
$ cd restapi

$ ./DynamicAnalysis.py -h
usage: DynamicAnalysis.py [-h] --action
                          {create_analysis,export_analysis,update_crawl_script,create_crawl_script,scan_now}
                          [--scan-name SCAN_NAME] [--start START_DATE]
                          [--team TEAMID] [--filename FILENAME]
                          [--output-filename OUTPUT_FILENAME]
                          [--base-url BASE_URL]

optional arguments:
  -h, --help            show this help message and exit
  --action {create_analysis,export_analysis,update_crawl_script,create_crawl_script,scan_now}
                        Script Action.
  --scan-name SCAN_NAME
                        Scan Name. Example: "Scan MyApp".
  --start START_DATE    Start Date for scan. Applicable when
                        --action=create_analysis. Example:
                        "2020-03-03T02:00+00:00". Default: (not scheduled).
  --team TEAMID         Team ID. Applicable when --action=create_analysis. If
                        empty, only Security Leads will have visibility.
  --filename FILENAME   Path to input file name. CSV file when
                        --action=create_analysis. Path to Selenium script when
                        --action=update_crawl_script. Path to input text file
                        (list of paths) for new_crawl_script.
  --output-filename OUTPUT_FILENAME
                        Path to output file name. Required for
                        --action=create_crawl_script (extension should be
                        ".side").
  --base-url BASE_URL   Base URL for crawl script. Required for
                        --action=create_crawl_script.
```

### Creating Dynamic Analysis scans with form login and crawl scripts

Example run to create a new Dynamic Analysis scan, as specified in a CSV file.

```bash
$ ./DynamicAnalysis.py --action create_analysis \
    --scan-name 'Scan DVNA, with login/crawl scripts' \
    --start 2020-03-03T02:00+00:00 \
    --team 132892 \
    --filename ../data/dynscan-dvna.csv

2020/02/06-22:35:35 INFO: Creating a new scan by sending a POST request to https://api.veracode.com/was/configservice/v1/analyses?run_verification=true
2020/02/06-22:35:37 INFO: Successful response: <Response [201]>
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
-   (\*\*) To obtain those IDs, you can use `DynamicAnalysis.py --action=export_analysis --name=<EXISTING_SCAN_NAME>` and view the resulting JSON file content.

See this [sample CSV file](sample_data/dynscan-dvna.csv) for an example.

```bash
$ vi data/dynscan.csv
url,app_uuid,base_path,login_script_file,logout_script_file,crawl_script_file,allowed_hosts_file,blacklist_file,ism_endpoint_id,ism_gateway_id
http://dvna:9090/learn,,../sample_data/,dvna-login.side,,dvna-crawl.side,dvna-allowed-hosts.txt,dvna-blacklist.txt,,
```

### Exporting Scan Information

Example run:

```bash
$ ./DynamicAnalysis.py --action=export_analysis --scan-name 'Scan DVNA, with login/crawl scripts'
2020/02/06-22:48:24 INFO: Exporting scan spec data for scan named 'Scan DVNA, with login/crawl scripts'
2020/02/06-22:48:24 INFO: Saved Veracode scan spec for 'Scan DVNA, with login/crawl scripts' to /app/data/WAS_CSAPI_Analysis_Summary.json
2020/02/06-22:48:24 INFO: Saved Veracode scan details for 'Scan DVNA, with login/crawl scripts' to /app/data/WAS_CSAPI_Scan_Details.json
2020/02/06-22:48:25 INFO: Saved Veracode analysis details for 'Scan DVNA, with login/crawl scripts' to /app/data/WAS_CSAPI_Analysis_Details.json
```

#### Using exports as part of Pipeline/CI/CD jobs

The export_analysis action can be used to check if a Dynamic Analysis scan passed or failed, with a simple severity count check...

**WARNING**: this mechanism currently doesn't support checks against a linked application's policy.

```bash
### Example of scan that passed with no Medium+ sev flaws:
$ ./DynamicAnalysis.py --action=export_analysis --scan-name="Mix_Status_Dynamic_Analysis_30_Jan_final" 2>scan.log

$ grep PASSED scan.log
2020/02/07-17:45:37 INFO: PASSED. (VeryHigh:0, High:0, Med:0, Low:0)


### Example of scan that failed with at least one Medium+ sev flaws:
$ ./DynamicAnalysis.py --action=export_analysis --scan-name="Identity Manager Dynamic Analysis" 2>scan.log

$ grep FAILED scan.log
2020/02/07-17:50:19 WARNING: FAILED. (VeryHigh:0, High:0, Med:6, Low:5)

### Using the sample looper script
#... when the results are not yet available:
$ ./LoopUntilScanResults.sh "Scan My App"
[02/07/20-19:26:37] Results not available:  "FINISHED_VERIFYING_RESULTS" (try 1 of 96)

#... when the results are available:
$ ./LoopUntilScanResults.sh "Scan MyApp"
2020/02/07-19:25:38 WARNING: FAILED. (VeryHigh:0, High:0, Med:6, Low:5)
STATUS: FAILED
```

### Creating a simple Crawl Script from a path list

```bash
$ vi ../data/dvna-path-list.txt
/learn/vulnerability/a1_injection
/learn/vulnerability/a2_broken_auth
/learn/vulnerability/a3_sensitive_data
/learn/vulnerability/a4_xxe
/learn/vulnerability/a5_broken_access_control
/learn/vulnerability/a6_sec_misconf
/learn/vulnerability/a7_xss
/learn/vulnerability/a8_ides
/learn/vulnerability/a9_vuln_component
/learn/vulnerability/a10_logging
/learn/vulnerability/ax_csrf
/learn/vulnerability/ax_redirect
/app/usersearch
/forgotpw
/app/admin/users
/app/bulkproducts
/app/admin
/app/calc
/app/products
/app/modifyproduct
/app/bulkproducts?legacy=true
/app/bulkproductslegacy
/app/redirect?url=/app/calc

$ ./DynamicAnalysis.py --action=create_crawl_script --filename=../data/dvna-path-list.txt --output-filename=../data/dvna-simple-crawl.side --base-url=http://dvna:9090/learn
```

### Updating Crawl Scripts

Example run to update the crawl script for an existing scan:

```bash
$ ./DynamicAnalysis.py --action=update_crawl_script --scan-name='Scan DVNA, with login/crawl scripts' --filename=../data/dvna-simple-crawl.side
2020/02/06-22:57:41 INFO: Updating crawl script for scan named 'Scan DVNA, with login/crawl scripts' from ../data/dvna-simple-crawl.side
2020/02/06-22:57:41 INFO: Exporting scan spec data for scan named 'Scan DVNA, with login/crawl scripts'
2020/02/06-22:57:42 INFO: Updating scan Scan DVNA, with login/crawl scripts by sending a PUT request to https://api.veracode.com/was/configservice/v1/scans/531c6da908fda93a19e0ece47e2cc776/configuration?runtime=false&method=PATCH
2020/02/06-22:57:42 INFO: Successful response: <Response [204]>
```

## Triggering the immediate execution for an existing scan

```bash
$ ./DynamicAnalysis.py --action=scan_now --scan-name='Scan for Veracode_Testing, with login/crawl scripts'
2020/02/06-21:39:01 INFO: Updating scan named 'Scan for Veracode_Testing, with login/crawl scripts' to scan ASAP
2020/02/06-21:39:01 INFO: Exporting scan spec data for scan named 'Scan for Veracode_Testing, with login/crawl scripts'
2020/02/06-21:39:02 INFO: Successful response: <Response [204]>
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
