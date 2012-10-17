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
    local('git checkout %s' % branch)
    local('cp * %s' % env.codedir)
    with cd(env.codedir):
        virtualenv('python manage.py collectstatic')
    local('%s/%s/bin/restart' % (env.home, env.appname))


def virtualenv(command):
    local('source %s/bin/activate &&' + command, user=env.user)


def test():
    pass
