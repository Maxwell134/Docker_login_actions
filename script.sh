#!/bin/bash

set -e

echo "Installing Python "
apt-get update -y 
apt-get uninstall python3.10.12 -y && apt-get install python3.9

# Show Python version
python3 --version
