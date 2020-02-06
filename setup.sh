#!/bin/bash
# Install Python dependencies
pip3 install -r requirements.txt --user

# Create output data directory (used by 'DynamicAnalysis.py --action=export ...')
mkdir /app/data
chmod 700 /app/data