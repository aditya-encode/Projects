from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    peoples=[{'name':'Aditya',"age":24},
             {'name':'Het',"age":23},
             {'name':'Bhautik',"age":15}
             ]
    return render(request,"index.html",context={'peoples':peoples})

