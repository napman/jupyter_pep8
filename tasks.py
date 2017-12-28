from invoke import task, MockContext, run

@task
def pypi(ctx):
    run('python setup.py sdist upload')