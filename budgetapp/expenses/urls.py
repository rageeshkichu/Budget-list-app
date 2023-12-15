from django.urls import path
from . import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('incomes/', views.income_list, name='income_list'),
    path('savings/', views.calculate_savings, name='calculate_savings'),
]
