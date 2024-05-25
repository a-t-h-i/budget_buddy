from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def check_username(request):
    username = request.GET.get("username")
    restricted_usernames = ["admin", "athi", "king", "test"]

    if username.lower() in restricted_usernames:
        return render(request, "autentication/username_taken.html")
    else:
        return render(request, "autentication/username_available.html")


def login_page(request):
    return render(request, "autentication/login.html")


def registratiom_page(request):
    return render(request, "autentication/register.html")


# @login_required(login_url="login")
def main_page(request):
    return render(request, "budget_buddy/home_page.html")
