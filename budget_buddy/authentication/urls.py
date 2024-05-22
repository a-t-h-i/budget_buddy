from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("register/", views.registratiom_page, name="register"),
    path("home_page/", views.main_page, name="register"),
]
