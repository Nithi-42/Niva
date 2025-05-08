from django.shortcuts import render

def home(request):
    return render(request, 'mykart/index.html')
def cart(request):
    return render(request, 'mykart/cart.html')
def register(request):
    return render(request, 'mykart/register.html')
def categories(request):
    return render(request, 'mykart/categories.html')








# Create your views here.
