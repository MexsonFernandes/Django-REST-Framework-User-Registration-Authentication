# Django REST Framework - UserRegistration-Authentication
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMexsonFernandes%2FDjango-REST-Framework-User-Registration-Authentication&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

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
