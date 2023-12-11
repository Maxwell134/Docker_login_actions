import os
import requests


def get_repository_list(username, token):
    api_url = f'https://hub.docker.com/v2/repositories/{username}/'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        repositories = data.get('results', [])
        return repositories
    else:
        print(
            f"Failed to get repository list. Status code: {response.status_code}")
        # Print the response content for further inspection
        print(response.text)
        return None


def main():
    # Get Docker Hub credentials from environment variables
    username = os.environ.get('username')
    token = os.environ.get('token')

    if not username or not token:
        print("Please provide Docker Hub credentials.")
        return

    # Get Docker Hub repository list
    repositories = get_repository_list(username, token)

    if repositories:
        print(f"Repository List for user: {username}")
        for repository in repositories:
            repository_name = repository.get('name', '')
            print(f"  Repository: {username}/{repository_name}")
    else:
        print("Failed to fetch repository list.")


if __name__ == "__main__":
    main()
