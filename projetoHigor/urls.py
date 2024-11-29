
from django.contrib import admin
from django.urls import path
from app.views import Gerenciar,index, listaAlunos,listaProfessores,listaDisciplinas,listaTurmas,listaHorarios, editarAlunos, editarProfessores,deletarAlunos, deletarProfessor, deletarTurmas,deletarHorarios, deletarDisciplinas

urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('', index),
    path('gerenciar',Gerenciar,name='gerenciar'),
    
   
    path('listaAlunos',listaAlunos,name="listaAlunos"),
    path('listaProfessores',listaProfessores, name="listaProfessores"),
    path('listaDisciplinas',listaDisciplinas, name="listaDisciplinas"),
    path('listaTurmas',listaTurmas, name="listaTurmas"),
    path('listaHorarios',listaHorarios, name="listaHorarios"),
  
    path('editarAlunos/<int:id>', editarAlunos,name="editarAlunos"),
    path('editarProfessores/<int:id>', editarProfessores, name="editarProfessores"),
   
    path('deletarAlunos/<int:id>', deletarAlunos, name="deletarAlunos"),
    path('deletarProfessor/<int:id>', deletarProfessor, name="deletarProfessor"),
    path('deletarDisciplinas/<int:id>', deletarDisciplinas, name="deletarDisciplinas"),
    path('deletarTurmas/<int:id>', deletarTurmas, name="deletarTurmas"),
    path('deletarHorarios/<int:id>', deletarHorarios, name=" deletarHorarios")

    
]
