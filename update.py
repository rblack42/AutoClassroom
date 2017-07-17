#!/usr/bin/env python
import os
from git import Repo
ORG = "https://github.com/ACC-COSC2325-001-SU17"

LABS = [
    "homework",
    "lab1-memory-unit",
    "lab2-alu-unit",
    "lab3-control-unit",
]

REPOS = "_repos/SU-17"

lines  = open("repo_names.txt","r").readlines()
for l in lines:
    try:
        # process one student
        f,l,g = l.split()
        print("user: %s %s" % (f,l))
        
        # check each lab for this student
        for lab in LABS:
            rname = "%s/%s-%s/%s-%s" % (REPOS,f,l,lab,g)
            print("\tchecking",rname)

            # clone the repo if not present
            if not os.path.isdir(rname):
                print("\t\tnot found - cloning")
                git_url = "%s/%s-%s" % (ORG,lab,g)
                repo_dir = rname
                print("cloning",git_url,"to",repo_dir)
                try:
                    print("running git")
                    Repo.clone_from(git_url, repo_dir)
                except:
                    print("failed")
                    continue;

            # update repo from Github
            repo = Repo(rname)
            try:
                repo.remotes.origin.pull()
            except:
                print("pull failed")

            # display log messages
            try:
                commits = repo.commits()
                for c in commits:
                    print(c.id,c.authored_date)
            except:
                print("no commits")

    except:
        pass

