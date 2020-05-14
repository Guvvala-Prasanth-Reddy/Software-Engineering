# Software-Engineering
Webapp using Django 
## Inorder to safely run the webapp few variables have to be set in webapp/webapp/settings.py  module ##

## DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.postgresql',
        'NAME'      : '', [ This is the name of your project ]
        'USER'      :'',   [ This the name of the user i.e the postgres username ]
        'PASSWORD'  :'',   [ This is the database  password ]
        'HOST'      :'localhost'
    }


##  EMAIL_HOST          = 'smtp.gmail.com' 
	EMAIL_HOST_USER     = ''   [ This is the username of our project email ]
	EMAIL_HOST_PASSWORD = ''   [ This is the  password of the email ]
##




## Steps to run the project
	1:  After performing the above steps migrate to webapp directory 
	2:  execute the following commands :
						* python manage.py makemigrations
						* python manage.py migrate
						* python manage.py runserver [ It starts the server on the port 5432 and address is the local host adddress i.e 127.0.0.1 ]

## The credentials for the project email will be shared in the whatsapp group ##

## Kindly look through the requiremtents.txt ##
To cross check whether all of them are installed in your virtualenv run "pip freeze > requirements.txt" inside the venv and cross check the installed modules 
