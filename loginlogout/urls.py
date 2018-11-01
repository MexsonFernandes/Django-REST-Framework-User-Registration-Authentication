from django.urls import path, include
from .views import Record, Login

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
]
