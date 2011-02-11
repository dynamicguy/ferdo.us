from fabric.api import *
from fabric.contrib import project

# Where the static files get collected locally
env.local_static_root = '/tmp/static'

# Where the static files should go remotely
env.remote_static_root = '/home/www/static.example.com'

@roles('static')
def deploy_static():
    local('./manage.py collectstatic')
    project.rysnc_project(
        remote_dir = env.remote_static_root,
        local_dir = env.local_static_root,
        delete = True
    )