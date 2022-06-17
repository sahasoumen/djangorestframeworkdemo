# DJango Rest Framework

## All executed commands


### Environment setup
$ source env/bin/activate\
$ pip install django\
$ pip install djangorestframework

### Create Project
$ django-admin startproject djangorestframeworkdemo\

### Configure git
$ cd djangorestframeworkdemo/\
$ git init\
$ echo "# djangorestframeworkdemo" >> README.md\
$ git add .\
$ git commit -m "Initial commit"\
$ git branch -M main\
$ git remote add origin git@github.com:sahasoumen/djangorestframeworkdemo.git\
$ git push -u origin main

### Start Server
$ python manage.py runserver

### Response in JSON format
http://127.0.0.1:8000/?format=json

### Create backend
$ python manage.py startapp base

### Create Models
$ python manage.py makemigrations\
$ python manage.py migrate\
$ python manage.py shell
> from base.models import Project\
> Project.objects.create(name = "Project 1")\
> Project.objects.create(name = "Project 2")\
> Project.objects.create(name = "Project 3")\
> projects = Project.objects.all()\
> print(projects)\
> exit()

# Final APIs
1. list - GET http://127.0.0.1:8000/api/project/
2. add - POST http://127.0.0.1:8000/api/project/add
3. get - GET http://127.0.0.1:8000/api/project/2
4. update - PUT http://127.0.0.1:8000/api/project/2
5. delete - DELETE http://127.0.0.1:8000/api/project/2