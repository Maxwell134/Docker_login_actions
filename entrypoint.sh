#!/bin/sh

echo "Logging into Docker Hub with username: $INPUT_USERNAME"
apt-get update -y && apt-get install docker.io -y
docker login -u $INPUT_USERNAME -p $INPUT_PASSWORD
