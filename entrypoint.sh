#!/bin/sh

echo "Logging into Docker Hub with username: $INPUT_USERNAME"
docker login -u $INPUT_USERNAME -p $INPUT_PASSWORD
