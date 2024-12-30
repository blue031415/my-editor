from invoke import task


@task
def setup(c):
    c.run("python -m venv .venv")
    c.run(".venv\\Scripts\\activate && pip install --upgrade pip")
    c.run(".venv\\Scripts\\activate && pip install -r requirements.txt")


@task
def test(c):
    c.run(".venv\\Scripts\\activate && pytest")


@task
def format(c):
    c.run(".venv\\Scripts\\activate && black src")


@task
def lint(c):
    c.run(".venv\\Scripts\\activate && flake8 src")


@task
def dev(c):
    c.run("python src/main.py")
