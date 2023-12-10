import os
import subprocess
import json

def docker_login(username, password):
    login_cmd = f'docker login -u {username} -p {password}'
    subprocess.run(login_cmd, shell=True, check=True)

def build_and_push_image(image_name, image_tag, registry_url):
    build_cmd = f'docker build -t {registry_url}/{image_name}:{image_tag} .'
    push_cmd = f'docker push {registry_url}/{image_name}:{image_tag}'

    subprocess.run(build_cmd, shell=True, check=True)
    subprocess.run(push_cmd, shell=True, check=True)

def main():
    # Get environment variables from GitHub Actions inputs
    image_name = os.environ.get('image')
    image_tag = os.environ.get('image_tag')
    registry_url = os.environ.get('registry_url')
    username = os.environ.get('username')
    password = os.environ.get('password')

    # Perform Docker login
    docker_login(username, password)

    # Build and push Docker image
    build_and_push_image(image_name, image_tag, registry_url)

    # Print details as JSON
    details = {
        "image_name": image_name,
        "image_tag": image_tag,
        "registry_url": registry_url,
        
    }

    print(json.dumps(details, indent=2))

if __name__ == "__main__":
    main()
