from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Blog Name")

def about(request):
    return HttpResponse("<h1> About Page")

def contact(request):
    return HttpResponse("<h1> Contact Page")



