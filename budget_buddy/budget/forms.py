from django import forms
from .models import Budget, Expense_Category, Expense


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ["name", "income", "other_income", "start_date", "end_date"]


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = Expense_Category
        fields = ["name", "rating"]


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["name", "amount", "date", "category", "budget"]
