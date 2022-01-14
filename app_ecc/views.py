from django.shortcuts import render, HttpResponse

def alerts(request):
    return HttpResponse('alerts')

def alertDetails(request):
    return HttpResponse('alertDetails')

def myProfile(request):
    return HttpResponse('myProfile')
