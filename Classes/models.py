#coding:utf-8
from django.db import models

TIPO_ACESSO = [

      ('1','Livre'),
      ('2','Restrito'),
      ('3','Reservado')
]

SEXO = [

	('M','Masc'),
	('F','Fem')

]

ACAO = [

	('Entra','Entrada'),
	('Saida','Saida')

]

SETOR = [

	('1','Setor - 1'),
	('2','Setor - 2'),
	('3','Setor - 3'),
	('4','Setor - 4'),
	('5','Setor - 5'),
	('6','Setor - 6'),
	('7','Setor - 7')

]

AREA = [

	('A','Area - A'),
	('B','Area - B'),
	('C','Area - C'),
	('D','Area - D')

]

TURNO = [

	('M','Matutino'),
	('V','Vespertino'),
	('N','Noturno')

]

ESTADO = [
	('AC','Acre - AC'),
	('AL','Alagoas - AL'),
	('AP','Amapá - AP'),
	('AM','Amazonas - AM'),
	('BA','Bahia  - BA'),
	('CE','Ceará - CE'),
	('DF','Distrito Federal  - DF'),
	('ES','Espírito Santo - ES'),
	('GO','Goiás - GO'),
	('MA','Maranhão - MA'),
	('MT','Mato Grosso - MT'),
	('MS','Mato Grosso do Sul - MS'),
	('MG','Minas Gerais - MG'),
	('PA','Pará - PA'),
	('PB','Paraíba - PB'),
	('PR','Paraná - PR'),
	('PE','Pernambuco - PE'),
	('PI','Piauí - PI'),
	('RJ','Rio de Janeiro - RJ'),
	('RN','Rio Grande do Norte - RN'),
	('RS','Rio Grande do Sul - RS'),
	('RO','Rondônia - RO'),
	('RR','Roraima - RR'),
	('SC','Santa Catarina - SC'),
	('SP','São Paulo - SP'),
	('SE','Sergipe - SE'),
	('TO','Tocantins - TO')
]


''' Pessoa; Local ; Acesso ; Permissao . '''

class Pessoa(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length=15,blank=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,blank=True)
	Celular = models.CharField('Celular',max_length=15,blank=True)
	Email = models.EmailField('Endereço de email',max_length=100)
	Logradouro = models.CharField('Logradouro', max_length=100,null=True)
	Numero = models.IntegerField('Número',null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade', max_length=100,null=True)
 	UF = models.CharField('UF', max_length=2,choices=ESTADO_OPCOES,null=True)
 	CEP = models.CharField('CEP', max_length=9,null=True)	
	Tipo_Acesso = models.CharField('Tipo de Acesso',max_length=1,choices=TIPO_ACESSO,null=True)
	Turno = models.CharField('Escolha o Turno',max_length=1,choices=TURNO,null=True)

	def __unicode__(self):
		return self.Nome

class Local(models.Model):
	Pessoa = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Area = models.CharField('Acesso Negado', blank=True)
	Setor = models.CharField('Escolha o Setor',max_length=1,choices=SETOR,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Area, self.Setor)

class Acesso(models.Model):
	Pessoa = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Nivel = models.DateField('Escolha o Nivel de Acesso',max_length=1,choices=TIPO_ACESSO,null=True)
	Entrada = models.DateField('Escolha o turno de Entrada',max_length=5,choices=ACAO,null=True)
	Saida = models.DateField('Escolha o Turno de Saida',max_length=5,choices=ACAO,null=True)
	def __unicode__(self):
		return "%s" % (self.Nivel)

class Permissao(models.Model):
	Pessoa = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Alerta = models.CharField('Nome',max_length=1,choices=DESCTURMA,null=True)
	Data = models.DateField('hora',null=True)
	Horario = models.TimeField('hora',null=True)

	def __unicode__(self):
		return "%s - %s" % ( self.Nome, self.Alerta)


