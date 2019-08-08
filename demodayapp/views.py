from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
   
      return render(request, 'sac.html', contexto)



def sac(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
        return render(request, 'sac.html', contexto)


def price(request):
    #essa página vai cadastrar uma pessoa
    contexto = {}
        return render(request, 'price.html', contexto)