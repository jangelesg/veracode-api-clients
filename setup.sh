#!/bin/bash
# Setup python virtual env
python3 -m venv .venv
chmod 700 .venv/bin/activate
. .venv/bin/activate
echo '. .venv/bin/activate' >> ~/.profile
chmod 700 ~/.profile

# Install Python dependencies
pip3 install -r requirements.txt --user

# Create output data directory (used by 'DynamicAnalysis.py --action=export ...')
mkdir /app/data
chmod 700 /app/data