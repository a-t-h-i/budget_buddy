from django.db import models
from user.models import User


class Budget(models.Model):
    name = models.CharField(max_length=255)
    income = models.DecimalField(max_digits=100, decimal_places=2)
    other_income = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="budget_owner"
    )

    def __str__(self):
        return self.name


class Expense_Category(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="category_owner"
    )

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(
        Expense_Category, on_delete=models.CASCADE, related_name="expense_cat"
    )
    budget = models.ForeignKey(
        Budget, on_delete=models.CASCADE, related_name="linked_budget"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_owner"
    )

    def __str__(self):
        return self.name
