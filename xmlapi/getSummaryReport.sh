#!/bin/bash
#=========================================================================================
# getSummaryReportData.sh: Get summary report data for all Veracode builds
#=========================================================================================

# Load values for OUTPUT_DIR, API_USER_NAME and API_USER_PWD 
. ../.env 

# App-specific settings
OUTPUT_FILE_BASE="SummaryReportData"
VERACODE_URI="https://analysiscenter.veracode.com/api/4.0/summaryreport.do"
REPORT_PARAM="build_id"

# Initialize
XSL_FILE=xsl/${OUTPUT_FILE_BASE}.xsl
VERBOSE="-v"
VERBOSE=""
APP_BUILDS=$(awk '{FS=","}{print $12}' $OUTPUT_DIR/Apps.csv | sed 's/"//g' | grep -v '^$')
CURL_OPTS="--retry 3 --retry-connrefused  --retry-delay 30 --compress -k $VERBOSE"

# Check file to see if it's newer than 1 day
isNew=0
checkFile(){
  isNew=0
  filename="$1"
  if [ -f $filename ];then
    file_time=$(stat -f '%m' "$filename")
    current_time=$(date +%s)
    if (( file_time >= ( current_time - ( 60 * 60 * 24 ) ) )); then
      isNew=1
    fi
  fi
}

# Create output dir if needed
mkdir "$OUTPUT_DIR" 2>/dev/null

# Remove old CSV files
rm "${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-*.csv"

# Interate through all build IDs obtained from getAppBuilds.sh 
echo -e "\n-- Iterating through all app builds..."
for ab in $APP_BUILDS;do
  if [ "$ab" == "" ];then
     continue
  fi

  # Send XML API query if the file is older than 1 day
  filename="${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.xml"
  checkFile "$filename"
  if [ $isNew -eq 0 ];then
    echo -e "\n-- Invoking Veracode API to get ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.xml"
    http --auth-type=veracode_hmac --output "${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.xml" "${VERACODE_URI}?${REPORT_PARAM}=${ab}"
  else
    echo -e "\n-- Using local file ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.xml"
  fi

  # Convert XML to CSV
  echo -e "\n-- Converting XML file to ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.csv"
  xsltproc -o ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.csv ${XSL_FILE} ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-${ab}.xml  
done

# Consolidate all CSV data
echo -e "\n-- Consolidating all CSV data into ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv"
echo "AppName,AppId,BU,Owner,BuildId,Submitter,GenerationDate,VeracodeLevel,TotalFlaws,FlawsNotMitigated,LastUpdateTime,IsLatestBuild,PolicyName,PolicyComplianceStatus,ScanOverdue" > ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv
cat ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}-*.csv | grep -v "^$" | sort >> ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv

# Show first few lines of CSV file
echo -e "\n-- Printing first few lines of ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv"
head ${OUTPUT_DIR}/${OUTPUT_FILE_BASE}.csv 
