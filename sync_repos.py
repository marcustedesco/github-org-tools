"""
Sync an organization's Github repos to your local machine.

- Works with public repos and private repos that your Github account has access to.
- Assumes you are using SSH keys to connect to Github (https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

Setup:
    pip install PyGithub
    Reference Link: https://pypi.org/project/PyGithub/
    Getting the access token.
        Go to Github <settings>.
        Go to <Developer Settings>.
        Go to <Personal access tokens>.
        Click on <Generate new token> button.
        Add a note.
        Check the <read:org> option under <admin:org>
        Click on <Generate token> button.
        Copy the access token and paste in below code.
"""
import os
from github import Github

# Add your Github access token
access_token = ''
# Add orgs to sync
# Example: orgs = ['babbel']
orgs = []

cwd = os.getcwd()
for org in orgs:
    path = os.path.join(cwd,org)
    if os.path.exists(path):
        print(f'{org} directory already exists')
    else:
        os.mkdir(path)
        print(f'Made new {org} directory')

gh = Github(access_token)

repos = gh.get_user().get_repos()
for repo in repos:
    if repo.organization is not None and repo.organization.login in orgs:
        print(f'Found a {repo.organization.login} repo!')
        org_path = os.path.join(cwd,repo.organization.login)
        os.chdir(org_path)
        repo_path = os.path.join(org_path,repo.name)
        # If the repo exists, pull the latest
        if os.path.exists(repo_path):
            print('Repo already exists locally. Pulling latest...')
            os.chdir(repo_path)
            os.system(f'git pull')
        # Else clone the repo
        else: 
            os.system(f'git clone {repo.ssh_url}')
        os.chdir(cwd)