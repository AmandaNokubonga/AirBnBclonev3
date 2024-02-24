#!/usr/bin/python3
"""
Fabric script for deploying archives to web servers
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['142.44.167.228', '144.217.246.195']

def deploy_archive(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        base_name = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, base_name))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, base_name))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, base_name))
        run('rm -rf {}{}/web_static'.format(path, base_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, base_name))
        return True
    except Exception as e:
        print(e)
        return False
