# HR
HR API that Can User Register and Upload his Resume

# Requirments
1. Python 3: https://www.python.org/downloads/
2. Postgres DB: https://www.postgresql.org/download/
3. PgAdmin: https://www.pgadmin.org/download/

# Getting Started
1. Clone the Project: https://github.com/Hamza-abughazaleh/HR.git
2. Create Python Enviroment:
   - Open Terminal
   - sudo apt install virtualenv
   - virtualenv "env name" --python=/usr/bin/python3
3. Activate Your Enviroment:
   - Open Terminal
   - source "env name"/bin/activate
4. Go to project Directory and Install requirements file by Terminal: pip install -r requirements.txt
5. Create Your DB from pgadmin
6. Go to settings.py and edit this code:
   - DATABASES = {
    	'default': {
       		'ENGINE': 'django.db.backends.postgresql_psycopg2',
       		'NAME': 'hr', #add your db name you created
       		'USER': 'postgres', #add your db authentication
       		'PASSWORD': 'postgres',
       		'HOST': '127.0.0.1',
       		'PORT': '5432',
    		}
   	}
7. Go to project Directory and do this Commands by Terminal: 
   - python manage.py makemigrations
   - python manage.py createsuperuser #to create super user (admin)
   - python manage.py runserver

8. if you Need to Access All Api:
   - Login as Super User (Admin)
   - Install Modify Headers: https://chrome.google.com/webstore/detail/modify-headers-for-google/innpjfdalfhpcoinfnehdnbkglpmogdi
   - Open it and Add : Name: Authorization , Value: X-ADMIN=1

9. Go to localhost:8000/api-v1/

# What's included
1. Django 2.2.4: https://docs.djangoproject.com/en/2.2/
2. sDjango Rest Framework 3.10.2: https://www.django-rest-framework.org/

