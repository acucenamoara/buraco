from django.shortcuts import render

# Create your views here.

def index(request): 
  return render(request,'index.html')

def cadastro_buraco(request): 
  return render(request,'cadastro-buraco.html')

def administrador(request): 
  return render(request,'administrador.html')

