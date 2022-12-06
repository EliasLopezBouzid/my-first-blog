from fabric.api import env
from fabric.api import run
from fabric.context_managers import cd
from fabric.contrib.files import exists

env.hosts = ['3.15.38.15','18.217.241.86']
PROJECT_REPO = 'https://github.com/EliasLopezBouzid/my-first-blog.git'
PROJECT_NAME = 'my-first-blog'
PROJECT_PATH = f'/home/elias/sistemas/{PROJECT_NAME}'
PYTHON_VENV = f'{PROJECT_PATH}/.venv/bin/python3'
PIP_VENV = f'{PROJECT_PATH}/.venv/bin/pip'
DJANGO_SUPERUSER_PASSWORD='12345'
DJANGO_SUPERUSER_USERNAME='admin'
DJANGO_SUPERUSER_EMAIL='e.lopezbouzid@gmail.com'

def git_clone():
    print(f'git clone {PROJECT_REPO}...')

    if exists(PROJECT_PATH):
        print('repo already exist in server - skipping clone')
    else:
        run(f'git clone {PROJECT_REPO} {PROJECT_PATH}')

def create_env():
    print('creating virtual enviroment...')
    
    with cd(PROJECT_PATH):
        run(f'python3 -m venv .venv')
        run(f'source .venv/bin/activate')
        
def install_requirements():
    print('installing requirements...')
    
    with cd(PROJECT_PATH):
        run(f'{PIP_VENV} install -r requirements.txt')

def run_migrations():
    print('installing migrations...')
    
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py makemigrations')
        run(f'{PYTHON_VENV} manage.py migrate')
        
def load_data():
    print('installing data...')
    
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py loaddata db.json')
        
def create_superuser():
    print('creating superuser...')
    
    with cd(PROJECT_PATH):
        try:
            run(f'DJANGO_SUPERUSER_PASSWORD=12345 {PYTHON_VENV} manage.py createsuperuser --noinput --username {DJANGO_SUPERUSER_USERNAME} --email {DJANGO_SUPERUSER_EMAIL}')
        except:
            print("This Superuser is already created, Skipping this step")
        
def runserver():
    print('running server...')
    
    with cd(PROJECT_PATH):
        run(f'{PYTHON_VENV} manage.py runserver')

def deploy():
    git_clone()
    create_env()
    install_requirements()
    run_migrations()
    load_data()
    create_superuser()
    runserver()