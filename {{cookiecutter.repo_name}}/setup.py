#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import {{ cookiecutter.project_slug }}

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []
setup_requirements = ["pytest-runner"]
test_requirements = ["pytest"]

setup(
    author={{ cookiecutter.project_slug }}.__author__,
    author_email={{ cookiecutter.project_slug }}.__email__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="{{ cookiecutter.description }}",
    entry_points={
        "console_scripts": [
            "{{ cookiecutter.project_slug }} = {{ cookiecutter.project_slug }}.__main__:main"
        ]
    },
    install_requires=requirements,
    license="LGPLv3+",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="{{ cookiecutter.project_slug }}",
    name="{{ cookiecutter.project_slug }}",
    packages=find_packages(include=["{{ cookiecutter.project_slug }}"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}",
    version={{ cookiecutter.project_slug }}.__version__,
    zip_safe=False,
)
