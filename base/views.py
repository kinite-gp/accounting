from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Expense,Income,Note
from .script import exin
from .forms import LoginForm,ExpenseForm,IncomeForm,NoteForm
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
        "ss" : exin()[1],
        "ssmark" : exin()[0],
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
            obj_form = Expense.objects.create()
            mdl = form.cleaned_data
            obj_form.title = mdl["title"]
            obj_form.description = mdl["description"]
            obj_form.price = mdl["price"]
            obj_form.tag = mdl["tag"]
            obj_form.favorite = mdl["favorite"]
            obj_form.save()
            return redirect("dashbourd")
    else:
        form = ExpenseForm()
        return render(request, "base\\html\\expense.html", {"form":form})
    

@login_required
def income_page(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            obj_form = Income.objects.create()
            mdl = form.cleaned_data
            obj_form.title = mdl["title"]
            obj_form.description = mdl["description"]
            obj_form.price = mdl["price"]
            obj_form.tag = mdl["tag"]
            obj_form.favorite = mdl["favorite"]
            obj_form.save()
            return redirect("dashbourd")
    else:
        form = IncomeForm()
        return render(request, "base\\html\\income.html", {"form":form})
    

@login_required
def note_page(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            obj_form = Note.objects.create()
            mdl = form.cleaned_data
            obj_form.title = mdl["title"]
            obj_form.description = mdl["description"]
            obj_form.tag = mdl["tag"]
            obj_form.favorite = mdl["favorite"]
            obj_form.save()
            return redirect("dashbourd")
    else:
        form = NoteForm()
        return render(request, "base\\html\\note.html", {"form":form})
    
    
def expense_list_page(request):
    objects_expense = Expense.objects.all()
    context = {
        "objects":objects_expense,
    }
    return render(request, "base\html\expense_list.html", context=context)


def expense_item(request, obj_id):
    object = Expense.objects.get(obj_id=obj_id)
    context = {
        "obj":object, 
    }
    return render(request, "base\html\item.html", context=context)