from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("contact",views.contact,name='contact'),
    path("about",views.about,name='about'),
    # path("services",views.services,name='services')
]