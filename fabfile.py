from fabric.api import *  # NOQA
from .fabsettings import (PROJECTNAME, APPNAME, REMOTE, USER, HOMEDIR, CODEDIR)

env.projectname = PROJECTNAME
env.appname = APPNAME
env.remote = REMOTE
env.user = USER
env.home = HOMEDIR
env.codedir = CODEDIR
env.venv = VIRTUALENV


def deploy(branch='master'):
    local('git pull %s %s' % (env.remote, branch))
    with checkout(branch):
        local('rsync -auv * %s' % env.codedir)
    with cd(env.codedir):
        virtualenv('python manage.py collectstatic')
    local('%s/webapps/%s/bin/restart' % (env.home, env.projectname))


def virtualenv(command):
    local('source %s/bin/activate && %s' % (env.venv, command))


def checkout(command):
    local('git checkout %s && %s' % (branch, command))
