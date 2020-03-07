from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductFrom

def all(request):
    return render(request,"product/all.html",{"products":Product.objects.all()}) 


def create(request):
    if request.method == "POST":
        form = ProductFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect("product-home")
    else : 
         form = ProductFrom()
   
    return render(request,"product/create.html",{'form':form}) 

def edit(request):
    return render(request,"product/edit.html") 

def delete(request):
    pass

