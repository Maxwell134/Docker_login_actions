#!/bin/sh

# Accessing the GitHub actor context variable
echo "Logging into Docker Hub with username: $INPUT_USERNAME as GitHub user: $GITHUB_ACTOR"
apt-get update -y && apt-get install docker.io -y
docker login -u $INPUT_USERNAME --password-stdin
