#!/bin/bash

set -e

echo "Installing Python $1"

# Add your actual commands to install Python based on the provided version
if [ "$1" == "3.8" ]; then
    # Example: Install Python 3.8 using apt
    sudo apt-get update
    sudo apt-get install -y python3.8
elif [ "$1" == "3.9" ]; then
    # Example: Install Python 3.9 using apt
    sudo apt-get update
    sudo apt-get install -y python3.9
else
    echo "Unsupported Python version: $1"
    exit 1
fi

# Show Python version
python3 --version
