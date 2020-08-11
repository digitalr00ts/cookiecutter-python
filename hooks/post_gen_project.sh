#!/usr/bin/env sh

git init
git config user.name || git config --add user.name "{{ cookiecutter.full_name }}"
git config user.email || git config --add user.email "{{ cookiecutter.email }}"
git commit --allow-empty -m '🎉 initial commit'
git add .
git commit --message='✨ feat: initial project scaffolding'
git tag {{ cookiecutter.version }}
