from django.urls import path
from . import views

urlpatterns = [
    path("analysis/", views.analysis_view),
    path("budget/", views.budget_view),
    path("expenses/", views.expenses_view),
    path("insights/", views.insights_view),
    path("create/new_budget", views.new_budget, name="new_budget"),
    path("delete/budget_item", views.delete_budget),
]
