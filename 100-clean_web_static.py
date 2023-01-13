#!/usr/bin/python3
""" test file """
import os.path
import os
from fabric.api import *
from fabric.operations import run, put, sudo
import time


env.hosts = ['54.87.231.230', '52.91.116.139']
env.user = "ubuntu"


def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)

    files = sorted(os.listdir("versions"))
    [files.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(j) for j in files)]

    with cd("data/web_static/releases"):
        files = run("ls -tr").split()
        files = [j for j in files if "web_static_" in j]
        [files.pop() for i in range(number)]
        [run("sudo rm -rf ./{}".format(j)) for j in files]
