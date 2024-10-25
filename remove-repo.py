# Remove Repos on github
import requests

token = "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"
username = "THP297"
def delete_repos(repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    else:
        print(f"Failed to delete repository '{repo_name}'. Error: {response.content.decode()}")
        
repo_list = ['callback-list','observerForm2','dashboard-callback2','test'] # List of repositories to delete
for repo in repo_list:
    try:
        delete_repos(repo)
    except Exception as e:
        print(e)