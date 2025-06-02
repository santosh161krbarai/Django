from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# Every view takes a request and returns a response

def home(request):
    return HttpResponse("<h1>This is the Home Page</h1>")

def about(request):
    return HttpResponse("<h1>This is the About Page</h1>")

def contact(request):
    return HttpResponse("<h1>This is the Contact Page</h1>")
