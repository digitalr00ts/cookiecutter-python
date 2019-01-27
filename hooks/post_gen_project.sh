#!/bin/sh

git init
git add .
git commit --message='cookiecutter generated'
# Lightweight placeholder tag
git tag {{ cookiecutter.version }}
