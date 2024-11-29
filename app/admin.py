from django.contrib import admin
from .models import Aluno, Professor, Disciplina, Turma, Horario

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Horario)


