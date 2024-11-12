from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    featured_products=Product.objects.order_by('priority')[:4] # [:4] will extract first 4 items
    latest_products=Product.objects.order_by('-id')[:4]
    context={'featured_products':featured_products,
             'latest_products':latest_products}
    return render(request,'index.html',context)

def product_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priority') # for descending : order_by('-priority')
    product_paginator=Paginator(product_list,4) 
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'product_list.html',context)

def product_detail(request,pk):
    product=Product.objects.get(pk=pk) # or 'id=pk'
    context={'product':product}

    return render(request,'product_detail.html',context)

def search(request):
    search_products=None
    context=None
    if request.GET:
        search_key=request.GET.get('search_box')
        search_products=Product.objects.all().filter(Q(title__contains=search_key)|Q(description__contains=search_key))
        if search_products:
            context={'products':search_products}
        else:
            search_products=Product.objects.all()
            context={'products':search_products}
    return render(request,'product_list.html',context)









