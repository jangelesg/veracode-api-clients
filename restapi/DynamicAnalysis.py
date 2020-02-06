#!/usr/bin/env python3
#=================================================================================================================
# DynamicAnalysis.py: Python class that uses the Veracode Dynamic Analysis REST API. 
#                     Can be used as a Python module or as a command line.
#                     See README.md for example runs.
#
# COMMAND LINE USAGE: 
#  usage: DynamicAnalysis.py [-h] --action
#                            {create_analysis,export_analysis,update_crawl_script,create_crawl_script,scan_now}
#                            [--scan-name SCAN_NAME] [--start START_DATE]
#                            [--team TEAMID] [--filename FILENAME]
#                            [--output-filename OUTPUT_FILENAME]
#                            [--base-url BASE_URL]
#  
#  optional arguments:
#    -h, --help            show this help message and exit
#    --action {create_analysis,export_analysis,update_crawl_script,create_crawl_script,scan_now}
#                          Script Action.
#    --scan-name SCAN_NAME
#                          Scan Name. Example: "Scan MyApp".
#    --start START_DATE    Start Date for scan. Applicable when
#                          --action=create_analysis. Example:
#                          "2020-03-03T02:00+00:00". Default: (not scheduled).
#    --team TEAMID         Team ID. Applicable when --action=create_analysis. If
#                          empty, only Security Leads will have visibility.
#    --filename FILENAME   Path to input file name. CSV file when
#                          --action=create_analysis. Path to Selenium script when
#                          --action=update_crawl_script. Path to input text file
#                          (list of paths) for new_crawl_script.
#    --output-filename OUTPUT_FILENAME
#                          Path to output file name. Required for
#                          --action=create_crawl_script (extension should be
#                          ".side").
#    --base-url BASE_URL   Base URL for crawl script. Required for
#                          --action=create_crawl_script.
#=================================================================================================================
import os, sys, requests, json, logging, csv, argparse
import JsonExport
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
app_name="DynamicAnalysis"
data_dir=os.environ.get("HOME")+ "/data/"

#Uncomment only when debugging through Burp
#import urllib3
#urllib3.disable_warnings()
#verifyCert=False
verifyCert=True


### DynamicAnalysis class that uses the Veracode Dynamic Analysis REST API. 
class DynamicAnalysis:
    headers = {"User-Agent": "Veracode DynamicAnalysis REST API Client"}


    ### get_scan_details: Get scan details for a given scan_name (the 1st one if there's more than one match)
    def get_scan_details(self, scan_name, data, export=False):
        try:
            scan_details_url = data["_embedded"]["analyses"][0]["_links"]["scans"]["href"]
            log.debug("Sending request to %s", scan_details_url)
            response = requests.get(scan_details_url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, verify=verifyCert)

            if response.ok:
                if (export):
                    json_file_base = data_dir + "WAS_CSAPI_Scan_Details"
                    JsonExport.saveFormatted(response.json(), json_file_base)
                    log.info("Saved Veracode scan details for '%s' to %s.json", scan_name, json_file_base)
                return response.json()
            else:
                log.error("Request for scan details failed with %s code", response.text)
                prettyPrintObj(response.json())
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for scan details failed.")
            print(e)
            sys.exit(1)


    ### get_analysis_details: Get analysis details for a given analysis ID 
    def get_analysis_details(self, scan_name, data, export=False):
        try:
            analysis_details_url = data["_embedded"]["analyses"][0]["_links"]["self"]["href"]
            log.debug("Sending request to %s", analysis_details_url)
            response = requests.get(analysis_details_url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, verify=verifyCert)

            if response.ok:
                if (export):
                    json_file_base = data_dir + "WAS_CSAPI_Analysis_Details"
                    JsonExport.saveFormatted(response.json(), json_file_base)
                    log.info("Saved Veracode analysis details for '%s' to %s.json", scan_name, json_file_base)
                return response.json()
            else:
                log.error("Request for analysis details failed with %s code", response.text)
                prettyPrintObj(response.json())
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for analysis details failed.")
            print(e)
            sys.exit(1)


    ### get_analysis(): get analysis summary for a given scan name
    def get_analysis(self, scan_name, export=False):
        log.info("Exporting scan spec data for scan named '%s'", scan_name)
        api_base="https://api.veracode.com/was/configservice/v1/analyses"
        try:
            arg1 = "name=" + scan_name
            log.debug("Sending request to %s", api_base)
            response = requests.get(api_base+"?"+arg1, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, verify=verifyCert)
            data = response.json()
            if response.ok:
                if (export):
                    json_file_base = data_dir + "WAS_CSAPI_Analysis_Summary"
                    JsonExport.saveFormatted(data, json_file_base)
                    log.info("Saved Veracode scan spec for '%s' to %s.json", scan_name, json_file_base)
                scan_details = self.get_scan_details(scan_name, data, export)
                analysis_details = self.get_analysis_details(scan_name, data, export)
                return (data, scan_details, analysis_details)
            else:
                log.error("Request for scan spec failed with %s code", response.text)
                prettyPrintObj(response.json())
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for scan data failed.")
            print(e)
            sys.exit(1)


    ### build_scan_spec_from_csv(): Get form-auth scan spec from CSV file
    def build_scan_spec_from_csv(self, csv_filename):
        scans = []
        with open(csv_filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                scan = {}
                scan["scan_config_request"] = {}
                scan["scan_config_request"]["target_url"] = {}

                # Add URL
                if (row['url'] != ""):
                    scan["scan_config_request"]["target_url"]["url"] = row['url']

                ## Add ISM config
                if (row['ism_endpoint_id'] != ""):
                    scan["internal_scan_configuration"] = {}
                    scan["internal_scan_configuration"]["enabled"] = True
                    scan["internal_scan_configuration"]["endpoint_id"] = row['ism_endpoint_id']
                    scan["internal_scan_configuration"]["gateway_id"] = row['ism_gateway_id']

                # Add App UUID
                if (row['app_uuid'] != ""): 
                    scan["linked_platform_app_uuid"] = row['app_uuid']

                # Add Allowed Hosts
                if (row['allowed_hosts_file'] != ""):
                    scan["scan_config_request"]["allowed_hosts"] = {}
                    path = row['base_path'] + "/" + row['allowed_hosts_file']
                    allowed_hosts = []
                    with open(path) as fp:
                        for line in fp:
                            allowed_host = line.strip()
                            allowed_hosts.append({"url": allowed_host})
                    scan["scan_config_request"]["allowed_hosts"] = allowed_hosts
                    log.debug("Allowed hosts: %s", str(allowed_hosts))

                # Add Blacklist
                if (row['blacklist_file'] != ""):
                    scan["scan_config_request"]["scan_setting"] = {}
                    scan["scan_config_request"]["scan_setting"]["blacklist_configuration"] = {}
                    blacklist = []
                    path = row['base_path'] + "/" + row['blacklist_file']
                    with open(path) as fp:
                        for line in fp:
                            blacklist_entry = line.strip()
                            blacklist.append({"url": blacklist_entry})
                    scan["scan_config_request"]["scan_setting"]["blacklist_configuration"]["black_list"] = blacklist
                    log.debug("Blacklist: %s", str(blacklist))

                # Add Form Login script
                if (row['login_script_file'] != ""):
                    login_script_path = row['base_path'] + "/" + row['login_script_file']
                    log.debug("Reading login script data from %s", login_script_path)
                    f = open(login_script_path, "r")
                    login_script_data = f.read()
                    scan["scan_config_request"]["auth_configuration"] = \
                        { "authentications":{ \
                            "FORM":{ \
                                "authtype":"FORM", \
                                "login_script_data":{ \
                                    "script_body":login_script_data,\
                                    "script_type": "SELENIUM" \
                                } \
                            } \
                        }}

                    # Add Form Logout script
                    if (row['logout_script_file'] != ""):
                        logout_script_path = row['base_path'] + "/" + row['logout_script_file']
                        log.debug("Reading logout script data from %s", logout_script_path)
                        f = open(logout_script_path, "r")
                        logout_script_data = f.read()
                        scan["scan_config_request"]["auth_configuration"]["authentications"]["FORM"]["logout_script_data"] = \
                                    { \
                                        "script_body": logout_script_data, \
                                        "script_type": "SELENIUM" \
                                    }

                # Add Crawl script. Result not visible in Veracode UI but Veracode Support can confirm.
                if (row['crawl_script_file'] != ""):
                    crawl_script_path = row['base_path'] + "/" + row['crawl_script_file']
                    log.debug("Reading crawl script data from %s", crawl_script_path)
                    f = open(crawl_script_path, "r")
                    crawl_script_data = f.read()
                    scan["scan_config_request"]["crawl_configuration"] = \
                        {   "scripts": [ \
                            {   "crawl_script_data":{ \
                                    "script_body": crawl_script_data, \
                                    "script_type": "SELENIUM" \
                                }\
                            }], \
                            "disabled": False \
                        }  

                # App to scan spec (for all URLs)
                scans.append(scan)
        return scans


    ### create_scan(): Send request to create a Dynamic Analysis scan 
    def create_scan(self, scan_request_data):
        api_base="https://api.veracode.com/was/configservice/v1/analyses"

        try:
            param1 = "?run_verification=true"
            url= api_base + param1
            log.info("Creating a new scan by sending a POST request to %s", url)
            log.debug("POST Body: " + json.dumps(scan_request_data, sort_keys=True, indent=4))
            response = requests.post(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, json=scan_request_data, verify=verifyCert)
            if response.ok:
                log.info("Successful response: %s", str(response))
                return response
            else:
                log.error("Request to create scan failed with %s code: %s", response.status_code, response.text)
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for application list failed.")
            print(e)
            sys.exit(1)


    ### update_crawl_script(): Update a scan's crawl script
    def update_crawl_script(self, scan_name, crawl_script_filename):

        # Get Scan metadata and details
        log.info("Updating crawl script for scan named '%s' from %s", scan_name, crawl_script_filename)
        (scan_data, scan_details, analysis_details) = self.get_analysis(scan_name, False)
        log.debug("Scan Details: %s", scan_details)
        scan_id = scan_details["_embedded"]["scans"][0]["scan_id"]
        url = scan_details["_embedded"]["scans"][0]["_links"]["scan_config"]["href"]
        #log.debug("Analysis Details: %s", analysis_details)

        # Get crawl script data
        log.debug("Reading crawl script data from %s", crawl_script_filename)
        f = open(crawl_script_filename, "r")
        crawl_script_data = f.read()

        # Build JSON body to send
        log.debug("New crawl script data: %s", crawl_script_data)
        scan_config = {}
        scan_config["crawl_configuration"] = \
                        {   "scripts": [ \
                            {   "crawl_script_data":{ \
                                    "script_body": crawl_script_data, \
                                    "script_type": "SELENIUM" \
                                }\
                            }], \
                            "disabled": False \
                        }  

        # Send scan config update REST call 
        parm = "&method=PATCH" # using "&" because url already has a parameter
        url = url + parm
        log.info("Updating scan %s by sending a PUT request to %s", scan_name, url)
        log.debug("PUT Body: " + json.dumps(scan_config, sort_keys=True, indent=4))
        response = requests.put(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, json=scan_config, verify=verifyCert)
        if response.ok:
            log.info("Successful response: %s", str(response))
            return response
        else:
            log.error("Request to update crawl script failed with %s code: %s", response.status_code, response.text)
            sys.exit(1)



    ### scan_now(): Update a scan's schedule to start ASAP
    def scan_now(self, scan_name):

        # Get Scan metadata and the current schedule details
        log.info("Updating scan named '%s' to scan ASAP", scan_name)
        (scan_data, scan_details, analysis_details) = self.get_analysis(scan_name, False)
        scan_id = scan_details["_embedded"]["scans"][0]["scan_id"]
        current_schedule = analysis_details["schedule"]
        log.debug("Current Scan Schedule: %s", json.dumps(current_schedule))
        url = analysis_details["_links"]["self"]["href"]

        # Build schedule structure
        schedule_data = {"schedule": {"now": True, "duration": { "length": 3, "unit": "DAY" }}}
        log.debug("New schedule data: %s", schedule_data)

        # Send scan config update REST call 
        parm = "?method=PATCH"
        url = url + parm
        log.info("Updating scan by sending a PUT request to %s", url)
        log.debug("PUT Body: " + json.dumps(schedule_data, sort_keys=True, indent=4))
        response = requests.put(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, json=schedule_data, verify=verifyCert)
        if response.ok:
            log.info("Successful response: %s", str(response))
            return response
        else:
            log.error("Request to update scan schedule failed with %s code: %s", response.status_code, response.text)
            sys.exit(1)


    ### create_crawl_script(): Create a new crawl script for later use 
    def create_crawl_script(self, input_filename, base_url, crawl_script_filename):

        # Create a base JSON structure for crawl script
        script_data = { "id":"aaaaaaaa-bbbb-cccc-dddd-000000000001", "version":"2.0", "name":"Simple Crawl Script", "url":"", \
                        "tests": [{ "id":"aaaaaaaa-bbbb-cccc-dddd-000000000002", "name":"Happy Path", "commands":[] }] , \
                        "suites": [{ "id": "4409edf9-9781-440d-a742-bb3d18c6a0a6", "name": "Default Suite", "persistSession": False, \
                                     "parallel": False, "timeout": 300, "tests": ["aaaaaaaa-bbbb-cccc-dddd-000000000002"] }], \
                        "urls": [base_url], "plugins": [] }

        # Add base URL for crawling
        script_data["url"] = base_url

        # Add list of crawl destinations, using the Selenium open command
        commands = []
        with open(input_filename) as fp:
            for line in fp:
                target = line.strip()
                commands.append({"command":"open", "target":target})

        # Save crawl script data to file
        script_data["tests"][0]["commands"] = commands
        with open(crawl_script_filename, "w") as fp:
            fp.write(json.dumps(script_data, sort_keys=False, indent=2)) 

### validate_args(): Validate command line arguments
def validate_args(args):

    # Make sure there's a CSV file name provided for create action
    if ((args.script_action == "create_analysis") and ((args.filename == None) or (args.scan_name == None))):
        log.error("To create an analysis, please provide a CSV file name via --filename and a scan name via --scan_name.")
        sys.exit(1)

    # Make sure there's a crawl script file name provided for update_crawl_script action
    if ((args.script_action == "update_crawl_script") and (args.filename == None)):
        log.error("To update a crawl script, please provide a crawl script file name via --filename.")
        sys.exit(1)

    # Make sure there's an input file name provided for create_crawl_script action
    if ((args.script_action == "create_crawl_script") and (args.filename == None)):
        log.error("To create a crawl script, please provide an input file name via --filename.")
        sys.exit(1)

    # Make sure there's an output file name provided for create_crawl_script action
    if ((args.script_action == "create_crawl_script") and (args.output_filename == None)):
        log.error("To create a crawl script, please provide an output filename via --output-filename.")
        sys.exit(1)

    # Make sure there's a base URL provided for create_crawl_script action
    if ((args.script_action == "create_crawl_script") and (args.base_url == None)):
        log.error("To create a crawl script, please provide a base URL via --base-url.")
        sys.exit(1)

    # Make sure that the scan name is included for scan_now action
    if ((args.script_action == "scan_now") and (args.scan_name == None)):
        log.error("To scan now/ASAP, please provide a scan name via --scan-name.")
        sys.exit(1)

    # Make sure that the scan name is included for export_analysis action
    if ((args.script_action == "export_analysis") and (args.scan_name == None)):
        log.error("To export analysis data, please provide a scan name via --scan-name.")
        sys.exit(1)


    # TODO: Validate args.start_date (date string format)
    # TODO: Validate args.filename (file exists, format of content)
    # TODO: Validate args.teamId (numeric format > 0, less than some value)


### main()
if __name__ == "__main__":

    # Configure logging
    log = logging.getLogger(app_name)
    log_format = '%(asctime)-15s %(levelname)s: %(message)s'
    logging.basicConfig(format=log_format, datefmt='%Y/%m/%d-%H:%M:%S')
    log.setLevel(logging.INFO)
    log.setLevel(logging.DEBUG)

    # Read CLI Options
    action_choices = ["create_analysis","export_analysis","update_crawl_script","create_crawl_script","scan_now"]
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', help='Script Action.', dest="script_action", choices=action_choices, required=True)
    parser.add_argument('--scan-name', help='Scan Name. Example: "Scan MyApp".', dest="scan_name")
    parser.add_argument('--start', help='Start Date for scan. Applicable when --action=create_analysis. Example: "2020-03-03T02:00+00:00". Default: (not scheduled).', dest="start_date")
    parser.add_argument('--team', help='Team ID. Applicable when --action=create_analysis. If empty, only Security Leads will have visibility.', dest="teamId")
    parser.add_argument('--filename', help='Path to input file name. CSV file when --action=create_analysis. Path to Selenium script when --action=update_crawl_script. Path to input text file (list of paths) for new_crawl_script.', dest="filename")
    parser.add_argument('--output-filename', help='Path to output file name. Required for --action=create_crawl_script (extension should be ".side").', dest="output_filename")
    parser.add_argument('--base-url', help='Base URL for crawl script. Required for --action=create_crawl_script.', dest="base_url")

    # Parse and validation CLI parameters
    args = parser.parse_args()
    validate_args(args)

    # Instantiate class
    a = DynamicAnalysis()

    if (args.script_action == "create_analysis"):

        # Build-up the scan request data:
        # - Set the visibility
        visibility = { "setup_type": "SEC_LEADS_ONLY" }
        if (args.teamId != ""):
            visibility ={ "setup_type" : "SEC_LEADS_AND_TEAM", "team_identifiers" : [ args.teamId ] }

        # - Build a scan spec by getting inputs (URLs, login/crawl script...) from CSV
        scans = a.build_scan_spec_from_csv(args.filename)

        # - Set the schedule
        schedule = {}
        if (args.start_date != ""):
            schedule = { "start_date": args.start_date, "duration": { "length": 1, "unit": "DAY" } }
            # - Build the request body 
            scan_request_data = {"name": args.scan_name, "scans": scans, "schedule": schedule, "visibility": visibility} 
        else:
            # - Build the request body 
            scan_request_data = {"name": args.scan_name, "scans": scans, "visibility": visibility} 


        # Send request
        a.create_scan(scan_request_data)

    elif (args.script_action == "export_analysis"):
        a.get_analysis(args.scan_name, True)

    elif (args.script_action == "update_crawl_script"):
        a.update_crawl_script(args.scan_name, args.filename)

    elif (args.script_action == "create_crawl_script"):
        a.create_crawl_script(args.filename, args.base_url, args.output_filename)

    elif (args.script_action == "scan_now"):
        a.scan_now(args.scan_name)
