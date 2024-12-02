from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=15, unique=True)
    data_nascimento = models.DateField()
    turma = models.ForeignKey('Turma', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    codigo_professor = models.CharField(max_length=15, unique=True)
    especialidade = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo_disciplina = models.CharField(max_length=15, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.nome
    

class Turma(models.Model):
    nome = models.CharField(max_length=50)
    sala = models.CharField(max_length=50, null=True)
    ano = models.CharField(max_length=4, null=True)
    
    def __str__(self):
       return self.nome
   

class Horario(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=20)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    
    def __str__(self):
        return f"{self.turmas.nome} - {self.disciplina.nome} - ({self.dia_semana})"
    

    
    

