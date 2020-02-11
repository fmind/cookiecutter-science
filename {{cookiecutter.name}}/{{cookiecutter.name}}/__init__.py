"""Main module of the project."""

from pathlib import Path

import toml

FILE = Path(__file__)
MODULE = FILE.parent
PROJECT = MODULE.parent

FLOWS = PROJECT / 'flows'
CONFIGS = PROJECT / 'configs'

TEST_CONFIGS = [
    CONFIGS / 'test.toml',
]

MAIN_CONFIGS = [
    CONFIGS / 'public.toml',
    CONFIGS / 'private.toml',
    CONFIGS / 'production.toml',
]

def load(files):
    """Load a list of project configurations."""
    return toml.load(files)

def config(files=MAIN_FILES):
    """Return the project main configuration."""
    return _config(files)

def test_config(files=TEST_FILES):
    """Return the project test configuration."""
    return _config(files)
