from django.shortcuts import render, redirect
from main.models import *
from main.forms import LocalForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as sigin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url='/login')
def meus_pontos(request):
    return render(request, "meuspontos.html")

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
        form = LocalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = LocalForm()
    else:
        form = LocalForm()
    
    return render(request, 'forms.html', { 'form' : form })

def cadastro_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('/login')
        except:
            return redirect('/cadastro-usuario')
    else:
        return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)

        if user: 
            sigin(request,user)
            print("deu certo")
            return redirect('/index')
        else:
            print("deu errado")
            return redirect('/login')
    else:
        return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/login')