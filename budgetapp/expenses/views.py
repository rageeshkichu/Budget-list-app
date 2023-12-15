from django.shortcuts import render
from .models import Expense, Income
from django.db import models

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

def income_list(request):
    incomes = Income.objects.all()
    return render(request, 'expenses/income_list.html', {'incomes': incomes})

def calculate_savings(request):
    expenses_total = Expense.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0
    incomes_total = Income.objects.aggregate(models.Sum('amount'))['amount__sum'] or 0
    savings = incomes_total - expenses_total
    return render(request, 'expenses/savings.html', {'savings': savings})
