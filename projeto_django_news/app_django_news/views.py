from django.shortcuts import render
from .models import *

def inicio(request):
    return render(request,"inicio.html")

def cadastro(request):
    if request.method =='POST':
        checkbox = request.POST.get('myCheckbox')
        print(checkbox)
        #Gambiarra
        if checkbox is None:
            pass
        else:
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


