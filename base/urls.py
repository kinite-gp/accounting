from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
    path("", dashbourd, name="dashbourd"),
    path("login/", login_page, name="login-page"),
    path("logout/", logout_page, name="logout_page"),
    path("expense/", expense_page, name="expense_page"),
    path("income/", income_page, name="income_page"),
    path("note/", note_page, name="note_page"),
    path("expense_list/", expense_list_page, name="expense_list_page"),
    path("expense_item/<str:obj_id>", expense_item, name="expense_item")
]
