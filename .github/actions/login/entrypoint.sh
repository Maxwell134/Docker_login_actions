#!/bin/bash
set -e

echo "Logging in to Docker registry..."
apt-get install docker.io -y
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin "$DOCKER_REGISTRY"

echo "Docker login successful!"
