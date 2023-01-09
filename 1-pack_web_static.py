#!/usr/bin/python3
"""script that generates .tgz archive from the contents of the web_static folder"""
from fabric.api import local
import time


def do_pack():
    """generate .tgz archive of web_static/ folder"""
    time_now = strftime("%Y%M%d%H%M%S")
    try:
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(time_now)
        local("tar -cvzf {} web_static/".format(file_name))
        return file_name
    except:
        return None
