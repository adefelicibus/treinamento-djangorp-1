treinamento-djangorp-1
======================

Instalação
===========

* Criar um virtualenv: mkvirtualenv busao

* Instalar as dependencias no OS: sudo apt-get install mysql-server python-dev build-essential libmysqld-dev libmysqlclient-dev nginx libevent-dev supervisor

* Instalar dependencias: pip install -r requirements.txt 

* Criar banco no mysql: create database busao; 

* Configurar o settings_local.py para acessar seu banco mysql

* Sincronizar banco: python manage.py syncdb

* Migrar banco: python manage.py migrate
