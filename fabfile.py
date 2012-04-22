from fabric.api import local, task
from extjs4 import version


@task
def versiontag():
    """
    Add git tag for current ``extjs.version``.
    """
    local('git tag {0}'.format(version))

@task
def pypi_update():
    """
    Upload to pypi.
    """
    local('python setup.py sdist upload')

@task
def push_tags():
    local('git push --tags')

@task
def release():
    """
    Runs ``versiontag`` ``push_tags`` and ``pypi_update``.
    """
    versiontag()
    push_tags()
    pypi_update()
