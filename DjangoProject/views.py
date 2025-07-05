from django.shortcuts import render

def hello_world(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')