from django.urls import path
from .auth_views import register

urlpatterns = [
    path("register/", register, name="register"),
]