#!/usr/bin/python3
'''  Fabric script that creates and distributes an archive to your web servers
'''
from fabric.api import *


def deploy():
    ''' calls pack to deploy archive to web servers
    '''
    path = do_pack()
    if path is None:
        return False
    else:
        do_deploy(path)
