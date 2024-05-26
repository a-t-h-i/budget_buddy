from django.shortcuts import render


def budget_view(request):
    return render(request, "sections/budget.html")


def analysis_view(request):
    return render(request, "sections/analysis.html")


def insights_view(request):
    return render(request, "sections/insights.html")


def expenses_view(request):
    return render(request, "sections/expenses.html")
