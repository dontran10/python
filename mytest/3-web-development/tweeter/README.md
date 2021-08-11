# Don Tran's Python Practice: Tweeter Social Application

### INSTALLATION NOTES
- Create a fresh database at database server
    - My SQL or SQL Server
- If use My SQL as backend DB:
    - $python -m pip install mysqlclient==2.0.3
    - Select DATABASES in settings.py (comment out the on for SQL Server)
    - Notes: in DATABASES setting, use the account with permission (CRUD), then manage.py migrate can works

- If use SQL Server as backend DB:
    - $python -m pip install mysql-django
    - Select DATABASES in settings.py (comment out the on for My SQL )
    - Notes: in DATABASES setting, use the account with permission (CRUD), then manage.py migrate can works

- Install django-tailwind==2.0.1
    - $python -m pip install django-tailwind==2.0.1

### MIGRATE DB, CREATE supperuser for /admin page
- Move to 'tweeter' folder, run command belwo to migrate database (create schemas from models in code)
    - $python manage.py migrate
    - $python manage.py createsuperuser   
        - Notes the username and password (ex: admin/123) of supperuser to log on /admin page

### START APP
- Move to 'tweeter' folder, run
    - $python manage.py runserver

### BROWSE APP 
- Browse: http://localhost:8000/accounts/login/
- Use supperuser above to log on admin page: http://localhost:8000/admin