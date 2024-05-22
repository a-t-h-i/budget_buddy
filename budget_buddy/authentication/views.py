from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def set_current_page(page: str, request: object) -> object:
    current_page = request.session["current_page"] = page
    return current_page


def get_current_page(request: object) -> object:
    current_page = request.session["current_page"]
    return current_page if current_page else ""


def login_page(request):
    set_current_page("", request)
    return render(request, "autentication/index.html")


def registratiom_page(request):
    return render(request, "autentication/register.html")


def main_page(request):
    if get_current_page(request) == "home" or get_current_page(request) == "":
        return render(request, "budget_buddy/home_page.html")
    else:
        redirect("")
