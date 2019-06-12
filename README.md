# Project401

REQUIREMENTS (VIEWFLOW)
------------
 * Python3
 * Pip3
 * Virtualenv 

Most of the requirements is already in requirements.txt file except:

 * update the pkg-resources
 * you'll need viewflow pro version visit this site http://viewflow.io/pro/

INSTALLATION (VIEWFLOW)
------------
 * this sample command is for ubantu 
 
 1. install Python 3
    sudo apt-get update
    sudo apt-get install python3.6
    
 2. install Pip3
    sudo apt install python3-pip
    
 3. install Virtualenv from Pip3
    sudo pip3 install virtualenv 
    
 4. creat new virtual environment in empty directory and activate virtual environment
    python3 -m venv env
    source env/bin/activate
    
 5. copy source code to your directory
 
 6. use Pip3 to install requirements.txt file (include update pkg-resources and install viewflow pro version)
    pip3 install -r requirements.txt
    
 7. run this command 
    ./manage.py makemigrations
 8. run this command
    ./manage.py migrate
 9. run this command 
    ./manage.py createsuperuser
 10. run this command 
    ./manage.py runserver
    
 11. your applicatiion is now available

STRUCTURE (VIEWFLOW)
------------
 
Project401/
├── myproject
│   ├── api
│   │   ├── __pycache__
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── views.py
│   ├── media
│   ├── myapp
│   │   ├── __pycache__
│   │   ├── migrations
│   │   ├── templates
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── flows.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── views.py
│   ├── myproject
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── setting.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── manage.py
│   ├── requirements.txt
└── README.md
