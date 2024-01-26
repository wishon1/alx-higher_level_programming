#!/usr/bin/python3
"""script that takes 2 arguments in order to solve this challenge.

   - The first argument will be the repository name
   - The second argument will be the owner name
   - You must use the packages requests and sys
   - You are not allowed to import packages other than requests and sys
   - You don’t need to check arguments passed to the script (number or type)
"""
from sys import argv
import requests


def list_commitInGithub(repo_name, owners_name):
    """list 10 commits (from the most recent to oldest) of the repository
       “rails” by the user “rails” You must use the GitHub API, here is the
       documentation https://developer.github.com/v3/repos/commits/Print all
       commits by:`<sha>: <author name>` (one by line)
    """
    url = "https://api.github.com/repos/{}/{}/commits".format(
        owners_name, repo_name)
    response = requests.get(url)
    res = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                res[i].get("sha"),
                res[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    repo_name = argv[1]
    owners_name = argv[2]

    list_commitInGithub(repo_name, owners_name)
