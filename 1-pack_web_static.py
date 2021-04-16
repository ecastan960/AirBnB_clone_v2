#!/usr/bin/python3
"""[summary]
"""
from fabric.api import *
from datetime import *
import web_static


def do_pack():
    """[summary]
    """
    today = date.today()
    now = datetime.now()
    year = today.strftime("%Y")
    month = today.strftime("%m")
    day = today.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")
    folder = local("mkdir -p versions")
    name = "web_static_{}{}{}{}{}{}".format(year, month, day,
                                            hour, minute, second)
    compresion = local("tar -cvzf {}.tgz web_static".format(name))
    destination = local("mv {}.tgz versions".format(name))
