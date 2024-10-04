from django.shortcuts import render ;
from django.shortcuts import redirect ;
from django.http import HttpResponse
from datetime import datetime 
from myapp.models import Contact
from django.contrib import messages

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
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name , email=email , phone= phone , desc = desc , date = datetime.today())
        contact.save()
        messages.success(request,"Your information has been saved")
        return redirect("/")
    return render(request,'contact.html')

# def greet(request,name):
#     # return HttpResponse(f"Hello, {name.capitalize()}")
#     return render(request,'greeting.html',{
#         "name" : name.capitalize()
#     })

