from convertor.issue import Issue
from convertor.project import Project
from github import Github
import json
import os


settings = {}
projects = []

with open('settings.json') as f:
    settings = json.load(f)

username = settings["GITHUB_USERNAME"]
password = settings["GITHUB_PASSWORD"]
directory = settings["ROOT_BUG_DIR"]

github = Github(username, password)

for filename in os.listdir(directory):
    if len(filename.split(".")) == 1:
        project = Project(filename, os.path.join(directory, filename))
        projects.append(project)