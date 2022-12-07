from django.contrib import admin
from .models import *
# Register your models here.

class LocalAdmin(admin.ModelAdmin):
    list_display = ['nome_local', 'nome_responsavel',]
    # list_filter = ['cidade']

admin.site.register(Local, LocalAdmin)