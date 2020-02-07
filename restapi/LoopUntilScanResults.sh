#!/bin/bash
#=============================================================================
# LoopUntilScanResults.sh: Loop until the DynamicAnalysis scan results are in.
#=============================================================================
if [ $# -ne 1 ];then
  echo "Syntax: $0 SCAN_NAME"
  exit 1
fi

# Init. vars
SCAN_NAME="$1"
TMP_FILE=/tmp/scan.log
JSON_FILE=../data/Exported_DetailedScanOccurrence.json
SLEEP_SECONDS=1800 # check every half hour (expect more than 24 hours but no less that 48)
MAX_ITERATIONS=96  # stop after trying for 2 days 
status=""
i=1

# Loop until we get a PASSED or FAILED results
while [ "$status" = "" ];do
    # Get the scan results
    TIMESTAMP="[$(date +%D-%T)]"
    ./DynamicAnalysis.py --action=export_analysis --scan-name "$SCAN_NAME" 2>"$TMP_FILE"

    # Check if results are available
    grep "FINISHED_RESULTS_AVAILABLE" "$JSON_FILE" >/dev/null
    if [ $? != 0 ];then
        echo "$TIMESTAMP Results not available: $(grep status_type $JSON_FILE | cut -f2 -d:) (try $i of $MAX_ITERATIONS)"
    else
        # Get the scan results (PASSED or FAILED)
        grep FAILED "$TMP_FILE"
        if [ $? = 0 ];then
            status="FAILED"
            continue
        fi
        grep PASSED "$TMP_FILE"
        if [ $? = 0 ];then
            status="PASSED"
            continue
        fi
    fi

    # Check that we're not looping indefinitely due to a problem on the Veracode side
    if [ "$i" -ge "$MAX_ITERATIONS" ];then
        status="FAILED (max iterations reached, please check Veracode UI or contact Veracode Support)"
    else
        sleep $SLEEP_SECONDS
    fi
    i="$(expr $i + 1)"
done
echo "STATUS: $status"