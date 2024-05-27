from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("register/", views.registratiom_page, name="register"),
    path("check_username/", views.check_username),
    path("home_page/", views.main_page, name="home"),
    path("logout/", views.leave_app, name="logout"),
]
