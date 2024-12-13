
from django.contrib import admin
from django.urls import path
from app.views import Gerenciar,index, listaAlunos,listaProfessores,listaDisciplinas,listaTurmas,listaHorarios, editarAlunos,editarProfessores,editarDisciplinas,editarTurmas,editarHorarios,deletarAlunos, deletarProfessor, deletarTurmas,deletarHorarios, deletarDisciplinas, adicionarAluno, adicionarProfessor, adicionarTurma, adicionarDisciplina, adicionarHorario


urlpatterns = [
   
    path('admin/', admin.site.urls),


    path('', index, name='login'),
    path('gerenciar',Gerenciar,name='gerenciar'),
    
   
    path('listaAlunos',listaAlunos,name="listaAlunos"),
    path('listaProfessores',listaProfessores, name="listaProfessores"),
    path('listaDisciplinas',listaDisciplinas, name="listaDisciplinas"),
    path('listaTurmas',listaTurmas, name="listaTurmas"),
    path('listaHorarios',listaHorarios, name="listaHorarios"),
  
    path('editarAlunos/<int:id>', editarAlunos,name="editarAlunos"),
    path('editarProfessores/<int:id>', editarProfessores, name="editarProfessores"),
    path('editarDisciplinas/<int:id>', editarDisciplinas,name="editarDisciplinas"),
    path('editarTurmas/<int:id>', editarTurmas ,name="editarTurmas"),
    path('editarHorarios/<int:id>', editarHorarios,name="editarHorarios"),
   
    path('deletarAlunos/<int:id>', deletarAlunos, name="deletarAlunos"),
    path('deletarProfessor/<int:id>', deletarProfessor, name="deletarProfessor"),
    path('deletarDisciplinas/<int:id>', deletarDisciplinas, name="deletarDisciplinas"),
    path('deletarTurmas/<int:id>', deletarTurmas, name="deletarTurmas"),
    path('deletarHorarios/<int:id>', deletarHorarios, name="deletarHorarios"),
   
    path('adicionarAluno/', adicionarAluno, name='adicionarAluno'),
    path('adicionarProfessor/', adicionarProfessor, name='adicionarProfessor'),
    path('adicionarTurma/', adicionarTurma, name='adicionarTurma'),
    path('adicionarDisciplina/', adicionarDisciplina, name='adicionarDisciplina'),
    path('adicionarHorario/', adicionarHorario, name='adicionarHorario')

]
