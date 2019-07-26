from invoke import task
from pathlib import Path


@task
def venv(c, force=False):
    """Create a virtual environment."""
    if Path("venv").exists() and not force:
        return None
    c.run("python3 -m venv venv --clear")
    c.run("venv/bin/pip install --requirement requirements.txt")


@task(venv)
def work(c):
    """Run an instance of jupyter lab."""
    c.run("venv/bin/jupyter lab")
