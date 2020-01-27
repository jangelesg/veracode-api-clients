#!/usr/bin/python
import json,os

### Save well-formatted JSON data to file ###
def saveFormatted(jsonData, filebase):

  # Open output file to save JSON data (use .json.tmp in case the .json is busy)
  fileBufSize = 10
  f = open(filebase+".json.tmp", 'w', fileBufSize)

  # Save the JSON data as a well-formatted file
  jsonStr = json.dumps(jsonData, sort_keys=True, indent=4, separators=(',', ': '))
  f.write(jsonStr + "\n\n")
  f.close()

  # Rename the file to the expected filename
  os.rename(filebase+".json.tmp", filebase+".json")
