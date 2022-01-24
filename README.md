# Projeto-Crud_Django_and_Mongo
### Configuração para rodar o projeto

Download Project

    git clone https://github.com/samueloliveiraf/crud-django-and-mongo/    

Intall Python
    
    sudo apt -y install build-essential python3-venv python3-dev libpq-dev
    
---------------------------------------------------------------------
### Os camandos a seguir tem ser executado dentro da pasta do projeto
---------------------------------------------------------------------
   
Run Project

    python3 -m venv .venv

Active venv

    source venv/bin/activate
    
Install Requirements

    pip install -r requeriments.txt

Config DB_MONGO settings.py

    DATABASES = {
      'default': {
          'ENGINE': 'djongo',
          'NAME': 'db_name_mongo'
       }
    }


Comands ends

    python manage.py migrate
    
Run

    python manage.py runserver
    
