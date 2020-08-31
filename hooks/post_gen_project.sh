#!/usr/bin/env sh

git init
git config user.name || git config --add user.name "{{ cookiecutter.full_name }}"
git config user.email || git config --add user.email "{{ cookiecutter.email }}"
git commit --allow-empty -m '🎉 initial commit'
git add .
git commit --message='✨ feat: initial project scaffolding'
git tag {{ cookiecutter.version }}
git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git
ssh-keygen -t ed25519 -a 100 -N "" -C "{{ cookiecutter.project_slug }}@gh-actions" -f GH_DEPLOY_ed25519-key