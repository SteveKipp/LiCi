import os
import subprocess


class Remote(object):

    def __init__(self, repo):
        if repo[-3:] == "git":
            print("git repo detected -> using git")
            #does this already exist? -> no:clone -> yes:pull
            git_clone =subprocess.Popen(["git", "clone", repo])
            git_clone.wait()
        if repo[:3] == "svn":
            print("svn repo detected -> using subversion")

        self.repo = repo
        self.location = "~/.LiCi/routines"
