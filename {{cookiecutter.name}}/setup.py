#!/usr/bin/env python3

import setuptools

META = dict(
   name="{{cookiecutter.name}}",
   version="0.1.0",
   packages=["{{cookiecutter.name}}"],
   install_requires=[],
)

if __name__ == "__main__":
    setuptools.setup(**META)
