from django.shortcuts import render
from main.models import *
from main.forms import LocalForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, 'sobre.html')

def lista_pontos(request):
    lista = Local.objects.all() #Local (class do models.py)
    print(lista)
    context={'locais' : lista }
    return render(request,'pontos.html',context)

def detalhes(request, id):
    local = Local.objects.get(id=id)
    context = {'local' : local}
    return render(request,'detalhes.html',context)


def cadastro_ponto(request):
    print(request.method)
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            form = LocalForm()
    else:
        form = LocalForm()
    
    return render(request, 'forms.html', { 'form' : form })