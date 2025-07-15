from django import forms

from expense_tracker.models import Expenses


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['title', 'amount', 'description', 'expense_date', 'category']