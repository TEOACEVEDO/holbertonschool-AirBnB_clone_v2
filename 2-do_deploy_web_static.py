#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web
servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['3.91.84.106', '3.80.230.115']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if not exists(archive_path):
        return False
    try:
        file = archive_path.split('/')[-1].split('.')[0]
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        # Create the folder to uncompress the archive
        run('mkdir -p /data/web_static/releases/{}/'.format(file))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}'
            .format(file, file))
        # Remove file from /tmp/ dir
        run('rm /tmp/{}.tgz'.format(file))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(file, file))
        # Deletes existing symbilic link
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file))
        run('rm -rf /data/web_static/current')
        # New symbolic link
        run('ln -s /data/web_static/releases/{}\
            /data/web_static/current'.format(file))
        return True
    except Exception as e:
        return False
