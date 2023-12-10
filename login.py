import os
import subprocess
import json
import requests

def docker_login(username, password):
    login_cmd = f'docker login -u {username} -p {password}'
    subprocess.run(login_cmd, shell=True, check=True)

def build_and_push_image(image_name, image_tag, username):
    build_cmd = f'docker build -t {image_name}:{image_tag} .'
    build_tag = f'docker tag {image_name}:{image_tag} {username}/{image_name}:{image_tag}'
    push_cmd = f'docker push {username}/{image_name}:{image_tag}'

    subprocess.run(build_cmd, shell=True, check=True)
    subprocess.run(build_tag, shell=True, check=True)
    subprocess.run(push_cmd, shell=True, check=True)

def image_exists(username, image_name, image_tag):
    api_url = f'https://hub.docker.com/v2/repositories/{username}/{image_name}/tags/{image_tag}/'
    response = requests.head(api_url)
    return response.status_code == 200

def delete_image(username, image_name, image_tag, password):
    api_url = f'https://hub.docker.com/v2/repositories/{username}/{image_name}/tags/{image_tag}/'
    auth = requests.auth.HTTPBasicAuth(username, password)
    response = requests.delete(api_url, auth=auth)
    return response.status_code == 204

def main():
    # Get environment variables from GitHub Actions inputs
    image_name = os.environ.get('image')
    image_tag = os.environ.get('image_tag')
    username = os.environ.get('username')
    password = os.environ.get('password')

    # Perform Docker login
    docker_login(username, password)

    # Check if image with tag exists in Docker Hub
    if image_exists(username, image_name, image_tag):
        print(f"Image with tag {image_tag} exists. Deleting from Docker Hub...")
        # Delete the existing image from Docker Hub
        delete_image(username, image_name, image_tag, password)

    # Build and push Docker image
    build_and_push_image(image_name, image_tag, username)

    # Print details as JSON
    details = {
        "image_name": image_name,
        "image_tag": image_tag,
        "username": username,
    }

    print(json.dumps(details, indent=2))

if __name__ == "__main__":
    main()
