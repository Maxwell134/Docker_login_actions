#!/bin/bash
set -e

echo "Logging in to Docker registry..."
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin "$DOCKER_REGISTRY"

echo "Docker login successful!"
