from django.shortcuts import render, HttpResponse

def alerts(request):
    return HttpResponse('alerts')

def alertDetails(request):
    return HttpResponse('alertDetails')

def eccList(request):
    return HttpResponse('eccList')

def eccProfile(request):
    return HttpResponse('eccProfile')

def eccAdd(request):
    return HttpResponse('eccAdd')

def customerList(request):
    return HttpResponse('customerList')

def customerProfile(request):
    return HttpResponse('customerProfile')

