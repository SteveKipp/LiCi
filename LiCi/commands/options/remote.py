import os
import subprocess


class Remote(object):

    def __init__(self, repo):
        if repo[-3:] == "git":
            print("git repo detected -> using git")
            #does this already exist? -> no:clone -> yes:pull
            name = self.get_repo_folder_git(repo)
            self.location = "~/LiCi/routines/"
            if os.path.exists(os.path.expanduser(self.location + "{}".format(name))):
                #pull
                os.chdir(os.path.expanduser(self.location + "{}".format(name)))
                git_pull = subprocess.Popen(["git", "pull"])
                git_pull.wait()
            else:
                #clone
                os.chdir(os.path.expanduser(self.location))
                git_clone = subprocess.Popen(["git", "clone", repo])
                git_clone.wait()
            self.location = "~/LiCi/routines/{}".format(name)
            print("**** SCM Complete ****")
            print(" ")
        if repo[:3] == "svn":
            print("svn repo detected -> using subversion")
            #soon
        self.repo = repo

    def get_repo_folder_git(self, repo_url):
        folders = repo_url.split("/")
        folder_name = folders[len(folders)-1][:-4]
        return folder_name
