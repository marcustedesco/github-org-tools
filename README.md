# Github Org Tools
Tools for managing a Github organization

## Sync repos script
Sync an organization's Github repos to your local machine.

- Works with public repos and private repos that your Github account has access to.
- Assumes you are using [SSH keys to connect to Github](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

### Setup
- `pip install PyGithub`
    - Reference Link: https://pypi.org/project/PyGithub/
- Add Github access token and organization names list to the script

#### Getting the access token
1. Go to Github "Settings".
2. Go to "Developer Settings".
3. Go to "Personal access tokens".
4. Click on "Generate new token" button.
5. Add a note.
6. Check the "read:org" option under "admin:org"
7. Click on "Generate token" button.
8. Copy the access token and paste in below code.

### Run
- `python sync_repos.py`