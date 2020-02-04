#!/bin/bash
#=========================================================================================
# getAppList.sh: Get list of Veracode apps and save them to CSV file
#=========================================================================================

# App-specific settings
OUTPUT_FILE_BASE="AppList"
VERACODE_URI="https://analysiscenter.veracode.com/api/4.0/getappbuilds.do?only_latest=true"

# Initialize
XSL_FILE=xsl/${OUTPUT_FILE_BASE}.xsl
VERBOSE="-v"
VERBOSE=""

# Create output dir if needed
mkdir "$OUTPUT_DIR" 2>/dev/null

# Send XML API query
echo -e "\n-- Invoking Veracode API to get ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.xml"
http --auth-type=veracode_hmac --output "${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.xml" ${VERACODE_URI}

# Convert XML to CSV
echo -e "\n-- Converting XML file to ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv"
xsltproc -o ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv ${XSL_FILE} ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.xml  

# Show first few lines of CSV file
echo -e "\n-- Printing first few lines of ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv"
head -20 ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv 
