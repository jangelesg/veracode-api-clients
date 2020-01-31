#!/usr/bin/env python3
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

class DynamicAnalysis:
    headers = {"User-Agent": "Veracode DynamicAnalysis REST API Client"}

    def export_scan_details(self, scan_name, data):
        try:
            scan_details_url = data["_embedded"]["analyses"][0]["_links"]["scans"]["href"]
            log.debug("Sending request to %s", scan_details_url)
            response = requests.get(scan_details_url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, verify=verifyCert)

        except requests.RequestException as e:
            log.error("Request for scan details failed.")
            print(e)
            sys.exit(1)

        if response.ok:
            json_file_base = data_dir + "ScanDetails"
            JsonExport.saveFormatted(response.json(), json_file_base)
            log.info("Saved Veracode scan details for '%s' to %s.json", scan_name, json_file_base)
        else:
            log.warning("Request for scan details failed with %s code", response.text)
            prettyPrintObj(response.json())
            sys.exit(2)

    def export_scan(self, scan_name):
        api_base="https://api.veracode.com/was/configservice/v1/analyses"
        try:
            arg1 = "name=" + scan_name
            log.debug("Sending request to %s", api_base)
            response = requests.get(api_base+"?"+arg1, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, verify=verifyCert)
            data = response.json()
            if response.ok:
                json_file_base = data_dir + "ScanSpec"
                JsonExport.saveFormatted(data, json_file_base)
                log.info("Saved Veracode scan spec for '%s' to %s.json", scan_name, json_file_base)
                self.export_scan_details(scan_name, data)
            else:
                log.warning("Request for scan spec failed with %s code", response.text)
                prettyPrintObj(response.json())
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for scan data failed.")
            print(e)
            sys.exit(2)




    # Get form-authentication scan specification from CSV file (must be in data_dir)
    def get_scan_spec_from_csv(self, csv_filename):
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

                # Don't uncomment the below code, it won't work. It was added when the sample JSON (on help.veracode.com) was inaccurate.
                # # Add Crawl script
                # # TODO: Support crawl_script_file (or validate what's already here)
                # if (row['crawl_script_file'] != ""):
                #     crawl_script_path = row['base_path'] + "/" + row['crawl_script_file']
                #     log.debug("Reading crawl script data from %s", crawl_script_path)
                #     f = open(crawl_script_path, "r")
                #     crawl_script_data = f.read()
                #     scan["crawl_configuration"] = { \
                #             "scripts": [ {\
                #                 "crawl_script_data": { \
                #                     "script_type": "SELENIUM", \
                #                     "script_body": crawl_script_data \
                #                 }, \
                #                 "name": row['crawl_script_file'] \
                #             }], \
                #             "disabled": False \
                #         }


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

                # Add Crawl script. 
                # PLEASE NOTE: Today (Jan. 2020), the result will not be visible in the Veracode UI. 
                #              Only Veracode Support can confirm proper deployment.
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

    # Send request to create a Dynamic Analysis scan 
    def create_scan(self, scan_request_data):
        api_base="https://api.veracode.com/was/configservice/v1/analyses"

        try:
            param1 = "?run_verification=true"
            param2 = "&validate_only=true"
            url= api_base + param1 # + param2
            log.info("Sending POST request to %s", url)
            log.debug("POST Body: " + json.dumps(scan_request_data, sort_keys=True, indent=4))
            response = requests.post(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, json=scan_request_data, verify=verifyCert)
            if response.ok:
                log.debug("Successful response: %s", str(response))
                return response
            else:
                log.warning("Request to create scan failed with %s code: %s", response.status_code, response.text)
                sys.exit(1)

        except requests.RequestException as e:
            log.error("Request for application list failed.")
            print(e)
            sys.exit(2)

# TODO: Implement validations
def check_args(args):
    log.debug("name = %s", args.name)
    log.debug("start_date = %s", args.start_date)
    log.debug("teamId = %s", args.teamId)
    log.debug("csv_filename = %s", args.csv_filename)

if __name__ == "__main__":
    ### Define some defaults
    name = "Scan created by python script DynamicAnalysis.py"
    start_date="2020-03-03T02:00+00:00"
    teamId = "101736"
    teamId = "132892"
    csv_filename = "../data/dynscan-dvna.csv"
    scan_action = "create"

    ### Configure logging
    log = logging.getLogger(app_name)
    log_format = '%(asctime)-15s %(levelname)s: %(message)s'
    logging.basicConfig(format=log_format, datefmt='%Y/%m/%d-%H:%M:%S')
    log.setLevel(logging.INFO)
    log.setLevel(logging.DEBUG)

    ### Read CLI Options
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', help='Scan Action := [create, export]', dest="scan_action", default=scan_action)
    parser.add_argument('--name', help='Scan Name.', dest="name", default=name)
    parser.add_argument('--start', help='Start Date for scan.', dest="start_date", default=start_date)
    parser.add_argument('--team', help='Team ID.', dest="teamId", default=teamId)
    parser.add_argument('--csvfile', help='CSV file name.', dest="csv_filename", default=csv_filename)
    args = parser.parse_args()
    log.debug("Args: %s", str(args))

    ### Instantiate class
    a = DynamicAnalysis()

    if (args.scan_action == "create"):
        check_args(args)

        ### Build-up the scan request data
        # Set the visibility
        visibility = { "setup_type": "SEC_LEADS_ONLY" }
        if (args.teamId != ""):
            visibility ={ "setup_type" : "SEC_LEADS_AND_TEAM", "team_identifiers" : [ args.teamId ] }

        # Set the schedule
        schedule = {}
        if (start_date != ""):
            schedule = { "start_date": args.start_date, "duration": { "length": 1, "unit": "DAY" } }

        # Get URLs and login scripts
        scans = a.get_scan_spec_from_csv(args.csv_filename)

        # Build the request body 
        scan_request_data = {"name": args.name, "scans": scans, "schedule": schedule, "visibility": visibility} 

        ### Send request
        a.create_scan(scan_request_data)

    elif (args.scan_action == "export"):
        log.info("Exporting scan spec data for scan named '%s'", args.name)
        a.export_scan(args.name)
