from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('pontos/', lista_pontos, name='pontos'),
    path('detalhes/<int:id>',detalhes,name='detalhes'),
    path('sobrenos/', sobre, name='sobre'),
    path('meus-pontos/', meus_pontos, name='meus_pontos'),
    path('novo-ponto/', cadastro_ponto, name='cadastro_ponto'),
    path('cadastro-usuario/', cadastro_user, name='cadastro_user'),
    path('editar/<int:id>',editar_local,name='editar'),
    path('remover/<int:id>',remover_local,name='remover'),
    path('login/', login, name='login'),
    path('sair/',sair,name='sair')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)