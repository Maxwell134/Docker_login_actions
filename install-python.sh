# install-python.sh
#!/bin/bash

set -e

echo "Installing Python $1"
# Add your actual commands to install Python based on the provided version
apt-get update -y && apt-get install python3 -y
chmod +x install-python
