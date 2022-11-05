from django.shortcuts import render, redirect
from .models import *
from core.form import *
# Create your views here.

def index(request): 
  buraco = buracos.objects.all() 
  return render(request,'index.html', {"buraco":buraco})

def administrador(request): 
  buraco = buracos.objects.all() 
  return render(request,'administrador.html', {"buraco":buraco})

def cadastro_buraco(request): 
 form = buracoForm(request.POST or None)
 if form.is_valid():
    form.save()
    return redirect("index")
 pacote = {"buracoForm":form}
 return render(request, "cadastro-buraco.html", pacote)

def editar(request, id):
  buraco = buracos.objects.get(pk=id)
  form = buracoForm(request.POST or None, instance = buraco)
  if form.is_valid():
    form.save()
    return redirect("index")
  pacote = {"buracoForm": form}
  return render(request, "editar-buraco.html", pacote)
  
def deletar(request, id):
  buraco = buracos.objects.get(pk=id)
  buraco.delete()
  return redirect("index")