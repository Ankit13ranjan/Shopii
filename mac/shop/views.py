from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil



def index(request):
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n//4 + ceil((n/4) - (n//4))
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    # params = {'allProds':allProds}

    allProds = []
    catProds = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catProds}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])


    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Welcome to contact")


def tracker(request):
    return HttpResponse("Welcome to Tracker")


def search(request):
    return HttpResponse("Welcome to Search")


def productView(request, myid):
    #Fetch the product using the id
    product = Product.objects.filter(id=myid)
    print(product);
    return render(request, "shop/prodView.html", {'product': product[0]})

def checkout(request):
    return HttpResponse("Welcome to checkout")
