#coding:utf-8
from django.db import models

PERIODO = [

      ('1','1°'),
      ('2','2°'),
      ('3','3°'),
      ('4','4°'),
      ('5','5°'),
      ('6','6°'),
      ('7','7°'),
      ('8','8°',),
      ('9','9°',),
      ('10','10°'),
      ('11','11°'),
      ('12','12°'),
      ('Dependência','Dependência')

]

SEXO = [

	('M','M'),
	('F','F')

]

SEMESTRE = [

	('1','1'),
	('2','2')

]

TURNO = [

	('Matutino', 'Matutino'),
	('Vespertino','Vespertino'),
	('Noturno','Noturno')

]

DESCTURMA = [

	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	('E','E')

]

''' Curso ; Semestre ; Estrutura ; Turma ; Disciplina ; Periodo ; EstruturaDisciplinaPeriodo ; TurmaDisciplina ;
 Aluno ; TurmaAluno ; DisciplinaAluno ; Professor ; Horario ; TurmaDiscHorProf . '''

class Curso(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Turno = models.CharField('Escolha o Turno',max_length=12,choices=TURNO,null=True)

	def __unicode__(self):
		return self.Nome

class Semestre(models.Model):
	Ano = models.CharField('Ano',max_length=100,null=True)
	Semestre = models.CharField('Escolha o Semestre',max_length=1,choices=SEMESTRE,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Semestre, self.Ano)

class Estrutura(models.Model):
	Ano = models.DateField('Ano de Criação',null=True)
	Curso = models.ForeignKey(Curso,verbose_name="Curso",null=True)
	
	def __unicode__(self):
		return "%s" % (self.Curso)

class Turma(models.Model):
	Nome = models.CharField('Nome',max_length=1,choices=DESCTURMA,null=True)
	AnoInicio = models.DateField('Ano de Início',null=True)
	Semestre = models.ForeignKey(Semestre,verbose_name="Semestre",null=True)
	Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	Descricao = models.CharField('Descricao',max_length=100,null=True)

	def __unicode__(self):
		return "%s - %s" % ( self.Nome, self.AnoInicio)

class Disciplina(models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Descricao = models.CharField('Descrição da Disciplina',max_length=100,null=True)
	
	def __unicode__(self):
		return self.Nome

class Periodo(models.Model):
	Descricao = models.CharField('descrição do Período ',max_length=100,null=True)
	Periodo = models.CharField('Escolha o Periodo ',max_length=2,choices=PERIODO,null=True)
	Identificacao = models.CharField('Identificação ',max_length=1,choices=DESCTURMA,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Periodo, self.Identificacao)

class EstruturaDisciplinaPeriodo(models.Model):
	Estrutura = models.ForeignKey(Estrutura,verbose_name="Estrutura",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Periodo = models.ForeignKey(Periodo,verbose_name="Periodo",null=True)
	
	def __unicode__(self):
		return unicode("%s") % (self.Periodo)

class TurmaDisciplina(models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	EstruturaDisciplina = models.ForeignKey(EstruturaDisciplinaPeriodo,verbose_name="Estrutura Disciplina Período",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma,  self.EstruturaDisciplina)
	
		
	
class Aluno(models.Model):
	Nome = models.CharField('Nome do Aluno',max_length=100,null=True)
	Sexo = models.CharField('Sexo',max_length=10,choices=SEXO,null=True)

	def __unicode__(self):
		return self.Nome
	
	
	
class TurmaAluno(models.Model):
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	Aluno = models.ForeignKey(Aluno,verbose_name="Aluno",null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Turma,self.Aluno)
	 
	
class DisciplinaAluno(models.Model):
	TurmaAluno = models.ForeignKey(TurmaAluno,verbose_name="Turma Aluno",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Descricao = models.TextField('Descricao',null=True)

	def __unicode__(self):
		return "%s - %s" % (self.TurmaAluno.Aluno.Nome, self.Disciplina.Nome)

class Professor(models.Model):
	Nome = models.CharField('Nome do Professor',max_length=100,null=True)
	Formacao = models.TextField('Formação do Professor')
	Sexo = models.CharField('Sexo',max_length=10,choices=SEXO,null=True)
	
	def __unicode__(self):
		return  unicode("%s") % (self.Nome)

class Horario(models.Model):
	Turno = models.CharField('Escolha o Turno',max_length=11,choices=TURNO,null=True)
	Comeco = models.TimeField('Início da aula',null=True)
	Fim = models.TimeField('Término da Aula',null=True)
	
	def __unicode__(self):
		return unicode("%s - %s") % (self.Comeco, self.Fim)
	
class TurmaDisciplina_X_HorarioProfessor(models.Model):
	Professor = models.ForeignKey(Professor,verbose_name="Professor",null=True)
	Horario = models.ForeignKey(Horario,verbose_name="Horario",null=True)
	Disciplina = models.ForeignKey(Disciplina,verbose_name="Disciplina",null=True)
	Turma = models.ForeignKey(Turma,verbose_name="Turma",null=True)
	
	def __unicode__(self):
		return "%s - %s - %s - %s" % (self.Professor, self.Horario, self.Disciplina, self.Turma)
