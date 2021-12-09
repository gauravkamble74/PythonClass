from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("this is home")
    return render(request,'index.html')

def contact(request):
    return HttpResponse("this is contact page")

def about(request):
    return HttpResponse("this is about page")

def servies(request):
    return HttpResponse("this is services page")

