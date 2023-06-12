from django.shortcuts import render
from .models import *

def inicio(request):
    return render(request,"inicio.html")

def cadastro(request):
    if request.method =='POST':
        checkbox = request.POST.get('myCheckbox')
        if checkbox is not None:

            nome = request.POST.get('nome')
            email = request.POST.get('email')
            print(nome,email)

            registro = Registro()
            registro.nome = nome
            registro.email = email
            registro.save()          
    return render(request,'cadastro.html')

def contato(request):
    return render(request,"contato.html")

def noticia(request):
    return render(request,"noticia.html")

def termo(request):
    return render(request,"termo.html")

def cancelar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            registro = Registro.objects.get(email=email)
            registro.delete()
        except Registro.DoesNotExist:
            pass
    return render(request,"cancelar.html")



