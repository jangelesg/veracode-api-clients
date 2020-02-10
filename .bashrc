# Setup bash editor and prompt
set -o vi
export EDITOR=vim
export PS1='$(hostname)($PWD)$ '
export DATA_DIR="/app/data"
export VC_CREDS_FILE="$HOME/.veracode/credentials"

# Setup python virtual environment on first use
if [ ! -d .venv ];then
  echo -e "\n-- Setting you up for first time use by downloading python dependencies..."
  python3 -m venv .venv
  chmod 700 .venv/bin/activate
  . .venv/bin/activate
  pip3 install -r requirements.txt --user
fi

# Create output data directory (used by 'DynamicAnalysis.py --action=export ...')
if [ ! -d "$DATA_DIR" ];then
  echo -e "\n-- Creating $DATA_DIR directory"
  mkdir "$DATA_DIR"
  chmod 700 "$DATA_DIR"
fi 

# If needed, warn about the missing .env file
if [ ! -f .env ];then
  echo -e "\n*** WARNING: Please create a $HOME/.env file (see README.md for details) ***"
else
  . ./.env
fi

# If needed, warn about the missing veracode credentials file
if [ ! -f "$VC_CREDS_FILE" ];then
  echo "\n*** WARNING: Please create a $VC_CREDS_FILE file (see README.md for details) ***"
fi

# Activate Python virtual env.
. .venv/bin/activate