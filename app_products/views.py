from django.shortcuts import render, HttpResponse

def products(request):
    return HttpResponse('products')

def confirmProduct(request):
    return HttpResponse('confirmProduct')
