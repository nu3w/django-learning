# install virtual environment
pip install virtualenv

# create virtual environment
virtualenv name     # or
python -m venv name

# activate virtual env
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned        # bypass powershell
.\venv_name\Scripts\activate      # (powershell)

source /path/to/the/folder/venv_name/Scripts/activate       # (gitbash)

# Django: Python-based full stack framework(backend, frontend), 
# MVT Architecture 
Model: data, database, tables, fields, datatypes
View: logic : request-response, Model data HttpRequest, template building
Templates: Frontent(html, css)

- projects: core configurations
# start project
django-admin startproject project_name .        # . is optional

- apps: functions

# create app
python manage.py startapp app_name

# run sever
python manage.py runserver

