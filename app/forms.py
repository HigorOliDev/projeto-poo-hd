from django import forms
from .models import Aluno


class Alunoform(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'data_nascimento', 'turma']