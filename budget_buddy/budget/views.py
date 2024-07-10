# Django imports
from django.shortcuts import render
from django.http import request, HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from user.models import User
from django.template.loader import render_to_string

# App imports
from .forms import BudgetForm, Expense_Category, ExpenseForm
from .models import Budget, Expense, Expense_Category


def budget_view(request):
    try:
        budget_items = _get_budget_items(request.user.id)

    except:
        budget_items = None

    return render(request, "sections/budget.html", {"budget_items": budget_items})


def analysis_view(request):
    return render(request, "sections/analysis.html")


def insights_view(request):
    return render(request, "sections/insights.html")


def expenses_view(request):
    budget_items = _get_budget_items(request.user.id)
    return render(request, "sections/expenses.html", {"budget_items": budget_items})


def new_budget(request):

    if request.POST:
        form = BudgetForm(request.POST)

        if form.is_valid():
            return _create_new_budget(form, request.user.id)
        else:
            return HttpResponse(_error_message(form.errors))


@require_http_methods(["DELETE"])
def delete_budget(request):
    budget_id = request.GET.get("budget_id")

    if budget_id != None:
        return _delete_budget_item(budget_id)
    else:
        return HttpResponse(_warning_message("Budget item not found!"))


def _create_new_budget(form: object, user_id: int) -> HttpResponse:

    try:
        post = form.save(commit=False)
        post.created_by = User.objects.get(pk=user_id)
        post.save()

        return HttpResponse(
            _success_message(f"New budget created!"),
        )

    except Exception as error:
        return HttpResponse(
            _error_message(error),
        )


def _get_budget_items(user_id: int) -> list:
    budget_items = list(
        Budget.objects.filter(is_deleted=False or None, created_by=user_id)
    )
    return budget_items


def _delete_budget_item(item_id: int):
    try:
        budget = Budget.objects.get(id=item_id)
        budget.is_deleted = True
        budget.save()

        return HttpResponse(
            _success_message(f"{budget.name} has been deleted!"),
        )

    except Exception as error:
        return JsonResponse({"error": str(error)})


def _success_message(message: str):
    return render_to_string(
        "sections/alerts/success.html", {"success_message": message}
    )


def _error_message(message: str):
    return render_to_string("sections/alerts/error.html", {"error_message": message})


def _warning_message(message: str):
    return render_to_string(
        "sections/alerts/warning.html", {"warning_message": message}
    )
