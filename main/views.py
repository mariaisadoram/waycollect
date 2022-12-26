from django.shortcuts import render, redirect, get_object_or_404
from main.models import *
from main.forms import LocalForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as sigin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import sweetify
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, "index.html")

@login_required(login_url='/login')
def meus_pontos(request):
    lista = Local.objects.all() #Local (class do models.py)
    print(lista)
    context={'locais' : lista }
    return render(request,'meuspontos.html',context)

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

@login_required(login_url='/login')
def cadastro_ponto(request):
    print(request.method)
    if request.method == 'POST':
        form = LocalForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = LocalForm()
            return redirect('pontos')
    else:
        form = LocalForm()
    
    return render(request, 'forms.html', { 'form' : form })

@login_required
def editar_local(request, id):
    local = Local.objects.get(id=id)
    form = LocalForm(request.POST or None, request.FILES or None, instance=local)

    if request.POST: 
        if form.is_valid():
            try: 
                form.save()
                messages.success(request, "This is a message!")
                # sweetify.sweetalert(request,'Ponto alterado com sucesso!')
                return redirect('editar')
            except:
                pass

    return render(request, 'forms-edit.html', {'local': local, 'form': form})


    # local= get_object_or_404(Local, id=id)
    # form = LocalForm(request.POST or None, request.FILES or None, instance=local)
    # if request.method == 'POST':
    #     form = LocalForm(request.POST,request.FILES,instance=local)
    #     if form.is_valid():
    #         form.save()
    #         sweetify.sweetalert(request,'Ponto alterado com sucesso!')
    #         return redirect('/meus_pontos')
    
    # return render(request, "forms-edit.html", {'form':form})

@login_required
def remover_local(request, id):
    local= get_object_or_404(Local, id=id)
    local.delete()
    sweetify.sweetalert(request,'Ponto excluído com sucesso!')
    return redirect('meus_pontos')

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
            return redirect('/')
        else:
            print("deu errado")
            return redirect('/login')
    else:
        return render(request, 'login.html')

def sair(request):
    logout(request)
    return redirect('/login')