from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import  messages
# Create your views here.
def index(request):
    context = {
        "variable":"Hello There"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("this is homepage")
def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is aboutpage")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is servicepage")
def contact(request):
    serial =2
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        serial+1
        contact = Contact(name =name, email = email, phone =phone , desc = desc , date = datetime.today(), serial = serial)
        contact.save()
        messages.success(request, 'Profile details sent')
        
    return render(request,'contact.html')
    #return HttpResponse("this is contactpage")