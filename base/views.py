from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Expense,Income,Note
from .script import exin
from .forms import LoginForm,ExpenseForm
from django.contrib.auth import authenticate, login, logout,user_logged_in
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def dashbourd(request):
    exp = Expense.objects.all()
    inc = Income.objects.all()
    nt = Note.objects.all()
    
    context = {
        "exp" : len(exp),
        "inc" : len(inc),
        "nt" : len(nt),
        "ss" : exin,
    }
    
    return render(request,"base\\html\\base.html",context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("dashbourd")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request=request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect("dashbourd")
            else:
                return redirect("login-page")
    else:
        return render(request, "base\\html\\login.html")

    
def logout_page(request):
    if request.user.is_authenticated == True:
        logout(request)
        return redirect("login-page")
    else:
        return redirect("login-page")
    
@login_required
def expense_page(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            mdl = Expense.objects.create()
            mdl.title = form.title
            mdl.description = form.description
            mdl.price = form.price
            mdl.tag = form.tag
            mdl.favorite = form.tag
            mdl.save()
            return redirect("dashbourd")
    else:
        form = ExpenseForm()
        return render(request, "base\\html\\expense.html", {"form":form})
    
