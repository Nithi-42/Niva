
from .models import Product, CartItem

from django.shortcuts import render,redirect

def home(request):
    return render(request, "mykart/index.html",)
def view(request):
    return render(request, 'mykart/view.html')
def checkout(request):
    return render(request,'mykart/checkout.html')

def register(request):
    return render(request, 'mykart/register.html')
def categories(request):
    return render(request, 'mykart/categories.html')

def cart(request):
	return render(request, 'mykart/cart.html')

def skirts(request):
     return render(request, 'mykart/skirts.html')


