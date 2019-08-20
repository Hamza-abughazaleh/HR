# HR
HR API that Can User Register and Upload his Resume

# Requirments
1.Python 3: https://www.python.org/downloads/
2.Postgres DB: https://www.postgresql.org/download/
3.PgAdmin: https://www.pgadmin.org/download/

# Getting Started
1.Clone the Project: https://github.com/Hamza-abughazaleh/HR.git
2.Create Python Enviroment:
  A.Open Terminal
  B.sudo apt install virtualenv
  C.virtualenv "env name" --python=/usr/bin/python3
3.Activate Your Enviroment:
  A.Open Terminal
  B.source "env name"/bin/activate
4.Go to project Directory and Install requirements file by Terminal: pip install -r requirements.txt
5.Create Your DB from pgadmin
6.Go to settings.py and edit this code:
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hr', #add your db name you created
        'USER': 'postgres', #add your db authentication
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
       }
   }
7.Go to project Directory and do this Commands by Terminal: 
  A.python manage.py makemigrations
  B.python manage.py createsuperuser #to create super user (admin)
  C.python manage.py runserver

8.if you Need to Access All Api:
  A.Login as Super User (Admin)
  B.Install Modify Headers: https://chrome.google.com/webstore/detail/modify-headers-for-google/innpjfdalfhpcoinfnehdnbkglpmogdi
  C.Open it and Add : Name: Authorization , Value: X-ADMIN=1

9.Go to localhost:8000/api-v1/

# What's included
1.Django 2.2.4: https://docs.djangoproject.com/en/2.2/
2.Django Rest Framework 3.10.2: https://www.django-rest-framework.org/

