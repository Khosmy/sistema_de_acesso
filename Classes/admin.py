#coding:utf-8

from django.contrib import admin

from models import Pessoa
from models import Local
from models import Acesso
from models import Permissao

class AdminPessoa(admin.ModelAdmin):
	 list_display = ['Nome','Tipo_Acesso']
	 list_filter = []
	 search_fields = ['Nome']

class AdminLocal(admin.ModelAdmin):
	 list_display = ['pessoa','setor','area']
	 list_filter = []
	 search_fields = ['setor','area']

class AdminAcesso(admin.ModelAdmin):
	 list_display = ['pessoa','nivel','Entrada','Saida']
	 list_filter = []
	 search_fields = ['pessoa','nivel']

class AdminPermissao(admin.ModelAdmin):
	 list_display = ['alerta','horario','data']
	 list_filter = []
	 search_fields = ['alerta']

admin.site.register(Pessoa,AdminPessoa)
admin.site.register(Local, AdminLocal)
admin.site.register(Acesso,AdminAcesso)
admin.site.register(Permissao,AdminPermissao)

