from django.shortcuts import render;
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable':'This is a page',
        'new':'Yay i am using django'
    }
    # return HttpResponse("Hello! ")
    return render(request , 'index.html',context)

def about(request):
    return render(request,'about.html')

def explore(request):
    return render(request,'explore.html')

def contact(request):
    return render(request,'contact.html')

# def greet(request,name):
#     # return HttpResponse(f"Hello, {name.capitalize()}")
#     return render(request,'greeting.html',{
#         "name" : name.capitalize()
#     })

