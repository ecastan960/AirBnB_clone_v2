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
        put(archive_path, remote_path="/tmp/")
        return True
    else:
        return False
