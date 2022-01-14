from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('home')

def signout(request):
    return HttpResponse('signout')
