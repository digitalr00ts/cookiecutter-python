#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(here, "requests", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()
with open("HISTORY.md", "r", "utf-8") as f:
    history = f.read()

requirements = []
setup_requirements = ["pytest-runner"]
test_requirements = ["pytest"]

setup(
    author=about["__author__"],
    author_email=about["__author_email__"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description=about["__description__"],
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.__main__:main"
        ]
    },
    install_requires=requirements,
    license=about["__license__"],
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name=about["__title__"],
    packages=find_packages(include=["{{ cookiecutter.project_slug }}"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url=about["__url__"],
    version=about["__version__"],
    zip_safe=False,
)
