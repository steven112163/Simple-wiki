# Simple wiki
A simple website using Django and Nuxt.js

## Prerequisites
* Python >= 3.6
* Django >= 3.0.3
    * django-ckeditor >= 5.9.0
    * django-3-jet >= 1.0.7
    * djangorestframework >= 3.11.0
    * django-cors-headers >= 3.2.1
* Nuxt.js >= 2.12.1
* feedparser >= 5.2.1
* mysqlclient >= 1.4.6

## Environment Setup
1. Create database in MySQL
    ```mysql
    CREATE DATABASE wiki
    CHARACTER SET utf8
    COLLATE utf8_general_ci;
    ```

2. Update database
    ```shell script
    ~/wiki$ python3 manage.py makemigrations
    ~/wiki$ python3 manage.py migrate
    ```

3. Collect static files
    ```shell script
    ~/wiki$ python3 manage.py collectstatic
    ```

4. Run server
    ```shell script
    ~/wiki$ python3 manage.py runserver
    ```
 