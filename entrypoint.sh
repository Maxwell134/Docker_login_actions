#!/bin/sh

# Accessing the GitHub actor context variable
echo "Logging into Docker Hub with username: $INPUT_USERNAME as GitHub user: $GITHUB_ACTOR"
docker login -u $INPUT_USERNAME -p $INPUT_PASSWORD
