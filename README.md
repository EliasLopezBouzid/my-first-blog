Pasos que incluye el proyecto:
1. Descarga el proyecto del repo con git
2. Crea un entorno virtual
3. Activa el entorno virtual
4. Instala las librerías del `requirements.txt`
5. Genera las migraciones del proyecto con `python manage.py makemigrations`
6. Ejecuta las migraciones en la base de datos con `python manage.py migrate`
7. Carga los datos iniciales del fichero `db.json` con `python manage.py loaddata db.json`
8. Crea el Superusuario 'admin'
9. Ejecuta el servidor de django para probar la aplicación

Tras activar el venv con:  source .venv/bin/activate
1. Fabric:
fab deploy

2. Ansible:
ansible-playbook ansible/playbooks/deploy.yml

3. Docker:
docker build --tag my-first-blog .
docker run --publish 8000:8000 my-first-blog




