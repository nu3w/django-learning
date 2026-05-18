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

# migration file create
python manage.py makemigrations

python manage.py migrate

# create superuser
python manage.py createsuperuser

# shell
python manage.py shell

# CRUD: Create, Retrieve, Updata, Delete

# get all data
model_name.objects.all()        

# create data
model_name.objetcs.create(field1 = "...", field2 = "...", >>>)

# retrieve: single data 
model_name.objects.get()        # or
a = model_name.objects.get()  
a.field1
a.field2

# update: 
a.field1 = new_data
a.field2 = new_data
a.save()

# delete: 
- retrieve data
- a.delete()

# filter
model_name.objects.filter(field1 = "...", field2 = "...", ...)
