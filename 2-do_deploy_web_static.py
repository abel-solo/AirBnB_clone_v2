#!/usr/bin/python3
"""
Script that distributes an archive to your web servers using do_deploy
"""

import os.path
from fabric.api import local
from fabric.operations import run, put, sudo
from fabric.api import env
env.hosts = ['54.237.65.144', '54.88.134.53']


def do_deploy(archive_path):
    """Deploy an archive to a web server"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        wsconfig = archive_path.split("/")[-1]
        wsdir = ("/data/web_static/releases/" + wsconfig.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(wsdir))
        run("sudo tar -xzf /tmp/{} -C {}".format(wsconfig, wsdir))
        run("sudo rm /tmp/{}".format(wsconfig))
        run("sudo mv {}/web_static/* {}/".format(wsdir, wsdir))
        run("sudo rm -rf {}/web_static".format(wsdir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(wsdir))
        return True
    except:
        return False
