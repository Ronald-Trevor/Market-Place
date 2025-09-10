from django.shortcuts import render,redirect

from item.models import Category,Item
from .form import SingUpForm

def index(req):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    
    return render(req,'core/index.html',{
        'categories': categories,
        'items': items,
    })

def contact(req):
    return render(req,'core/contact.html')

def signup(req):
    if req.method == "POST":
        form = SingUpForm(req.POST)
        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SingUpForm

    return render(req,'core/signup.html',{'form':form})
