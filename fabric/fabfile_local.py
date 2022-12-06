import os

from fabric.api import local
from fabric.context_managers import lcd

PROJECT_REPO = 'https://github.com/EliasLopezBouzid/my-first-blog'
PROJECT_NAME = 'my-first-blog'
PROJECT_PATH = f'/home/elias/sistemas/{PROJECT_NAME}'
PYTHON_VENV = f'{PROJECT_PATH}/.venv/bin/python'
PIP_VENV = f'{PROJECT_PATH}/.venv/bin/pip'

def git_clone():
    print('git clone...')

    if os.path.exists(PROJECT_PATH):
        print('repo already exist in local - skipping clone')
    else:
        local(f'git clone {PROJECT_REPO} {PROJECT_PATH}')

def create_env():
    print('creating virtual enviroment...')
    
    with lcd(PROJECT_PATH):
        local(f'python3 -m venv .venv')
        
def install_requirements():
    print('installing requirements...')
    
    with lcd(PROJECT_PATH):
        local(f'{PIP_VENV} install -r requirements.txt')

def run_migrations():
    print('installing migrations...')
    
    with lcd(PROJECT_PATH):
        local(f'{PYTHON_VENV} manage.py loaddata db.json ')
        
def load_data():
    print('installing migrations...')
    
    with lcd(PROJECT_PATH):
        local(f'{PYTHON_VENV} manage.py migrate')
        
def create_superuser():
    print('creating superuser...')
    
    with lcd(PROJECT_PATH):
        local('DJANGO_SUPERUSER_PASSWORD=12345 python manage.py createsuperuser --noinput --username admin --email e.lopezbouzid@gmail.com')

def deploy():
    git_clone()
    create_env()
    install_requirements()
    run_migrations()
    load_data()
    create_superuser()
    