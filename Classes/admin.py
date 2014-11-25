#coding:utf-8

from django.contrib import admin

from models import Nivel_Acesso
from models import Pessoa
from models import Local
from models import Permissao

class Nivel_AcessoAdmin(admin.ModelAdmin):

	list_display = ['NiveS']
	list_filter = ['NiveS']
	search_fields = ['NiveS']
	save_as = True

class PessoaAdmin(admin.ModelAdmin):

	 list_display = ['Pessoa','Nivel_Acesso','Sexo','CPF','Email']
	 list_filter = ['Pessoa','Nivel_Acesso']
	 search_fields = ['Pessoa','Nivel_Acesso','CPF','Email']

class LocalAdmin(admin.ModelAdmin):
	 list_display = ['Pessoa','Nivel_Acesso']
	 list_filter = ['Pessoa','Nivel_Acesso']
	 search_fields = ['Pessoa','Nivel_Acesso']

class PermissaoAdmin(admin.ModelAdmin):
	 list_display = ['Local','Pessoa','Data','HoraChegada','HoraSaida','status']
	 list_filter = ['Local','Pessoa','Data','HoraChegada','HoraSaida','status']
	 search_fields = ['Local','Pessoa']


admin.site.register(Nivel_Acesso,Nivel_AcessoAdmin)
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Local, LocalAdmin)
admin.site.register(Permissao,PermissaoAdmin)

