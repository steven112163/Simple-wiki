# Simple wiki
A simple website using Django REST and Nuxt.js

## Dependencies
### Backend
    * Python >= 3.6
    * Django >= 3.0.3
        * django-ckeditor >= 5.9.0
        * django-3-jet >= 1.0.7
        * djangorestframework >= 3.11.0
        * django-cors-headers >= 3.2.1
    * feedparser >= 5.2.1
    * mysqlclient >= 1.4.6
### Frontend
    * nuxt >= 2.14.0
    * bootstrap >= 4.5.0
        * bootstrap-vue >= 2.15.0
    * jarallax >= 1.12.1
    * object-fit-images >= 3.2.4

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

4. Run API server at localhost:8000
    ```shell script
    ~/wiki$ python3 manage.py runserver
    ```

5. Install frontend dependencies
    ```shell script
    ~/wiki/NuxtFrontend$ npm install
    ```

6. Serve with hot reload at localhost:3000
    ```shell script
    ~/wiki/NuxtFrontend$ npm run dev
    ```
 