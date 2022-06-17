# DJango Rest Framework

## All executed commands


### Environment setup
source env/bin/activate
pip install django\
pip install djangorestframework

### Create Project
django-admin startproject djangorestframeworkdemo\

### Configure git
cd djangorestframeworkdemo/\
git init\
echo "# djangorestframeworkdemo" >> README.md\
git add .\
git commit -m "Initial commit"\
git branch -M main\
git remote add origin git@github.com:sahasoumen/djangorestframeworkdemo.git\
git push -u origin main

### Start Server
python manage.py runserver

### Response in JSON format
http://127.0.0.1:8000/?format=json



