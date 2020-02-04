#!/bin/bash
#==================================================================================================
# addVeracodeUser.sh: Create a Veracode SSO user and enrich the profile with Active Directory data
#                     Reads a list of user email addresses from a file (one per line)
#
# Usage: ./addVeracodeUser.sh FILENAME
#==================================================================================================

# Veracode Parameters
VERACODE_URI="https://analysiscenter.veracode.com/api/3.0/createuser.do"
VERACODE_TEAMS="Default Team"
VERADODE_ROLES="Submitter,Reviewer,Greenlight IDE User,Sandbox User,Any Scan"

syntax(){
  echo "syntax: $0 FILENAME"
  exit 1
}

# Check readiness to run this script
if [ $# -ne 1 ];then
    syntax
fi
INFILE="$1"
if [ ! -f "$INFILE" ];then
    syntax
fi
LOGFILE="$(basename -s .txt $INFILE).log"
echo -e "\n-- Content of input file ${INFILE}: "
cat "${INFILE}"
echo -e "\n"
read -p "-- Are you ready to import the above list of new users (valid Nuance emails)? [y] " answer
if [ "$answer" = "n" ];then
  echo "Come back when you're ready! Exiting. "
  exit 1
fi 

# Prompt for Veracode team name(s)
echo -e "\n"
read -p "-- Which Veracode Team name(s) should the users be added to (comma-delimited)? [$VERACODE_TEAMS] " answer
if [ "$answer" != "" ];
then 
  VERACODE_TEAMS="$answer"
fi

# Authenticate to AD prior to LDAP search
echo -e "\n-- Authenticating to LDAP with DN: ${LDAP_DN}.\n"
read -s -p "LDAP Password: " LDAP_PASS

# Iterating through all Nuance emails in the input file
URL="ldap://$AD"
echo -e "\n\n-- Searching for user data in AD ($URL)"
mv "$LOGFILE" "$LOGFILE.$$" 2>/dev/null
mkdir "$LOGDIR" 2>/dev/null
for i in $(cat $INFILE);do

  # Searching for user data in AD
  echo -e "\n- Searching for $i..."
  QUERY="mail=$i"
  USER="$(basename -s @nuance.com $i)"
  OUTFILE="${LOGDIR}/${USER}.txt"
  ldapsearch -x -D "$LDAP_DN" -w "$LDAP_PASS" -b "$BASEDN" -ZZ -H "$URL" "$QUERY" > "${OUTFILE}"
  if [ $? = 0 ];then
    givenName=$(grep '^givenName:' ${OUTFILE} | cut -f2 -d: | cut -c2-)
    sn=$(grep '^sn:' ${OUTFILE} | cut -f2 -d: | cut -c2-)
    #telephoneNumber=$(grep telephoneNumber ${OUTFILE} | cut -f2 -d: | cut -c2-)
    title=$(grep '^title:' ${OUTFILE} | cut -f2 -d: | cut -c2-)
    department=$(grep '^department:' ${OUTFILE} | cut -f2 -d:  | cut -c2-)
    echo "Values from LDAP:"
    echo "  First: $givenName"
    echo "  Last : $sn"
    echo "  Title: $title, $department"
    echo "  Email: $i"
    echo -e "\n"

    # Add new Veracode user
    read -p "- Are you ready to add this user? [y]" answer
    if [ "$answer" = "y" -o "$answer" = "" ];then
        echo "Connecting to Veracode..."
        curl --compressed -u ${API_USER_NAME}:${API_USER_PWD} ${VERACODE_URI} \
        -F "first_name=${givenName}" \
        -F "last_name=${sn}" \
        -F "email_address=${i}" \
        -F "is_saml_user=true" \
        -F "custom_id=${i}" \
        -F "roles=$ROLES" \
        -F "title=${title}, ${department}" \
        -F "teams=${VERACODE_TEAMS}" \
        | tee $LOGDIR/${USER}.userinfo.xml 
    fi
  else
      echo "WARNING: Could not find user $i (or LDAP authentication failed)"
  fi 
done 
