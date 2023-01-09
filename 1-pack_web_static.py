#!/usr/bin/python3
"""script that generates .tgz archive from the contents of the web_static folder"""
from fabric.api import local
import time


def do_pack():
    """ generate an tar archive from web_static folder"""
    time_string = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.string)))
        return ("versions/web_static_{}.tgz".format(time.string))
    except:
        return None
