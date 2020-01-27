# README for veracode-api_clients

## Overview

-   Simple project with bash and python scripts calling the Veracode XML and REST APIs
-   Dockerfile included to ensure proper execution environment
-   Bash scripts using the XML API use XML parsing performed via xsltproc and produces CSV outputs.

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
 ./DynamicAnalysis.py -h
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
