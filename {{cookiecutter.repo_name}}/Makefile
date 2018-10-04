.PHONY: init clean clean-test clean-pyc clean-build docs help
.NOTPARALLEL:
.POSIX:
.ONESHELL:
.DEFAULT_GOAL := help
SHELL := /bin/bash

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

init: ## create local virtualenv w/ packages for dev
	PIPENV_VENV_IN_PROJECT=1 pipenv install --dev
	pipenv run pre-commit
	@echo -e '\nTo enter the virtualenv run:\n    pipenv shell --fancy'

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	pipenv run pylint {{ cookiecutter.project_slug }} tests setup.py
	pipenv run black --check --py36 {{ cookiecutter.project_slug }} tests setup.py

test: ## run tests quickly with the default Python
	pipenv run pytest -v

test-all: ## run tests on every Python version with tox
	pipenv run tox

coverage: ## check code coverage quickly with the default Python
	pipenv run coverage run --source {{ cookiecutter.project_slug }} -m pytest
	pipenv run coverage report -m
	pipenv run coverage html
	pipenv run $(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	pipenv run sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	pipenv run $(MAKE) -C docs clean
	pipenv run $(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

# servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	pipenv run twine upload dist/*

dist: clean ## builds source and wheel package
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
