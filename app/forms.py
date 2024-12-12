from django import forms
from .models import Aluno,Professor,Turma,Disciplina,Horario


class Alunoform(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'data_nascimento', 'turma']

class Professorform(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'codigo_professor', 'especialidade']

class Turmaform(forms.ModelForm):
    
    class Meta:
        model = Turma
        fields = ['nome_turma', 'sala', 'ano']

class Disciplinaform(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome_disciplina', 'codigo_disciplina', 'professor']

class Horarioform(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['turma','disciplina', 'dia_semana', 'horario_inicio', 'horario_fim']