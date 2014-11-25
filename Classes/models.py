# coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError


NIVEL_ACESSO = [

    ('NivelB', 'Livre'),
    ('NivelA', 'Restrito'),
    ('NivelS', 'Reservado')
]

TIPO_ACESSO = [

    ('Neg', 'Negado'),
    ('Aut', 'Autorizado')
]

SEXO = [

    ('M', 'Masc'),
    ('F', 'Fem')

]

TIPO_AREA = [

    ('INT', 'Interna'),
    ('EXT', 'Externa')

]

TIPO_SETOR = [

    ('PAT', 'Patio'),
    ('RFT', 'Refeitorio'),
    ('CZN', 'Cozinha'),
    ('GRE', 'Gremio'),
    ('JDM', 'Jardim'),
    ('EST', 'Estacionamento'),
    ('ADM', 'Administrativo'),
    ('PRO', 'Producao'),
    ('ALM', 'Almoxarifado'),
    ('ENG', 'Engenharia'),
    ('DIR', 'Diretoria')
]

ESTADO = [
    ('AC', 'Acre - AC'),
    ('AL', 'Alagoas - AL'),
    ('AP', 'Amapá - AP'),
    ('AM', 'Amazonas - AM'),
    ('BA', 'Bahia  - BA'),
    ('CE', 'Ceará - CE'),
    ('DF', 'Distrito Federal  - DF'),
    ('ES', 'Espírito Santo - ES'),
    ('GO', 'Goiás - GO'),
    ('MA', 'Maranhão - MA'),
    ('MT', 'Mato Grosso - MT'),
    ('MS', 'Mato Grosso do Sul - MS'),
    ('MG', 'Minas Gerais - MG'),
    ('PA', 'Pará - PA'),
    ('PB', 'Paraíba - PB'),
    ('PR', 'Paraná - PR'),
    ('PE', 'Pernambuco - PE'),
    ('PI', 'Piauí - PI'),
    ('RJ', 'Rio de Janeiro - RJ'),
    ('RN', 'Rio Grande do Norte - RN'),
    ('RS', 'Rio Grande do Sul - RS'),
    ('RO', 'Rondônia - RO'),
    ('RR', 'Roraima - RR'),
    ('SC', 'Santa Catarina - SC'),
    ('SP', 'São Paulo - SP'),
    ('SE', 'Sergipe - SE'),
    ('TO', 'Tocantins - TO')
]

''' Nivel_Acesso ; Pessoa; Local ;  Permissao . '''


class Pessoa(models.Model):
    Nome = models.CharField('Nome', max_length=100, null=True)
    Nivel_Acesso = models.ForeignKey(Nivel_Acesso, verbose_name='Nivel de Acesso')
    Sexo = models.CharField('Sexo', max_length=1, choices=SEXO_OPCOES, null=True)
    CPF = models.CharField('CPF', max_length=15, unique=True, null=True)
    DataNascimento = models.DateField('Data de Nascimento', null=True)
    Telefone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    Celular = models.CharField('Celular', max_length=15, null=True, blank=True)
    Email = models.EmailField('Endereço de email', max_length=100, null=True)
    Logradouro = models.CharField('Logradouro', max_length=100, null=True, blank=True)
    Numero = models.IntegerField('Número',max_length=4, null=True, blank=True,)
    Complemento = models.CharField('Complemento', max_length=100, null=True, blank=True)
    Bairro = models.CharField('Bairro', max_length=100, null=True)
    Cidade = models.CharField('Cidade', max_length=100, null=True)
    UF = models.CharField('UF', max_length=2, choices=ESTADO_OPCOES, null=True)
    CEP = models.CharField('CEP', max_length=9, null=True)

    def __unicode__(self):
        return self.Nome


class Local(models.Model):
    Nome_Area = models.CharField('Area:', max_length=3, choices=TIPO_AREA, null=True)
    Nome_Setor = models.CharField('Setor', max_length=3, choices=TIPO_SETOR, null=True)
    Nivel_Acesso = models.ForeignKey(Nivel_Acesso, verbose_name='Nivel de Acesso')

    def __unicode__(self):
        return "%s - %s" % (self.Area, self.Setor, self.Nivel_Acesso)


class Nivel_Acesso(models.Model):
    Nivel = models.CharField('Nivel de Acesso', max_length=6, choices=NIVEL_ACESSO, null=True)
    Peso = models.IntergerField('Peso', null=True)

    def __unicode__(self):
        return "%s" % (self.Nivel)


class Permissao(models.Model):
    Pessoa = models.ForeignKey(Pessoa, verbose_name='Pessoa')
    Local = models.ForeignKey(Local, verbose_name='Local de Acesso')
    Data = models.DateField('Data', null=True)
    HoraChegada = models.TimeField('Hora de Entrada', null=True)
    HoraSaida = models.TimeField('Hora de Saída',blank=True,null=True)
    status = models.BooleanField('Acesso:', max_length=3, choices=TIPO_ACESSO, null=True)

    def __unicode__(self):
        return "%s - %s" % ( self.Pessoa,self.Local,self.status)
    if
        sel.status = Neg return print("Acesso Negado")and Register HoraChegada


