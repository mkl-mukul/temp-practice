from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"first/index.html")

def inp(request,name):
    return render(request,"first/input.html",
    {
        "name":name.capitalize()
    })
