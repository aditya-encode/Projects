from django.shortcuts import render


from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> This is Home Page")

def contact(request):
    return HttpResponse("<h1> This is Contact Page")

def about(request):
    return HttpResponse("<h1> This is About Page")