from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
    print(request.user)
    return render(request,"pages/home.html")
def another_view(request,*args, **kwargs):
    return render(request,"pages/another.html",{})