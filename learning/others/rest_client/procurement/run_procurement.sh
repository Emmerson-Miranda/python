#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Function to check if venv is active
is_venv_active() {
    [[ "$VIRTUAL_ENV" != "" ]]
}

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment if not already active
if ! is_venv_active; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

# Run the Python script
echo "Running procurement downloader..."
python procurement_downloader.py

# Deactivate virtual environment if it was activated by this script
if ! is_venv_active; then
    deactivate
fi 