#!/usr/bin/env python3
import os, sys, requests, json, logging, csv, argparse
import JsonExport
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
app_name="DynamicAnalysis"
data_dir=os.environ.get("HOME")+ "/data/"


class DynamicAnalysis:
  headers = {"User-Agent": "Veracode DynamicAnalysis REST API Client"}

  # Get form-authentication scan specification from CSV file (must be in data_dir)
  # CSV header required: "url,http_and_https,directory_restriction_type,script_file"
  def get_form_auth_scan_data_from_csv(self, csv_filename):
    scans = []
    with open(csv_filename) as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
        url                   = row["url"]
        http_and_https        = row["http_and_https"]
        dir_restriction_type  = row["directory_restriction_type"]
        script_file           = row["script_file"]
        f = open(data_dir + script_file, "r")
        login_script = f.read()
        auth_configuration = {"authentications":{"FORM":{"authtype":"FORM","login_script_data":{"script_body":login_script,"script_type": "SELENIUM"},"script_file":script_file}}}
        scans.append({"scan_config_request":{"target_url":{"url":url,"http_and_https":http_and_https,"directory_restriction_type": dir_restriction_type},"auth_configuration":auth_configuration}})
    return scans

  # Send request to create a Dynamic Analysis scan 
  def create_scan(self, scan_request_data):
    api_base="https://api.veracode.com/was/configservice/v1/analyses"

    try:
      run_verification = "run_verification=" + str(False)
      validate_only = "validate_only=" + str(False)
      #url= api_base + "?" + run_verification + "&" + validate_only
      url= api_base
      log.info("Sending POST request to %s", url)
      log.debug("POST Body: " + json.dumps(scan_request_data, sort_keys=True, indent=4))
      response = requests.post(url, auth=RequestsAuthPluginVeracodeHMAC(), headers=self.headers, json=scan_request_data)

    except requests.RequestException as e:
      log.error("Request for application list failed.")
      print(e)
      sys.exit(1)

    if response.ok:
      #return response.json()
      return response
    else:
      log.warning("Request for application list failed with %s code: %s", response.status_code, response.text)
      sys.exit(2)

if __name__ == "__main__":
  ### Define some defaults
  name = "Scan created by python script DynamicAnalysis.py"
  start_date="2020-03-03T02:00+00:00"
  teamId = ""
  csv_filename = "../data/dynscan1.csv"

  ### Configure logging
  log = logging.getLogger(app_name)
  log_format = '%(asctime)-15s %(levelname)s: %(message)s'
  logging.basicConfig(format=log_format, datefmt='%Y/%m/%d-%H:%M:%S')
  log.setLevel(logging.INFO)
  log.setLevel(logging.DEBUG)

  ### Read CLI Options
  parser = argparse.ArgumentParser()
  parser.add_argument('--name', help='Scan Name.', dest="name", default=name)
  parser.add_argument('--start', help='Start Date for scan.', dest="start_date", default=start_date)
  parser.add_argument('--team', help='Team ID. Default: none.', dest="teamId", default=teamId)
  parser.add_argument('--csvfile', help='CSV file name. Default: "../data/dynscan1.csv"', dest="teamId", default=teamId)
  args = parser.parse_args()
  print(args)
  #parser.print_help();
  #parser.print_usage();

  ### Instantiate class
  a = DynamicAnalysis()

  ### Build-up the scan request data
  # Set the visibility
  visibility = { "setup_type": "SEC_LEADS_ONLY" }
  if (teamId != ""):
    visibility ={ "setup_type" : "SEC_LEADS_AND_TEAM", "team_identifiers" : [ teamId ] }

  # Set the schedule
  schedule = {}
  if (start_date != ""):
    schedule = { "start_date": start_date, "duration": { "length": 1, "unit": "DAY" } }

  # Get URLs and login scripts
  scans = a.get_form_auth_scan_data_from_csv(csv_filename)

  # Build the request body 
  scan_request_data = {"name": name, "scans": scans, "schedule": schedule, "visibility": visibility} 
                    #, "org_info": org_info, "scan_setting": scan_setting}

  ### Send request
  a.create_scan(scan_request_data)