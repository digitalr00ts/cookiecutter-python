cookiecutter-python
===================

.. image:: https://github.com/digitalr00ts/cookiecutter-python/workflows/Tests/badge.svg?branch=master
     :target: https://github.com/digitalr00ts/cookiecutter-python/actions?workflow=Tests
     :alt: CI Status

A Cookiecutter_ template for Python 3.6+ projects

.. _cookiecutter: https://github.com/audreyr/cookiecutter


Usage
------


Quickstart
^^^^^^^^^^

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.6.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/digitalr00ts/cookiecutter-python.git


Features
--------

- tox
- pylint
- pytest
- bandit
- coverage
- editorconfig
- gitignore

  - python
  - vim
  - vscode
  - InteliJ

- License (Apache 2.0)
- Python Packaging
- Readme
- Pipfile
- gitattributes
- Black formater
- Travis
- versioning from git tag
- cli w/ docopt
- use package as module


To Do
-----

- [ ] Add LGTM.com
- [ ] Add `nitpick`
- [ ] Cleanup this readme
- [ ] finish config for flake8/flakehell
- [ ] add Github Actions

- Add license options to template

   - Creative Commons Attribution
   - Creative Commons Zero
   - Creative Commons Attribution Share Alike
   - GNU Free Documentation License (FDL)
   - Public Documentation License (PDL)
   - FreeBSD Documentation License
   - Open Publication License

- add ability to select built-in theme for docs
- Documentation
- VCS Templates

  - Github
  - Gitlab
  - Gitea/Gogs ???

- exceptions
- CI/CD: Jenkins file
- License Options
- testing

  - hypothosis
  - pytest-bdd

- logging
- includes, Better Exceptions
- precommit
- testing
- coverall
- push to pypi

License
=======
Copyright 2020 digitalr00ts

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
