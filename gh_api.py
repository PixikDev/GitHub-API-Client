import requests
import json
from typing import Dict, List, Optional

class GitHubAPI:
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: Optional[str] = None):
        self.session = requests.Session()
        if token:
            self.session.headers.update({
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            })
    
    def get_user_repos(self, username: str) -> List[Dict]:
        url = f"{self.BASE_URL}/users/{username}/repos"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def create_repo(self, name: str, description: str = "", private: bool = False) -> Dict:
        url = f"{self.BASE_URL}/user/repos"
        data = {
            'name': name,
            'description': description,
            'private': private,
            'auto_init': True
        }
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    github = GitHubAPI()
    repos = github.get_user_repos("torvalds")
    for repo in repos[:5]:
        print(f"{repo['name']}: {repo['description']}")