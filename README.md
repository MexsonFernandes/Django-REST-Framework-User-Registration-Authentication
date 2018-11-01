# Django REST Framework - UserRegistration-Authentication

Django app to register and authenticate user using REST API framework.

## How to use:
  - pip install -r requirements.txt
  - python manage.py runserver
  
## URLs to target:
  - to register a user
    - localhost:8000/api/addUser/
  - to login a user
    - localhost:8000/api/rest-auth/login/
  - to logout a user
    - localhost:8000/api/rest-auth/logout/

## API Call demo:
  - curl -X POST http://localhost:8000/api/addUser/ -d "email=test@test.com&password=abcd123&username=test"

## Useful commands:
  - python manage.py createsuperuser
  - python manage.py makemigrations
  - python manage.py migrate
