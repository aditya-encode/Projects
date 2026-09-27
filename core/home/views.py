from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[{'name':'Aditya',"age":24},
             {'name':'Het',"age":23},
             {'name':'Bhautik',"age":15}
             ]

    return render(request,"index.html",context={'peoples':peoples,'page':'home'})

def about(request):
    cont={'page':'about'}
    return render(request,"about.html",cont)

def contact(request):
    cont={'page':'contact'}
    return render(request,"contact.html",cont)

