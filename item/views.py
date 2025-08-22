from django.shortcuts import render,get_object_or_404

from .models import Item

def detail(req,primary_key):
    item = get_object_or_404(Item,pk=primary_key)

    return render(req,'item/detail.html',({
        'item':item
    }))
