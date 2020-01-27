# README for veracode-api_clients

## Overview

-   Simple project with bash and python scripts calling the Veracode XML and REST APIs
-   Python scripts use the [Veracode REST API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/TNCmFBcyE6F902_fr9Qz0g). The main one is [DynamicAnalysis.py](./restapi/DynamicAnalysis.py) that allows the use of new Veracode functionality that's not even covered by the Veracode Web UI (using crawl scripts) or the existing wrappers used for CI/CD -- AFAIK, the [Veracode API Wrappers](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/Ib32zUpRx3cEwdR3duvUdg) still doesn't support REST APIs.
-   Bash scripts use the [Veracode XML API](https://help.veracode.com/reader/LMv_dtSHyb7iIxAQznC~9w/SdntedDhtLGc_zmxQ339OA). XML response parsing uses xsltproc.
-   The included Dockerfile helps ensure the proper execution environment (getting all OS and python dependencies, configuring the python3 virtual environment...).

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
$ vi data/dynscan1.csv
url,http_and_https,directory_restriction_type,script_file
https://www.example.com/app/index.html,True,DIRECTORY_AND_SUBDIRECTORY,userlogin.side
https://www.example.com/admin/index.html,True,DIRECTORY_AND_SUBDIRECTORY,adminlogin.side

$ cd restapi

$ ./DynamicAnalysis.py -h
usage: DynamicAnalysis.py [-h] [--name NAME] [--start START_DATE]
                          [--team TEAMID] [--csvfile TEAMID]

optional arguments:
  -h, --help          show this help message and exit
  --name NAME         Scan Name.
  --start START_DATE  Start Date for scan.
  --team TEAMID       Team ID. Default: none.
  --csvfile TEAMID    CSV file name. Default: "../data/dynscan1.csv"

$ ./DynamicAnalysis.py

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
