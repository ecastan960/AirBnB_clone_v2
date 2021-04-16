#!/usr/bin/python3
"""[summary]
"""
from fabric.api import *
from os import path

env.hosts = [
    '35.227.67.236',
    '35.231.147.151'
]


def do_deploy(archive_path):
    """[summary]

    Args:
        archive_path ([type]): [description]

    Returns:
        [type]: [description]
    """
    if path.exists(archive_path):
        fileP = archive_path.split('/')
        name_file = fileP[1].split('.')
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(name_file[0]))
        run("tar -xzf /tmp/{} -C\
            /data/web_static/releases/{}".format(fileP[1], name_file[0]))
        run("rm /tmp/{}".format(fileP[1]))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name_file[0], name_file[0]))
        run("rm -rf /data/web_static/current")
        slink = "ln -s /data/web_static/releases/{} /data/web_static/current"
        run(slink.format(name_file[0]))
        return True
    else:
        return False
