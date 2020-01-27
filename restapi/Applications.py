#!/usr/bin/env python3 
import os, sys, requests, json, logging
import JsonExport
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
app_name="Applications"
page_size="100"
data_dir=os.environ.get("HOME")+ "/data/"

# Configure logging
log = logging.getLogger(app_name)
log_format = '%(asctime)-15s %(levelname)s: %(message)s'
logging.basicConfig(format=log_format, datefmt='%Y/%m/%d-%H:%M:%S')
log.setLevel(logging.INFO)

class Applications:
  headers = {"User-Agent": "Veracode Applications REST API Client Script"}

  def to_string(self, obj, name):
      log.debug(name + ":" + json.dumps(obj, sort_keys=True, indent=4))

  def get_paged_app_data(self, auth, page_num):
      api_base = "https://api.veracode.com/appsec/v1"
      try:
        arg1 = "page=" + str(page_num)
        arg2 = "size=" + str(page_size)
        response = requests.get(api_base + "/applications?"+arg1+"&"+arg2, auth=auth, headers=self.headers)

      except requests.RequestException as e:
        log.error("Request for application list failed.")
        print(e)
        sys.exit(1)

      if response.ok:
        return response.json()
      else:
        log.warning("Request for application list failed with %s code", response.text)
        prettyPrintObj(response.json())
        sys.exit(2)


  # Export all app definitions to JSON
  def export(self, data_dir):
      page_num = 0
      total_pages = 0
      done = False
      apps = []
      while (not done):
        data = self.get_paged_app_data(RequestsAuthPluginVeracodeHMAC(), page_num)
        JsonExport.saveFormatted(data, data_dir + "Data"+str(page_num))
        try:
          total_pages = data["page"]["total_pages"]
          log.info("Got page %d of %d", page_num+1, total_pages)
          for app in data["_embedded"]["applications"]:
            log.debug("Got app data for profile %s", app["profile"]["name"])
            apps.append(app)
          page_num = page_num + 1
          if (page_num >= total_pages):
            done = True
        except KeyError as e:
          # TODO: Handle Key Error exception properly
          log.debug("KeyError exception: %s", e)
          done = True

      self.to_string(apps[0], f"App 1 of {len(apps)}")
      json_file_base = data_dir + "Apps"
      JsonExport.saveFormatted(apps, json_file_base)
      log.info("Saved %d Veracode App Profiles to %s.json", len(apps), json_file_base)

if __name__ == "__main__":
  #log.setLevel(logging.DEBUG)
  a = Applications()
  a.export(data_dir)
