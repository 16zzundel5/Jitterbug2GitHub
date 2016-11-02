# Project
import os
from issue import Issue

class Project:
    def __init__(self, name, dir):
        self.name = name
        self.directory = dir
        self.get_issues()
    
    def get_issues(self):
        self.issues = []
        for filename in os.listdir(self.directory):
            if len(filename.split(".")) == 1:
                issue = Issue(self.directory, filename)
                self.issues.append(issue)