# Django REST Framework - UserRegistration-Authentication

Django app to register and authenticate user using REST API framework.

## How to use:
  - `pip install -r requirements.txt`
  - `python manage.py runserver`
  
## URLs to target:
  - to register a user
    - localhost:8000/api/addUser/
  - to login a user
    - localhost:8000/api/login/
  - to logout a user
    - localhost:8000/api/logout/

## API Call demo:
  - `curl -X POST http://localhost:8000/api/addUser/ -d "email=test@test.com&password=abcd123&username=test"`
  - `curl -X POST http://localhost:8000/api/login/ -d "email=test@test.com&password=abcd123"`
  - `curl -X POST http://localhost:8000/api/logout/ -d "token=b75f9fc8-f598-4d4c-8698-d98ee808c1f3"`

## Note: token is generated using uuid package.

## Useful commands:
  - `python manage.py createsuperuser`
  - `python manage.py makemigrations`
  - `python manage.py migrate`
