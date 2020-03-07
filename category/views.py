from django.shortcuts import render,redirect
from .models import Category
from .forms import CategoryForm


def home(request):
    return render(request,"category/home.html",{"cats":Category.objects.all()})

def create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save() 
            return redirect("/cat/")
    else : 
        form = CategoryForm()
    return render(request,"category/create.html",{"form":form})

def about(request):
    return render(request,"category/about.html")
