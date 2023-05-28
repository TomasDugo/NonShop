from django.http import HttpResponse
from django.shortcuts import render 

def pagina(request):
    contexto = {}
    HttpResponse = render(
        request=request,
        template_name='NonApp/index.html',
        context=contexto,
    )
    return HttpResponse

def productos(request): 
    contexto = {}
    HttpResponse = render(
        request=request,
        template_name='NonApp/Productos.html',
        context= contexto,
    )
    return HttpResponse

def vender(request): 
    contexto = {}
    HttpResponse = render(
        request=request,
        template_name='NonApp/vender.html',
        context= contexto,
    )
    return HttpResponse

def login(request): 
    contexto = {}
    HttpResponse = render(
        request=request,
        template_name='NonApp/login.html',
        context= contexto,
    )
    return HttpResponse
