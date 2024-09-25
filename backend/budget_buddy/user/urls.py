urlpatterns = [
    path("register/new_user", views.register, name="register_user"),
    path("user/login", views.login_view, name="user_login"),
]

