from django.urls import path
from . import views

urlpatterns = [
    path("analysis/", views.analysis_view),
    path("budget/", views.budget_view),
    path("expenses/", views.expenses_view),
    path("insights/", views.insights_view),
]
